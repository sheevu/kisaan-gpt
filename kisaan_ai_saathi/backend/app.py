# Kisaan AI Saathi Backend

from flask import Flask, jsonify, request
from services.weather_service import get_weather_updates
from services.crop_advisory_service import get_crop_advisory
from services.market_price_service import get_market_price

app = Flask(__name__)

@app.route('/')
def home():
    return "Welcome to Kisaan AI Saathi!"

@app.route('/weather', methods=['GET'])
def weather():
    location = request.args.get('location')
    return jsonify({"weather": get_weather_updates(location)})

@app.route('/crop-advisory', methods=['GET'])
def crop_advisory():
    crop = request.args.get('crop')
    return jsonify({"advisory": get_crop_advisory(crop)})

@app.route('/market-price', methods=['GET'])
def market_price():
    crop = request.args.get('crop')
    return jsonify({"market_price": get_market_price(crop)})

if __name__ == '__main__':
    app.run(debug=True)
