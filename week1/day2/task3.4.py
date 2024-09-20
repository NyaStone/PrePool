import sys

def enitrePart(fnum):
    numStr = str(fnum)
    inte = numStr.split(".")
    return eval(inte[0])


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
    print(enitrePart(eval(num)))
else:
    print("argument is not a number")