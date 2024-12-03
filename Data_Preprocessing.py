import pandas as pd

def preprocess_data(input_csv):
    # Load the CSV into a DataFrame
    df = pd.read_csv(input_csv)

    # Fill missing values with 0
    df.fillna(0, inplace=True)

    # Clean season data
    if "SEASON_ID" in df.columns:
        df["SEASON_ID"] = df["SEASON_ID"].astype(str).str.replace("-", "/")

    # Convert percentages to readable scales (e.g., 0.45 -> 45%)
    percentage_columns = ["FG_PCT", "FG3_PCT", "FT_PCT"]
    for col in percentage_columns:
        if col in df.columns:
            df[col] = df[col] * 100

    # Add a calculated column for overall efficiency (if turnovers are present)
    if "PTS" in df.columns and "REB" in df.columns and "AST" in df.columns:
        if "TO" in df.columns:
            df["EFFICIENCY"] = df["PTS"] + df["REB"] + df["AST"] - df["TO"]
        else:
            df["EFFICIENCY"] = df["PTS"] + df["REB"] + df["AST"]

    return df
