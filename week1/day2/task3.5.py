import sys

def decimalPart(fnum):
    numStr = str(fnum)
    splitnum = numStr.split(".")
    res = 0
    if len(splitnum) > 1:
        res = eval(splitnum[1])

    return res


def is_number(arg): 
    try: 
        eval(arg)  # Try to convert the argument to an number 
        return True 
    except ValueError: 
        return False


num = "12.24"

if len(sys.argv) > 1:
    num = sys.argv[1]
if is_number(num):
    print(decimalPart(eval(num)))
else:
    print("argument is not a number")