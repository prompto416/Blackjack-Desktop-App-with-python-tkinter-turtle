import random
import abc

class Deck:

    def __init__(self):

        self.val = ['A',2, 3, 4, 5, 6, 7, 8,9, 10, 'J', 'Q', 'K']
        self.suit = ['club', 'diamond', 'heart', 'spade']
    def drawCard(self):
        valPick = self.val[random.randint(0, len(self.val) - 1)]
        suitPick = self.suit[random.randint(0, len(self.suit) - 1)]
        card = [suitPick, valPick]
        return card

class Hand(Deck):
    def __init__(self):
        super().__init__()
        self.hand = []


    def Hit(self):
        self.hand.append(self.drawCard())


    def initializeHand(self):
        for i in range(2):
            self.Hit()

    def seeHand(self):
        return self.hand

    def evalHand(self):
        handSum = 0

        for i in self.hand:
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

    def clearHand(self):
        self.hand = []

    def restartHand(self):
        self.clearHand()
        self.initializeHand()

class Player(Hand,abc.ABC):
    def __init__(self):
        super().__init__()

    @abc.abstractmethod
    def initializeHand(self):
        pass



class BlackjackPlayer(Player):
    def __init__(self):
        super().__init__()
        self.initializeHand()
    def initializeHand(self):
        for i in range(2):
            self.Hit()



class Dealer(Player):
    def __init__(self):
        super().__init__()
        self.initializeHand()
    def initializeHand(self):
        self.Hit()
    def dealerPlay(self):
        b = self.evalHand()
        if b < 5:
            dealerChoice = random.choice([2,3])
        elif b > 5 and b < 14:
            dealerChoice = 2

        elif b > 14 and b <= 17:
            dealerChoice = random.choice([0,1])
        elif b > 17:
            dealerChoice = 0
        else:
            dealerChoice= random.choice([0,1,2,3])

        for i in range(dealerChoice):
            self.Hit()







def bustCheck(score):

    if score > 21:
        return True
    if score <= 21:
        return False

def gameCheck(p1,p2):


    if bustCheck(p1) == True:
        print('Busted! You LOSE!')
        return True

    elif bustCheck(p2) == True:
        print('Dealer BUST! You Win!')
        return True
    elif (bustCheck(p1) and bustCheck(p2)) == True:
        print('Still, You LOSE!')
        return True
def winCheck(p1,p2):
    if p1 > p2:
        print('You WIN')
    elif p1 == p2:
        print('ITS A DRAW!')
    else:
        print('You LOSE!')
def blackjack(p1,p2):
    if p1 == 21 and p2 != 21:
        print('You WIN')
        return True
    elif p1 != 21 and p2 == 21:
        print('You LOSE ')
        return True
    elif p1 == 21 and p2 == 21:
        print('DRAW')
        return True
    elif p1 > 21 and p2 > 21 :
        print('Still,You LOSE')
        return True

# p1 = BlackjackPlayer()
# dealer = Dealer()
#
# cmd = 0
# while cmd != 'q':
#     a = p1.evalHand()
#     b = dealer.evalHand()
#
#
#
#
#
#
#
#     print(f"Your Score: {p1.evalHand()}")
#     print(f"Your Hand: {p1.seeHand()}")
#     print(f"Dealer Score: {dealer.evalHand()}")
#     print(f"Dealer Hand: {dealer.seeHand()}")
#
#
#     if  blackjack(a,b) == True:
#         p1.restartHand()
#         dealer.restartHand()
#         continue
#     if gameCheck(a,b) == True:
#         p1.restartHand()
#         dealer.restartHand()
#         continue
#
#     cmd = input("Enter your command: ")
#     if cmd == 'h':
#         p1.Hit()
#
#
#
#
#     elif cmd == 's':
#         dealer.dealerPlay()
#         print(f"Dealer Score: {dealer.evalHand()}")
#         print(f"Dealer Hand: {dealer.seeHand()}")
#
#         if gameCheck(p1.evalHand(),dealer.evalHand()) == True:
#             pass
#
#         else:
#             if p1.evalHand() > dealer.evalHand():
#                 print('You WIN')
#             elif p1.evalHand() == dealer.evalHand():
#                 print('ITS A DRAW!')
#             else:
#                 print('You LOSE!')
#
#
#         p1.restartHand()
#         dealer.restartHand()
#
#     elif cmd == 'q':
#         pass
#     else:
#         print('Invalid Input')
#         continue

def main():
    p1 = BlackjackPlayer()
    dealer = Dealer()

    cmd = 0
    while cmd != 'q':
        a = p1.evalHand()
        b = dealer.evalHand()

        print(f"Your Score: {p1.evalHand()}")
        print(f"Your Hand: {p1.seeHand()}")
        print(f"Dealer Score: {dealer.evalHand()}")
        print(f"Dealer Hand: {dealer.seeHand()}")

        if blackjack(a, b) == True:
            p1.restartHand()
            dealer.restartHand()
            continue
        if gameCheck(a, b) == True:
            p1.restartHand()
            dealer.restartHand()
            continue

        cmd = input("Enter your command: ")
        if cmd == 'h':
            p1.Hit()




        elif cmd == 's':
            dealer.dealerPlay()
            print(f"Dealer Score: {dealer.evalHand()}")
            print(f"Dealer Hand: {dealer.seeHand()}")

            if gameCheck(p1.evalHand(), dealer.evalHand()) == True:
                pass

            else:
                if p1.evalHand() > dealer.evalHand():
                    print('You WIN')
                elif p1.evalHand() == dealer.evalHand():
                    print('ITS A DRAW!')
                else:
                    print('You LOSE!')

            p1.restartHand()
            dealer.restartHand()

        elif cmd == 'q':
            pass
        else:
            print('Invalid Input')
            continue



































