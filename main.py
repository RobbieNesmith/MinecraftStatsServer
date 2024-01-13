from flask import Flask, jsonify, render_template
from dotenv import load_dotenv
import json
import requests
import os

load_dotenv()

app = Flask(__name__)

@app.route("/")
def main():
  return render_template("index.html", server_name=os.environ["SERVER_NAME"])

@app.route("/api/stats")
def get_stats():
  stats_path = os.path.join(os.environ["SERVER_PATH"], "stats")
  player_files = os.listdir(stats_path)
  player_stats = {}
  for filename in player_files:
    player_uuid = os.path.splitext(filename)[0]
    with open(os.path.join(stats_path, filename)) as stats_file:
      stats = json.load(stats_file)
      info_response = requests.get(f"https://playerdb.co/api/player/minecraft/{player_uuid}")
      stats["info"] = info_response.json()
      player_stats[player_uuid] = stats
  return jsonify(player_stats)
