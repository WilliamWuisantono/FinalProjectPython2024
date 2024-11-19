import pandas as pd

def preprocess_data(input_csv):
    df = pd.read_csv(input_csv)
    
    # Print the column names to check for the 'TO' column
    print("Columns in the dataset:", df.columns)

    # Fill missing values with 0
    df.fillna(0, inplace=True)

    # Clean season data
    df["SEASON_ID"] = df["SEASON_ID"].str.replace("-", "/")

    # Convert percentages to readable scales (e.g., 0.45 -> 45%)
    percentage_columns = ["FG_PCT", "FG3_PCT", "FT_PCT"]
    for col in percentage_columns:
        df[col] = df[col] * 100

    # Add a calculated column for overall efficiency (check if 'TO' exists)
    if 'TO' in df.columns:
        df["EFFICIENCY"] = df["PTS"] + df["REB"] + df["AST"] - df["TO"]
    else:
        print("Warning: 'TO' (turnovers) column is missing. Skipping efficiency calculation.")
        df["EFFICIENCY"] = df["PTS"] + df["REB"] + df["AST"]  # You can modify this calculation if necessary

    return df
