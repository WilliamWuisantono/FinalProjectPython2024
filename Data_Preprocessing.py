import pandas as pd

def preprocess_data(input_csv):
    """Preprocess player stats from a CSV file."""
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

    return df
