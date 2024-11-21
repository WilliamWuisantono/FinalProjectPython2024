from nba_api.stats.endpoints import playercareerstats
from nba_api.stats.static import players
import pandas as pd

def get_player_id_from_name(player_name):
    player_data = players.find_players_by_full_name(player_name)
    if player_data:
        return player_data[0]["id"]
    return None

def fetch_player_stats_and_save(player_id, output_file="player_stats.csv"):
    career = playercareerstats.PlayerCareerStats(player_id=player_id)
    df = career.get_data_frames()[0]
    df.to_csv(output_file, index=False)
    return output_file