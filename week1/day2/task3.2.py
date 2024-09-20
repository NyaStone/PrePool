import sys


def evenfinder(fnum):
    if fnum == 0:
        print("0 is neither odd nor even")
    elif fnum%2 == 0:
        print(str(fnum) + " is event")
    else:
        print(str(fnum) + " is odd")



def is_integer(arg): 
    try: 
        int(arg)  # Try to convert the argument to an integer 
        return True 
    except ValueError: 
        return False




num = "0"

if len(sys.argv) > 1:
    num = sys.argv[1]
if is_integer(num):
    evenfinder(eval(num))
else:
    print("argument is not a number")