import pandas as pd

def preprocess_data(input_csv):
    # Load data
    df = pd.read_csv(input_csv)

    # Fill missing values with 0
    df.fillna(0, inplace=True)

    # Clean season data
    df["SEASON_ID"] = df["SEASON_ID"].str.replace("-", "/")

    # Convert percentages to readable scales (e.g., 0.45 -> 45%)
    percentage_columns = ["FG_PCT", "FG3_PCT", "FT_PCT"]
    for col in percentage_columns:
        df[col] = df[col] * 100

    # Add a calculated column for overall efficiency
    if 'TO' in df.columns:
        df["EFFICIENCY"] = df["PTS"] + df["REB"] + df["AST"] - df["TO"]
    else:
        df["EFFICIENCY"] = df["PTS"] + df["REB"] + df["AST"]

    # Ensure required columns exist for both Generate_visuals and Machine_learning
    required_columns = ["SEASON_ID", "PTS", "REB", "AST", "STL", "BLK", "MIN", "FG_PCT", "FG3_PCT", "FT_PCT"]
    for col in required_columns:
        if col not in df.columns:
            raise ValueError(f"Missing required column: {col}")

    # Create derived features for machine learning and visualizations
    df["PTS_per_game"] = df["PTS"] / df["GP"]
    df["REB_per_game"] = df["REB"] / df["GP"]
    df["AST_per_game"] = df["AST"] / df["GP"]

    return df
