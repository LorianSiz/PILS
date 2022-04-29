import os
import tkinter.messagebox
from tkinter import filedialog

from ivy.std_api import *
from tkinter import *
import queue
import turtle

root = Tk();

NextShape = {
    "arrow" : "turtle",
    "turtle" : "circle",
    "circle" : "square",
    "square" : "triangle",
    "triangle" : "classic",
    "classic" : "arrow"
}

class Visuel:

#----------------------------------------- Zone fonction turtle -------------------------------------------------------#

    #########################################################
    # gestion des commandes pas msg Ivy                     #
    # format attendu:                                       #
    # Visuel --> {NomFonction} : {arg1} {arg2} {arg..}      #
    #########################################################

    def Avancer(self, args=[]):            # argument attendu: float distance
        self.pen.forward(float(args[0]))

    def Reculer(self, args=[]):            # argument attendu: float distance
        self.pen.backward(float(args[0]))

    def TournerGauche(self, args=[]):      # argument attendu: float angle
        self.pen.left(float(args[0]))

    def TournerDroite(self, args=[]):      # argument attendu: float angle
        self.pen.right(float(args[0]))

    def LeverCrayon(self, args=[]):        # argument attendu: None
        self.pen.penup()

    def BaisserCrayon(self, args=[]):      # argument attendu: None
        self.pen.pendown()

    def Restaurer(self, args=[]):                # argument attendu: None
        self.pen.reset()
        self.pen.seth(90)    # a defaut la turtle pointe vers la droite mais la on veux le haut Cf: Sujet
        self.pen.pendown()
        self.pen.pencolor(0,0,0)
        self.currentShape = "turtle"
        self.pen.shape(self.currentShape)

    def Origine(self, args=[]):            # argument attendu: None
        self.pen.home()

    def Nettoyer(self, args=[]):           # argument attendu: None
        self.pen.clear()

    def FCC(self, args=[]):                # argument attendu: int rouge, int vert, int bleu
        couleur = (int(args[0]), int(args[1]), int(args[2]))
        self.pen.pencolor(couleur)

    def FCAP(self, args=[]):               # argument attendu: float angle
        angle = float(args[0])
        if angle <= 360 and angle >= 0:
            self.pen.seth(angle)

    def FPOS(self, args=[]):               # argument attendu: float axeX, float axeY
        self.pen.setposition(float(args[0]), float(args[1]))

    def Changer(self, args=[]):               # argument attendu: None
        self.currentShape = NextShape[self.currentShape]
        self.pen.shape(self.currentShape)

#----------------------------------------- Zone sauvegarde en img -----------------------------------------------------#


        #ATTENTION: partie a commenter si ghostscript n'est pas instaler
    def SaveImg(self):
        path = filedialog.asksaveasfilename(title="Enregistrement", filetypes=[("fichier jpeg", "*.jpg")])
        if(path):
            path = path.replace(".jpg","")
            fileesp = self.pen.getscreen().getcanvas().postscript(file=path + '.eps', width=600, height=600)
            try:
                from PIL import Image
                img = Image.open(path + '.eps')
                img.save(path + '.jpg')
                img.close()
                os.remove(path + '.eps')
            except Exception:
                tkinter.messagebox.showwarning("Info exportation image", "L'image sera exporter au format .eps\n"
                                                                     "En l'absence de ghostscript qui gere la transformation vers .jpg")

#----------------------------------------------------------------------------------------------------------------------#




    def read_msg(self, *args):   # Ivy msg Handler
        print("From: " + str(args[0]) + " --> " + args[1])
        self.queue.put(args[1])


    def __init__(self, _master):
        self.master = _master
        self.running = 1
        self.queue = queue.Queue()

        self.master.title("Visuel")
        self.master.geometry("600x650")
        self.master.configure(bg="#FFFFFF")

        couleurPanel = '#777777'
        couleurBtn = '#335c67'
        couleurTxt = '#fff3b0'
        couleurFond = '#e09f3e'

        self.panelHaut = Frame(self.master, bg=couleurPanel)
        self.panelBas = Frame(self.master, bg=couleurPanel)
        self.panelHaut.pack(fill=X, padx=5, pady=5, side=TOP)
        self.panelBas.pack(fill=X, padx=5, pady=5, side=BOTTOM)

        self.canvas = Canvas(
            self.panelHaut,
            bg="#FFFFFF",
            height=600,
            width=600,
            bd=0,
            highlightthickness=0,
            relief="ridge"
        )
        self.canvas.pack(fill=X, padx=3, pady=3, side=TOP)
        self.screen = turtle.TurtleScreen(self.canvas)
        self.pen = turtle.RawTurtle(self.screen)
        self.currentShape = "turtle"
        self.pen.shape(self.currentShape)
        self.pen.screen.colormode(255)
        self.Restaurer()

        self.btnCharger = Button(self.panelBas, text="télécharger l'image", font=("Helvetica", 12), bg=couleurBtn, fg=couleurTxt, command=self.SaveImg)
        self.btnCharger.pack(fill=X, ipadx=55)

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

