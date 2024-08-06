#Calculate Information Gain
tvInitDs = input("Give me the target values separate by a space: ").split()
tvLSplit = input("Give me the target values for the left split: ").split()
tvRSplit = input("Give the target values for the right split: ").split()
print("\n")

def GiniImpurity(arr): 
    counterPositive = 0
    counterNegative = 0
    for i in arr: 
        if i == '1':
            counterPositive = counterPositive + 1
        elif i == '0':
            counterNegative = counterNegative + 1

    giniImpurity = 2 * (counterPositive/len(arr)) * (counterNegative/len(arr))
    giniImpurity = round(giniImpurity,5)
        
    return giniImpurity
#Gini Impurity 
#gini = 2*p*(1-p)
#gini = 2*(a/s)*(b/s)
giInitDs = GiniImpurity(tvInitDs)
print("The gini impurity for the initial set is: ") 
print(giInitDs, end="\n\n")


giLSplit = GiniImpurity(tvLSplit)
print("The gini impurity for the left split is: ") 
print(giLSplit, end="\n\n")

giRSplit = GiniImpurity(tvRSplit)
print("The gini impurity for the right split is: ") 
print(giRSplit, end="\n\n")

informationGain = giInitDs + giLSplit + giRSplit
print("The information gain is: ") 
print(informationGain, end="\n\n")

