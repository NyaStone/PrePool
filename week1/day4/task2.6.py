data = ""
while not data.isdigit():
    data = input("Enter a number: ")

data = int(data)


for number in range(2, (data//2)+1):
    multiples = []
    for maybeMulti in range (data-1, number-1, -1):
        if maybeMulti % number == 0:
            multiples.append(maybeMulti)
    print(multiples)