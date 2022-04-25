from tkinter import *
from tkinter.colorchooser import askcolor
import turtle


# Création de la tortue
turtle.colormode(255)
pen = turtle.Turtle()

listeHistorique = []


# Définition des fonctions
def VerifFloat():
    try:
        float(txtBoxBase.get())
        return True
    except ValueError:
        return False

def VerifXYFormat():
    try:
        listeRGB = txtBoxBase.get().split(",")
        if len(listeRGB) == 2:
            float(listeRGB[0])
            float(listeRGB[1])
            return True
        else:
            return False
    except ValueError:
        return False

def VerifRGBFormat():
    try:
        listeRGB = txtBoxBase.get().split(",")
        if len(listeRGB) == 3:
            int(listeRGB[0])
            int(listeRGB[1])
            int(listeRGB[2])
            return True
        else:
            return False
    except ValueError:
        return False

def ChoixCouleur():
    couleurs = askcolor(title="Palette de couleurs")
    if couleurs[0] != None:
        pen.pencolor(couleurs[0])
        btnCouleur.configure(bg=couleurs[1])

def Avancer():
    if VerifFloat():
        pen.forward(float(txtBoxBase.get()))

def Reculer():
    if VerifFloat():
        pen.backward(float(txtBoxBase.get()))

def TournerGauche():
    if VerifFloat():
        pen.left(float(txtBoxBase.get()))

def TournerDroite():
    if VerifFloat():
        pen.right(float(txtBoxBase.get()))

def LeverCrayon():
    pen.penup()

def BaisserCrayon():
    pen.pendown()

def Origine():
    pen.home()

def Restaurer():
    pen.home()
    pen.clear()

def Nettoyer():
    pen.clear()

def FCC():
    if VerifRGBFormat():
        listeRGB = txtBoxBase.get().split(",")
        couleur = (int(listeRGB[0]), int(listeRGB[1]), int(listeRGB[2]))
        pen.pencolor(couleur)
        btnCouleur.configure(bg='#%02x%02x%02x' % couleur)

def FCAP():
    if VerifFloat():
        angle = float(txtBoxBase.get())
        if angle <= 360 and angle >= 0:
            pen.seth(angle)

def FPOS():
    if VerifXYFormat():
        listeCoor = txtBoxBase.get().split(",")
        pen.setposition(float(listeCoor[0]), float(listeCoor[1]))

def Repeter():
    for x in range(6):
        pen.forward(10)

def Enregistrer():
    print("Enregistrer en xml")

def Charger():
    print("Charger en xml")

def Supprimer():
    print("Supprimer de l'historique")


# Définition du style de la page
couleurPanel = '#777777'
couleurBtn = '#335c67'
couleurTxt = '#fff3b0'
couleurFond = '#e09f3e'

# Création de la fenêtre
fen = Tk()
fen.title("Editeur")
fen.geometry("600x550") #A voir si on change la taille
fen.resizable(False, False)


# Création des panels
panelHaut = Frame(fen, bg=couleurPanel)
panelGauche = Frame(fen, bg=couleurPanel)
panelDroite = Frame(fen, bg=couleurPanel)

panelCommandes = Frame(panelGauche, bg=couleurPanel) #Voir couleur cest pas a nous
panelHistorique = Frame(panelDroite, bg=couleurPanel)
panelXML = Frame(panelDroite, bg=couleurPanel)
panelOptions = Frame(panelDroite, bg=couleurPanel) #Changer la tortue, autres?


# Créations des éléments des panels
txtBoxBase = Entry(panelHaut, width = 50, font=("Helvetica", 12), fg=couleurFond) #Voir couleur et font cest pas a nous
btnCouleur = Button(panelHaut, width = 2, bg="black", command=ChoixCouleur) #Voir couleur et font cest pas a nous
btnAvancer = Button(panelCommandes, text="avancer", font=("Helvetica", 12), bg=couleurBtn, fg=couleurTxt, command=Avancer)
btnReculer = Button(panelCommandes, text="reculer", font=("Helvetica", 12), bg=couleurBtn, fg=couleurTxt, command=Reculer)
btnTournerGauche = Button(panelCommandes, text="tourner à gauche", font=("Helvetica", 12), bg=couleurBtn, fg=couleurTxt, command=TournerGauche)
btnTournerDroite = Button(panelCommandes, text="tourner à droite", font=("Helvetica", 12), bg=couleurBtn, fg=couleurTxt, command=TournerDroite)
btnLeverCrayon = Button(panelCommandes, text="lever le crayon", font=("Helvetica", 12), bg=couleurBtn, fg=couleurTxt, command=LeverCrayon)
btnBaisserCrayon = Button(panelCommandes, text="baisser le crayon", font=("Helvetica", 12), bg=couleurBtn, fg=couleurTxt, command=BaisserCrayon)
btnOrigine = Button(panelCommandes, text="origine", font=("Helvetica", 12), bg=couleurBtn, fg=couleurTxt, command=Origine)
btnRestaurer = Button(panelCommandes, text="restaurer", font=("Helvetica", 12), bg=couleurBtn, fg=couleurTxt, command=Restaurer)
btnNettoyer = Button(panelCommandes, text="nettoyer", font=("Helvetica", 12), bg=couleurBtn, fg=couleurTxt, command=Nettoyer)
btnFCC = Button(panelCommandes, text="changer couleur", font=("Helvetica", 12), bg=couleurBtn, fg=couleurTxt, command=FCC)
btnFCAP = Button(panelCommandes, text="changer angle", font=("Helvetica", 12), bg=couleurBtn, fg=couleurTxt, command=FCAP)
btnFPOS = Button(panelCommandes, text="changer position", font=("Helvetica", 12), bg=couleurBtn, fg=couleurTxt, command=FPOS)
btnRepeter = Button(panelCommandes, text="répéter", font=("Helvetica", 12), bg=couleurBtn, fg=couleurTxt, command=Repeter)
btnEnregistrer = Button(panelXML, text="enregistrer", font=("Helvetica", 12), bg=couleurBtn, fg=couleurTxt, command=Enregistrer)
btnCharger = Button(panelXML, text="charger", font=("Helvetica", 12), bg=couleurBtn, fg=couleurTxt, command=Charger)
listeBoxHistorique = Listbox(panelHistorique, bg=couleurFond)
btnSupprimer = Button(panelOptions, text="supprimer commande", font=("Helvetica", 12), bg=couleurBtn, fg=couleurTxt, command=Supprimer)
#Bouton quitter?


# Disposition des éléments sur les panels
txtBoxBase.pack(fill=X, padx=(50, 0), pady=(10,10), side=LEFT)
btnCouleur.pack(side=RIGHT, padx=20)
btnAvancer.pack(fill=X, ipadx=55)
btnReculer.pack(fill=X, ipadx=55)
btnTournerGauche.pack(fill=X, ipadx=55)
btnTournerDroite.pack(fill=X, ipadx=55)
btnLeverCrayon.pack(fill=X, ipadx=55)
btnBaisserCrayon.pack(fill=X, ipadx=55)
btnOrigine.pack(fill=X, ipadx=55)
btnRestaurer.pack(fill=X, ipadx=55)
btnNettoyer.pack(fill=X, ipadx=55)
btnFCC.pack(fill=X, ipadx=55)
btnFCAP.pack(fill=X, ipadx=55)
btnFPOS.pack(fill=X, ipadx=55)
btnRepeter.pack(fill=X, ipadx=55)
btnEnregistrer.pack(fill=X, ipadx=55)
btnCharger.pack(fill=X, ipadx=55)
listeBoxHistorique.pack(fill=X)
btnSupprimer.pack(fill=X, ipadx=55)


# Disposition des panels sur la fenêtre
panelHaut.pack(fill=X, padx=10, pady=10, side=TOP)
panelCommandes.pack(fill=X, padx=10, pady=10)
panelHistorique.pack(fill=BOTH, padx=10, pady=10)
panelOptions.pack(fill=X, padx=10, pady=10)
panelXML.pack(fill=X, padx=10, pady=10)

panelGauche.pack(fill=X, padx=10, side=LEFT)
panelDroite.pack(fill=X, padx=10, side=RIGHT)


fen.mainloop()