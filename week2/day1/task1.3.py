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

for i in range(42): 
    burger()
    if i != 41:
        print("\n")
