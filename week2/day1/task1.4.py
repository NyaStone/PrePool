def bread () :
    print ("<//////////>")
def lettuce () :
    print ("~~~~~~~~~~~~")
def tomato () :
    print ("O O O O O O")
def ham () :
    print ("============")

def burger():
    bread()
    lettuce()
    tomato()
    ham(); ham()
    bread()

def makeBurgers(num: int):
    if num <= 0:
        print(f'I can\'t do this, {num} is not strictly positive')
        return
    for i in range(num): 
        burger()
        if i != num - 1:
            print("\n")

makeBurgers(0)