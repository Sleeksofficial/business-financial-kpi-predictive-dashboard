# Functions to load and preprocess data
def load_data(file_path):
    import pandas as pd
    return pd.read_csv(file_path)