import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load the dataset
income = pd.read_csv("income_per_person_gdppercapita_ppp_inflation_adjusted.csv")
life_exp = pd.read_csv("life_expectancy_years.csv")
combined = pd.DataFrame({'Gross domestic product': income['1900'], 'Life Expectancy': life_exp['1900']})
combined['Life Expectancy'].fillna(combined['Life Expectancy'].median(), inplace=True)
combined

sns.scatterplot(data=combined, x='Gross domestic product', y='Life Expectancy')
plt.title('1900')
plt.show()
