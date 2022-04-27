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


import inspect

def first():
    print(inspect.currentframe().f_code.co_name)
    print(inspect.stack()[1][3])
    second()


def second():
    print(inspect.currentframe().f_code.co_name)
    print(inspect.stack()[1][3])
    print(inspect.stack()[2][3])

def main():
    first()

main()