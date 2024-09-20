from typing import Tuple
from functools import reduce


def getColor(card: str):
    return card[len(card)-1]


def isFlush(cards: Tuple[str,str,str,str,str]):
    color = getColor(cards[0])
    res = True
    index = 1
    while res and index < 5:
        res = color == getColor(cards[index])
        index += 1
    return res

cards1 = ("AS", "3S", "9S", "KS", "4S")
cards2 = ("AD", "4S", "7H", "KS", "10S")
print(cards1)
print(isFlush(cards1))
print(cards2)
print(isFlush(cards2))