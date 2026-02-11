# Housing Price Predictor - Flask Web App

A beginner-friendly web application for predicting housing prices using machine learning!

## 📁 Project Structure

```
templates/
  └── index.html       # Web form & results page
static/
  └── style.css        # Styling & layout
app.py                 # Flask application
main.py                # ML model training
requirements.txt       # Python dependencies
```

## 🚀 How to Run

### 1. Install Dependencies
```bash
pip install -r requirements.txt
```

### 2. Make Sure You Have Trained the Model
First, train your ML model by running:
```bash
python main.py
```
This creates `model.pkl` and `pipeline.pkl` files.

### 3. Start the Flask App
```bash
python app.py
```

### 4. Open in Browser
Go to: **http://localhost:5000**

## 📝 How to Use

1. Fill in the housing property details:
   - **Longitude & Latitude**: Location coordinates
   - **Housing Median Age**: Age of the property
   - **Total Rooms & Bedrooms**: Number of rooms/bedrooms
   - **Population & Households**: Area statistics
   - **Median Income**: Income level in the area
   - **Ocean Proximity**: How close to the ocean

2. Click **"Predict Price"** button

3. The AI model will predict the house value!

## 🎨 Features

✅ Clean & modern UI
✅ Real-time prediction
✅ Input validation
✅ Responsive design (works on mobile too)
✅ Live loading indicator
✅ Error handling

## 🔧 Customization

- **Modify the look**: Edit `static/style.css`
- **Change form fields**: Edit `templates/index.html`
- **Add new routes**: Edit `app.py`

## 📚 Learning Tips for Beginners

- **app.py**: Main Flask server code
- **@app.route()**: URLs your app responds to
- **request.json**: Data sent from the form
- **jsonify()**: Converts Python data to JSON response
- **url_for()**: Links to static files (CSS, JS)

Enjoy! 🎉
