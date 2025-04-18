from time import sleep as t
from assets.info.information import Describe
import sys
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
    wait.longwait()
    return desc.descricaoRaca(classasked)
def showRace():
    print("Qual seria a raça?")
    wait.smallwait()
    raceasked = str(input())
    desc = Describe
    wait.longwait()
    return desc.descricaoRaca(raceasked)
def getClass(classe):
    classasked = classe
    desc = Describe
    wait.mediumwait()
    return desc.descricaoClasse(classasked)
def getRace(race):
    raceasked = race
    desc = Describe
    wait.mediumwait()
    return desc.descricaoRaca(raceasked)
def showPericias(race):
    match race:
        case 'druida':
            pericias = Describe.descricaoPericias(race)
            return pericias
        case 'barbaro':
            pericias = Describe.descricaoPericias(race)
            return pericias
        case 'mago':
            pericias = Describe.descricaoPericias(race)
            return pericias
        case 'guerreiro':
            pericias = Describe.descricaoPericias(race)
            return pericias
        

def digitar(*args, delay=0.05):
    for arg in args:
        texto = str(arg)
        for char in texto:
            sys.stdout.write(char)
            sys.stdout.flush()
            t(delay)
    print()
