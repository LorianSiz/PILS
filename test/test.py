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

test = [0,1,2,3,4,5,6,7,8,9]

def superss(lst, i):
    del lst[i]

print(test)

superss(test, 3)

print(test)
