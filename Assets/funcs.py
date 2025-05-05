from time import sleep as t
from assets.info.information import Describe
from random import randint as r
import sys
import os

class wait:
    def smallwait():
        t(1)
    def mediumwait():
        t(2.5)
    def longwait():
        t(5)
def showClasse(type):
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
def getClass(classe,type):
    match type:
        case 1:
            classasked = classe
            desc = Describe
            wait.mediumwait()
            return digitar(desc.descricaoClasse(classasked))
        case 2:
            desc = Describe
            return digitar(desc.classXrace(classe))
        
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

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')
    
def allclasse():
   desc = Describe
   return digitar(desc.allClasses)
def allraces():
    desc = Describe
    return digitar(desc.allRaces)

    
    