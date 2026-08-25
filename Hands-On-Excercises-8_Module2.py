import csv
import pandas as pd
df = pd.read_csv('Messy_Employee_dataset.csv')
dataframe = pd.DataFrame(df)
failedRecords = 0
totalRecords = len(dataframe)
successfulRecord = 0
failedRecords = dataframe[(dataframe['Age'].isna()) | (dataframe['Salary'].isna())]
failedRecordsCount = len(failedRecords)
successfulRecord = totalRecords - failedRecordsCount
print('Successful Records:' + str(successfulRecord))
print('Failed Records:' + str(failedRecordsCount))
print('Total Records:' + str(totalRecords))
