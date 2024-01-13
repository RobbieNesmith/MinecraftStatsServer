from flask import Flask, jsonify, render_template
from dotenv import load_dotenv
import json
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
    with open(os.path.join(stats_path, filename)) as stats_file:
      stats = json.load(stats_file)
      player_stats[os.path.splitext(filename)[0]] = stats
  return jsonify(player_stats)
