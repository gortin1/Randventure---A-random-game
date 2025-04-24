from time import sleep as t
from Assets.info.information import Describe
from random import randint as r
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
    return digitar(desc.descricaoClasse(classasked))
def showRace():
    print("Qual seria a raça?")
    wait.smallwait()
    raceasked = str(input())
    desc = Describe
    wait.longwait()
    return digitar(desc.descricaoRaca(raceasked))
def getClass(classe):
    classasked = classe
    desc = Describe
    wait.mediumwait()
    return digitar(desc.descricaoClasse(classasked))
def getRace(race):
    raceasked = race
    desc = Describe
    wait.mediumwait()
    return digitar(desc.descricaoRaca(raceasked))
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

def rolaracao(pericia, atributo):
    pericia = (pericia)/2 + atributo
    valor = r(1,20)
    result = pericia + valor
    return result

def showClasses():
    desc = Describe
    classes = digitar(desc.allClasses())
    return classes