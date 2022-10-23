from random import *

def test_random(n):
    l=[]
    for i in range(100):
        l.append([])
        for j in range(100):
            l[-1].append(0)
    for i in range(n):
        x = randint(0,99)
        l[x][randint(0,99)] += 1
        
    return l
