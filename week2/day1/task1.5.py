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
def vergieBurger():
    bread()
    lettuce()
    tomato()
    lettuce()
    tomato()
    bread()

def makeBurgers(num: int, vegie: bool = False):
    if num <= 0:
        print(f'I can\'t do this, {num} is not strictly positive')
        return
    burgerFunct: function = vergieBurger if vegie else burger
    print(f'{num} {"vegie " if vegie else ""}burgers comming up!')
    for i in range(num): 
        burgerFunct()
        if i != num - 1:
            print("\n")

makeBurgers(3, True)