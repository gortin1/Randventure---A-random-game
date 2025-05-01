from Assets.funcs import digitar,showClasses,clear
from .points import distribuirPericias,distribuirPontos
from Assets.info.information import Describe
def charCreate():
    desc = Describe
    digitar("Bem vindo a criação de personagem de Randeventure")
    digitar("Primeiramente iremos definir o nome do seu personagem: ")
    name = str(input("Digite o nome do personagem: "))
    digitar("Que belo nome! Qual vai ser a sexualidade do seu personagem? ")
    genero = int(input("Digite 1 para Mulher e 2 para Homem: "))
    match genero:
        case 1:
            digitar("Seja bem vinda",name,"Vamos escolher a sua classe e raça!")
            digitar("Gostaria de saber algumas combinações boas entre Classe e Raça? ")
            help = str(input("Digite S para sim e N para não")).lower()
            if help == "n":
                pass
            elif help == "s":
                digitar("Qual seria a classe na qual você gostaria de saber uma boa combinação?")
                showClasses()
                classeChoose = int(input("Digite o numero que fica na frente da classe desejada: "))
                """match classeChoose:
                    case 1:
                        showClasses()"""
            digitar("Vamos escolher sua classe!")
            digitar(desc.allClasses())
            while True:
                classe = int(input("Digite o numero indicado "))
                if classe is not None:
                    digitar("Voce escolheu a classe:",classe,". Deseja continuar?")
                    yn = str(input("S para sim, N para nao")).lower
                    if yn == "s":
                        break
                    else: 
                        continue
                else:
                    digitar("Por favor digite um numero valido!")
                    continue    
            clear()
            digitar("Vamos começar com a distribuição de pontos!")
            distribuirPontos(name)
            