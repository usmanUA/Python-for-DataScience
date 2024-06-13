import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from load_csv import load

def main():
    ''' 
    Loads a CSV file into a Pandas DataFrame and displays a specified column as a graph.

    This function reads the data from the provided CSV file path into a DataFrame.
    It then extracts the specified column and plots its values using a line graph.

    Args:
        None

    Returns:
        None

    Example:
        main()

    Raises:
        FileNotFoundError: If the CSV file is not found at the specified path.
        KeyError: If the specified column does not exist in the DataFrame.
        Exception: For any other exceptions that may occur during file reading or plotting.

    Note:
        Ensure that the CSV file and column name provided are correct to avoid errors.
    '''
    df = load("life_expectancy_years.csv")
    try:
        df.set_index("country", inplace=True)
        years = df.columns.tolist()
        new = df.T
        new['Years'] = years
        df = new
        finland = df['Finland']
    except KeyError:
        print("Finland is not included in this dataset")
    sns.lineplot(data=df, x='Years', y='Finland')
    plt.title(f"Finland Life Expectancy Projections")
    plt.xlabel('Year')
    plt.ylabel('Life Expectancy')
    plt.show()


if __name__ == "__main__":
    main()
