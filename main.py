from card import *
import time
import turtle
import tkinter as tk
import winsound


class BlackJackScreen:
    def __init__(self):

        self.player = BlackjackPlayer()
        self.dealer = Dealer()
        self.root = tk.Tk()
        self.root.title('Python Tkinter+Turtle BlackJack')
        self.root.iconbitmap(r'card.ico')
        self.canvas = tk.Canvas(self.root)
        self.canvas.config(width=800, height=600)
        self.canvas.pack()
        self.hitCount = -300
        self.dealerCount = -400
        self.updateCount = 90

        button_hit = tk.Button(self.root, text="Hit", width=5,height=0,command=self.hitButton)
        button_hit.pack()
        button_stand = tk.Button(self.root, text="Stand",width=5,height=0,command=self.standButton)
        button_stand.pack()







    def displayStart(self,yourHand,dealerHand):
        yourlst = self.displayHand(yourHand)

        dealst = self.displayHand(dealerHand)
        try:
            winsound.PlaySound('swipe', winsound.SND_FILENAME)
        except:
            print('Warning: Missing Audio File')



        self.t.speed(5)
        self.screen.addshape('cardbacktest.gif')
        self.t.shape('cardbacktest.gif')
        self.t.goto(-300,-100)
        self.t.stamp()
        self.t.forward(100)


        previous = 0
        for i in yourlst:
            try:
                self.t.shape(i)

                self.t.forward(100)
                self.t.stamp()
            except:
                self.screen.addshape(i)
                self.t.shape(i)
                self.t.forward(100)
                self.t.stamp()





        self.t.shape('cardbacktest.gif')

        self.t.goto(-300,200)


        self.t.stamp()
        self.t.speed(4)

        self.t.forward(100)

        for i in dealst:
            try:
                self.t.shape(i)

                self.t.forward(100)
                self.t.stamp()
            except:

                self.screen.addshape(i)
                self.t.shape(i)
                self.t.forward(100)
                self.t.stamp()
        self.t.shape('arrow')
        self.t.hideturtle()


        self.t.speed(0)

        self.t.goto(-105,-300)
        self.t.write("Player Score:"+str(self.player.evalHand()), font=("Courier New", 16, "bold"))
        self.t.color('red')
        self.t.goto(-105, -280)
        self.t.write("Dealer Score:" + str(self.dealer.evalHand()), font=("Courier New", 16, "bold"))

        # print(self.player.seeHand())
        # print(self.dealer.seeHand())





    def displayHand(self,hand):
        displaylst = []
        for card in hand:
            displaylst.append(card[0]+str(card[1])+'.gif')
        return displaylst
    def bustCheck(self,buster):

        if buster > 24:
            return True
        else:
            return False
    def drawHit(self,card):
        card = card[0]+str(card[1])+'.gif'
        try:
            self.t.shape(card)
            try:
                winsound.PlaySound('swipe', winsound.SND_FILENAME)
            except:
                print('Warning: Missing Audio File')


            self.t.forward(400)
            self.t.stamp()
        except:

            self.screen.addshape(card)
            self.t.shape(card)
            try:
                winsound.PlaySound('swipe', winsound.SND_FILENAME)
            except:
                print('Warning: Missing Audio File')


            self.t.forward(400)
            self.t.stamp()
    def dealerHit(self,card):
        card = card[0]+str(card[1])+'.gif'

        try:
            self.t.shape(card)

            self.t.fd(100)
            self.t.stamp()
        except:

            self.screen.addshape(card)
            self.t.shape(card)

            self.t.fd(100)
            self.t.stamp()

    def RestartScreen(self):
        try:
            winsound.PlaySound('level', winsound.SND_FILENAME)
        except:
            print('Warning: Missing Audio File')



        self.hitCount = -300
        self.updateCount = 90
        self.dealerCount = -400
        self.player = BlackjackPlayer()
        self.dealer = Dealer()
        self.screen.clear()
        self.run()

    def updateScore(self,robusta):
        if robusta == True:
            self.t.hideturtle()
            self.t.color('red')
            self.t.goto(self.updateCount, -300)
            self.t.write(str(self.player.evalHand())+" Busted!!" , font=("Courier New", 16, "bold"))
            self.t.goto(-160,0)
            self.t.write("YOU LOSE!!" , font=("Courier New", 40, "bold"))
            try:
                winsound.PlaySound('lose', winsound.SND_FILENAME)
            except:
                print('Warning: Missing Audio File')




        else:
            self.t.color('black')

            self.t.hideturtle()
            self.t.penup()
            self.t.goto(self.updateCount, -300)


            self.t.forward(3)
            self.t.write("," + str(self.player.evalHand()), font=("Courier New", 16, "bold"))
        self.updateCount += 50
    def updateDealer(self,robusta):
        if robusta == True:
            self.t.hideturtle()
            self.t.color('red')
            self.t.goto(87, -280)
            self.t.write(','+str(self.dealer.evalHand()) +"Busted", font=("Courier New", 16, "bold"))
            self.t.goto(-160,0)
            self.t.write("YOU WIN!!" , font=("Courier New", 40, "bold"))
            try:
                winsound.PlaySound('win', winsound.SND_FILENAME)
            except:
                print('Warning: Missing Audio File')



        else:
            self.t.hideturtle()
            self.t.color('red')
            self.t.goto(87, -280)
            self.t.write(','+str(self.dealer.evalHand()), font=("Courier New", 16, "bold"))
    def win_lose(self,det):
        if det == 1:
            self.t.goto(-160, 0)
            self.t.write("YOU WIN!!", font=("Courier New", 40, "bold"))
            try:
                winsound.PlaySound('win', winsound.SND_FILENAME)
            except:

                print('Warning: Missing Audio File')


        elif det == 2:
            self.t.goto(-140, 0)
            self.t.write("DRAW!!", font=("Courier New", 40, "bold"))
            try:
                winsound.PlaySound('win', winsound.SND_FILENAME)
            except:
                print('Warning: Missing Audio File')


        else:
            self.t.goto(-160, 0)
            self.t.write("YOU LOSE!!", font=("Courier New", 40, "bold"))
            try:
                winsound.PlaySound('lose', winsound.SND_FILENAME)
            except:
                print('Warning: Missing Audio File')






    def determine(self):
        a = self.player.evalHand()
        b = self.dealer.evalHand()


        if a > b:
            self.win_lose(1)
        elif b > a:
            self.win_lose(0)
        elif a == b:
            self.win_lose(2)


    def initializeScreen(self):
        self.screen = turtle.TurtleScreen(self.canvas)


        self.t = turtle.RawTurtle(self.screen)
        self.screen.bgcolor('#30c744')
        self.t.penup()
    def hitButton(self):

        self.player.Hit()
        ourHand = self.player.seeHand()
        self.t.hideturtle()
        self.t.speed(0)
        self.t.showturtle()
        self.t.goto(self.hitCount, -100)
        self.hitCount+=100
        self.t.speed(7)

        self.drawHit(ourHand[-1])
        self.updateScore(bustCheck(self.player.evalHand()))


        if bustCheck(self.player.evalHand()) == True:
            time.sleep(1)
            self.RestartScreen()
    def standButton(self):

        dealerChoice = self.dealer.dealerPlay()
        print(dealerChoice)
        self.t.showturtle()



        self.t.goto(self.dealerCount,200)
        self.dealerCount+=10
        self.t.speed(7)


        for i in range(dealerChoice):
            self.dealer.Hit()
        dealerHand = self.dealer.seeHand()
        winsound.PlaySound('swipe', winsound.SND_FILENAME)
        for num in range(dealerChoice,0,-1):
            self.dealerHit(dealerHand[num])
        self.updateDealer(bustCheck(self.dealer.evalHand()))
        print(self.dealer.seeHand())
        print(self.dealer.evalHand())
        if bustCheck(self.dealer.evalHand()) == True:

            time.sleep(1)
            self.RestartScreen()
        else:
            self.determine()
            time.sleep(1)
            self.RestartScreen()
    def finalize(self):
        self.root.mainloop()
    def run(self):
        self.initializeScreen()

        self.displayStart(self.player.seeHand(),self.dealer.seeHand())




        self.finalize()
    def mainmenu(self):
        self.screen = turtle.TurtleScreen(self.canvas)

        self.t = turtle.RawTurtle(self.screen)
        self.screen.bgcolor('#30c744')
        self.t.penup()

        self.t.goto(-270,0)
        self.t.hideturtle()
        self.t.write("Welcome To BlackJack", font=("Courier New", 36, "bold"))
        self.t.goto(-180, -50)
        self.t.write("Click here to start the game", font=("Courier New", 16, "normal"))
        def startgame(x,y):
            self.t.goto(-270,0)


            for i in range(12):

                self.t.color('#30c744')


                self.t.write("Welcome To BlackJack", font=("Courier New", 36, "bold"))
                self.t.color('white')
                self.t.write("Welcome To BlackJack", font=("Courier New", 36, "bold"))

                self.t.color('black')
                self.t.write("Welcome To BlackJack", font=("Courier New", 36, "bold"))
            winsound.PlaySound('win', winsound.SND_FILENAME)


            self.run()
        self.screen.onclick(startgame)

        self.finalize()






t1= BlackJackScreen()
t1.mainmenu()