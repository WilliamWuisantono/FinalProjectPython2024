from flask import Flask, render_template, request, redirect, url_for
from Generate_Visuals import generate_all_visuals
from Data_collections import get_player_id_from_name, fetch_player_stats_and_save

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('HomePage.html')

@app.route('/results', methods=['POST'])
def results():
    player_name = request.form.get('player_name')

    # Fetch player ID and stats
    player_id = get_player_id_from_name(player_name)
    if not player_id:
        return render_template('HomePage.html', error=f"Player {player_name} not found.")

    # Save stats to a CSV and generate visuals
    stats_csv = fetch_player_stats_and_save(player_id)
    visuals = generate_all_visuals(stats_csv, player_name)

    # Pass visuals to the results template
    return render_template('Results_template.html', player_name=player_name, visuals=visuals)

if __name__ == '__main__':
    app.run(debug=True)
