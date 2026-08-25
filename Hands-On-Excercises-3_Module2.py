import pandas as pd

df = pd.read_csv('Messy_Employee_dataset.csv')
pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)
filtered_data = df[(df['Age'].isna()) | (df['Salary'] == 'N/A')]
print(filtered_data)
