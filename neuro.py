import math
import pickle
import random

def sigmoid(x):
    return 1/(1+2**(-x))

class Neuron:
    def __init__(self, k= 1, x= 0, outs= set()):
        self.outs = outs
        self.k = k
        self.x = x
        
    
    def calc(self, x= (0)):
        ret = 0
        for i in outs:
            ret += i.calc(x)
        return sigmoid(ret)

    def addNeuron(self, neuron):
        self.outs.add(neuron)
        
    def remNeuron(self, neuron):
        self.outs.remove(neuron)
        
class LastNeuron:
    def __init__(self, k= 0):
        self.k = 0
        self.x = 1
        
    def calc(self, x= (0)):
        return sigmoid(x[self.k])

class FirstNeuron(Neuron):
    def __init__(self, outs = set()):
        super.__init__(1, 0, outs)



class Neuro():
    def __init__(self, amount_of_ins:int = 1, amount_of_outs:int = 1):
        self.aoi = amount_of_ins
        self.aoo = amount_of_outs
        self.lasts = set(*[LastNeuron(i) for i in range(amount_of_ins)])
        self.firsts = set(*[FirstNeuron() for i in range(amount_of_outs)])
        self.inbetween = set()
        self.connections = set()
        
    def calculate(self, *ins):
        ret = 0
        for i in firsts:
            ret.append(i.calc(ins))
        return ret
    
    def mutate(self):
        rannum = random.randint(0, 2)
        if rannum == 0 and len(self.connections):
            a, b = *random.choice(self.connections)
            a.remNeuron(b)
            self.connections.remove((a, b))
        elif rannum == 1 and len(self.connections):
            a, b = *random.choice(self.connections)
            temp = Neuron(random.choice((-1, 1)), random.uniform(a.x, b.x), b)
            a.remNeuron(b)
            a.addNeuron(temp)
            self.inbeetween.add(temp)
            self.connections.remove((a, b))
            self.connections.add((a, temp))
            self.connections.add((temp, b))
        else:
            a = random.choice((*firsts, *inbeetween))
            while True:
                b = random.choice([*inbeetween, *lasts])
                if b != a and b.x != a.x:
                    break
            if a.x < b.x:
                a.addNeuron(b)
                self.connections.add((a, b))
            elif a.x > b.x:
                b.addNeuron(a)
                self.connections.add((b, a))
            
            
                
                    

        
        
