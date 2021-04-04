import math
import pickle
import random

class Neuro():
    def __init__(self, amount_of_ins:int = 1, amount_of_outs:int = 1, matrix:list = [[[1]], [[1]], [[1]]]):
        self.aoi = amount_of_ins
        self.aoo = amount_of_outs
        self.mx = matrix

    def remember(self, filename= "memory.txt"):
        with open(filename, "rb") as f:
            self.mx = pickle.load(f)
            
    def mutate(self, max_amount, lim= 99999999, chance= 100):
        if random.randint(1, 100) <= chance:
            max_amount = abs(max_amount)
            for i in range(len(self.mx)):
                for j in range(len(self.mx[i])):
                    for k in range(len(self.mx[i][j])):
                        self.mx[i][j][k] += random.uniform(-max_amount, max_amount)
                        if self.mx[i][j][k] > lim:
                            print("fuck")
                            self.mx[i][j][k] = lim
                        elif self.mx[i][j][k] < -lim:
                            print("fuck")
                            self.mx[i][j][k] = -lim 

        
    def sigmoid(self, x):
        try:
            return 1/(1+math.exp(-x))    
        except OverflowError:
            print(x, "zhopa")
            input()
            return False

    
    
    
    def calculate(self, *ins):
        #print(ins)
        results = [self.sigmoid(i) for i in ins]
        temp = [0 for i  in range(self.aoi)]
        for i in range(self.aoi):
            for j in range(self.aoi):
                temp[i] += results[j] * self.mx[0][i][j]
        for i in temp:
            results = [self.sigmoid(i) for i in temp]
        temp = [0 for i in range(self.aoi)]
        for i in range(self.aoi):
            for j in range(self.aoi):
                temp[i] += results[j] * self.mx[1][i][j]
        results = [self.sigmoid(i) for i in temp]
        ret = [0 for _ in range(self.aoo)]
        for i in range(self.aoo):
            for j in range(self.aoi):
                ret[i] += results[j] * self.mx[2][i][j]
            ret[i] = self.sigmoid(ret[i])
        return ret
        



