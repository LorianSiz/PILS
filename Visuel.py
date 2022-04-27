from ivy.std_api import *
from tkinter import Tk, Canvas
import queue
import turtle

root = Tk();


class Visuel:


#----------------------------------------- Zone fonction turtle -------------------------------------------------------#

    #########################################################
    # gestion des commandes pas msg Ivy                     #
    # format attendu:                                       #
    # Visuel --> {NomFonction} : {arg1} {arg2} {arg..}      #
    #########################################################

    def Avancer(self, args):            # argument attendu: float distance
        self.pen.forward(float(args[0]))

    def Reculer(self, args):            # argument attendu: float distance
        self.pen.backward(float(args[0]))

    def TournerGauche(self, args):      # argument attendu: float angle
        self.pen.left(float(args[0]))

    def TournerDroite(self, args):      # argument attendu: float angle
        self.pen.right(float(args[0]))

    def LeverCrayon(self, args):        # argument attendu: None
        self.pen.penup()

    def BaisserCrayon(self, args):      # argument attendu: None
        self.pen.pendown()

    def Origine(self, args):            # argument attendu: None
        self.pen.home()

    def Restaurer(self, args):          # argument attendu: None
        self.pen.home()
        self.pen.clear()

    def Nettoyer(self, args):           # argument attendu: None
        self.pen.clear()

    def FCC(self, args):                # argument attendu: int rouge, int vert, int bleu
        couleur = (int(args[0]), int(args[1]), int(args[2]))
        self.pen.pencolor(couleur)

    def FCAP(self, args):               # argument attendu: float angle
        angle = float(args[0])
        if angle <= 360 and angle >= 0:
            self.pen.seth(angle)

    def FPOS(self, args):               # argument attendu: float axeX, float axeY
        self.pen.setposition(float(args[0]), float(args[1]))

#----------------------------------------------------------------------------------------------------------------------#


    def read_msg(self, *args):   # Ivy msg Handler
        print("From: " + str(args[0]) + " --> " + args[1])
        self.queue.put(args[1])


    def __init__(self, _master):
        self.master = _master
        self.running = 1
        self.queue = queue.Queue()

        self.master.title("Visuel")
        self.master.geometry("600x600")
        self.master.configure(bg="#FFFFFF")

        self.canvas = Canvas(
            self.master,
            bg="#FFFFFF",
            height=600,
            width=600,
            bd=0,
            highlightthickness=0,
            relief="ridge"
        )
        self.canvas.place(x=0, y=0)
        self.screen = turtle.TurtleScreen(self.canvas)
        self.pen = turtle.RawTurtle(self.screen, shape="turtle")
        self.pen.screen.colormode(255)

        IvyInit("Visuel")
        IvyStart()
        IvyBindMsg(self.read_msg, "Visuel --> (.*)")

        self.loop();

    def loop(self):
        while not self.queue.empty():
            cmd = self.queue.get()
            buffer = cmd.split(" : ")

            func = getattr(Visuel, buffer[0])
            args = None
            if (len(buffer) > 1):
                args = buffer[1].split(" ")

            func(self, args)


        if not self.running:
            import sys
            sys.exit(1)

        self.master.after(100, self.loop)


Visuel(root)
root.mainloop()

