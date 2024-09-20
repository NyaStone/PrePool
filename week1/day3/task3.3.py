firstNum = ""
while not firstNum.isdigit():
    firstNum = input("Please enter a number: ")
    if not firstNum.isdigit():
        print(f'"{firstNum}" is not a number')


secondNum = ""
while not secondNum.isdigit():
    secondNum = input("Please enter another number: ")
    if not secondNum.isdigit():
        print(f'"{secondNum}" is not a number')

print(f'The sum of the provided numbers is: {eval(firstNum) + eval(secondNum)}')