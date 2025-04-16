from Assets.funcs import wait, showRace, showClasse
from Informations.information import Describe

def distribuirPontos(name):
    while True:
        print(f"Bem-Vindo {name} a distribuição de pontos do Randventure!")
        wait()
        print(f"Iremos fazer a distribuição de pontos do seu personagem")
        wait()
        print(f"Quer saber quais são os melhores tipo de distribuição para o seu personagem?")
        wait()
        answer1 = str(input("(Escreva S para sim ou N para não) \n"))
        running = True
        while running == True:
            if answer1.lower == "n":
                break   
            else:
                showClasse()
                print("Deseja saber de outra classe?")
                answer2 = str(input("(Escreva S para sim ou N para não) \n"))
                if answer2.lower == "s":
                    continue
                else:
                    break
        print("Bem, vamos começar com a distribuição de pontos!")
        
        forca, destreza, constituicao, inteligencia, sabedoria, carisma = 0,0,0,0,0,0
        pontosdisponiveis = 10
                
        while pontosdisponiveis > 0:
            print("Voce tem ", pontosdisponiveis, " digite qual o atributo que deseja aumentar")
            wait()
            print(
                "1- Força = ",forca,
                "\n2- Destreza = ",destreza,
                "\n3- Constituição = ",constituicao,
                "\n4- Inteligencia",inteligencia,
                "\n5- Sabedoria = ", sabedoria,
                "\n6- Carisma = ", carisma,
            )
            wait()
            choose = int(input("\nDigite qual você deseja aumentar (use os numeros indicados na frente do atributo!)\n"))
            match choose:
                case 1:
                    wait()
                    print("Atributo escolhido: (força)")
                    wait()
                    add = int(input("Digite a quantidade de pontos que deseja adicionar: "))
                    if add < pontosdisponiveis:
                        pass
                    else:
                        print("Erro ao adicionar! pontos insuficientes")
                        continue 
                    forca = forca + add
                    pontosdisponiveis -= add
                    print("\n\n\n\n\n\n\n")
                    continue
                case 2:
                    wait()
                    print("Atributo escolhido: (Destreza)")
                    wait()
                    add = int(input("Digite a quantidade de pontos que deseja adicionar: "))
                    if add < pontosdisponiveis:
                        pass
                    else:
                        print("Erro ao adicionar! pontos insuficientes")
                        continue
                    destreza = destreza + add
                    pontosdisponiveis -= add
                    print("\n\n\n\n\n\n\n")
                    continue
                case 3:
                    wait()
                    print("Atributo escolhido: (Constituição)")
                    wait()
                    add = int(input("Digite a quantidade de pontos que deseja adicionar: "))
                    if add < pontosdisponiveis:
                        pass
                    else:
                        print("Erro ao adicionar! pontos insuficientes")
                        continue
                    constituicao = constituicao + add
                    pontosdisponiveis -= add
                    print("\n\n\n\n\n\n\n")
                    continue
                case 4:
                    wait()
                    print("Atributo escolhido: (Inteligencia")
                    wait()
                    add = int(input("Digite a quantidade de pontos que deseja adicionar: "))
                    if add < pontosdisponiveis:
                        pass
                    else:
                        print("Erro ao adicionar! pontos insuficientes")
                        continue
                    inteligencia = inteligencia + add
                    pontosdisponiveis -= add
                    print("\n\n\n\n\n\n\n")
                    continue
                case 5:
                    wait()
                    print("Atributo escolhido: (Sabedoria)")
                    wait()
                    add = int(input("Digite a quantidade de pontos que deseja adicionar: "))
                    if add < pontosdisponiveis:
                        pass
                    else:
                        print("Erro ao adicionar! pontos insuficientes")
                        continue
                    sabedoria = sabedoria + add
                    pontosdisponiveis -= add
                    print("\n\n\n\n\n\n\n")
                    continue
                case 6:
                    wait()
                    print("Atributo escolhido: (Carisma)")
                    wait()
                    add = int(input("Digite a quantidade de pontos que deseja adicionar: "))
                    if add < pontosdisponiveis:
                        pass
                    else:
                        print("Erro ao adicionar! pontos insuficientes")
                        continue
                    carisma = carisma + add
                    pontosdisponiveis -= add
                    print("\n\n\n\n\n\n\n")
                    continue
                
def distribuirPericias(classe):
    #druida, guerreiro, barbaro e mago
    
    match classe:
        case "druida":
            #Arcanismo, Adestrar Animais, Intuição, Medicina, Natureza, Percepção, Religião e Sobrevivência
            wait()
            print("Bem vindo! iremos fazer a escolha de pericias!\n")
            wait()
            print("A raça que você escolheu anteriormente foi: ", classe)
            print("Gostaria de rever algumas coisas sobre a classe")
             
            