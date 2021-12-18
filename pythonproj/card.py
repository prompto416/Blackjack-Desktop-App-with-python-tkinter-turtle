import random

def drawCard():
    val = ['A', 1, 2, 3, 4, 5, 6, 7, 8, 10, 'J', 'Q', 'K']
    suit = ['club', 'diamond', 'heart', 'spade']

    valPick = val[random.randint(0, len(val) - 1)]
    suitPick = suit[random.randint(0, len(suit) - 1)]
    card = [suitPick, valPick]
    return card

def evalHand(card):
    handSum = 0
    softHand = False
    for i in card:
        if i[1] == 'K' or i[1] == 'Q' or i[1] == 'J':
            handSum += 10
        elif i[1] == 'A':
            if (handSum + 11) > 21:
                handSum += 1
            else:
                handSum += 11

        else:
            handSum += i[1]
        # print(i, handSum)

    return handSum

class Player:
    def __init__(self):
        self.player = Hand()





class Hand:
    def __init__(self):
        self.hand = []


    def Hit(self):
        self.hand.append(drawCard())


    def initializeHand(self):
        for i in range(2):
            self.hand.append(drawCard())



    def seeHand(self):
        return self.hand















