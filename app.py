from flask import Flask, jsonify
import requests

app = Flask(__name__)

@app.route('/')
def home():
    return "NBA API is running"

@app.route('/stats', methods=['GET'])
def get_nba_stats():
    try:
        # Replace this with the actual NBA stats API you want to use
        url = "https://www.balldontlie.io/api/v1/players"  # Example API
        response = requests.get(url)

        if response.status_code == 200:
            return jsonify(response.json())  # Return actual NBA data
        else:
            return jsonify({"error": "Failed to fetch NBA stats"}), response.status_code

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
