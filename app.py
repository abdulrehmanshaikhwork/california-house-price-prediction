from flask import Flask, render_template, request, jsonify
import pandas as pd
import joblib
import os
from main import build_pipeline

app = Flask(__name__)

# Load the model and pipeline
MODEL_FILE = "model.pkl"
PIPELINE_FILE = "pipeline.pkl"

# Check if model exists, if not train it
if not os.path.exists(MODEL_FILE):
    print("Model not found. Training model first...")
    import main
    # main.py will train the model

# Load trained model and pipeline
model = joblib.load(MODEL_FILE)
pipeline = joblib.load(PIPELINE_FILE)

# Load sample data to get feature info
input_data = pd.read_csv("input.csv")

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Get data from form
        data = request.json
        
        # Create dataframe with the input
        new_data = pd.DataFrame([{
            'longitude': float(data.get('longitude', 0)),
            'latitude': float(data.get('latitude', 0)),
            'housing_median_age': float(data.get('housing_median_age', 0)),
            'total_rooms': float(data.get('total_rooms', 0)),
            'total_bedrooms': float(data.get('total_bedrooms', 0)),
            'population': float(data.get('population', 0)),
            'households': float(data.get('households', 0)),
            'median_income': float(data.get('median_income', 0)),
            'ocean_proximity': data.get('ocean_proximity', 'INLAND')
        }])
        
        # Transform using the pipeline
        new_data_prepared = pipeline.transform(new_data)
        
        # Make prediction
        prediction = model.predict(new_data_prepared)[0]
        
        return jsonify({
            'success': True,
            'prediction': round(prediction, 2),
            'message': f'Predicted House Value: ${prediction:,.2f}'
        })
    
    except Exception as e:
        return jsonify({
            'success': False,
            'message': f'Error: {str(e)}'
        })

if __name__ == '__main__':
    app.run(debug=True)
