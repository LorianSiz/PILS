from tkinter import *
from tkinter.colorchooser import askcolor
import turtle


# Création de la tortue
turtle.colormode(255)
pen = turtle.Turtle()

# Variables globales
listeHistorique = []
tab = ""
profondeur = 0


# Définition des fonctions
def AjouterListe(commande):
    listeBoxHistorique.insert(END, tab + commande)
    listeHistorique.append(commande)

def SupprimerListe():
    index = listeBoxHistorique.curselection()[0]
    listeBoxHistorique.delete(index)
    listeHistorique.pop(int(index))
    #redo commande liste

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
        btnCouleur["bg"] = couleurs[1]
        AjouterListe("Changer couleur en " + str(couleurs[0][0]) + "," + str(couleurs[0][1]) + "," + str(couleurs[0][2]))

def Avancer():
    if VerifFloat():
        pen.forward(float(txtBoxBase.get()))
        AjouterListe("Avancer " + txtBoxBase.get())

def Reculer():
    if VerifFloat():
        pen.backward(float(txtBoxBase.get()))
        AjouterListe("Reculer " + txtBoxBase.get())

def TournerGauche():
    if VerifFloat():
        pen.left(float(txtBoxBase.get()))
        AjouterListe("Tourner à gauche " + txtBoxBase.get())

def TournerDroite():
    if VerifFloat():
        pen.right(float(txtBoxBase.get()))
        AjouterListe("Tourner à droite " + txtBoxBase.get())

def LeverCrayon():
    pen.penup()
    AjouterListe("Lever le crayon")

def BaisserCrayon():
    pen.pendown()
    AjouterListe("Baisser le crayon")

def Origine():
    pen.home()
    AjouterListe("Retour à l'origine")

def Restaurer():
    pen.home()
    pen.clear()
    AjouterListe("Restaurer")

def Nettoyer():
    pen.clear()
    AjouterListe("Nettoyer")

def FCC():
    if VerifRGBFormat():
        listeRGB = txtBoxBase.get().split(",")
        couleur = (int(listeRGB[0]), int(listeRGB[1]), int(listeRGB[2]))
        pen.pencolor(couleur)
        btnCouleur["bg"] = '#%02x%02x%02x' % couleur
        AjouterListe("Changer couleur en " + listeRGB[0] + "," + listeRGB[1] + "," + listeRGB[2])

def FCAP():
    if VerifFloat():
        angle = float(txtBoxBase.get())
        if angle <= 360 and angle >= 0:
            pen.seth(angle)
            AjouterListe("Changer angle " + txtBoxBase.get() + "°")

def FPOS():
    if VerifXYFormat():
        listeCoor = txtBoxBase.get().split(",")
        pen.setposition(float(listeCoor[0]), float(listeCoor[1]))
        AjouterListe("Changer position pour x: " + listeCoor[0] + ", y:" + listeCoor[1])

def Repeter():
    global tab
    global profondeur

    AjouterListe("Début répéter")
    profondeur += 1
    tab += "-"
    btnFinRepeter["state"] = NORMAL

def FinRepeter():
    global tab
    global profondeur

    profondeur -= 1
    tab = tab[:-1]
    AjouterListe("Fin répéter")
    if profondeur == 0:
        btnFinRepeter["state"] = DISABLED

def Enregistrer():
    print("Enregistrer en xml")

def Charger():
    print("Charger en xml")


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
panelDeplacement = Frame(panelCommandes, bg=couleurPanel)
panelCrayon = Frame(panelCommandes, bg=couleurPanel)
panelSpeciale = Frame(panelCommandes, bg=couleurPanel)
panelChanger = Frame(panelCommandes, bg=couleurPanel)
panelRepeter = Frame(panelCommandes, bg=couleurPanel)
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
btnFinRepeter = Button(panelCommandes, text="fin répéter", font=("Helvetica", 12), bg=couleurBtn, fg=couleurTxt, state=DISABLED, command=FinRepeter)
btnEnregistrer = Button(panelXML, text="enregistrer", font=("Helvetica", 12), bg=couleurBtn, fg=couleurTxt, command=Enregistrer)
btnCharger = Button(panelXML, text="charger", font=("Helvetica", 12), bg=couleurBtn, fg=couleurTxt, command=Charger)
listeBoxHistorique = Listbox(panelHistorique, bg=couleurFond)
btnSupprimer = Button(panelOptions, text="supprimer commande", font=("Helvetica", 12), bg=couleurBtn, fg=couleurTxt, command=SupprimerListe)
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
btnFinRepeter.pack(fill=X, ipadx=55)
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