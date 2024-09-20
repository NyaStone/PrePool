def removeNines(someString: str):
    if len(someString) < 3:
        return someString
    res = someString[0]
    for index in range(1, len(someString) - 1):
        if not someString[index] == "9":
            res += someString[index]
        elif not someString[index-1] == "7":
            res += someString[index]
        elif not someString[index+1] == "7":
            res += someString[index]
    res += someString[len(someString)-1]
    return res

print(removeNines("79712312"))
print(removeNines("79797"))
print(removeNines("797997"))
