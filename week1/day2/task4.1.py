
import time

def piCalculator(fnum):
    divisor = 1
    signer = 1
    fracTotal = 0
    res = 0
    while True:
        time.sleep(1)
        frac = signer/divisor
        fracTotal += frac
        res = 4*fracTotal
        print(res)
        signer *= -1
        divisor += 2


print(piCalculator(8))