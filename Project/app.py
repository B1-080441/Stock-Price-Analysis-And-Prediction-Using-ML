from flask import Flask, render_template, request
import pandas as pd
import numpy as np
from statsmodels.tsa.arima.model import ARIMA
import pickle

app = Flask(__name__)

# Load the ARIMA model from the Pickle file
with open('Reliance_Stock.pkl', 'rb') as file:
    model_arima = pickle.load(file)


# Assuming 'train_data' and 'test_data' are your training and testing datasets
# Replace this with your actual data
# train_data = stock_data.iloc[:7447] # Your training data
# test_data = stock_data.iloc[7447:8180]  # Your testing data

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/predict', methods=['POST'])
def predict():
    try:
        start = int(request.form['start'])
        end = int(request.form['end'])

        # Make predictions with the ARIMA model
        pred_arima = model_arima.forecast(steps=end - start + 1)

        # Render the result page with the predictions
        return render_template('result.html', start=start, end=end, pred_arima=pred_arima)

    except Exception as e:
        # Print the error message to the console
        print("Error:", str(e))

        # If an error occurs, render the error page
        return render_template('error.html', error_message=str(e))


if __name__ == '__main__':
    app.run(debug=True)
