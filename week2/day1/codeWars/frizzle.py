def chooseTwo(setSize: int):
    if setSize < 2:
        raise Exception("The set is smaller than a pair")
    return int((setSize * (setSize -1))/2)

print(f'For a set of two: {chooseTwo(2)}')
print(f'For a set of four: {chooseTwo(4)}')