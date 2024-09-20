def askForNum():
    num = ""
    while not num.isdigit():
        num = input("Please enter a whole number: ")
        if not num.isdigit():
            print(f'"{num}" is not a number')
    return int(num)

theNum = askForNum()
print(f'"{theNum}" is of type {type(theNum)}')