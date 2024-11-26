import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
from Data_Preprocessing import preprocess_data

# Function to prepare data for ML
def prepare_data_for_model(input_csv):
    # Preprocess the data
    df = preprocess_data(input_csv)

    # Select relevant features and target
    features = ["REB", "AST", "STL", "BLK", "MIN"]  # Input features
    target = "PTS"  # Target variable (Points)

    X = df[features]
    y = df[target]

    return X, y

# Function to train the ML model
def train_model(X, y):
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    model = LinearRegression()
    model.fit(X_train, y_train)

    # Evaluate the model
    predictions = model.predict(X_test)
    mse = mean_squared_error(y_test, predictions)
    print(f"Model Mean Squared Error: {mse}")
    
    return model

# Function to predict player performance
def predict_performance(model, input_data):
    predictions = model.predict(input_data)
    return predictions

# Train and return the model
def get_trained_model(input_csv):
    X, y = prepare_data_for_model(input_csv)
    model = train_model(X, y)
    return model
