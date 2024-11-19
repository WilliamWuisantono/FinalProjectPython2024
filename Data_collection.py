from nba_api.stats.endpoints import playercareerstats
from nba_api.stats.static import players
import pandas as pd

def get_player_id_from_name(player_name):
    player_data = players.find_players_by_full_name(player_name)
    if player_data:
        return player_data[0]["id"]  # Return the first match
    return None

def fetch_player_stats_and_save(player_id, output_file="player_stats.csv"):
    career = playercareerstats.PlayerCareerStats(player_id=player_id)
    df = career.get_data_frames()[0]
    df.to_csv(output_file, index=False)
    return output_file

# Testing the function with a player's name
player_name = "Kevin Durant"

# Get Player ID from name
player_id = get_player_id_from_name(player_name)

if player_id:
    print(f"Player ID for {player_name}: {player_id}")
    
    # Fetch and save stats to CSV
    output_file = fetch_player_stats_and_save(player_id)
    print(f"Player stats saved to {output_file}")
else:
    print(f"Player {player_name} not found.")
