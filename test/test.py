# MASSONCamille
# Fichier de test pour eviter les coquilles
# A supprimer



# def test(name, *args):
#     print(name)
#     for arg in args:
#         print(arg)
#
# vName = "moi"
# vArg1 = 1
# vArg2 = 2
#
# test(vName)

#----------------------------------------------------------------------------------------------------------------------#


# import inspect
#
# def first():
#     print(inspect.currentframe().f_code.co_name)
#     print(inspect.stack()[1][3])
#     second()
#
#
# def second():
#     print(inspect.currentframe().f_code.co_name)
#     print(inspect.stack()[1][3])
#     print(inspect.stack()[2][3])
#
# def main():
#     first()
#
# main()

#----------------------------------------------------------------------------------------------------------------------#

# from time import sleep
# from AdapterEditeur import *
#
# test = AdapterEditeur("test")
# test.initialisation()
# print("attente")
# sleep(5)
# test.Avancer(100)
# print("envoyer")

#----------------------------------------------------------------------------------------------------------------------#

#for i in range(5,-1,-1): print(i)

# DicoXMLtoCmd = {
#     "avancer" : ["Avancer", "Avancer de "],
#     "reculer" : ["Reculer", "Reculer de "],
#     "droite" : ["TournerDroite", "Tourner à droite "],
#     "gauche" : ["TournerGauche", "Tourner à gauche "],
#     "lever" : ["LeverCrayon", "Lever le crayon"],
#     "baisser" : ["BaisserCrayon", "Baisser le crayon"],
#     "origine" : ["Origine", "Retour à l'origine"],
#     "restaurer" : ["Restaurer", "Restaurer"],
#     "nettoyer" : ["Nettoyer", "Nettoyer"],
#     "crayon" : ["FCC", "Changer couleur en "],
#     "cap" : ["FCAP", "Changer angle "],
#     "position" : ["FPOS", "Changer position pour x y: "],
#     "répéter" : ["Repeter", "Début répéter "]
# }
#
# for t in DicoXMLtoCmd:
#     print(t)

#----------------------------------------------------------------------------------------------------------------------#

# import codecs
# import xml.etree.cElementTree as ET
#
# # with open('C:\Temp\Test2.xml') as xml_file:
# #     xmlstr = xml_file.read()
# #
# #     test = str(xmlstr).encode("")
#
# s = codecs.open('C:\Temp\Test2.xml', 'r', 'utf-8')
# xmlstr = s.read()
#
# xml = ET.fromstring(xmlstr)
#
# for elem in xml:
#     print(elem)

#----------------------------------------------------------------------------------------------------------------------#

test = [0,1,2,3,4,5,6,7,8,9]
print(test)

del test[0 : len(test)]
print(test)
