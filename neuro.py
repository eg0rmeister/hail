'''import math

class Neuro():
    def __init__(self, amount_of_ins:int = 1, amount_of_outs:int = 1, matrix:list = [[1, 1],[1, 1],[1, 1],[1, 1], [1], [1], [1], [1]]):
        self.aoi = amount_of_ins
        self.aoo = amount_of_outs
        self.mx = matrix

    def calculate(self, *ins):
        results = [i for i in ins]
        temp = [0 for i  in range(aoi)]
        for i in range(aoi):
            for j in range(aoi):
                temp[i] += results[j] * mx[i][j]
        results = [1/(1+math.exp(-i)) for i in temp]
        temp = [0 for i in range(aoi)]
        for i in range(aoi):
            for j in range(aoi, 2*aoi):
                temp[i] += 



'''