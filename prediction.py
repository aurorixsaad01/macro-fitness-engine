import numpy as np
from tracker import load_data

def weight_trend():
    df = load_data()
    y = df["weight"].values
    x = np.arange(len(y))

    slope, intercept = np.polyfit(x, y, 1)

    return slope, intercept

def predict_future(days_ahead):
    slope, intercept = weight_trend()
    current_day = len(load_data())
    future_day = current_day + days_ahead

    return slope * future_day + intercept
