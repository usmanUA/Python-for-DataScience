import pandas as pd

def load(path: str) -> pd.DataFrame:
    '''
    Reads a CSV file and returns a Pandas DataFrame.
    
    Args:
    path (str): The path to the CSV file.

    Returns:
    pd.DataFrame: The resulting DataFrame.
    '''

    try:
        df = pd.read_csv(path)
        pass
    except FileNotFoundError as e:
        print(f"{path} does not exist.")
        print(f"Error: {e}")
        return None
    except IsADirectoryError as e:
        print(f"{path} is a directory, not a file.")
        print(f"Error: {e}")
        return None
    except IOError as e:  # For other I/O related errors
        print(f"Error accessing {path}.")
        print(f"Error: {e}")
        return None
    print(f"Loading dataset of dimensions {df.shape}")
    return df
