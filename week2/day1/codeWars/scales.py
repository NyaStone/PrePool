from random import randint
from functools import reduce

class Scale:
    def __init__(self) -> None:
        self.balls = []
        for i in range(8):
            self.balls.append(1)
        randomNumber = randint(0, 7)
        self.balls[randomNumber] += 1
        print(self.balls)
        self.uses = 4

    def getWeight(self, left: list[int], right: list[int]):
        if self.uses == 0:
            raise Exception('Scale is out of uses')
        leftWeight = reduce(lambda acc, ballIndex: acc + self.balls[ballIndex], left, 0)
        rightWeight = reduce(lambda acc, ballIndex: acc + self.balls[ballIndex], right, 0)
        self.uses -= 1
        if leftWeight > rightWeight:
            return -1
        if rightWeight > leftWeight:
            return 1
        return 0


scale = Scale()

ballIds = [ball for ball  in range(8)]
while len(ballIds) != 1:
    heavy = scale.getWeight(ballIds[0:len(ballIds)//2], ballIds[len(ballIds)//2:len(ballIds)])
    if heavy < 0:
        ballIds = ballIds[0:len(ballIds)//2]
    elif heavy > 0:
        ballIds = ballIds[len(ballIds)//2:len(ballIds)]
print(f'The heaviest ball was ball number {ballIds[0]}')