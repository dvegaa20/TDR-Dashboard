import pandas as pd


def load_data(file_path):
    """
    Loads data from a csv file and returns a pandas DataFrame.

    Args:
    file_path: The path to the csv file containing the data.

    Returns:
    A pandas DataFrame containing the loaded data.
    """

    data = pd.read_csv(file_path)
    return data


tdr_data = load_data("tdrV2.csv")
