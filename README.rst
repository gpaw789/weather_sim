Weather Simulator
========================

Author: George Paw
Date: 29/11/2017

This is a simple project to simulator weather into a specific output as listed below:

Sydney|-33.86,151.2,39|2017-11-29T01:19:25Z|Sunny|+0|-4.68668655|2
Melbourne|-37.73,144.91,78|2017-11-29T01:19:25Z|Sunny|+0|-9.3733731|53
Adelaide|-34.93,138.58,29|2017-11-29T01:19:25Z|Sunny|+0|-3.48497205|32

Location is an optional label describing one or more positions
Position is a comma-separated triple containing latitude, longitude, and elevation in metres above sea
level
Local time is an ISO8601 date time
Conditions is either Snow, Rain, Sunny
Temperature is in °C
Pressure is in hPa, and
Relative humidity is a %

Usage:
1. Install requirements.txt, recommend using virtual environment (uploaded for your convenience)
2. Navigate to \master\
3. Execute in terminal "python GenerateWeather.py"
4. Follow the command prompts
5. The script will generate a fixed amount of station data in a datastream format as mentioned above

Optional: run nn.py to generate a new neural network fitting based on CSV file

Theory:
Output all stations at the same time, data per second is dependent on user.
The time is set to current time and every new datastream is at an hour interval into the future
This is a unsolicated output stream

Used Neural Network to predict temperature, the topology is as below:
Features: Latitude, Longtitude, Elevation, Temperature
Output: Temperature
Layer: 1000

Data obtained from https://data.gov.au/dataset/rainfall-and-temperature-forecast-and-observations-hourly-verification-2016-05-to-2017-04/resource/5920f661-79cc-4740-8d76-20cd11f033d4

Limitation:
Stations are narrowed to 10 cities
Custom values are not working yet
Timezones are not taking into account
Pressure only take into account elevation
Humidity is currently a pseudo-random number generator
Weather condition is a pseudo-random number generator

Future Improvements:
Use more stations datapoints
Fix custom values
Enable solicated output stream
Take timezones into consideration
Allow python script to take arguments
Construct better test scripts using pytest
Find a better way to generate pressure (e.g. lookup table)
Use rainfall temperature to calculate humidity
Use time as a factor in neural network training
Use neural network training to produce a better weather conditon prediciton
Train neural network better

