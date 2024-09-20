some = "Hello world"


def printNth(findex, fstring):
    if len(fstring) > findex:
        print(f'{findex + 1}th char: {fstring[findex]}')
    else:
        print('Index outt of range')

def printLast(fstring):
    length = len(fstring)
    if (length) == 0:
        print('Empty string')
    else:
        print(f'Last character: {fstring[length-1]}')



print(some)

printNth(0, some)
printNth(4, some)

printLast(some)

print(f'"{some[4:9]}"')