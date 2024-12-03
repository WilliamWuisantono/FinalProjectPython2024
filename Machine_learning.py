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
    targets = ["PTS", "REB", "AST"]  # Predict Points, Rebounds, Assists
 
    X = df[features]
    y = df[targets]
    return X, y
 
# Function to train a multi-output regression model
def train_multi_target_model(X, y):
    model = MultiOutputRegressor(LinearRegression())
    model.fit(X, y)
 
    # Evaluate model performance
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
    df["High_Performer"] = (df["PTS"] > 20).astype(int)  # Example threshold: Points > 20
 
    X = df[features]
    y = df[target]
    return X, y
 
# Function to train a classification model
def train_classification_model(X, y):
    model = RandomForestClassifier(random_state=42)
    model.fit(X, y)
 
    # Evaluate model performance
    predictions = model.predict(X)
    accuracy = accuracy_score(y, predictions)
    print(f"Classification Model Accuracy: {accuracy}")
 
    return model
 
# Functions to train and return models
def get_multi_target_model(input_csv):
    X, y = prepare_data_for_multi_target(input_csv)
    return train_multi_target_model(X, y)
 
def get_classification_model(input_csv):
    X, y = prepare_data_for_classification(input_csv)
    return train_classification_model(X, y)
 
# Function to predict performance stats and high performer classification
def predict_performance_and_classification(multi_model, classification_model, input_data):
    # Predict multiple stats
    multi_predictions = multi_model.predict(input_data)
 
    # Predict classification
    classification_prediction = classification_model.predict(input_data)
 
    return multi_predictions, classification_prediction