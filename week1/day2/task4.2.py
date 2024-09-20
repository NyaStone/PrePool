import sys

def aproximatePi(fiterations):    
    num = 1 + (fiterations * 2)
    fracTotal = (num**2)/6
    num += -2
    while num > 0:
        fracTotal = (num**2)/(6+fracTotal)
        num += -2
    return fracTotal + 3









def is_integer(arg): 
    try: 
        int(arg)  # Try to convert the argument to an integer 
        return True 
    except ValueError: 
        return False
    

iterations = "10"    
if len(sys.argv) > 1:
    iterations = sys.argv[1]
if is_integer(iterations):
    print(aproximatePi(eval(iterations)))
else:
    print("argument is not a number")