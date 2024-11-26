import pandas as pd 
from flask import Flask, render_template, request
from Generate_visuals import generate_all_visuals
from Data_collections import get_player_id_from_name, fetch_player_stats_and_save
from player_images import save_career_totals_with_headshot
from Machine_learning import get_multi_target_model, get_classification_model, predict_performance_and_classification

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('HomePage.html')

@app.route('/results', methods=['POST'])
def results():
    player_name = request.form.get('player_name').strip()

    # Fetch player ID and stats
    player_id = get_player_id_from_name(player_name)
    if not player_id:
        return render_template('HomePage.html', error=f"Player '{player_name}' not found. Please try again.")

    # Save stats to a CSV and generate visuals
    stats_csv = fetch_player_stats_and_save(player_id)
    visuals = generate_all_visuals(stats_csv, player_name)
    player_image = save_career_totals_with_headshot(player_name)

    # Load the models
    multi_target_model = get_multi_target_model(stats_csv)
    classification_model = get_classification_model(stats_csv)

    # Prepare the input data for prediction (features)
    df = pd.read_csv(stats_csv)
    input_data = df[["REB", "AST", "STL", "BLK", "MIN"]].values

    # Get predictions and average predicted points
    multi_predictions, classification_prediction, average_predicted_points = predict_performance_and_classification(
        multi_target_model, classification_model, input_data
    )

    # Determine if the player is a high performer
    is_high_performer = "Yes" if classification_prediction[0] == 1 else "No"

    # Pass visuals, player details, and predictions to the results template
    return render_template(
        "Results_template.html",
        player_name=player_name,
        visuals=visuals,
        player_image="player_photo.png",
        predicted_points=average_predicted_points,
        predicted_rebounds=multi_predictions[0][1],  # Rebounds prediction (index 1)
        predicted_assists=multi_predictions[0][2],  # Assists prediction (index 2)
        is_high_performer=is_high_performer
    )

if __name__ == '__main__':
    app.run(debug=True)