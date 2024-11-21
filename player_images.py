from nba_api.stats.endpoints import playercareerstats
from nba_api.stats.static import players
import pandas as pd
import matplotlib.pyplot as plt
from PIL import Image
from io import BytesIO
import requests

# Function to fetch player data by name
def get_player_id(player_name):
    nba_players = players.get_players()
    player = next((p for p in nba_players if p['full_name'].lower() == player_name.lower()), None)
    if player:
        return player['id'], player['full_name']
    else:
        raise ValueError(f"Player {player_name} not found!")

# Function to fetch career stats
def get_career_totals(player_id):
    player_career = playercareerstats.PlayerCareerStats(player_id=player_id)
    career_data = player_career.get_data_frames()[0]
    career_totals = career_data.sum(numeric_only=True)  # Calculate totals across numeric columns
    career_totals['SEASONS'] = len(career_data)
    return career_totals

# Function to fetch player headshot
def get_player_headshot(player_id):
    url = f"https://cdn.nba.com/headshots/nba/latest/260x190/{player_id}.png"
    response = requests.get(url)
    if response.status_code == 200:
        return Image.open(BytesIO(response.content))
    else:
        raise ValueError(f"Headshot not found for player ID {player_id}.")

# Function to create the visualization
def plot_career_totals_with_headshot(player_name):
    try:
        # Get player ID and details
        player_id, full_name = get_player_id(player_name)
        print(f"Found player: {full_name}, ID: {player_id}")
        
        # Get career totals
        career_totals = get_career_totals(player_id)
        stats_to_display = career_totals[['SEASONS', 'GP', 'PTS', 'REB', 'AST', 'STL', 'BLK', 'MIN']]
        
        # Get player headshot
        headshot = get_player_headshot(player_id)
        
        # Create the plot layout
        fig, ax = plt.subplots(1, 2, figsize=(12, 6), gridspec_kw={'width_ratios': [1, 2]})
        
        # Display headshot
        ax[0].imshow(headshot)
        ax[0].axis("off")
        ax[0].set_title(f"{full_name}", fontsize=20, weight='bold')
        
        # Display career totals as a table
        ax[1].axis("off")
        table_data = pd.DataFrame(stats_to_display).reset_index()
        table_data.columns = ['Stat', 'Value']
        ax[1].table(cellText=table_data.values, colLabels=table_data.columns, loc='center', cellLoc='center', colLoc='center')
        ax[1].set_title("Career Totals", fontsize=14)
        
        # Show the plot
        plt.tight_layout()
        plt.show()
        
    except ValueError as e:
        print(e)

# Display career stats and headshots for multiple players
players_to_display = ["LeBron James", "Stephen Curry", "Kevin Durant"]  # Add more player names here

for player_name in players_to_display:
    print(f"Displaying stats for {player_name}")
    plot_career_totals_with_headshot(player_name)