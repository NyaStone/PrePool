import sys

def maths(frange, fexponent):
    total = 0
    num = ""

    for i in range(frange):
        num += "1" 
        total += eval(num)


    print(total**fexponent)


def is_integer(arg): 
    try: 
        int(arg)  # Try to convert the argument to an integer 
        return True 
    except ValueError: 
        return False




exponent = "1"
therange = "10"

if len(sys.argv) > 1:
    therange = sys.argv[1]
if len(sys.argv) > 2:
    exponent = sys.argv[2]
if is_integer(therange) and is_integer(exponent):
    maths(eval(therange), eval(exponent))
else:
    print("arguments arent numbers")