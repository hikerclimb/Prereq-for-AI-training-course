import pandas as pd

df = pd.read_csv("Employee.csv")
filtered_df = df[df['ExperienceInCurrentDomain'] > 2]
filtered_df.to_csv('experienced.csv', index=False)
