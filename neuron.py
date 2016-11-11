from activation import ActivationFunction

class Neuron:
	
	def __init__(self, layer_number, title):
		self.layer_number = layer_number
		self.activation_function = ActivationFunction(title)
	
	def run(self, input_value, input_value_weight):
		self.input_value = input_value
		if self.layer_number == 0: temp = input_value[0]
		else:
			self.input_value_weight = input_value_weight
			self.sum = 0
			for i in range(len(input_value)):
				self.sum += input_value[i] * input_value_weight[i]
			temp = self.sum
		self.output_value = self.activation_function.calculate(temp)
