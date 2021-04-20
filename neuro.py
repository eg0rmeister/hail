import math
import pickle
import random
import copy

def sigmoid(x):
    return 1/(1+2**(-x))

class Neuron:
    def __init__(self, k= 1, x= 0, outs= set()):
        self.outs = outs
        self.k = k
        self.x = x
        
    
    def calc(self, x= (0)):
        ret = 0
        temp = []
        for i in self.outs:
            ret += i.calc(x)
        return sigmoid(ret)

    def addNeuron(self, neuron):
        self.outs.add(neuron)
        
    def remNeuron(self, neuron):
        self.outs.remove(neuron)
        
class LastNeuron:
    def __init__(self, k= 0):
        self.k = k
        self.x = 1
        
    def calc(self, x= (0)):
        return sigmoid(x[self.k])

class FirstNeuron:
    def __init__(self, outs = set()):
        self.outs = outs
        self.k = 1
        self.x = 0
        
    def calc(self, x= (0)):
        ret = 0
        for i in self.outs:
            ret += i.calc(x)
        return sigmoid(ret)

    def addNeuron(self, neuron):
        self.outs.add(neuron)
        
    def remNeuron(self, neuron):
        try:
            self.outs.remove(neuron)
        except:
            print(self.outs)
            print(neuron)
            print(neuron in self.outs)


class Neuro():
    def __init__(self, amount_of_ins:int = 1, amount_of_outs:int = 1, score:int = 0):
        self.aoi = amount_of_ins
        self.aoo = amount_of_outs
        self.lasts = set([LastNeuron(i) for i in range(amount_of_ins)])
        self.firsts = set([FirstNeuron() for i in range(amount_of_outs)])
        self.inbetween = set()
        self.connections = set()
        self.score = score
        
    def calculate(self, *ins):
        ret = []
        for i in self.firsts:
            ret.append(i.calc(ins))
        return ret
    
    def mutate(self):
        rannum = random.randint(0, 7)
        if rannum <= 3 and len(self.connections):
            temp = []
            for i in self.connections:
                temp.append(i)
            choice = random.choice(temp)
            a = choice[0]
            b = choice[1]
            a.remNeuron(b)
            self.connections.remove((a, b))
        elif rannum <= 4 and len(self.connections):
            temp = []
            for i in self.connections:
                temp.append(i)
            choice = random.choice(temp)
            a = choice[0]
            b = choice[1]
            temp = Neuron(random.choice((-1, 1)), random.uniform(a.x, b.x), set([b]))
            a.remNeuron(b)
            a.addNeuron(temp)
            self.inbetween.add(temp)
            self.connections.remove((a, b))
            self.connections.add((a, temp))
            self.connections.add((temp, b))
        else:
            a = random.choice((*self.firsts, *self.inbetween))
            while True:
                b = random.choice([*self.inbetween, *self.lasts])
                if b != a and b.x != a.x:
                    break
            if a.x < b.x:
                a.addNeuron(b)
                self.connections.add((a, b))
            elif a.x > b.x:
                b.addNeuron(a)
                self.connections.add((b, a))
        
        
        
        
if __name__ == "__main__":
    nn = Neuro(3, 1)
    m = [nn]
    for i in range(49):
        m.append(copy.deepcopy(nn))
        m[-1].mutate()
    while True:
        scoreboard = {}
        for i in m:
            scoreboard[i.calculate(5, 3, 1)] = i
        nn = scoreboard[max(scoreboard.keys())]
        input(nn.calculate(5, 3, 1))
        m = [nn]
        for i in range(49):
            m.append(copy.deepcopy(nn))
            m[-1].mutate()
            m[-1].mutate()
            m[-1].mutate()
            