from flask import Flask, render_template, request
from Generate_visuals import generate_all_visuals
from Data_collections import get_player_id_from_name, fetch_player_stats_and_save
from player_images import save_career_totals_with_headshot
from Machine_learning import (
    get_multi_target_model,
    get_classification_model,
    prepare_data_for_multi_target,
    predict_performance_and_classification,
)
import pandas as pd
 
app = Flask(__name__)
 
@app.route("/")
def index():
    return render_template("HomePage.html")
 
@app.route("/results", methods=["POST"])
def results():
    player_name = request.form.get("player_name").strip()
 
    # Fetch player ID and stats
    player_id = get_player_id_from_name(player_name)
    if not player_id:
        return render_template("HomePage.html", error=f"Player '{player_name}' not found. Please try again.")
 
    # Save stats to a CSV and generate visuals
    stats_csv = fetch_player_stats_and_save(player_id)
    visuals = generate_all_visuals(stats_csv, player_name)
 
    # Generate player headshot and career totals PNG
    player_image = save_career_totals_with_headshot(player_name)
 
    # Train the models
    multi_model = get_multi_target_model(stats_csv)
    classification_model = get_classification_model(stats_csv)
 
    # Prepare input data for prediction (last season's stats)
    X, _ = prepare_data_for_multi_target(stats_csv)
    input_data = X.tail(1)  # Use the most recent season's data for prediction
 
    # Make predictions
    predicted_stats, high_performer_prediction = predict_performance_and_classification(
        multi_model, classification_model, input_data
    )
 
    # Parse predictions
    predicted_points, predicted_rebounds, predicted_assists = predicted_stats[0]
    is_high_performer = "Yes" if high_performer_prediction[0] == 1 else "No"
 
    # Pass data to the results template
    return render_template(
        "Results_template.html",
        player_name=player_name,
        visuals=visuals,
        player_image="player_photo.png",
        predicted_points=predicted_points,
        predicted_rebounds=predicted_rebounds,
        predicted_assists=predicted_assists,
        is_high_performer=is_high_performer,
    )
 
if __name__ == "__main__":
    app.run(debug=True)