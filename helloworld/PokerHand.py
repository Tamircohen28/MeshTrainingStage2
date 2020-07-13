import sys

C_NUM_OF_CARDS = 5

C_HANDS_DICT = {
    'HighCard': 1,
    'Pair': 2,
    'TwoPairs': 3,
    'ThreeOfaKind': 4,
    'Straight': 5,
    'Flush': 6,
    'FullHouse': 7,
    'FourOfaKind': 8,
    'StraightFlush': 9,
    'RoyalFlush': 10
}

C_SYMBOL_DICT = {
    '2': 2,
    '3': 3,
    '4': 4,
    '5': 5,
    '6': 6,
    '7': 7,
    '8': 8,
    '9': 9,
    'T': 10,
    'J': 11,
    'Q': 12,
    'K': 13,
    'A': 14
}

C_NUM_POS = 0
C_TYPE_POS = 1


class PokerHand:
    def __init__(self, cards):
        self.cards = cards.split(" ")
        self.series = []
        self.highest = 0
        self.score = 0
        self.get_highest_card()
        self.numbers = self.get_same(C_NUM_POS)
        self.shapes = self.get_same(C_TYPE_POS)
        self.sort_numbers()
        self.calc_hand()

        if (len(self.cards)) != C_NUM_OF_CARDS:
            sys.exit("Num of cards has to be {}, given num was {}".format(C_NUM_OF_CARDS, len(self.cards)))

    def sort_numbers(self):

        new = []
        while self.numbers:
            highest = "02"

            for num in self.numbers:
                if int(num[0]) > int(highest[0]):
                    highest = num
                elif int(num[0]) == int(highest[0]):
                    if C_SYMBOL_DICT[num[1]] > C_SYMBOL_DICT[highest[1]]:
                        highest = num

            self.numbers.remove(highest)
            new.append(highest)

        self.numbers = new

    def get_same(self, index):
        """
        counting the number of number / symbols in the hand
        :param index: index in card
        :return: None, update object
        """
        series = []
        done_num = []

        for i in range(len(self.cards)):
            # ignore numbers i already saw
            if self.cards[i][index] in done_num:
                continue

            done_num.append(self.cards[i][index])
            counter = 0

            for j in range(len(self.cards)):
                if self.cards[i][index] == self.cards[j][index]:
                    counter += 1

            series.append(str(counter) + self.cards[i][index])

        return series

    def is_sequence(self):
        """
        checks if the numbers i have are sequential
        :return: bool
        """
        counter = 0
        for i in range(len(self.numbers)):
            for j in range(len(self.numbers)):
                # found the next number
                if C_SYMBOL_DICT[self.numbers[i][1]] + 1 == C_SYMBOL_DICT[self.numbers[j][1]]:
                    counter += 1
                    break

        if counter == len(self.cards) - 1:
            return True

        return False

    def got_flush(self):
        return len(self.shapes) == 1

    def get_highest_card(self):
        highest = 0
        for card in self.cards:
            if C_SYMBOL_DICT[card[C_NUM_POS]] > highest:
                highest = C_SYMBOL_DICT[card[C_NUM_POS]]

        self.highest = highest

    def calc_hand(self):
        alone = []
        pairs = []
        threesome = []
        foursome = []
        best_hand = 0

        # divide into groups
        for num in self.numbers:
            if int(num[0]) == 1:
                alone.append(num[1])
            if int(num[0]) == 2:
                pairs.append(num[1])
            if int(num[0]) == 3:
                threesome.append(num[1])
            if int(num[0]) == 4:
                foursome.append(num[1])

        # four of a kind
        if len(foursome) > 0:
            best_hand = C_HANDS_DICT['FourOfaKind']

        # three of a kind
        elif len(threesome) > 0:
            # full house
            if len(pairs) > 0:
                best_hand = C_HANDS_DICT['FullHouse']

            else:
                best_hand = C_HANDS_DICT['ThreeOfaKind']

        # pair
        elif len(pairs) > 0:
            # two pair
            if len(pairs) > 1:
                best_hand = C_HANDS_DICT['TwoPairs']
            else:
                best_hand = C_HANDS_DICT['Pair']
        # high card
        else:
            best_hand = C_HANDS_DICT['HighCard']

        if self.got_flush():
            if self.is_sequence():
                # Royal Flush
                if self.highest == C_SYMBOL_DICT["A"]:
                    best_hand = C_HANDS_DICT['RoyalFlush']

                # Straight Flush
                else:
                    best_hand = C_HANDS_DICT['StraightFlush']

            # flush, check if im the best
            if C_HANDS_DICT['Flush'] > best_hand:
                best_hand = C_HANDS_DICT['Flush']

        if self.is_sequence():
            # straight , check if im the best
            if C_HANDS_DICT['Straight'] > best_hand:
                best_hand = C_HANDS_DICT['Straight']

        self.score = best_hand

    def compare(self, other):
        """
        compares between hands
        :param other: another hand
        :return: 1 if self won, -1 if other won, 0 in a tie
        """
        if self.score > other.score:
            return 2
        elif self.score < other.score:
            return 0
        # same hands, lets check kickers
        else:
            for i in range(len(self.numbers)):
                if C_SYMBOL_DICT[self.numbers[i][1]] > C_SYMBOL_DICT[other.numbers[i][1]]:
                    return 2
                elif C_SYMBOL_DICT[self.numbers[i][1]] < C_SYMBOL_DICT[other.numbers[i][1]]:
                    return 0

        return 1


if __name__ == '__main__':
    p1 = PokerHand("9s Ks 4s Js Ts")
    p2 = PokerHand("9s Ks 3s Js Ts")
    print(p1.compare(p2))
