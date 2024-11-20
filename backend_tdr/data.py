import pandas as pd


def load_data(file_path):
    data = pd.read_csv(file_path)
    return data


tdr_data = load_data("tdrV2.csv")
