import pandas as pd


def load_csv(file_path):
    """
    Load a CSV file into a pandas DataFrame.

    Parameters:
    file_path (str): The path to the CSV file.

    Returns:
    pd.DataFrame: The loaded DataFrame.
    """
    try:
        df = pd.read_csv(file_path)
        return df
    except Exception as e:
        print(f"Error loading CSV file: {e}")


def load_historical_data(sticker):
    """
    Load historical financial data for a given stock ticker.

    Parameters:
    sticker (str): The stock ticker symbol.

    Returns:
    pd.DataFrame: The loaded DataFrame containing historical data.
    """
    try:
        # Assuming the data is stored in a CSV file named after the sticker
        stock_data = 'F:/Week1_Challenge/Data/{sticker}_historical_data.csv'
        df = pd.read_csv(stock_data)
        return df
    except Exception as e:
        print(f"Error loading historical data for {sticker}: {e}")
        return pd.DataFrame()  # Return an empty DataFrame on error

