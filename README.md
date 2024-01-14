# Minecraft Stats Server

Displays a leaderboard for searchable Minecraft player statistics. 

## Setup

0. Requires Python >= 3.6
1. Create an *.env file for your server including the path to the server files and name of the server
2. Create and activate a virtual environment for installing dependencies `python -m venv [environment-name]` then `env/bin/activate` or `env\Scripts\Activate.(bat|ps1)`
3. Install dependencies `pip install -r requirements.txt`
4. Start the server with `python main.py -e [your-environment-file-name]`
5. See `python main.py -h` for options