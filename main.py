from tkinter import *
import turtle


# Création de la tortue
turtle = turtle.Turtle()

listeHistorique = []


# Définition des fonctions
def Avancer():
    turtle.forward(10)

def Reculer():
    turtle.backward(10)

def TournerGauche():
    turtle.left(10)

def TournerDroite():
    turtle.right(10)

def LeverCrayon():
    turtle.penup()

def BaisserCrayon():
    turtle.pendown()

def Origine():
    turtle.home()

def Restaurer():
    turtle.clear()
    turtle.home()

def Nettoyer():
    turtle.clear()

def FCC():
    turtle.pencolor(0.2, 0.8, 0.55)

def FCAP():
    turtle.seth(90)

def FPOS():
    turtle.setposition(60, 30)

def Repeter():
    for x in range(6):
        turtle.forward(10)

def FinRepeter():
    print("fin")

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
fen.geometry("600x900") #A voir si on change la taille
fen.minsize(600, 900) #Demander abraham pk chez eux ils ont une taille diff de la geometry
fen.maxsize(600, 900)


# Création des panels
panelGauche = Frame(fen, bg=couleurPanel)
panelDroite = Frame(fen, bg=couleurPanel)

panelTxtBox = Frame(fen, bg=couleurPanel) #Voir couleur cest pas a nous
panelCommandes = Frame(panelGauche, bg=couleurPanel)
panelHistorique = Frame(panelDroite, bg=couleurPanel)
panelXML = Frame(panelGauche, bg=couleurPanel)
panelOptions = Frame(panelDroite, bg=couleurPanel) #Changer la tortue, autres?


# Créations des éléments des panels
txtBoxBase = Entry(panelTxtBox, font=("Helvetica", 12), fg=couleurTxt) #Voir couleur et font cest pas a nous
btnAvancer = Button(panelCommandes, text="avancer", font=("Helvetica", 12), bg=couleurBtn, fg=couleurTxt, command=Avancer) #Voir couleur et font cest pas a nous
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
btnFinRepeter = Button(panelCommandes, text="fin répéter", font=("Helvetica", 12), bg=couleurBtn, fg=couleurTxt, state= DISABLED, command=FinRepeter)
btnEnregistrer = Button(panelXML, text="enregistrer", font=("Helvetica", 12), bg=couleurBtn, fg=couleurTxt, command=Enregistrer)
btnCharger = Button(panelXML, text="charger", font=("Helvetica", 12), bg=couleurBtn, fg=couleurTxt, command=Charger)
listeBoxHistorique = Listbox(panelHistorique, bg=couleurFond)
btnSupprimer = Button(panelOptions, text="supprimer commande", font=("Helvetica", 12), bg=couleurBtn, fg=couleurTxt, command=Supprimer)
#Bouton quitter?


# Disposition des éléments sur les panels
txtBoxBase.pack(fill=X, padx=(90, 90), pady=(30,10))
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
btnFinRepeter.pack(fill=X, ipadx=55)
btnEnregistrer.pack(fill=X, ipadx=55)
btnCharger.pack(fill=X, ipadx=55)
listeBoxHistorique.pack(fill=X)
btnSupprimer.pack(fill=X, ipadx=55)


# Disposition des panels sur la fenêtre
panelTxtBox.pack(fill=X, padx=10, pady=10, side=TOP)
panelCommandes.pack(fill=X, padx=10, pady=10)
panelXML.pack(fill=X, padx=10, pady=10)
panelHistorique.pack(fill=BOTH, padx=10, pady=10)
panelOptions.pack(fill=X, padx=10, pady=10)

panelGauche.pack(fill=X, padx=10, side=LEFT)
panelDroite.pack(fill=X, padx=10, side=RIGHT)


fen.mainloop()