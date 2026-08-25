import pandas as pd

df = pd.read_csv('employee_data.csv')
pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)
df['fullName'] = df['FirstName'] + df['LastName'] + df['ADEmail']
df.to_csv('transform.csv', index= False)
