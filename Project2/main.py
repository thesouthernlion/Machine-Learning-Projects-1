from sklearn.linear_model import LogisticRegression
import pandas as pd

nDataPoints = int(input("Type the number of values for the data matrix -> "))
rowValues = []
for i in range(nDataPoints):
    rowValues.append([float(item) for item in input("Type the row values separate by space -> ").split()])

print("Row values")
print(rowValues, end="\n\n")
df1 = pd.DataFrame(rowValues, columns=['a', 'b'])  
print("Data Frame")
print(df1, end="\n\n")

targetValues = [int(item) for item in input("Type the 6 digit values (0-1) for the targets -> ").split()]
print("Target values")
print(targetValues, end="\n\n")

datapoint = [float(item) for item in input("Type the single datapoint -> ").split()]
print("The Data Point")
print(datapoint, end="\n\n")

model = LogisticRegression()
model.fit(df1, targetValues)

print(model.coef_, model.intercept_)
print("Prediction for ", datapoint)

print(model.predict([datapoint]), end='\n\n')
