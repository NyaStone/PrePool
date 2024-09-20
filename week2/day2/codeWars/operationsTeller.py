def findOperation(firstNum: int, secondNum: int, result: int):
    if firstNum + secondNum == result:
        return "addition"
    if firstNum - secondNum == result:
        return "substraction"
    if firstNum * secondNum == result:
        return "multiplication"
    if firstNum // secondNum == result:
        return "division"
    raise Exception(f'"{firstNum}" and "{secondNum}" are not related to "{result}"')

def findOperations(sequence:str) -> None:
    splitSequence = sequence.split(" ")
    for value in splitSequence:
        if not value.isnumeric():
            raise Exception("Invalid sequence")
    res = findOperation(int(splitSequence[0]), int(splitSequence[1]), int(splitSequence[2]))
    for i in range(3, len(splitSequence)):
        res += f', {findOperation(int(splitSequence[i-2]), int(splitSequence[i-1]), int(splitSequence[i]))}'
    return res
        


print(findOperations(input("Input your number sequence:\n")))