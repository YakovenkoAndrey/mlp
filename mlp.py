# from mlp import *
# n = MultiLayerPerceptron([2,2,1])
# n.calculate_template()
# n.training([1,0,0,0])

from random import uniform
from neuron import Neuron

class MultiLayerPerceptron:
    net = []
    weight = []
    input_template = [[1, 1], [1, 0], [0, 1], [0, 0]]

    def __init__(self, net_config):
        for i in range(len(net_config)):
            self.net.append([])
            if i == 0: funtion_title = 'linear'
            else: funtion_title = 'threshold'
            neuron = Neuron(i, funtion_title)
            for j in range(net_config[i]):
                self.net[i].append(neuron)
        for i in range(len(net_config) - 1):
            self.weight.append([])
            for j in range(len(self.net[i])):
                self.weight[i].append([])
                for k in range(len(self.net[i + 1])):
                    self.weight[i][j].append(uniform(.1, .4))
    
    def calculate(self, input_data):
        
        input_value = input_data
        input_weight = []
        output_data = []
        
        # формируем входящие данные в первый слой
        
        for i in range(len(self.net[0])):
            input_weight.append(1)

        # прогоняем первый слой
        
        for i in range(len(self.net[0])):
            
            self.net[0][i].run(input_value, input_weight)
            
        # прогоняем следующие слои
        
        for n in range(len(self.net) - 1):
        
            i = n + 1
            
            # чистим входящие данные
            
            input_value.clear()
            input_weight.clear()        
            
            # формируем входящий данные для следующего слоя
            
            
            for j in range(len(self.net[i - 1])):
                    temp = self.net[i - 1][j].output_value
                    input_value.append(temp)
            
            for j in range(len(self.net[i])):
                input_weight.append([])
                for k in range(len(self.net[i - 1])):
                    temp = self.weight[i - 1][k][j]
                    input_weight[j].append(temp)
                    
            
            # прогоняем следующий слой
            
            for j in range(len(self.net[i])):
            
                self.net[i][j].run(input_value, input_weight[j])
            
            
        temp = len(self.net) - 1
        for i in range(len(self.net[temp])):
            output_data.append(self.net[temp][i].output_value)
                        
        print(output_data)
    
    def calculate_template(self):
        for i in range(len(self.input_template)):
            self.calculate(self.input_template[i])
    
    def training(self, output_template):
        speed = .3
        iteration = 0
        while True:
            iteration += 1
            print(iteration)
            total_error = 0
            for i in range(len(self.input_template)):
                self.calculate(self.input_template[i])
                net_error = []
                weight_delta = []
                for j in range(len(self.net)):
                    net_error.append([])
                    weight_delta.append([])
                    for k in range(len(self.net[j])):
                        weight_delta[j].append([])

                # calculate output layer error++++++++
                last = len(self.net) - 1
                for j in range(len(self.net[last])):
                    correct = output_template[i]
                    received = self.net[last][j].output_value
                    temp_error = correct - received
                    total_error += abs(temp_error)
                    net_error[last].append(temp_error)
                    
                # calculate hidden layers error
                for j in range(len(self.net) - 2):
                    index = len(self.net) - 2 - j
                    for k in range(len(self.net[index])):
                        temp = 0
                        for n in range(len(self.net[index + 1])):
                            a = net_error[index + 1][n]
                            b = self.weight[index][k][n]
                            temp += a * b
                        net_error[index].append(temp)
                    
                                
                
                # calculate weight delta
                for j in range(len(self.net) - 1):
                    for k in range(len(self.net[j])):
                        for n in range(len(self.net[j + 1])):
                            error = net_error[j + 1][n]
                            value = self.net[j][k].output_value
                            temp = speed * error * value
                            weight_delta[j][k].append(temp)
                
                
                # calculate new weight+++++++
                for j in range(len(self.net) - 1):
                    for k in range(len(self.net[j])):
                        for n in range(len(self.net[j + 1])):
                            delta = weight_delta[j][k][n]
                            self.weight[j][k][n] += delta
                
                
                net_error.clear()
                weight_delta.clear()
            if total_error == 0 or iteration == 20:
        #   if iteration == 1:
                break
