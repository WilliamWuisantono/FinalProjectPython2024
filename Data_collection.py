# Import necessary libraries
from nba_api.stats.endpoints import playercareerstats
from nba_api.live.nba.endpoints import scoreboard
import pandas as pd

# Function to get player career stats (using Nikola Jokić's player ID as an example)
def get_player_stats(player_id):
    # Initialize PlayerCareerStats endpoint with the player ID
    career = playercareerstats.PlayerCareerStats(player_id=player_id)
    
    # Retrieve data as a pandas DataFrame
    career_df = career.get_data_frames()[0]
    print("Player Career Stats:")
    print(career_df.head())  # Display the first few rows of the DataFrame
    return career_df

# Function to get today's NBA scoreboard data
def get_today_scoreboard():
    # Initialize ScoreBoard endpoint
    games = scoreboard.ScoreBoard()
    
    # Retrieve the data in JSON format
    games_json = games.get_json()
    print("Today's Scoreboard Data:")
    print(games_json)
    return games_json

# Main function to run both functions
if __name__ == "__main__":
    # Get stats for Nikola Jokić (player_id: 203999)
    player_id = '203999'
    get_player_stats(player_id)
    
    # Get today's scoreboard
    get_today_scoreboard()
