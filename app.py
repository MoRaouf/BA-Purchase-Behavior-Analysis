from flask import Flask, request, render_template
import pandas as pd
import numpy as np
from src.pipeline.predict_pipeline import PredictPipeline

application = Flask(__name__)

app = application

@app.route('/', methods=['GET','POST'])
def predict():
    if request.method=='GET':
        return render_template('index.html')
    else:
        # Get the input values from the form
        num_passengers = int(request.form['num_passengers'])
        sales_channel = request.form['sales_channel']
        trip_type = request.form['trip_type']
        purchase_lead = int(request.form['purchase_lead'])
        length_of_stay = int(request.form['length_of_stay'])
        flight_hour = int(request.form['flight_hour'])
        flight_day = request.form['flight_day']
        route = request.form['route']
        booking_origin = request.form['booking_origin']
        wants_extra_baggage = int(request.form['wants_extra_baggage'])
        wants_preferred_seat = int(request.form['wants_preferred_seat'])
        wants_in_flight_meals = int(request.form['wants_in_flight_meals'])
        flight_duration = float(request.form['flight_duration'])

        
        # Create a dataframe with the input values
        input_data = pd.DataFrame({
            'num_passengers': [num_passengers],
            'sales_channel': [sales_channel],
            'trip_type': [trip_type],
            'purchase_lead': [purchase_lead],
            'length_of_stay': [length_of_stay],
            'flight_hour': [flight_hour],
            'flight_day': [flight_day],
            'route': [route],
            'booking_origin': [booking_origin],
            'wants_extra_baggage': [wants_extra_baggage],
            'wants_preferred_seat': [wants_preferred_seat],
            'wants_in_flight_meals': [wants_in_flight_meals],
            'flight_duration': [flight_duration]
        })
        
        # print(input_data.iloc[:, :6])
        # print(input_data.iloc[:, 6:])

        # Get the department-wide sales prediction
        predict_pipeline=PredictPipeline()
        predictions = predict_pipeline.predict(input_data)
        # print(predictions)
        return render_template('index.html', results=predictions[0])

if __name__ == '__main__':
    app.run(host="0.0.0.0", debug=True)
