from card import *
import turtle
import tkinter as tk




class BlackJackScreen:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title('Python BlackJack')
        self.canvas = tk.Canvas(self.root)
        self.canvas.config(width=1000, height=800)
        self.canvas.pack()





        button_hit = tk.Button(self.root, text="Hit", width=5,height=0)#,command=self.press,)
        button_hit.pack()
        button_stand = tk.Button(self.root, text="Stand",width=5,height=0)#,command=self.press)
        button_stand.pack()



        # self.display_playerHand([['spade', 8], ['club', 8]])





    def display_playerHand(self,hand):
        displaylst = []
        for card in hand:
            displaylst.append(card[0]+str(card[1]))

    def initializeScreen(self):
        self.screen = turtle.TurtleScreen(self.canvas)


        self.t = turtle.RawTurtle(self.screen)
        self.screen.bgcolor('#30c744')



    def finalize(self):






        self.root.mainloop()


val = ['A',2, 3, 4, 5, 6, 7, 8,9, 10, 'J', 'Q', 'K']
suit = ['club', 'diamond', 'heart', 'spade']
count = 0

t1 = BlackJackScreen()
t1.initializeScreen()

t1.t.penup()
for i in val:
    for j in suit:
        t1.t.goto(-300,0)
        t1.screen.addshape('cardbacktest.gif')

        t1.t.shape('cardbacktest.gif')

t1.t.clear()
t1.finalize()



