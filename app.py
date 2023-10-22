from flask import Flask, request
import pandas as pd
from utils import get_tip
import pickle

app = Flask(__name__)
model = pickle.load(open("./models/cat.pkl", "rb"))
print("Model Loaded")

@app.route("/",methods=['GET'])
def home():
	return "Server is up and running on port 5000"

@app.route("/predict",methods=['GET', 'POST'])
def predict():
	if request.method == "POST":
		data = request.get_json()
		# DATE
		date = data['date']
		day = float(pd.to_datetime(date, format="%Y-%m-%dT").day)
		month = float(pd.to_datetime(date, format="%Y-%m-%dT").month)
		# MinTemp
		minTemp = float(data['mintemp'])
		# MaxTemp
		maxTemp = float(data['maxtemp'])
		# Rainfall
		rainfall = float(data['rainfall'])
		# Evaporation
		evaporation = float(data['evaporation'])
		# Sunshine
		sunshine = float(data['sunshine'])
		# Wind Gust Speed
		windGustSpeed = float(data['windgustspeed'])
		# Wind Speed 9am
		windSpeed9am = float(data['windspeed9am'])
		# Wind Speed 3pm
		windSpeed3pm = float(data['windspeed3pm'])
		# Humidity 9am
		humidity9am = float(data['humidity9am'])
		# Humidity 3pm
		humidity3pm = float(data['humidity3pm'])
		# Pressure 9am
		pressure9am = float(data['pressure9am'])
		# Pressure 3pm
		pressure3pm = float(data['pressure3pm'])
		# Temperature 9am
		temp9am = float(data['temp9am'])
		# Temperature 3pm
		temp3pm = float(data['temp3pm'])
		# Cloud 9am
		cloud9am = float(data['cloud9am'])
		# Cloud 3pm
		cloud3pm = float(data['cloud3pm'])
		# Cloud 3pm
		location = float(data['location'])
		# Wind Dir 9am
		winddDir9am = float(data['winddir9am'])
		# Wind Dir 3pm
		winddDir3pm = float(data['winddir3pm'])
		# Wind Gust Dir
		windGustDir = float(data['windgustdir'])
		# Rain Today
		rainToday = float(data['raintoday'])

		input_lst = [location , minTemp , maxTemp , rainfall , evaporation , sunshine ,
					 windGustDir , windGustSpeed , winddDir9am , winddDir3pm , windSpeed9am , windSpeed3pm ,
					 humidity9am , humidity3pm , pressure9am , pressure3pm , cloud9am , cloud3pm , temp9am , temp3pm ,
					 rainToday , month , day]
		pred = model.predict(input_lst)
		output = pred

		if output:
			return {"tip": get_tip(1), "rain": "1"}
		else:
			return {"tip": get_tip(0), "rain": "0"}
	return "Method not allowed"

if __name__=='__main__':
	app.run(debug=True)