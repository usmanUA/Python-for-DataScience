import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from load_csv import load

def plot_cols(df: pd.DataFrame) -> None:
    ''' doc '''

    plt.figure(figsize=(12, 6))
    sns.lineplot(data=df, x='Years', y='Belgium', label='Belgium')
    sns.lineplot(data=df, x='Years', y='France', label='France')
    plt.title('Population Projections')
    plt.xlabel('Year')
    plt.ylabel('Population')
    plt.legend()
    plt.show()


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
    df = load("population_total.csv")
    try:
        df.set_index("country", inplace=True)
    except KeyError:
        print("country is not included in this dataset")
    try:
        years = df.columns.tolist()
        new = df.T
        new.index = years
        new.index.name = 'Years'
        new.reset_index(inplace=True)
        finland = new['Finland']
        pakistan = new['Pakistan']
    except KeyError:
        print("Finland and Pakistan are not included in this dataset")
    try:
        new['Years'] = new['Years'].astype(int)
        until_2050 = new[new['Years'] <= 2050]
    except KeyError:
        print("Year 2050 is not included in this dataset")
    plot_cols(until_2050)


if __name__ == "__main__":
    main()
