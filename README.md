# NBA Player Statistics Visualization
 
## **Project Description**
This project is a Flask-based web application that allows users to explore NBA player statistics through interactive visualizations and predictive analytics. Users can input an NBA player's name, view their statistics, graphs, and headshots, and even explore machine learning predictions for their future performance.
 
---
 
## **Project Structure**
 
### **Folders and Files**
 
#### Static Folder
Contains CSS styles and dynamically generated images:
- **`style.css`**: Defines the web application's layout, themes, and styling.
- **Graph Images**:
  - `career_points.png`: Bar chart of career points by season.
  - `shooting_percentages.png`: Pie chart of shooting percentages.
  - `core_stats.png`: Line chart of rebounds, assists, and blocks per season.
  - `correlation_heatmap.png`: Heatmap showing statistical correlations (points, rebounds, assists, etc.).
  - `points_vs_assists.png`: Scatter plot of total points vs. assists.
  - `cluster_plot.png`: Scatter plot of points, rebounds, and assists with clustering.
- **`player_photo.png`**: Combines a player's headshot with career totals.
 
#### Templates Folder
Contains the HTML templates for rendering web pages:
- **`HomePage.html`**: Provides an input form for the user to search for an NBA player.
- **`Results_template.html`**: Displays player statistics, graphs, predictions, and the classification result.
 
#### Python Files
 
##### **`Website.py`**
The main Flask application that handles:
- **Routing**:
  - `/`: Displays the home page with the input form.
  - `/results`: Processes player data, generates visualizations, and renders predictions.
- **Core Features**:
  - Fetches the player ID and stats using `Data_collections.py`.
  - Generates visuals using `Generate_visuals.py`.
  - Combines headshots with career stats using `player_images.py`.
  - Implements machine learning models from `Machine_learning.py` to predict player performance.
- **Highlights**:
  - Automatically processes user input for player name validation.
  - Displays error messages for invalid or unrecognized names.
 
##### **`player_images.py`**
Functions for fetching and displaying player headshots alongside career stats:
- **Core Functions**:
  - `get_player_id(player_name)`: Retrieves a player's ID by searching the NBA database.
  - `get_career_totals(player_id)`: Calculates career totals (e.g., points, assists, rebounds) and seasons played.
  - `get_player_headshot(player_id)`: Fetches the player's headshot from the NBA's online database.
  - `save_career_totals_with_headshot(player_name)`: Combines the headshot with career stats into a visual representation.
- **Workflow**:
  - Fetches career stats and player images dynamically from the NBA API.
  - Generates a side-by-side layout of the player's headshot and key statistics table.
  - Saves the output as `player_photo.png` in the `static` folder.
 
##### **`Data_collections.py`**
Functions for fetching player statistics using `nba_api`:
- `get_player_id_from_name(player_name)`: Fetches a player's unique ID based on their name.
- `fetch_player_stats_and_save(player_id, output_file="player_stats.csv")`: Saves the player's stats to a CSV file.
 
##### **`Data_Preprocessing.py`**
Processes and cleans player data:
- Fills missing values and adjusts data formats (e.g., percentages to readable scales).
- Adds derived features (e.g., points per game, overall efficiency).
- Validates required columns for machine learning and visualizations.
 
##### **`Generate_visuals.py`**
Generates statistical visualizations:
- Produces graphs like bar charts, pie charts, scatter plots, and heat maps.
- Saves images to the `static` folder for rendering on the results page.
 
##### **`Machine_learning.py`**
Implements machine learning for predictive analytics:
- Multi-output regression to predict key statistics (e.g., points, rebounds, assists).
- Classification model to identify high-performing players.
- Functions for preparing data, training models, and making predictions.
