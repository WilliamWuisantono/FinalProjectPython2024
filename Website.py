from flask import Flask, render_template, request
from Generate_visuals import generate_all_visuals
from Data_collections import get_player_id_from_name, fetch_player_stats_and_save
from player_images import save_career_totals_with_headshot
from Machine_learning import get_trained_model, prepare_data_for_model, predict_performance
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

    # Train the model and make predictions
    model = get_trained_model("player_stats.csv")
    X, _ = prepare_data_for_model(stats_csv)
    predicted_points = predict_performance(model, X.tail(1)) # Most recent Season

    # Pass data to the results template
    return render_template(
        "Results_template.html",
        player_name=player_name,
        visuals=visuals,
        player_image="player_photo.png",
        predicted_points=predicted_points[0],  # Use the first prediction
    )

if __name__ == "__main__":
    app.run(debug=True)
