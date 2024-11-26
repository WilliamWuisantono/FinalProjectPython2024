import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.multioutput import MultiOutputRegressor
from sklearn.metrics import mean_squared_error, accuracy_score
from Data_Preprocessing import preprocess_data

# Function to prepare data for multi-output regression
def prepare_data_for_multi_target(input_csv):
    df = preprocess_data(input_csv)

    # Features and multiple targets
    features = ["REB", "AST", "STL", "BLK", "MIN"]
    targets = ["PTS", "REB", "AST"]

    X = df[features]
    y = df[targets]
    return X, y

# Function to train a multi-output regression model
def train_multi_target_model(X, y):
    model = MultiOutputRegressor(LinearRegression())
    model.fit(X, y)

    predictions = model.predict(X)
    mse = mean_squared_error(y, predictions, multioutput="raw_values")
    print(f"Mean Squared Error for Multi-Target Model: {mse}")
    return model

# Function to prepare data for classification
def prepare_data_for_classification(input_csv):
    df = preprocess_data(input_csv)

    # Features and binary classification target
    features = ["REB", "AST", "STL", "BLK", "MIN"]
    target = "High_Performer"

    # Create binary classification label
    df["High_Performer"] = (df["PTS"] > 20).astype(int)

    X = df[features]
    y = df[target]
    return X, y

# Function to train a classification model
def train_classification_model(X, y):
    model = RandomForestClassifier(random_state=42)
    model.fit(X, y)

    predictions = model.predict(X)
    accuracy = accuracy_score(y, predictions)
    print(f"Classification Model Accuracy: {accuracy}")
    return model

def get_multi_target_model(input_csv):
    X, y = prepare_data_for_multi_target(input_csv)
    return train_multi_target_model(X, y)

def get_classification_model(input_csv):
    X, y = prepare_data_for_classification(input_csv)
    return train_classification_model(X, y)

# Function to predict performance and classification, and calculate average predicted points
def predict_performance_and_classification(multi_model, classification_model, input_data):
    # Predict multi-output (including points)
    multi_predictions = multi_model.predict(input_data)

    # Extract the predicted points (first column in multi-target predictions)
    predicted_points = multi_predictions[:, 0]  # PTS column is at index 0

    # Calculate the average of the predicted points
    average_predicted_points = predicted_points.mean()
    print(f"Average Predicted Points: {average_predicted_points}")

    # Predict classification (whether the player is a high performer)
    classification_prediction = classification_model.predict(input_data)

    return multi_predictions, classification_prediction, average_predicted_points