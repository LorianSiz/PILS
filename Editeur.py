import inspect
from ivy.std_api import *
from tkinter import *
from tkinter.colorchooser import askcolor


root = Tk();


class Editeur:

#--------------------------------- Fonction de gestion d'historique ---------------------------------------------------#

    def AjouterListe(self, commande):
        self.listeBoxHistorique.insert(END, self.tab + commande)
        self.listeHistorique.append(commande)

    def SupprimerListe(self):
        index = self.listeBoxHistorique.curselection()[0]
        self.listeBoxHistorique.delete(index)
        self.listeHistorique.pop(int(index))

    def Repeter(self):
        self.AjouterListe("Début répéter")
        self.profondeur += 1
        self.tab += "-"
        self.btnFinRepeter["state"] = NORMAL

    def FinRepeter(self):
        self.profondeur -= 1
        self.tab = self.tab[:-1]
        self.AjouterListe("Fin répéter")
        if self.profondeur == 0:
            self.btnFinRepeter["state"] = DISABLED


    def Enregistrer(self):
        print("Enregistrer en xml")


    def Charger(self):
        print("Charger en xml")

#--------------------------------- Fonction de verification d'Input ---------------------------------------------------#

    def VerifFloat(self):
        try:
            float(self.txtBoxBase.get())
            return True
        except ValueError:
            return False

    def VerifXYFormat(self):
        try:
            listeRGB = self.txtBoxBase.get().split(",")
            if len(listeRGB) == 2:
                float(listeRGB[0])
                float(listeRGB[1])
                return True
            else:
                return False
        except ValueError:
            return False

    def VerifRGBFormat(self):
        try:
            listeRGB = self.txtBoxBase.get().split(",")
            if len(listeRGB) == 3:
                int(listeRGB[0])
                int(listeRGB[1])
                int(listeRGB[2])
                return True
            else:
                return False
        except ValueError:
            return False

#--------------------------------- Fonction de renvoie ----------------------------------------------------------------#

    def ChoixCouleur(self):
        couleurs = askcolor(title="Palette de couleurs")
        if couleurs[0] != None:
            self.SubmitRequet(couleurs[0][0], couleurs[0][1], couleurs[0][2])
            self.btnCouleur["bg"] = couleurs[1]
            self.AjouterListe("Changer couleur en " + str(couleurs[0][0]) + "," + str(couleurs[0][1]) + "," + str(couleurs[0][2]))


#--------------------------------- Fonction d'envoie de requete -------------------------------------------------------#
    # format attendu:
    # Visuel --> {NomFonction} : {arg1} {arg2} {arg..}
    def SubmitRequet(self, *args):
        name = inspect.stack()[1][3]
        if (name == "ChoixCouleur"): name = "FCC"

        msg = "Visuel --> " + name + " : "
        flag = 0;
        for arg in args:
            if flag: msg += " "
            else: flag = 1
            msg += str(arg)

        IvySendMsg(msg)



    def Avancer(self):
        if self.VerifFloat():
            self.SubmitRequet(float(self.txtBoxBase.get()))
            self.AjouterListe("Avancer " + self.txtBoxBase.get())

    def Reculer(self):
        if self.VerifFloat():
            self.SubmitRequet(float(self.txtBoxBase.get()))
            self.AjouterListe("Reculer " + self.txtBoxBase.get())

    def TournerGauche(self):
        if self.VerifFloat():
            self.SubmitRequet(float(self.txtBoxBase.get()))
            self.AjouterListe("Tourner à gauche " + self.txtBoxBase.get())

    def TournerDroite(self):
        if self.VerifFloat():
            self.SubmitRequet(float(self.txtBoxBase.get()))
            self.AjouterListe("Tourner à droite " + self.txtBoxBase.get())

    def LeverCrayon(self):
        self.SubmitRequet()
        self.AjouterListe("Lever le crayon")

    def BaisserCrayon(self):
        self.SubmitRequet()
        self.AjouterListe("Baisser le crayon")

    def Origine(self):
        self.SubmitRequet()
        self.AjouterListe("Retour à l'origine")

    def Restaurer(self):
        self.SubmitRequet()
        self.AjouterListe("Restaurer")

    def Nettoyer(self):
        self.SubmitRequet()
        self.AjouterListe("Nettoyer")

    def FCC(self):
        if self.VerifRGBFormat():
            listeRGB = self.txtBoxBase.get().split(",")
            couleur = (int(listeRGB[0]), int(listeRGB[1]), int(listeRGB[2]))
            self.SubmitRequet(int(listeRGB[0]), int(listeRGB[1]), int(listeRGB[2]))
            self.btnCouleur["bg"] = '#%02x%02x%02x' % couleur
            self.AjouterListe("Changer couleur en " + listeRGB[0] + "," + listeRGB[1] + "," + listeRGB[2])

    def FCAP(self):
        if self.VerifFloat():
            angle = float(self.txtBoxBase.get())
            if angle <= 360 and angle >= 0:
                self.SubmitRequet(angle)
                self.AjouterListe("Changer angle " + self.txtBoxBase.get() + "°")

    def FPOS(self):
        if self.VerifXYFormat():
            listeCoor = self.txtBoxBase.get().split(",")
            self.SubmitRequet(float(listeCoor[0]), float(listeCoor[1]))
            self.AjouterListe("Changer position pour x: " + listeCoor[0] + ", y:" + listeCoor[1])

#----------------------------------------------------------------------------------------------------------------------#


    def __init__(self, _master):
        self.master = _master
        self.running = 1
        self.listeHistorique = []
        self.tab = ""
        self.profondeur = 0

        self.master.title("Editeur")
        self.master.geometry("600x550")  # A voir si on change la taille
        self.master.resizable(False, False)

        couleurPanel = '#777777'
        couleurBtn = '#335c67'
        couleurTxt = '#fff3b0'
        couleurFond = '#e09f3e'

        # Création des panels
        self.panelHaut = Frame(self.master, bg=couleurPanel)
        self.panelGauche = Frame(self.master, bg=couleurPanel)
        self.panelDroite = Frame(self.master, bg=couleurPanel)

        self.panelCommandes = Frame(self.panelGauche, bg=couleurPanel)  # Voir couleur cest pas a nous
        self.panelDeplacement = Frame(self.panelCommandes, bg=couleurPanel)
        self.panelCrayon = Frame(self.panelCommandes, bg=couleurPanel)
        self.panelSpeciale = Frame(self.panelCommandes, bg=couleurPanel)
        self.panelChanger = Frame(self.panelCommandes, bg=couleurPanel)
        self.panelRepeter = Frame(self.panelCommandes, bg=couleurPanel)
        self.panelHistorique = Frame(self.panelDroite, bg=couleurPanel)
        self.panelXML = Frame(self.panelDroite, bg=couleurPanel)
        self.panelOptions = Frame(self.panelDroite, bg=couleurPanel)  # Changer la tortue, autres?

        # Créations des éléments des panels
        self.txtBoxBase = Entry(self.panelHaut, width=50, font=("Helvetica", 12), fg=couleurFond)  # Voir couleur et font cest pas a nous
        self.btnCouleur = Button(self.panelHaut, width=2, bg="black", command=self.ChoixCouleur)  # Voir couleur et font cest pas a nous
        self.btnAvancer = Button(self.panelCommandes, text="avancer", font=("Helvetica", 12), bg=couleurBtn, fg=couleurTxt, command=self.Avancer)
        self.btnReculer = Button(self.panelCommandes, text="reculer", font=("Helvetica", 12), bg=couleurBtn, fg=couleurTxt, command=self.Reculer)
        self.btnTournerGauche = Button(self.panelCommandes, text="tourner à gauche", font=("Helvetica", 12), bg=couleurBtn, fg=couleurTxt, command=self.TournerGauche)
        self.btnTournerDroite = Button(self.panelCommandes, text="tourner à droite", font=("Helvetica", 12), bg=couleurBtn, fg=couleurTxt, command=self.TournerDroite)
        self.btnLeverCrayon = Button(self.panelCommandes, text="lever le crayon", font=("Helvetica", 12), bg=couleurBtn, fg=couleurTxt, command=self.LeverCrayon)
        self.btnBaisserCrayon = Button(self.panelCommandes, text="baisser le crayon", font=("Helvetica", 12), bg=couleurBtn, fg=couleurTxt, command=self.BaisserCrayon)
        self.btnOrigine = Button(self.panelCommandes, text="origine", font=("Helvetica", 12), bg=couleurBtn, fg=couleurTxt, command=self.Origine)
        self.btnRestaurer = Button(self.panelCommandes, text="restaurer", font=("Helvetica", 12), bg=couleurBtn, fg=couleurTxt, command=self.Restaurer)
        self.btnNettoyer = Button(self.panelCommandes, text="nettoyer", font=("Helvetica", 12), bg=couleurBtn, fg=couleurTxt, command=self.Nettoyer)
        self.btnFCC = Button(self.panelCommandes, text="changer couleur", font=("Helvetica", 12), bg=couleurBtn, fg=couleurTxt, command=self.FCC)
        self.btnFCAP = Button(self.panelCommandes, text="changer angle", font=("Helvetica", 12), bg=couleurBtn, fg=couleurTxt, command=self.FCAP)
        self.btnFPOS = Button(self.panelCommandes, text="changer position", font=("Helvetica", 12), bg=couleurBtn, fg=couleurTxt, command=self.FPOS)
        self.btnRepeter = Button(self.panelCommandes, text="répéter", font=("Helvetica", 12), bg=couleurBtn, fg=couleurTxt, command=self.Repeter)
        self.btnFinRepeter = Button(self.panelCommandes, text="fin répéter", font=("Helvetica", 12), bg=couleurBtn, fg=couleurTxt, state=DISABLED, command=self.FinRepeter)
        self.btnEnregistrer = Button(self.panelXML, text="enregistrer", font=("Helvetica", 12), bg=couleurBtn, fg=couleurTxt, command=self.Enregistrer)
        self.btnCharger = Button(self.panelXML, text="charger", font=("Helvetica", 12), bg=couleurBtn, fg=couleurTxt, command=self.Charger)
        self.listeBoxHistorique = Listbox(self.panelHistorique, bg=couleurFond)
        self.btnSupprimer = Button(self.panelOptions, text="supprimer commande", font=("Helvetica", 12), bg=couleurBtn, fg=couleurTxt, command=self.SupprimerListe)
        # Bouton quitter?

        # Disposition des éléments sur les panels
        self.txtBoxBase.pack(fill=X, padx=(50, 0), pady=(10, 10), side=LEFT)
        self.btnCouleur.pack(side=RIGHT, padx=20)
        self.btnAvancer.pack(fill=X, ipadx=55)
        self.btnReculer.pack(fill=X, ipadx=55)
        self.btnTournerGauche.pack(fill=X, ipadx=55)
        self.btnTournerDroite.pack(fill=X, ipadx=55)
        self.btnLeverCrayon.pack(fill=X, ipadx=55)
        self.btnBaisserCrayon.pack(fill=X, ipadx=55)
        self.btnOrigine.pack(fill=X, ipadx=55)
        self.btnRestaurer.pack(fill=X, ipadx=55)
        self.btnNettoyer.pack(fill=X, ipadx=55)
        self.btnFCC.pack(fill=X, ipadx=55)
        self.btnFCAP.pack(fill=X, ipadx=55)
        self.btnFPOS.pack(fill=X, ipadx=55)
        self.btnRepeter.pack(fill=X, ipadx=55)
        self.btnFinRepeter.pack(fill=X, ipadx=55)
        self.btnEnregistrer.pack(fill=X, ipadx=55)
        self.btnCharger.pack(fill=X, ipadx=55)
        self.listeBoxHistorique.pack(fill=X)
        self.btnSupprimer.pack(fill=X, ipadx=55)

        # Disposition des panels sur la fenêtre
        self.panelHaut.pack(fill=X, padx=10, pady=10, side=TOP)
        self.panelCommandes.pack(fill=X, padx=10, pady=10)
        self.panelHistorique.pack(fill=BOTH, padx=10, pady=10)
        self.panelOptions.pack(fill=X, padx=10, pady=10)
        self.panelXML.pack(fill=X, padx=10, pady=10)

        self.panelGauche.pack(fill=X, padx=10, side=LEFT)
        self.panelDroite.pack(fill=X, padx=10, side=RIGHT)

        IvyInit("Editeur")
        IvyStart()


Editeur(root)
root.mainloop()

