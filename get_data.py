import pandas as pd


def fetch_data(url: str, name: str):
    """fetches table data from url. saves data as a pickle file to disk under df_name
    """
    list = pd.read_html(url)
    df = list[0]
    df.to_pickle(f"./{name}")
    