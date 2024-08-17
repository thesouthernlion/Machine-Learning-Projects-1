from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
import numpy as np

randomState = int(input("Type the random state to use: "))
dataPtsNum = int(input("Type the number of data points: "))
print("\n")
rows = []
for i in range(dataPtsNum):
    rows.append([float(a) for a in input("Type the values for the feature matrix, separated by spaces: ").split()])
print("\n")
print("The complete row is: ")
print(rows, end="\n")

X = np.array(rows)
y = np.array([int(a) for a in input("Target separated by spaces: ").split()])

# Split the dataset into a training set and test set
X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=randomState)
print("\n")
print('data dimensions', X.shape)
print("\n")
print('test values ', X_test)
print("\n")
# Creating the random forest classifier 
rf = RandomForestClassifier()
rf.fit(X_train, y_train)

first_row = X_test[0]
print("prediction: ", rf.predict([first_row]))
print("true value: ", y_test[0])
