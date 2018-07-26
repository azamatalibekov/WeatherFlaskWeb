import random
from flask import Flask, render_template

app = Flask(__name__)

# http://127.0..
# 0.1:8080/me
# http://127.0.0.1:8080/weather
# http://127.0.0.1:8080/
weather_list = [
    {'name': "sunny", "image": "/static/putin.jpg"},
    {'name': "rainy", "image": "/static/flood.jpg"},
    {'name': "cloudy", "image": "/static/cloud.jpg"},
    {'name': "stormy", "image": "/static/stormy.jpg"}
]


@app.route('/')
def index():
    return render_template('code')


@app.route('/me')
def about():
    return render_template('me')


@app.route('/weather')
def weather():
    random_weather = random.choice(weather_list)
    print(random_weather)
    return render_template('weather', weather=random_weather)



app.run(debug=True, port=8086)
