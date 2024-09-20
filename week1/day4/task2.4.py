for i in range(-30, 31):
    multipleOfTree = i % 3 == 0
    multipleOfFive = i % 5 == 0

    if multipleOfTree and multipleOfTree:
        print('FizzBuzz')
    elif multipleOfTree:
        print('Fizz')
    elif multipleOfFive:
        print('Buzz')
    else:
        print(str(i))