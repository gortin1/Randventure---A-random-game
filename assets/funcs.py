from time import sleep as t
from assets.info.information import racesAndClasses
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
    desc = racesAndClasses
    wait.longwait()
    return digitar(desc.descricaoClasse(classasked))
def showRace():
    print("Qual seria a raça?")
    wait.smallwait()
    raceasked = str(input())
    desc = racesAndClasses
    wait.longwait()
    return digitar(desc.descricaoRaca(raceasked))
def getClass(tipo,classe):
    match tipo:
        case 1:
            classasked = classe
            desc = racesAndClasses
            wait.mediumwait()
            return digitar(desc.descricaoClasse(classasked))
        case 2:
            desc = racesAndClasses
            classasked = classe
            return digitar(desc.classXrace(classasked))
def getRace(race):
    raceasked = race
    desc = racesAndClasses
    wait.mediumwait()
    return digitar(desc.descricaoRaca(raceasked))

def showPericias(race):
    match race:
        case 'druida':
            pericias = racesAndClasses.descricaoPericias(race)
            return pericias
        case 'barbaro':
            pericias = racesAndClasses.descricaoPericias(race)
            return pericias
        case 'mago':
            pericias = racesAndClasses.descricaoPericias(race)
            return pericias
        case 'guerreiro':
            pericias = racesAndClasses.descricaoPericias(race)
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
    
def showClasses():
    return racesAndClasses.allClasses()