from flask import Flask, jsonify
import nba_api.stats.endpoints as nba

app = Flask(__name__)

@app.route('/')
def home():
    return jsonify({"message": "NBA API is running!"})

@app.route('/players', methods=['GET'])
def get_players():
    # Example: Fetch active players
    players = nba.commonallplayers.CommonAllPlayers().get_dict()
    return jsonify(players)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
