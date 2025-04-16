from time import sleep as t
from Informations.information import Describe

def wait():
    t(1)

def showClasse():
    print("Qual seria a classe?")
    wait()
    classasked = str(input())
    desc = Describe
    wait()
    print(desc.descricaoClasse(None,classasked))
    wait()
def showRace():
    print("Qual seria a raça?")
    wait()
    raceasked = str(input())
    desc = Describe
    wait()
    print(desc.descricaoRaca(None,raceasked))
    wait()