from math import exp

def linear(input_value):
	return input_value

def threshold(input_value):
	if input_value >= .5: return 1
	else: return 0

def symbolic(input_value):
	if input_value > 0: return 1
	else: return -1

def sigmoid(input_value):
	print(input_value)
	return 1 / (1 + exp(-input_value))

def hyperbolic_tangent(input_value):
	numerator = exp(input_value) - exp(-input_value)
	denominator = exp(input_value) + exp(-input_value)
	return numerator / denominator
