from time import sleep as t
from assets.info.information import Describe
class wait:
    def smallwait():
        t(1)
    def mediumwait():
        t(2.5)
    def longwait():
        t(5)
        

def showClasse():
    print("Qual seria a classe?")
    wait.smallwait()
    classasked = str(input())
    desc = Describe
    print(desc.descricaoClasse(None,classasked))
    wait.longwait()
def showRace():
    print("Qual seria a raça?")
    wait.smallwait()
    raceasked = str(input())
    desc = Describe
    print(desc.descricaoRaca(None,raceasked))
    wait.longwait()
def getClass(classe):
    classasked = classe
    desc = Describe
    print(desc.descricaoClasse(None, classasked))
    wait.mediumwait()
def getRace(race):
    raceasked = race
    desc = Describe
    print(desc.descricaoClasse(None, raceasked))
    wait.mediumwait()