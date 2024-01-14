import argparse
from flask import Flask, jsonify, render_template
from dotenv import load_dotenv
import json
import requests
import os
from waitress import serve

parser = argparse.ArgumentParser(prog="Minecraft Stats Server", description="A web server for displaying in game stats for a Minecraft server")
parser.add_argument("-e", "--env", default=".env", help="Which environment file to use for configuration. See .env.template for details.")
parser.add_argument("-w", "--webhost", default="*", help="What web interface to serve on, leave off for all.")
parser.add_argument("-p", "--port", type=int, default=5000, help="What port to serve on. Leave off for 5000")

args = parser.parse_args()

load_dotenv(args.env)

player_infos = {}

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
    stats = {}
    with open(os.path.join(stats_path, filename)) as stats_file:
      stats = json.load(stats_file)
    if player_uuid in player_infos:
      stats["info"] = player_infos[player_uuid]
    else:
      info_response = requests.get(f"https://playerdb.co/api/player/minecraft/{player_uuid}")
      info_json = info_response.json()
      stats["info"] = info_json
      player_infos[player_uuid] = info_json
    player_stats[player_uuid] = stats
  return jsonify(player_stats)

print(f"Serving on {args.webhost}:{args.port}")
serve(app, listen=f"{args.webhost}:{args.port}")