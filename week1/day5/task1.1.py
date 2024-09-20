somelist = []

for i in range(5):
    somenumber = ""
    while not somenumber.isnumeric():
        somenumber = input(f'Choose a number ({i + 1}): ')
        if not somenumber.isnumeric():
            print(f'"{somenumber}" is not a number.')
    somelist.append(eval(somenumber))

print(somelist[0])

