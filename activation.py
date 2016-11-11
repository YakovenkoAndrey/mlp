from function import *

class ActivationFunction:
	
	def __init__(self, activation_function_title):
		if activation_function_title == 'linear':
			self.activation_function = linear
		elif activation_function_title == 'threshold':
			self.activation_function = threshold
		elif activation_function_title == 'symbolic':
			self.activation_function = symbolic
		elif activation_function_title == 'sigmoid':
			self.activation_function = sigmoid
		elif activation_function_title == 'hyperbolic tangent':
			self.activation_function = hyperbolic_tangent
	
	def calculate(self, input_value):
		return self.activation_function(input_value)
