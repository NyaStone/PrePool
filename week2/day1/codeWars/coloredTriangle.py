def point(firstColor: str, secondColor: str):
    rgb = "RGB"
    if firstColor not in rgb or secondColor not in rgb:
        raise Exception("Wrong character imput")
    if firstColor == secondColor:
        return firstColor
    else:
        color = filter(lambda x: x != firstColor and x != secondColor, rgb)
        for c in color:
            return c
        raise Exception('Color not found')
    
def splitIntoPairs(someString):
    res = []
    if len(someString) == 2:
        return [(someString[0], someString[1])]
    for i in range(len(someString) - 1):
        res.append((someString[i], someString[i+1]))
    return res

def buildTriangle(topline:str):
    if len(topline) == 1:
        return topline
    pairs = splitIntoPairs(topline)
    newLine = ""
    for pair in pairs:
        newLine += point(pair[0], pair[1])
    return buildTriangle(newLine)

test = 'RRGBRGBB'
print(test)
res = buildTriangle(test)
print(res)