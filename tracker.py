import pandas as pd
import os

DATA_PATH = "data/weight_log.csv"

def initialize_file():
    if not os.path.exists(DATA_PATH):
        os.makedirs("data", exist_ok=True)
        df = pd.DataFrame(columns=["date", "weight"])
        df.to_csv(DATA_PATH, index=False)

def load_data():
    initialize_file()
    return pd.read_csv(DATA_PATH)

def add_entry(date, weight):
    df = load_data()
    new_row = pd.DataFrame([[date, weight]], columns=["date", "weight"])
    df = pd.concat([df, new_row], ignore_index=True)
    df.to_csv(DATA_PATH, index=False)
