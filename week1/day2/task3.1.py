import sys

def extendedDiv(fnum, fdivisor):
    print(fnum/fdivisor)
    print(fnum//fdivisor)
    print(fnum%fdivisor)

def is_integer(arg): 
    try: 
        int(arg)  # Try to convert the argument to an integer 
        return True 
    except ValueError: 
        return False




divisor = "4"
num = "42"

if len(sys.argv) > 1:
    num = sys.argv[1]
if len(sys.argv) > 2:
    divisor = sys.argv[2]
if is_integer(num) and is_integer(divisor):
    num = eval(num)
    divisor = eval(divisor)
    if (divisor != 0):
        extendedDiv(num, divisor)
    else:
        print("Divisor can't be 0")
else:
    print("arguments arent numbers")