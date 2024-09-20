def negationValue(negation: str, base: any):
    res = not not base # making sure the base is boolean
    for char in negation:
        if char == "!":
            res = not res
    return res


print(negationValue("!", False))
print(negationValue("!!!!!", True))
print(negationValue("!!", ["Some"]))
print(negationValue("", ["Some"]))