import pandas as pd

def load_and_preprocess_data(filepath):
    df = pd.read_csv(filepath)
    df = df[['Date', 'Open', 'High', 'Low', 'Close', 'Volume']]
    df['Date'] = pd.to_datetime(df['Date'])
    df['Prediction'] = df['Close'].shift(-1)
    df.dropna(inplace=True)
    X = df[['Open', 'High', 'Low', 'Volume']]
    y = df['Prediction']
    return X, y
