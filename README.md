# NBA Player Stats Visualizer
 
## Overview
The **NBA Player Stats Visualizer** is a Flask-based web application that allows users to input the name of an NBA player and view their career statistics, interactive visualizations, and predicted future performance. This project leverages data from the [nba_api](https://github.com/swar/nba_api) library to fetch up-to-date statistics directly from the NBA database.
 
---
 
## Features
- **Player Search**: Input the name of an NBA player to fetch their statistics.
- **Interactive Visualizations**:
  - Career points by season.
  - Shooting percentages for the most recent season.
  - Correlation heatmap of various performance metrics.
  - Points vs assists scatter plot with clustering.
  - 3D cluster plot for advanced metrics.
- **Predicted Performance**: Use machine learning to predict the player’s performance in the next season.
- **Player Headshot and Career Totals**: Display player headshot alongside summarized career stats.
- **Responsive UI**: Styled with CSS for a clean and user-friendly design.
 
---
 
## File Structure
### Static Files
The `static` folder contains the stylesheet and generated interactive visualizations:
- **`style.css`**: Provides styling for the web application, ensuring a visually appealing and responsive design.
 
### Templates
The `templates` folder contains the HTML files for the user interface:
1. **`HomePage.html`**: The homepage where users can enter the name of an NBA player.
2. **`Results_template.html`**: Displays the player's career statistics, visualizations, and predicted performance.
 
### Python Scripts

1. **`Website.py`**: The main Flask application ([Click Here to See File](Website.py)):
   - [Website.py](https://github.com/WilliamWuisantono/FinalProjectPython2024/blob/main/Website.py)
   - Handles routing for the homepage (`/`) and results page (`/results`).
   - Fetches player statistics, generates visualizations, and uses machine learning models to make predictions.
   - Passes data and visualizations to the HTML templates for display.
 
2. **`player_images.py`**: Generates a combined visualization of a player's headshot and career totals ([Click Here to See File](player_images.py)):
   - [Player_images.py](https://github.com/WilliamWuisantono/FinalProjectPython2024/blob/main/player_images.py)
   - Fetches player headshot images and career stats using the `nba_api`.
   - Creates a side-by-side display of the headshot and a table summarizing key career stats.
   - Saves the visualization as an image in the `static` folder.
 
3. **`Data_Preprocessing.py`**: Handles the preprocessing of player statistics data ([Click Here to See File](Data_Preprocessing.py)):
   - [Data_Preprocessing.py](https://github.com/WilliamWuisantono/FinalProjectPython2024/blob/main/Data_Preprocessing.py)
   - Reads the input CSV file and fills missing values with 0.
   - Converts percentage columns (e.g., field goal percentage) to readable scales.
   - Cleans season data and sorts it for proper chronological order.
 
4. **`Data_collections.py`**: Fetches player data using the `nba_api` library ([Click Here to See File](Data_collections.py)):
   - [Data_collections.py](https://github.com/WilliamWuisantono/FinalProjectPython2024/blob/main/Data_collections.py)
   - Retrieves a player's unique ID based on their full name.
   - Fetches a player's career stats and saves them to a CSV file.
 
5. **`Generate_visuals.py`**: Creates interactive visualizations using `plotly` ([Click Here to See File](Generate_visuals.py)):
   - [Generate_Visuals.py](https://github.com/WilliamWuisantono/FinalProjectPython2024/blob/main/Generate_visuals.py)
   - Career points bar chart.
   - Shooting percentages pie chart.
   - Correlation heatmap.
   - Points vs assists scatter plot.
   - 3D clustered stats visualization.
 
6. **`Machine_learning.py`**: Implements machine learning models to predict player performance ([Click Here to See File](Machine_learning.py)):
   - [Machine_learning.py](https://github.com/WilliamWuisantono/FinalProjectPython2024/blob/main/Machine_learning.py)
   - **Multi-Output Regression**: Predicts multiple stats (points, rebounds, assists).
   - **Binary Classification**: Predicts whether a player will be a high performer (e.g., scoring more than 20 points per game).
---
 
## Data Source
This project uses the [nba_api](https://github.com/swar/nba_api) library to fetch player statistics and other relevant data. It is a reliable and comprehensive Python library for accessing NBA statistics, updated frequently.
 
---
 
## Setup Instructions
### Installing Dependencies
To set up the environment and install all necessary dependencies, use:
```bash
pip install -r requirements.txt
```
### Uninstalling Dependencies
If you do decide that you are done with our project and want to uninstall all dependencies, use:
```bash
pip uninstall -r requirements.txt -y
