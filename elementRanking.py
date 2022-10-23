d = {}
def rank(x):

    l = x.split("\n")

    d = {}

    largest = 0
    for i in l:
        if i in d:
            d[i] += 1            
        else:
            d[i] = 1
        if d[i] > largest:
                largest = d[i]

    while largest > 0:
        for i in d:
            if d[i] == largest:
                print(d[i], i)
        largest -= 1

def data(x):
    global d
    
    l = x.split("\n")

    d = {1:0,2:0,3:0,4:0,5:0}
    for i in l:
        a = input(i + ": ")
        while not a.isnumeric():
            a = input("try again: ")
        d[int(a)]+=1
            

    print(d)
