from flask import Flask, jsonify, request
import pandas as pd
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Enable CORS for frontend communication

# Load dataset (replace with actual data source)
data = pd.read_csv('brent_oil_prices.csv')

data['Date'] = pd.to_datetime(data['Date'])
data.set_index('Date', inplace=True)

@app.route('/api/historical', methods=['GET'])
def get_historical_data():
    start_date = request.args.get('start_date', '2020-01-01')
    end_date = request.args.get('end_date', '2022-12-31')
    filtered_data = data.loc[start_date:end_date]
    return jsonify(filtered_data.to_dict())

@app.route('/api/events', methods=['GET'])
def get_event_data():
    events = [
        {"date": "2021-03-01", "event": "OPEC production cut", "impact": "Increase"},
        {"date": "2022-02-24", "event": "Russia-Ukraine War", "impact": "Spike"}
    ]
    return jsonify(events)

if __name__ == '__main__':
    app.run(debug=True)
