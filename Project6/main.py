import math
# A neuron computations 
# w1 and w2 are the weights
# b is the bias

# Logistic regression formula
# w1x1 + w2x2 + b

# Activation function 
# y = f(w1x1 + w2x2 + b)

# Sigmoid function 
# sigmoid(x) = 1/1+e^-x

w1, w2, b, x1, x2 = [float(x) for x in input().split()]

formula = (w1 * x1) + (w2 * x2) + b

x = formula * -1

print(x)

sigmoid = (1) / (1 + math.exp(formula * -1))

print(sigmoid)
