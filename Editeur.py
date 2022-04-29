import inspect
import re
import xml.etree.ElementTree
from tkinter import *
from tkinter.colorchooser import askcolor
from AdapterEditeur import AdapterEditeur
import xml.etree.cElementTree as ET

root = Tk()

class Editeur:

#--------------------------------- Fonction de sctokage ---------------------------------------------------------------#

    def RefreshEdit(self):
        self.listeBoxHistorique.delete(0, END)
        for cmd in self.lstCmd:
            text = ""
            for i in range(cmd[3]): text += "-"
            text += cmd[1]
            self.listeBoxHistorique.insert(END, text)

    def RefreshVisu(self):
        self.adapter.Restaurer()
        self.ExecuteBoucle(self.lstCmd, 1)

    def ExecuteBoucle(self, liste, nbRep):
        for i in range(nbRep):
            nbRepBoucle = 0
            listboucle = []
            for cmd in liste:
                if(cmd[3] == 0):
                    if(cmd[0] == "Repeter"): nbRepBoucle = cmd[2][0]
                    elif(cmd[0] == "FinRepeter"):
                        self.ExecuteBoucle(listboucle, nbRepBoucle)
                        listboucle = []
                    else:
                        funct = getattr(self.adapter.__class__, cmd[0])
                        funct(self.adapter, *cmd[2])
                else:
                    buffer = cmd.copy()
                    buffer[3] -= 1
                    listboucle.append(buffer)


    def AddCmd(self, name, texte, *args):
        if(name == "FinRepeter"): self.nbBoucle-=1
        if(self.nbBoucle != 0): self.inBoucle.append([name, texte, args, self.nbBoucle-1])
        text = ""
        for i in range(self.nbBoucle): text += "-"
        text += texte
        self.lstCmd.append([name, texte, args, self.nbBoucle])
        self.listeBoxHistorique.insert(END, text)
        if(name == "Repeter"): self.nbBoucle+=1

    def SuppCmd(self):  #TODO : eviter le click sans selelection
        index = self.listeBoxHistorique.curselection()[0]

        self.SuppInList(self.lstCmd, index)
        if (self.nbBoucle) & (index > self.indexBoucle):
            self.SuppInList(self.inBoucle, (index - self.indexBoucle - 1))

        self.nbBoucle = 0;
        if(self.lstCmd):
            self.nbBoucle = self.lstCmd[-1][3]
            if (self.lstCmd[-1][0] == "Repeter"): self.nbBoucle += 1
        if self.nbBoucle:
            self.btnFinRepeter["state"] = NORMAL
        else:
            self.btnFinRepeter["state"] = DISABLED
            self.inBoucle = []

        self.RefreshEdit()
        self.RefreshVisu()

    def SuppInList(self, list, index):
        cmd = list[index].copy()

        if (cmd[0] == "Repeter"):
            while (len(list) > index):
                if ((list[index][0] == "FinRepeter") & (list[index][3] == cmd[3])):
                    del list[index]
                    break
                else:
                    del list[index]
        elif (cmd[0] == "FinRepeter"):
            for i in range(index, -1, -1):
                if ((list[i][0] == "Repeter") & (list[i][3] == cmd[3])):
                    del list[i]
                    break
                else:
                    del list[i]
        else:
            del list[index]


    def SaveXML(self):                  #FIXME: if not nbBoucle --> error
        root = ET.Element("Turtle")

        for elem in self.CmdToXMLElement(self.lstCmd):
            root.append(elem)

        xml = ET.ElementTree(root)
        xml.write("C:\Temp\Test2.xml")

    def LoadXML(self):                  #FIXME : a finir
        xml = ET.parse("C:\Temp\Test2.xml")
        root = xml.getroot()

        self.lstCmd = []

        elem = list(root)[0]
        name = elem.tag
        attribs = elem.attrib
        args = []
        for arg in re.sub("[()]", "", attribs["Arguments"]).split(","):
            if arg: args.append(arg)
        print(args)
        self.lstCmd.append([name, attribs["Texte"], args, int(attribs["Etage"])])

        self.nbBoucle = 0
        self.inBoucle = []
        self.RefreshEdit()
        self.RefreshVisu()

    def CmdToXMLElement(self, _list):
        list = _list.copy()
        elemList = []
        if list:
            profSousCmd = 0
            flag = 0
            sousCmd = []
            for cmd in list:
                if (flag) & (cmd[0] == "FinRepeter") & (cmd[3] == profSousCmd):
                    for elem in self.CmdToXMLElement(sousCmd):
                        elemList[-1].append(elem)
                elif flag:
                    sousCmd.append(cmd)
                else:
                    if(cmd[0] == "Repeter"):
                        flag = 1
                        profSousCmd = cmd[3]

                    elem = ET.Element(str(cmd[0]))
                    elem.set("Texte", str(cmd[1]))
                    elem.set("Arguments", str(cmd[2]))
                    elem.set("Etage", str(cmd[3]))
                    elemList.append(elem)

        return elemList

    def XMLElementToCmd(self, _list):
        list = _list.copy()
        listCmd = []

        for elem in list:
            name = elem.tag
            attribs = elem.attrib
            args = []
            for arg in re.sub("[()]","", attribs["Arguments"]).split(","):
                args.append(arg)
            del args[-1]
            listCmd.append([name, attribs["Texte"], args, int(attribs["Etage"])])

        return listCmd

#--------------------------------- Fonction de verification d'Input ---------------------------------------------------#

    def VerifFloat(self):
        try:
            float(self.txtBoxBase.get())
            return True
        except ValueError:
            return False

    def VerifInt(self):
        try:
            int(self.txtBoxBase.get())
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
                rg1 = int(listeRGB[0])
                rg2 = int(listeRGB[1])
                rg3 = int(listeRGB[2])
                if (0 <= rg1 <= 255 and 0 <= rg2 <= 255 and 0 <= rg3 <= 255):
                    return True
                else:
                    return False
            else:
                return False
        except ValueError:
            return False

#--------------------------------- Fonction d'envoie de requete -------------------------------------------------------#

    def ChoixCouleur(self):
        couleurs = askcolor(title="Palette de couleurs")
        if couleurs[0] != None:
            if(self.nbBoucle == 0): self.adapter.FCC(couleurs[0][0], couleurs[0][1], couleurs[0][2])
            self.btnCouleur["bg"] = couleurs[1]
            self.AddCmd("FCC", "Changer couleur en " + str(couleurs[0][0]) + "," + str(couleurs[0][1]) + "," + str(couleurs[0][2]), couleurs[0][0], couleurs[0][1], couleurs[0][2])

    def Avancer(self):
        if self.VerifFloat():
            if(self.nbBoucle == 0): self.adapter.Avancer(float(self.txtBoxBase.get()))
            self.AddCmd("Avancer", "Avancer de " + self.txtBoxBase.get(), float(self.txtBoxBase.get()))

    def Reculer(self):
        if self.VerifFloat():
            if(self.nbBoucle == 0): self.adapter.Reculer(float(self.txtBoxBase.get()))
            self.AddCmd("Reculer", "Reculer de " + self.txtBoxBase.get(), float(self.txtBoxBase.get()))

    def TournerGauche(self):
        if self.VerifFloat():
            if(self.nbBoucle == 0): self.adapter.TournerGauche(float(self.txtBoxBase.get()))
            self.AddCmd("TournerGauche", "Tourner à gauche " + self.txtBoxBase.get(), float(self.txtBoxBase.get()))

    def TournerDroite(self):
        if self.VerifFloat():
            if(self.nbBoucle == 0): self.adapter.TournerDroite(float(self.txtBoxBase.get()))
            self.AddCmd("TournerDroite", "Tourner à droite " + self.txtBoxBase.get(), float(self.txtBoxBase.get()))

    def LeverCrayon(self):
        if(self.nbBoucle == 0): self.adapter.LeverCrayon()
        # self.AjouterListe("Lever le crayon")
        self.AddCmd("LeverCrayon", "Lever le crayon")

    def BaisserCrayon(self):
        if(self.nbBoucle == 0): self.adapter.BaisserCrayon()
        # self.AjouterListe("Baisser le crayon")
        self.AddCmd("BaisserCrayon", "Baisser le crayon")

    def Origine(self):
        if(self.nbBoucle == 0): self.adapter.Origine()
        # self.AjouterListe("Retour à l'origine")
        self.AddCmd("Origine", "Retour à l'origine")

    def Restaurer(self):    #TODO : reset le color pick
        if(self.nbBoucle == 0): self.adapter.Restaurer()
        # self.AjouterListe("Restaurer")
        self.AddCmd("Restaurer", "Restaurer")
        print(self.inBoucle)

    def Nettoyer(self):
        if(self.nbBoucle == 0): self.adapter.Nettoyer()
        # self.AjouterListe("Nettoyer")
        self.AddCmd("Nettoyer", "Nettoyer")

    def FCC(self):
        if self.VerifRGBFormat():
            listeRGB = self.txtBoxBase.get().split(",")
            couleur = (int(listeRGB[0]), int(listeRGB[1]), int(listeRGB[2]))
            if(self.nbBoucle == 0): self.adapter.FCC(int(listeRGB[0]), int(listeRGB[1]), int(listeRGB[2]))
            self.btnCouleur["bg"] = '#%02x%02x%02x' % couleur
            self.AddCmd("FCC", "Changer couleur en " + listeRGB[0] + "," + listeRGB[1] + "," + listeRGB[2], int(listeRGB[0]), int(listeRGB[1]), int(listeRGB[2]))

    def FCAP(self):
        if self.VerifFloat():
            angle = float(self.txtBoxBase.get())
            if angle <= 360 and angle >= 0:
                if(self.nbBoucle == 0): self.adapter.FCAP(angle)
                self.AddCmd("FCAP", "Changer angle " + self.txtBoxBase.get() + "°", angle)


    def FPOS(self):
        if self.VerifXYFormat():
            listeCoor = self.txtBoxBase.get().split(",")
            if(self.nbBoucle == 0): self.adapter.FPOS(float(listeCoor[0]), float(listeCoor[1]))
            self.AddCmd("FPOS", "Changer position pour x: " + listeCoor[0] + ", y:" + listeCoor[1], float(listeCoor[0]), float(listeCoor[1]))


    def Repeter(self):
        if (self.VerifInt()):
            if(int(self.txtBoxBase.get()) > 0):
                self.nbRep = int(self.txtBoxBase.get())
                self.AddCmd("Repeter", "Début répéter " + self.txtBoxBase.get() + " fois :", int(self.txtBoxBase.get()))
                self.btnFinRepeter["state"] = NORMAL
                if self.nbBoucle == 1:
                    self.nbRep = int(self.txtBoxBase.get())
                    self.indexBoucle = self.listeBoxHistorique.index(END)-1

    def FinRepeter(self):
        self.AddCmd("FinRepeter", "Fin répéter")
        if self.nbBoucle == 0:
            self.ExecuteBoucle(self.inBoucle, self.nbRep)
            self.inBoucle = []
            self.btnFinRepeter["state"] = DISABLED

    def ReprendreEnvoi(self):
        self.btnReprendreEnvoi["state"] = DISABLED
        self.btnArreterEnvoi["state"] = NORMAL
        self.btnEnvoyer["state"] = DISABLED

    def ArreterEnvoi(self):
        self.btnReprendreEnvoi["state"] = NORMAL
        self.btnArreterEnvoi["state"] = DISABLED
        self.btnEnvoyer["state"] = NORMAL

    def Envoyer(self):
        print("Envoyer commandes")

#----------------------------------------------------------------------------------------------------------------------#


    def __init__(self, _master):
        self.master = _master
        self.running = 1
        self.adapter = AdapterEditeur("Editeur")

        self.nbBoucle = 0
        self.lstCmd = []
        self.inBoucle = []
        self.indexBoucle = 0
        self.nbRep = 0

        self.master.title("Editeur")
        self.master.geometry("570x550")  # A voir si on change la taille
        self.master.resizable(False, False)

        couleurPanel = '#171717'
        couleurBtn = '#2b2b2b' #1e2129
        couleurTxt = '#ffffff'
        couleurFond = '#c2c3c4'

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
        self.btnEnregistrer = Button(self.panelOptions, text="enregistrer", font=("Helvetica", 12), bg=couleurBtn, fg=couleurTxt, command=self.SaveXML)
        self.btnCharger = Button(self.panelOptions, text="charger", font=("Helvetica", 12), bg=couleurBtn, fg=couleurTxt, command=self.LoadXML)
        self.listeBoxHistorique = Listbox(self.panelHistorique, height=15, bg=couleurFond)
        self.btnSupprimer = Button(self.panelOptions, text="supprimer commande", font=("Helvetica", 12), bg=couleurBtn, fg=couleurTxt, command=self.SuppCmd)
        self.btnReprendreEnvoi = Button(self.panelOptions, text="reprendre l'envoi", font=("Helvetica", 12), bg=couleurBtn,fg=couleurTxt, command=self.ReprendreEnvoi)
        self.btnArreterEnvoi = Button(self.panelOptions, text="arrêter l'envoi", font=("Helvetica", 12), bg=couleurBtn,fg=couleurTxt, command=self.ArreterEnvoi)
        self.btnEnvoyer = Button(self.panelOptions, text="envoyer", font=("Helvetica", 12), bg=couleurBtn,fg=couleurTxt, command=self.Envoyer)
        # Bouton quitter?

        # Disposition des éléments sur les panels
        self.txtBoxBase.pack(fill=X, padx=(50, 0), pady=10, side=LEFT)
        self.btnCouleur.pack(side=RIGHT, padx=20, pady=10)

        self.btnAvancer.pack(fill=X, ipadx=55)
        self.btnReculer.pack(fill=X, ipadx=55, pady=(0,5))
        self.btnTournerGauche.pack(fill=X, ipadx=55)
        self.btnTournerDroite.pack(fill=X, ipadx=55, pady=(0,5))
        self.btnLeverCrayon.pack(fill=X, ipadx=55)
        self.btnBaisserCrayon.pack(fill=X, ipadx=55, pady=(0,5))
        self.btnOrigine.pack(fill=X, ipadx=55)
        self.btnRestaurer.pack(fill=X, ipadx=55)
        self.btnNettoyer.pack(fill=X, ipadx=55, pady=(0,5))
        self.btnFCC.pack(fill=X, ipadx=55)
        self.btnFCAP.pack(fill=X, ipadx=55)
        self.btnFPOS.pack(fill=X, ipadx=55, pady=(0,5))
        self.btnRepeter.pack(fill=X, ipadx=55)
        self.btnFinRepeter.pack(fill=X, ipadx=55, pady=(0,5))

        self.listeBoxHistorique.pack(fill=X)

        self.btnSupprimer.pack(fill=X, ipadx=55, pady=(0,5))
        self.btnReprendreEnvoi.pack(fill=X, ipadx=55)
        self.btnArreterEnvoi.pack(fill=X, ipadx=55)
        self.btnEnvoyer.pack(fill=X, ipadx=55, pady=(0,5))
        self.btnEnregistrer.pack(fill=X, ipadx=55)
        self.btnCharger.pack(fill=X, ipadx=55)

        # Disposition des panels sur la fenêtre
        self.panelHaut.pack(fill=X, side=TOP)

        self.panelCommandes.pack(fill=X, padx=10, pady=10)
        self.panelHistorique.pack(fill=BOTH, padx=10, pady=10)
        self.panelOptions.pack(fill=X, padx=10, pady=10)

        self.panelGauche.pack(fill=Y, pady=3, padx=(3,0), side=LEFT)
        self.panelDroite.pack(fill=Y, pady=3, padx=(0,3), side=RIGHT)

        self.adapter.initialisation()


Editeur(root)
root.mainloop()

