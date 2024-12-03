import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from Data_Preprocessing import preprocess_data
from Data_collections import fetch_player_stats_and_save

# Generate Career Points Bar Chart (Interactive)
def generate_career_points(preprocessed_data, output_file="career_points_interactive.html"):
    # Create the bar chart with clear formatting
    fig = px.bar(
        preprocessed_data,
        x="SEASON_ID", 
        y="PTS", 
        color="PTS",
        title="Career Points by Season",
        labels={"PTS": "Points Earned", "SEASON_ID": "NBA Season"},
        template="plotly_dark",
        text_auto=True
    )

    # Improve graph appearance with better spacing and marker styles
    fig.update_traces(
        marker=dict(line=dict(color='black', width=1))
    )
    fig.update_layout(
        xaxis_title="NBA Season",
        yaxis_title="Points Earned",
        xaxis=dict(type="category"),
        yaxis=dict(showgrid=True)
    )

    # Save the graph to the static folder
    output_path = f"static/{output_file}"
    fig.write_html(output_path)
    return output_file

# Generate Shooting Percentages Pie Chart (Interactive)
def generate_shooting_percentages(preprocessed_data, output_file="shooting_percentages_interactive.html"):
    df = preprocessed_data
    latest_season = df.iloc[-1]  # Use the latest season's stats
    data = {
        "Type": ["Field Goal Percentage", "Three-Point Percentage", "Free Throw Percentage"],
        "Percentage": [latest_season["FG_PCT"], latest_season["FG3_PCT"], latest_season["FT_PCT"]]
    }
    pie_df = pd.DataFrame(data)
    fig = px.pie(
        pie_df,
        names="Type",
        values="Percentage",
        title="Shooting Percentages for Current Season",
        template="plotly_dark",
        hole=0.4  #
    )
    fig.update_traces(textinfo='percent+label')
    fig.write_html(f"static/{output_file}")
    return output_file

# Generate Correlation Heatmap
def generate_correlation_heatmap(preprocessed_data, output_file="correlation_heatmap_interactive.html"):
    df = preprocessed_data
    correlation = df[["PTS", "REB", "AST", "STL", "BLK", "MIN"]].corr()

    fig = go.Figure(
        data=go.Heatmap(
            z=correlation.values,
            x=correlation.columns,
            y=correlation.columns,
            colorscale="Viridis"
        )
    )
    fig.update_layout(
        title="Correlation Heatmap",
        template="plotly_dark"
    )
    fig.write_html(f"static/{output_file}")
    return output_file

# Generate Points vs Assists Scatter Plot with Clustering
def generate_points_vs_assists(preprocessed_data, output_file="points_vs_assists_interactive.html"):
    df = preprocessed_data
    fig = px.scatter(
        df,
        x="PTS",
        y="AST",
        color="SEASON_ID",
        size="MIN",
        hover_name="SEASON_ID",
        title="Points vs Assists (Clustered by Season)",
        labels={"PTS": "Total Points", "AST": "Total Assists"},
        template="plotly_dark"
    )
    fig.update_traces(marker=dict(opacity=0.8, line=dict(width=1, color='black')))
    fig.write_html(f"static/{output_file}")
    return output_file

# Generate Clustered Stats Visualization
def generate_clustered_stats(preprocessed_data, output_file="cluster_plot_interactive.html"):
    df = preprocessed_data
    fig = px.scatter_3d(
        df,
        x="PTS",
        y="REB",
        z="AST",
        color="SEASON_ID",
        size="MIN",
        hover_name="SEASON_ID",
        title="Clustered Stats (Points, Rebounds, Assists)",
        template="plotly_dark"
    )
    fig.update_layout(scene=dict(xaxis_title='Points', yaxis_title='Rebounds', zaxis_title='Assists'))
    fig.write_html(f"static/{output_file}")
    return output_file