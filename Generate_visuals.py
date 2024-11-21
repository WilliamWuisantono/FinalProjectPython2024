import matplotlib.pyplot as plt
import seaborn as sns
from Data_Preprocessing import preprocess_data
import os

def generate_all_visuals(input_csv, player_name):
    """Generate all visualizations and save them to the static folder."""
    df = preprocess_data(input_csv)

    static_folder = "static"
    if not os.path.exists(static_folder):
        os.mkdir(static_folder)

    graph_filenames = {}

    # Career Points Bar Chart
    plt.figure(figsize=(10, 6))
    sns.barplot(x=df["SEASON_ID"], y=df["PTS"])
    plt.title(f"{player_name}'s Career Points by Season")
    plt.xlabel("Season")
    plt.ylabel("Total Points")
    plt.xticks(rotation=45)
    points_filename = os.path.join(static_folder, "career_points.png")
    plt.tight_layout()
    plt.savefig(points_filename)
    plt.close()
    graph_filenames["career_points"] = points_filename

    # Shooting Percentages Pie Chart
    percentages = {
        "Field Goals": df["FG_PCT"].mean(),
        "Three-Point FG": df["FG3_PCT"].mean(),
        "Free Throws": df["FT_PCT"].mean()
    }
    plt.figure(figsize=(8, 8))
    plt.pie(percentages.values(), labels=percentages.keys(), autopct='%1.1f%%', startangle=90)
    plt.title(f"{player_name}'s Shooting Percentages")
    percentages_filename = os.path.join(static_folder, "shooting_percentages.png")
    plt.savefig(percentages_filename)
    plt.close()
    graph_filenames["shooting_percentages"] = percentages_filename

    # Core Stats Line Chart
    plt.figure(figsize=(10, 6))
    plt.plot(df["SEASON_ID"], df["REB"], label="Rebounds", marker="o")
    plt.plot(df["SEASON_ID"], df["AST"], label="Assists", marker="o")
    plt.plot(df["SEASON_ID"], df["BLK"], label="Blocks", marker="o")
    plt.title(f"{player_name}'s Rebounds, Assists, and Blocks by Season")
    plt.xlabel("Season")
    plt.ylabel("Count")
    plt.xticks(rotation=45)
    plt.legend()
    core_stats_filename = os.path.join(static_folder, "core_stats.png")
    plt.tight_layout()
    plt.savefig(core_stats_filename)
    plt.close()
    graph_filenames["core_stats"] = core_stats_filename

    # Correlation Heatmap
    plt.figure(figsize=(10, 8))
    sns.heatmap(df[["PTS", "REB", "AST", "STL", "BLK"]].corr(), annot=True, cmap="coolwarm", fmt=".2f")
    plt.title(f"{player_name}'s Correlation Heatmap")
    heatmap_filename = os.path.join(static_folder, "correlation_heatmap.png")
    plt.savefig(heatmap_filename)
    plt.close()
    graph_filenames["correlation_heatmap"] = heatmap_filename

    # Scatter Plot for Assists vs Points
    plt.figure(figsize=(8, 6))
    sns.scatterplot(x=df["PTS"], y=df["AST"])
    plt.title(f"{player_name}'s Points vs Assists")
    plt.xlabel("Total Points")
    plt.ylabel("Total Assists")
    scatter_filename = os.path.join(static_folder, "points_vs_assists.png")
    plt.tight_layout()
    plt.savefig(scatter_filename)
    plt.close()
    graph_filenames["points_vs_assists"] = scatter_filename

    # Cluster Plot
    plt.figure(figsize=(8, 6))
    sns.scatterplot(x=df["PTS"], y=df["REB"], hue=df["AST"], palette="viridis")
    plt.title(f"{player_name}'s Cluster Plot: Points, Rebounds, and Assists")
    plt.xlabel("Total Points")
    plt.ylabel("Total Rebounds")
    cluster_filename = os.path.join(static_folder, "cluster_plot.png")
    plt.tight_layout()
    plt.savefig(cluster_filename)
    plt.close()
    graph_filenames["cluster_plot"] = cluster_filename

    return graph_filenames