import os
from flask import Flask, render_template, request
import pandas as pd  
from Data_collections import get_player_id_from_name, fetch_player_stats_and_save  
from Generate_visuals import generate_career_points, generate_shooting_percentages, generate_correlation_heatmap, generate_points_vs_assists, generate_clustered_stats
from player_images import save_career_totals_with_headshot
from Machine_learning import get_multi_target_model, get_classification_model, predict_performance_and_classification

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("HomePage.html")

@app.route('/results', methods=['POST'])
def results():
    player_name = request.form.get('player_name').strip()

    # Fetch player ID and stats
    player_id = get_player_id_from_name(player_name)
    if not player_id:
        return render_template('HomePage.html', error=f"Player '{player_name}' not found. Please try again.")

    # Save stats to a CSV and return its file path
    stats_csv = fetch_player_stats_and_save(player_id)
    
    # Read the CSV into a DataFrame to pass to the visual generation functions
    df = pd.read_csv(stats_csv)

    try:
        # Generate interactive visuals
        career_points = generate_career_points(df, "career_points_interactive.html")
        shooting_percentages = generate_shooting_percentages(df, "shooting_percentages_interactive.html")  
        correlation_heatmap = generate_correlation_heatmap(df, "correlation_heatmap_interactive.html") 
        points_vs_assists = generate_points_vs_assists(df, "points_vs_assists_interactive.html")  
        clustered_stats = generate_clustered_stats(df, "cluster_plot_interactive.html")  
    except Exception as e:
        return render_template('HomePage.html', error=f"Error generating visuals: {e}")

    # Create a dictionary to hold the filenames of the interactive graphs
    interactive_visuals = {
        "career_points_plot": career_points,
        "shooting_percentages_plot": shooting_percentages,
        "correlation_heatmap": correlation_heatmap,
        "points_vs_assists_plot": points_vs_assists,
        "cluster_plot": clustered_stats
    }

    # Debugging logs for generated visuals
    print("Generated Visuals:", interactive_visuals)

    # Generate the player headshot and save it
    player_image = save_career_totals_with_headshot(player_name) 
    
    # Load machine learning models
    multi_target_model = get_multi_target_model(stats_csv)
    classification_model = get_classification_model(stats_csv)

    # Prepare input data for prediction (features)
    input_data = df[["REB", "AST", "STL", "BLK", "MIN"]].values

    # Predict performance using machine learning models
    multi_predictions, classification_prediction, average_predicted_points = predict_performance_and_classification(
        multi_target_model, classification_model, input_data
    )

    # Determine if the player is a high performer
    is_high_performer = "Yes" if classification_prediction[0] == 1 else "No"

    # Pass visuals, player details, and predictions to the results template
    return render_template(
        "Results_template.html",
        player_name=player_name,
        interactive_visuals=interactive_visuals,  # Pass the interactive visuals
        player_image="player_photo.png",  # The headshot image
        predicted_points=average_predicted_points,
        predicted_rebounds=multi_predictions[0][1],  # Rebounds prediction
        predicted_assists=multi_predictions[0][2],  # Assists prediction
        is_high_performer=is_high_performer
    )

if __name__ == '__main__':
    app.run(debug=True)
