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
    wait.longwait()
    return desc.descricaoRaca(None,classasked)
def showRace():
    print("Qual seria a raça?")
    wait.smallwait()
    raceasked = str(input())
    desc = Describe
    wait.longwait()
    return desc.descricaoRaca(None,raceasked)
def getClass(classe):
    classasked = classe
    desc = Describe
    wait.mediumwait()
    return desc.descricaoClasse(None, classasked)
def getRace(race):
    raceasked = race
    desc = Describe
    wait.mediumwait()
    return desc.descricaoRaca(None, raceasked)
def showPericias(race):
    match race:
        case 'druida':
            pericias = {
                 'showPericias':[
                     'arcanismo',
                     'adestrar animais',
                     'intuicao',
                     'medicina',
                     'natureza',
                     'percepcao',
                     'religiao',
                     'sobrevivencia'
                     ]
            }
            return '\n'.join(pericias['showPericias'])