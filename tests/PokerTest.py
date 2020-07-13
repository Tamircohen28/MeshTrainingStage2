from enum import IntEnum
from helloworld.PokerHand import *
import os


class Result(IntEnum):
    Loss = 0x00
    Tie = 0x01
    Win = 0x02


specific_cases = [
    ["Highest straight flush wins",         Result.Loss,    "2H 3H 4H 5H 6H",   "KS AS TS QS JS"],
    ["Straight flush wins of 4 of a kind",  Result.Win,     "2H 3H 4H 5H 6H",   "AS AD AC AH JD"],
    ["Highest 4 of a kind wins",            Result.Win,     "AS AH 2H AD AC",   "JS JD JC JH 3D"],
    ["4 Of a kind wins of full house",      Result.Loss,    "2S AH 2H AS AC",   "JS JD JC JH AD"],
    ["Full house wins of flush",            Result.Win,     "2S AH 2H AS AC",   "2H 3H 5H 6H 7H"],
    ["Highest flush wins",                  Result.Win,     "AS 3S 4S 8S 2S",   "2H 3H 5H 6H 7H"],
    ["Flush wins of straight",              Result.Win,     "2H 3H 5H 6H 7H",   "2S 3H 4H 5S 6C"],
    ["Equal straight is tie",               Result.Tie,     "2S 3H 4H 5S 6C",   "3D 4C 5H 6H 2S"],
    ["Straight wins of three of a kind",    Result.Win,     "2S 3H 4H 5S 6C",   "AH AC 5H 6H AS"],
    ["3 Of a kind wins of two pair",        Result.Loss,    "2S 2H 4H 5S 4C",   "AH AC 5H 6H AS"],
    ["2 Pair wins of pair",                 Result.Win,     "2S 2H 4H 5S 4C",   "AH AC 5H 6H 7S"],
    ["Highest pair wins",                   Result.Loss,    "6S AD 7H 4S AS",   "AH AC 5H 6H 7S"],
    ["Pair wins of nothing",                Result.Loss,    "2S AH 4H 5S KC",   "AH AC 5H 6H 7S"],
    ["Highest card loses",                  Result.Loss,    "2S 3H 6H 7S 9C",   "7H 3C TH 6H 9S"],
    ["Highest card wins",                   Result.Win,     "4S 5H 6H TS AC",   "3S 5H 6H TS AC"],
    ["Equal cards is tie",                  Result.Tie,     "2S AH 4H 5S 6C",   "AD 4C 5H 6H 2C"],
]

if __name__ == '__main__':
    index = 0
    for test in specific_cases:
        p1 = PokerHand(test[2])
        p2 = PokerHand(test[3])

        result = p1.compare(p2)

        if result == test[1]:
            print("&> Test [{}] Pass".format(index))
        else:
            print("&> Test [{}] Failed!\n{}".format(index, test[0]))
            os.system('pause')

        index += 1
