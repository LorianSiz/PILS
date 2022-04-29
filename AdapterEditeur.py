import inspect
from ivy.std_api import *

# Cette classe permet la communication en l'editeur et le visuel (ou son adapter)
# Elle implemente donc Ivy est propose a l'Editeur l'utilisation de

class AdapterEditeur:

#--------------------------------- Fonction d'envoie de requete -------------------------------------------------------#
    # format attendu:
    # Visuel --> {NomFonction} : {arg1} {arg2} {arg..}
    def SubmitRequet(self, *args):
        name = inspect.stack()[1][3]    # recuppere le nom de la fonction (identique a celui cote visu)
        msg = "Visuel --> " + name + " : "
        flag = 0;
        for arg in args:                # serialise tous les arguments passer en (args)
            if flag:
                msg += " "
            else:
                flag = 1
            msg += str(arg)

        IvySendMsg(msg)

    # fonction "wrap" permettent l'interfacage entre Enditeur/Adaptateur
    # WARNIG: les fonctions qui suivent doivent imperativement avoir le meme
    #         nom que les fonctions du visualiseur (ou Adapteur corespondant)

    def Avancer(self, dist):
        self.SubmitRequet(dist)

    def Reculer(self, dist):
        self.SubmitRequet(dist)

    def TournerGauche(self, ang):
        self.SubmitRequet(ang)

    def TournerDroite(self, ang):
        self.SubmitRequet(ang)

    def LeverCrayon(self):
        self.SubmitRequet()

    def BaisserCrayon(self):
        self.SubmitRequet()

    def Restaurer(self):
        self.SubmitRequet()

    def Origine(self):
        self.SubmitRequet()

    def Nettoyer(self):
        self.SubmitRequet()

    def FCC(self, r, g, b):
        self.SubmitRequet(r, g, b)

    def FCAP(self, ang):
        self.SubmitRequet(ang)

    def FPOS(self, x, y):
        self.SubmitRequet(x,y)

#----------------------------------------------------------------------------------------------------------------------#

    def __init__(self, name, ip = ""):
        self._name = name
        self._ip = ip

    def initialisation(self):
        IvyInit(self._name)
        IvyStart(self._ip)