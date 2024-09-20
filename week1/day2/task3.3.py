import sys

def digitSum(fnum):
    numStr = str(fnum)
    total = 0
    for i in numStr:
        total += int(i)
    return total


def is_integer(arg): 
    try: 
        int(arg)  # Try to convert the argument to an integer 
        return True 
    except ValueError: 
        return False


num = "123434565"

if len(sys.argv) > 1:
    num = sys.argv[1]
if is_integer(num):
    print(digitSum(eval(num)))
else:
    print("argument is not a number")