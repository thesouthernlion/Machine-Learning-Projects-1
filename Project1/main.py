import pandas as pd
from pathlib import Path

fileSource = 'one.csv'
if(Path(fileSource).exists()):
    colName = input("Give me the name of the column you want to print: ")
    dataFrame = pd.read_csv(fileSource)
    columnsList = dataFrame.columns.to_numpy()
    for x in columnsList:
        if colName == x:
            column = dataFrame[colName]
            print(column.values)
        else:
            print("Research Ended")


else:
    print("Error: file not found or doesn't exist")
