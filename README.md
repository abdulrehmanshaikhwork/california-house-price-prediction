# California House Prediction (Machine Learning)

A machine learning regression project that predicts California house prices using the California Housing dataset.  
This project demonstrates a complete workflow from data preprocessing to model training, evaluation, and saving the trained model.

---

## Problem Statement
The goal of this project is to build a regression model that can predict house prices based on features like location, population, income, and housing-related attributes.

---

## Dataset
This project uses the **California Housing dataset**, a commonly used dataset for regression tasks in machine learning.

Typical features include:
- Median income
- House age
- Average rooms / bedrooms
- Population
- Latitude and longitude

Target:
- House price value (median house value)

---

## Tech Stack
- **Python**
- **NumPy**
- **Pandas**
- **Matplotlib**
- **Seaborn**
- **Scikit-learn**
- **Joblib**

---

## Project Workflow (Step-by-Step)
1. Load the California Housing dataset
2. Perform basic data cleaning (missing values, data types, etc.)
3. Exploratory Data Analysis (EDA) using plots and correlations
4. Feature selection and train-test split
5. Train a regression model using Scikit-learn
6. Evaluate model performance using standard regression metrics
7. Save the trained model using Joblib
8. Run predictions on new input data (optional)

---

## How to Run Locally

### 1) Clone the repository
```bash
git clone https://github.com/abdulrehmanshaikhwork/california-house-price-prediction
cd california-house-price-prediction
