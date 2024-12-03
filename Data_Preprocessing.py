import pandas as pd

def preprocess_data(input_csv):
    # Load the CSV into a DataFrame
    df = pd.read_csv(input_csv)

    # Fill missing values with 0
    df.fillna(0, inplace=True)

    # Clean season data
    if "SEASON_ID" in df.columns:
        df["SEASON_ID"] = df["SEASON_ID"].astype(str).str.replace("-", "/")

    # Ensure SEASON_ID is treated as a string for categorical sorting
    df["SEASON_ID"] = df["SEASON_ID"].astype(str)

    # Convert percentages to readable scales (e.g., 0.45 -> 45%)
    percentage_columns = ["FG_PCT", "FG3_PCT", "FT_PCT"]
    for col in percentage_columns:
        if col in df.columns:
            df[col] = df[col] * 100

    # Sort the data by season to ensure proper order
    df = df.sort_values(by='SEASON_ID', ascending=True)
    
    return df
