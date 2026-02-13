import matplotlib.pyplot as plt
from tracker import load_data
from prediction import weight_trend
import numpy as np

def plot_progress():
    df = load_data()
    y = df["weight"].values
    x = np.arange(len(y))

    slope, intercept = weight_trend()
    trend_line = slope * x + intercept

    plt.plot(x, y, label="Weight")
    plt.plot(x, trend_line, label="Trend", linestyle="--")
    plt.legend()
    plt.xlabel("Days")
    plt.ylabel("Weight (kg)")
    plt.title("Weight Progress")
    plt.show()
