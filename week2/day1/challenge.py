import time

def fastPower(num: int, exponent: int):
    res = 1
    while exponent > 0:
        if (exponent % 2 == 0):
            # if the exponent is even, calc half and reduce the exponent size by half
            num *= num
            exponent = exponent // 2
        else:
            # if the exponent is odd, extract 1 of the exponent to the res and make it even
            exponent -= 1
            res *= num
            # now that exponent is even, the previous provedure can be done
            exponent = exponent // 2
            num *= num
    return res

def slowPower(num: int, exponent: int):
    res = 1
    for i in range(exponent):
        res *= num
    return res


startTime = time.time()
val = 42**84
print(f'regular 42^84 took {time.time() - startTime}s ({val})\n')
startTime = time.time()
val = 42**168
print(f'regular 42^168 took {time.time() - startTime}s ({val})\n')
startTime = time.time()
val = slowPower(42, 84)
print(f'slow 42^84 took {time.time() - startTime}s ({val})\n')
startTime = time.time()
val = slowPower(42, 168)
print(f'slow 42^168 took {time.time() - startTime}s ({val})\n')
startTime = time.time()
val = fastPower(42, 84)
print(f'fast 42^84 took {time.time() - startTime}s ({val})\n')
startTime = time.time()
val = fastPower(42, 168)
print(f'fast 42^168 took {time.time() - startTime}s ({val})\n')
