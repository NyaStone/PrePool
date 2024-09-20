some = "Hello world"


def printNth(findex, fstring):
    if len(fstring) > findex:
        print(fstring[findex])
    else:
        print('Index outt of range')

print(some)

printNth(0, some)
printNth(4, some)
