import time as t
import random as r

execute = True

while execute:

    # Seleção de jogo

    print("Bem-vindo ao Randeventure")
    print()
    t.sleep(3)

    print("Qual jogo gostaria de jogar?")
    print()
    t.sleep(2)

    games = ["1- DnD (Indisponível)", "2- Call of Cthulhu (Indisponível)", "3- Tormenta"]
    print("Por favor, selecione utilizando o número da aventura que deseja")
    print()
    t.sleep(1.5)
    
    for game in games:
        print(game)
        t.sleep(3)

    game = int(input())
    print("\n")
    match game:

        case 1:
            print("Desculpe, mas esta experiência ainda não está disponível")
            t.sleep(1.5)
            print("Por favor, escolha uma experiência que esteja disponível")
            t.sleep(2)
            print("Voltando ao início da experiência")
            print("\n")
            execute = False
            execute = True
        case 2:
            print("Desculpe, mas esta experiência ainda não está disponível")
            t.sleep(1.5)
            print("Por favor, escolha uma experiência que esteja disponível")
            t.sleep(2)
            print("Voltando ao início da experiência")
            execute = False
            execute = True
        case 3:
            print("A experiência selecionada é Tormenta")
            t.sleep(1)
            print("Deseja continuar?")
            confirm = str(input())
            if confirm.lower() == 'sim' or confirm.lower() == 's':
                menu = True
                while menu:
                    t.sleep(2)
                    print("\n\n")
                    print("Bem vindo ao Menu da experiencia Tormenta")
                    opt = ["1- Começar","2- Descrição","3- Informaçôes","4- Sair"]
                    for opt in opt:
                        print(opt)
                        t.sleep(1)
                    state = int(input())
                    
                    match state:

                        case 1:
                            print("Seja muito bem-vindo ao mundo fantástico do Tormenta")
                            t.sleep(3)
                            print("Onde você encontrará seres mágicos, coisas surreais e monstros à espreita")
                            t.sleep(3)
                            print("Vamos começar com a criação do nosso aventureiro, que é você")
                            t.sleep(3)
                            print("Vamos começar pela sua raça, escolha com numeros uma das seguintes raças")
                            print("\n")
                            races = ['1- Humano','2- Anão','3- Dahllan','4-Elfo']
                            for races in races:
                                print(races)
                                print("\n")
                                t.sleep(2)
                            
                            choose = True
                            while choose:
                                race = int(input())
                                forp = desp = consp = intp = sabp = carp =  0
                                For = Des = Cons = Int = Sab = Car = 0
                                niv = 1
                                quantPontos = 20
                                match race:
                                    
                                    case 1:
                                        print("A raça escolhida é Humano")
                                        t.sleep(2)
                                        
                                        print("Deseja prosseguir e ver seus bonus")
                                        confi = str(input())
                                        if confi.lower == "sim" or confi.lower == "s":
                                          print("Humano")
                                          t.sleep(2)
                                          print("Bonus de atributo")
                                          print("+2 em três atributos diferentes")
                                          print("\n")
                                          t.sleep(2)
                                          print("Treinado em 2 pericias de sua escolha")
                                          print("\n")
                                          print(" Você confirma a sua escolha ?")
                                          confi2 = str(input())
                                          if confi2.lower == "sim" or confi2 == "s":
                                              pontos = True
                                              while pontos:
                                                print("A raça escolhida é humano")
                                                print("Escolha abaixo com numeros os atributos na qual você gostaria de aumentar: ")
                                                at = ["1-Força","2-Destreza","3-Constituição","4-Inteligencia","5-Sabedoria", "6-Carisma"]
                                                for at in at:
                                                    print(at)
                                                    print("\n")
                                                    t.time(3)
                                                at1 = int(input("Digite o numero do primeiro atributo aumentado:"))
                                                if at1 == 1:
                                                    forp = 2
                                                elif at1 == 2:
                                                    desp = 2
                                                elif at1 == 3:
                                                    consp = 2
                                                elif at1 == 4:
                                                    intp = 2
                                                elif at1 == 5:
                                                    sabp = 2
                                                elif at1 == 6:
                                                    carp = 2
                                                else:
                                                    print("Digite um numero correto!")
                                                    pontos=False
                                                    pontos=True
                                                at2 = int(input("Digite o numero segundo atributo:"))
                                                if at2 == 1:
                                                    forp = 2
                                                elif at2 == 2:
                                                    desp = 2
                                                elif at2 == 3:
                                                    consp = 2
                                                elif at2 == 4:
                                                    intp = 2
                                                elif at2 == 5:
                                                    sabp = 2
                                                elif at2 == 6:
                                                    carp = 2
                                                else:
                                                    print("Digite um numero correto!")
                                                    pontos=False
                                                    pontos=True
                                                at3 = int(input("Digite o numero terceiro atributo:"))
                                                if at3 == 1:
                                                    forp = 2
                                                elif at3 == 2:
                                                    desp = 2
                                                elif at3 == 3:
                                                    consp = 2
                                                elif at3 == 4:
                                                    intp = 2
                                                elif at3 == 5:
                                                    sabp = 2
                                                elif at3 == 6:
                                                    carp = 2
                                                else:
                                                    print("Digite um numero correto!")
                                                    pontos=False
                                                    pontos=True
                                                t.time(5)
                                                print("Agora você irá distribuir os ponto que estão disponiveis")
                                                print("Restam :", quantPontos)
                                                if quantPontos > 0:
                                                    print(quantPontos,"Restantes")
                                                    forp = int(input("quantos pontos deseja adicionar em Força? "))
                                                    quantPontos = quantPontos - forp
                                                    For = 0 + forp
                                                    print(" ")
                                                else:
                                                    pontos = False
                                                if quantPontos > 0:
                                                    print(quantPontos,"Restantes")
                                                    desp = int(input("quantos pontos deseja adicionar em Destreza? "))
                                                    quantPontos = quantPontos - desp
                                                    Des = 0 + desp
                                                    print(" ")
                                                else:
                                                    pontos = False
                                                if quantPontos > 0:
                                                    print(quantPontos,"Restantes")
                                                    consp = int(input("quantos pontos deseja adicionar em Constituição? "))
                                                    quantPontos = quantPontos - consp
                                                    Cons = 0 + consp
                                                    print(" ")
                                                else:
                                                    pontos = False
                                                if quantPontos > 0  :
                                                    print(quantPontos,"Restantes")
                                                    intp = int(input("quantos pontos deseja adicionar em Inteligencia? "))
                                                    quantPontos = quantPontos - intp
                                                    Int = 0 + intp
                                                    print(" ")
                                                else:
                                                    pontos = False
                                                if quantPontos > 0 :
                                                    print(quantPontos,"Restantes")
                                                    sabp = int(input("quantos pontos deseja adicionar em Sabedoria? "))
                                                    quantPontos = quantPontos - sabp
                                                    Sab = 0 + sabp
                                                    print(" ")
                                                else:
                                                    pontos = False
                                                if quantPontos > 0 :
                                                    print(quantPontos,"Restantes")
                                                    carp = int(input("quantos pontos deseja adicionar em Carisma? "))
                                                    quantPontos = quantPontos - carp
                                                    Car = 0 + carp
                                                else:
                                                    pontos = False
                                                
                                                if forp == -5:
                                                    modF = -5
                                                elif forp == -4:
                                                    modF = -4
                                                elif forp == -3:
                                                    modF = -3
                                                elif forp == -2:
                                                    modF = -2
                                                elif forp == -1:
                                                    modF = -1
                                                elif forp == 2 or forp == 3:
                                                    modF = 1
                                                elif forp == 0:
                                                    modF = 0
                                                elif forp == 4 or forp == 5:
                                                    modF = 2
                                                elif forp == 6 or forp == 7:
                                                    modF = 3
                                                elif forp== 8 or forp == 9:
                                                    modF = 4
                                                elif forp == 10 or forp == 11:
                                                    modF = 5
                                                elif forp == 12 or forp == 13:
                                                    modF = 6
                                                elif forp == 14 or forp == 15:
                                                    modF = 7
                                                elif forp == 16 or forp == 17:
                                                    modF = 8
                                                elif forp == 18 or forp == 19:
                                                    modF = 9
                                                else:
                                                    modF = 10

                                                if desp == -5:
                                                    modD = -5
                                                elif desp == -4:
                                                    modD = -4
                                                elif desp == -3:
                                                    modD = -3
                                                elif desp == -2:
                                                    modD = -2
                                                elif desp == -1:
                                                    modD = -1
                                                elif desp == 0:
                                                    modD = 0
                                                elif desp == 2 or desp == 3:
                                                    modD = 1
                                                elif desp == 4 or desp == 5:
                                                    modD = 2
                                                elif desp == 6 or desp == 7:
                                                    modD = 3
                                                elif desp == 8 or desp == 9:
                                                    modD = 4
                                                elif desp == 10 or desp == 11:
                                                    modD = 5
                                                elif desp == 12 or desp == 13:
                                                    modD = 6
                                                elif desp == 14 or desp == 15:
                                                    modD = 7
                                                elif desp == 16 or desp == 17:
                                                    modD = 8
                                                elif desp == 18 or desp == 19:
                                                    modD = 9
                                                else:
                                                    modD = 10

                                                if consp == -5:
                                                    modC = -5
                                                elif consp == -4:
                                                    modC = -4
                                                elif consp == -3:
                                                    modC = -3
                                                elif consp == -2:
                                                    modC = -2
                                                elif consp == -1:
                                                    modC = -1
                                                elif consp == 0:
                                                    modC = 0
                                                elif consp == 2 or consp == 3:
                                                    modC = 1
                                                elif consp == 4 or consp == 5:
                                                    modC = 2
                                                elif consp == 6 or consp == 7:
                                                    modC = 3
                                                elif consp == 8 or consp == 9:
                                                    modC = 4
                                                elif consp == 10 or consp == 11:
                                                    modC = 5
                                                elif consp == 12 or consp == 13:
                                                    modC = 6
                                                elif consp == 14 or consp == 15:
                                                    modC = 7
                                                elif consp == 16 or consp == 17:
                                                    modC = 8
                                                elif consp == 18 or consp == 19:
                                                    modC = 9
                                                else:
                                                    modC = 10

                                                if intp == -5:
                                                    modI = -5
                                                elif intp == -4:
                                                    modI = -4
                                                elif intp == -3:
                                                    modI = -3
                                                elif intp == -2:
                                                    modI = -2
                                                elif intp == -1:
                                                    modI = -1
                                                elif intp == 0:
                                                    modI = 0
                                                elif intp == 2 or intp == 3:
                                                    modI = 1
                                                elif intp == 4 or intp == 5:
                                                    modI = 2
                                                elif intp == 6 or intp == 7:
                                                    modI = 3
                                                elif intp == 8 or intp == 9:
                                                    modI = 4
                                                elif intp == 10 or intp == 11:
                                                    modI = 5
                                                elif intp == 12 or intp == 13:
                                                    modI = 6
                                                elif intp == 14 or intp == 15:
                                                    modI = 7
                                                elif intp == 16 or intp == 17:
                                                    modI = 8
                                                elif intp == 18 or intp == 19:
                                                    modI = 9
                                                else:
                                                    modI = 10

                                                if sabp == -5:
                                                    modS = -5
                                                elif sabp == -4:
                                                    modS = -4
                                                elif sabp == -3:
                                                    modS = -3
                                                elif sabp == -2:
                                                    modS = -2
                                                elif sabp == -1:
                                                    modS = -1
                                                elif sabp == 0:
                                                    modS = 0
                                                elif sabp == 2 or sabp == 3:
                                                    modS = 1
                                                elif sabp == 4 or sabp == 5:
                                                    modS = 2
                                                elif sabp == 6 or sabp == 7:
                                                    modS = 3
                                                elif sabp == 8 or sabp == 9:
                                                    modS = 4
                                                elif sabp == 10 or sabp == 11:
                                                    modS = 5
                                                elif sabp == 12 or sabp == 13:
                                                    modS = 6
                                                elif sabp == 14 or sabp == 15:
                                                    modS = 7
                                                elif sabp == 16 or sabp == 17:
                                                    modS = 8
                                                elif sabp == 18 or sabp == 19:
                                                    modS = 9
                                                else:
                                                    modS = 10

                                                if carp == -5:
                                                    modCa = -5
                                                elif carp == -4:
                                                    modCa = -4
                                                elif carp == -3:
                                                    modCa = -3
                                                elif carp == -2:
                                                    modCa = -2
                                                elif carp == -1:
                                                    modCa = -1
                                                elif carp == 0:
                                                    modCa = 0
                                                elif carp == 2 or carp == 3:
                                                    modCa = 1
                                                elif carp == 4 or carp == 5:
                                                    modCa = 2
                                                elif carp == 6 or carp == 7:
                                                    modCa = 3
                                                elif carp == 8 or carp == 9:
                                                    modCa = 4
                                                elif carp == 10 or carp == 11:
                                                    modCa = 5
                                                elif carp == 12 or carp == 13:
                                                    modCa = 6
                                                elif carp == 14 or carp == 15:
                                                    modCa = 7
                                                elif carp == 16 or carp == 17:
                                                    modCa = 8
                                                elif carp == 18 or carp == 19:
                                                    modCa = 9
                                                else:
                                                    modCa = 10
                                                    
                                                print("\nForça : ",For,"\nmodificador de força : ", modF,"\n\nDestreza : ",Des,"\nModificador de destreza : ", modD,"\n\nConstituição : ",Cons,"\nModificador de constituição : ",modC,"\n\nInteligencia : ",Int,"\nModificador de inteligencia : ",modI,"\n\nSabedoria : ",Sab,"\nModificador de sabedoria : ",modS,"\n\nCarisma : ",Car,"\nModificador de carisma : ",modCa)
                                                confi3 = str(input("Deseja manter todas as suas escolhas "))
                                                if confi3.lower == "sim" or confi3.lower == "s":
                                                    classeProcesso = True
                                                    while classeProcesso:
                                                        classeList = classes = ["\n1- Arcanista. Um conjurador de magias arcanas, por meio de estudo, um foco ou dom natural.\n","2- Bárbaro. Um combatente primitivo, que usa fúria e instintos para destruir seus inimigos.\n","3- Bardo. Um artista errante e faz-tudo versátil, sempre com a solução certa para cada ocasião.\n","4- Bucaneiro. Um navegador inconsequente e galante, sempre em busca de ouro ou emoção.\n","5- Caçador. Um exterminador de monstros e mestre da sobrevivência em áreas selvagens.\n","6- Cavaleiro. Um combatente honrado, especializado em suportar dano e proteger os outros.\n","7- Clérigo. Servo de um dos deuses de Arton, usa poderes divinos para defender seus ideais.\n","8- Druida. Guardião do mundo natural e devoto das forças selvagens, naturais ou monstruosas.\n","9- Guerreiro. O especialista supremo em técnicas de combate com armas.\n","10- Inventor. Um ferreiro, alquimista ou engenhoqueiro, especializado em fabricar e usar itens.\n","11- Ladino. Aventureiro cheio de truques, confiando mais em agilidade e esperteza que em força bruta.\n","12- Lutador. Um especialista em combate desarmado rústico e durão.\n","13- Nobre. Um membro da alta sociedade cujas principais armas são as palavras e o orgulho.\n","14- Paladino. Um campeão do bem e da ordem, o perfeito soldado dos deuses.\n"]
                                                    for cList in classeList:
                                                        print(cList)
                                                        t.sleep(1)
                                                    classe = int(input("Escolha uma das classes que foi mostrada (usando o numero que esta no começo da classe)\n"))
                                                    
                                                else:
                                                    choose = False
                                                    choose = True
                                        else:
                                          choose == False
                                          choose == True
                                    case 2:
                                        print
                                    case 3:
                                        print             
                                    case 4: 
                                        print
                            
                        case 2:
                            
                            print("Esta experiência é feita por um único fã, então espero que goste")
                            print("Se encontrar qualquer problema, por favor reporte ao criador")
                            t.sleep(2)
                            
                        case 3:
                            info = True
                            
                            while info:
                                print(" ")
                                print("O que voce gostaria de saber sobre o Tormenta")
                                QA = ['1- Raças','2- Atributos','3- Pericias','4- Voltar']
                                for QA in QA:
                                    print("\n")
                                    print(QA)
                                    t.sleep(1)
                                state = int(input())
                                match state:
                                    


                                    case 1:
                                        print(" ")
                                        print("Qual das raças abaixo gostaria de saber mais?")
                                        t.sleep(1)
                                        races = ['1- Humano','2- Anão','3- Dahllan','4- Elfo']
                                        for races in races:
                                            print(races)
                                            t.sleep(2)
                                            
                                        race = int(input())
                                            
                                        match race:
                                            
                                            case 1:
                                                print("Humano")
                                                t.sleep(2)
                                                print("Bonus de atributo")
                                                print("+2 em tres atributos diferentes")
                                                print("\n")
                                                t.sleep(2)
                                                print("Treinado em 2 pericias de sua escolha")
                                                print("\n")
                                                info = False
                                                info = True
                                            case 2:
                                                print("Anão")
                                                t.sleep(2)
                                                print("Bonus de atributo")
                                                print("Constituição +4, Sabedoria +2, Destreza -2")
                                                print("\n")
                                                t.sleep(2)
                                                print("Voce recebe visao no escuro")
                                                print("+2 em percepção e sobrevivencia no subterraneo")
                                                print("\n")
                                                t.sleep(2)
                                                print("Seu deslocamento é 6m")
                                                print("mas nao toma reduçao por armadilha ou excesso de carga")
                                                print("\n")
                                                t.sleep(2)
                                                print("recebe +3 de vida no nivel 1 e +1 por cada nivel")
                                                print("\n")
                                                t.sleep(2)
                                                print("Machados, Martelos, Marretas e picaretas")
                                                print("essas armas são simples para voce e recebe +2 em ataques com estas armas")
                                                print("\n")
                                                info = False
                                                info = True
                                            case 3:
                                                print("Dahllan")
                                                t.sleep(2)
                                                print("Bonus de atributo")
                                                print("Sabedoria +4, Destreza +2, Inteligencia -2")
                                                print("\n")
                                                t.sleep(2)
                                                print("Voce pode lançar a magia 'Controlar Plantas")
                                                print("Caso aprenda novamente esta magia voce gastara -1 ponto de mana")
                                                print("\n")
                                                t.sleep(2)
                                                print("Voce tem a pericia Adestramento")
                                                print("Caso aprenda esta pericia novamente recebe +2 em adestramento")
                                                print("\n")
                                                info = False
                                                info = True
                                            case 4:
                                                print("Elfo")
                                                t.sleep(2)
                                                print("\n")
                                                print("Bonus de atributo")
                                                print("Inteligência +4, Destreza +2,Constituição -2")
                                                print("\n")
                                                t.sleep(2)
                                                print("\n")
                                                print("Voce é pequeno mas seu deslocamento continua 12m")
                                                print("\n")
                                                t.sleep(2)
                                                print("\n")
                                                print("Voce recebe +1 de mana por nivel")
                                                print("\n")
                                                t.sleep(2)
                                                print("\n")
                                                print("Voce ve na penumbra")
                                                print("Recebe +2 em percepção e misticismo")
                                                print("\n")
                                                info = False
                                                info = True
                                    case 2:
                                        print
                
                                    case 3:
                                        print
                                        
                                        
                                    case 4:
                                        menu = False
                                        menu = True
                        case 4:
                            execute = False
                            
                    print("Então iremos continuar para a criação de personagem")
                    t.sleep(2.5)
            else:
                print("Compreendo, o levarei de volta para o início")
                t.sleep(2)
                execute = False
                execute = True
















# CODIGO ABAIXO AINDA NAO VOU USAR MAS SALVAR AQUI PQ SIM :)


"""t.sleep(3)

classeList = classes = ["\n1- Arcanista. Um conjurador de magias arcanas, por meio de estudo, um foco ou dom natural.\n","2- Bárbaro. Um combatente primitivo, que usa fúria e instintos para destruir seus inimigos.\n","3- Bardo. Um artista errante e faz-tudo versátil, sempre com a solução certa para cada ocasião.\n","4- Bucaneiro. Um navegador inconsequente e galante, sempre em busca de ouro ou emoção.\n","5- Caçador. Um exterminador de monstros e mestre da sobrevivência em áreas selvagens.\n","6- Cavaleiro. Um combatente honrado, especializado em suportar dano e proteger os outros.\n","7- Clérigo. Servo de um dos deuses de Arton, usa poderes divinos para defender seus ideais.\n","8- Druida. Guardião do mundo natural e devoto das forças selvagens, naturais ou monstruosas.\n","9- Guerreiro. O especialista supremo em técnicas de combate com armas.\n","10- Inventor. Um ferreiro, alquimista ou engenhoqueiro, especializado em fabricar e usar itens.\n","11- Ladino. Aventureiro cheio de truques, confiando mais em agilidade e esperteza que em força bruta.\n","12- Lutador. Um especialista em combate desarmado rústico e durão.\n","13- Nobre. Um membro da alta sociedade cujas principais armas são as palavras e o orgulho.\n","14- Paladino. Um campeão do bem e da ordem, o perfeito soldado dos deuses.\n"]

for cList in classeList:
  print(cList)
  t.sleep(1)
classe = int(input("Escolha uma das classes que foi mostrada (usando o numero que esta no começo da classe)\n"))
match classe:
  case 1:
    perArcana = ["1- Conhecimento (Int)","2- Iniciativa (Des)","3- Percepção (Sab)"]
    main_atr = ["Misticismo (Int)","Vontade (Sab)"]
    for atr in perArcana:
      print(atr)
      t.sleep(1)
    print("As pericias acima são as que são possiveis aprender (Voce so pode escolher uma, escreva a pericia desejada)")
    perAprendida = str(input())
    if perAprendida.lower() == "conhecimento":
      misticismoA = int(2 + modI + niv/2)
      vontadeA = int(2 + modS + niv/2)
      conhecimentoA = int(2 + modI + niv/2)
      acrobaciaA = int(0 + modD + niv/2)
      adestramentoA = 0
      atletismoA = int(0 + modF+ niv/2)
      atuacaoA = int(0 + modCa + niv/2)
      cavalgarA = int(0 + modD + niv/2)
      curaA = int(0 + modS + niv/2)
      diplomaciaA = int(0 + modCa + niv/2 )
      enganacaoA = int(0+modCa+ niv/2)
      fortitudeA = int(0+modC+ niv/2)
      furtividadeA = int(0+modD+ niv/2)
      guerraA = 0
      iniciativaA = int(0+modD+ niv/2)
      intimidacaoA = int(0+modCa+ niv/2)
      intuicaoA = int(0+modS+niv/2)
      investigacaoA = int(0+modI+niv/2)
      jogatinaA = 0
      ladinagemA = 0
      lutaA = int(0+modF+niv/2)
      nobrezaA = 0
      percepcaoA = int(0+modS+niv/2)
      pilotagemA = 0
      pontariaA = int(0+modS+niv/2)
      reflexosA = int(0+modD+niv/2)
      religiaoA = 0
      sobrevivenciaA = int(0+modS+niv/2)
      pericias= [
        ("Acrobacia (penalidade de armadura):",acrobaciaA),
        ("Adestramento (treinada):",adestramentoA),
        ("Atletismo:",atletismoA),
        ("Atuação:",atuacaoA),
        ("Cavalgar:",cavalgarA),
        ("Conhecimento (treinada):",conhecimentoA),
        ("Cura:",curaA),
        ("Diplomacia:",diplomaciaA),
        ("Enganação:",enganacaoA),
        ("Fortitude:",fortitudeA),
        ("Furtividade:",furtividadeA),
        ("Guerra (treinada):",guerraA),
        ("Iniciativa:",iniciativaA),
        ("Intimidação:",intimidacaoA),
        ("Intuição:",intuicaoA),
        ("Investigação:",investigacaoA),
        ("Jogatina (treinada):",jogatinaA),
        ("Ladinagem (treinada e penalidade por armadura):",ladinagemA),
        ("Luta:",lutaA),
        ("Misticismo:",misticismoA),
        ("Percepção:",percepcaoA),
        ("Pilotagem (treinada):",pilotagemA),
        ("Pontaria:",pontariaA),
        ("Reflexos:",reflexosA),
        ("Religião (Treinada):",religiaoA),
        ("Sobrevivência:",sobrevivenciaA),
        ("Vontade:",vontadeA)]
      for per in pericias:
        print(per)
        print("\n")
        t.sleep(1)
      acrobacia = ("Acrobacia (penalidade de armadura):",acrobaciaA),
      adestramento = ("Adestramento (treinada):",adestramentoA),
      atletismo = ("Atletismo:",atletismoA),
      atuacao = ("Atuação:",atuacaoA),
      cavalgar("Cavalgar:",calvalgarA),
      conhecimento = ("Conhecimento (treinada):",conhecimentoA),
      cura = ("Cura:",curaA),
      diplomacia = ("Diplomacia:",diplomaciaA)
      enganacao = ("Enganação:",enganacaoA)
      fortitude = ("Fortitude:",fortitudeA)
      furtividade = ("Furtividade:",furtividadeA)
      guerra = ("Guerra (treinada):",guerraA)
      iniciativa = ("Iniciativa:",iniciativaA)
      intimidacao = ("Intimidação:",intimidacaoA)
      intuicao = ("Intuição:",intuicaoA)
      investigacao = ("Investigação:",investigacaoA)
      jogatina = ("Jogatina (treinada):",jogatinaA)
      ladinagem = ("Ladinagem (treinada e penalidade por armadura):",ladinagemA)
      luta = ("Luta:",lutaA),
      misticismo = ("Misticismo:",misticismoA),
      percepcao = ("Percepção:",percepcaoA),
      pilotagem = ("Pilotagem (treinada):",pilotagemA),
      pontaria = ("Pontaria:",pontariaA),
      reflexos = ("Reflexos:",reflexosA),
      religiao = ("Religião (Treinada):",religiaoA),
      sobrevivencia = ("Sobrevivência:",sobrevivenciaA),
      vontade = ("Vontade:",vontadeA)
    elif perAprendida.lower == "iniciativa":
      misticismoA = int(2 + modI + niv/2)
      vontadeA = int(2 + modS + niv/2)
      conhecimentoA = int(0 + modI + niv/2)
      acrobaciaA = int(0 + modD + niv/2)
      adestramentoA = 0
      atletismoA = int(0 + modF+ niv/2)
      atuacaoA = int(0 + modCa + niv/2)
      cavalgarA = int(0 + modD + niv/2)
      curaA = int(0 + modS + niv/2)
      diplomaciaA = int(0 + modCa + niv/2 )
      enganacaoA = int(0+modCa+ niv/2)
      fortitudeA = int(0+modC+ niv/2)
      furtividadeA = int(0+modD+ niv/2)
      guerraA = 0
      iniciativaA = int(2+modD+ niv/2)
      intimidacaoA = int(0+modCa+ niv/2)
      intuicaoA = int(0+modS+niv/2)
      investigacaoA = int(0+modI+niv/2)
      jogatinaA = 0
      ladinagemA = 0
      lutaA = int(0+modF+niv/2)
      nobrezaA = 0
      percepcaoA = int(0+modS+niv/2)
      pilotagemA = 0
      pontariaA = int(0+modS+niv/2)
      reflexosA = int(0+modD+niv/2)
      religiaoA = 0
      sobrevivenciaA = int(0+modS+niv/2)
      pericias= [
        ("Acrobacia (penalidade de armadura):",acrobaciaA),
        ("Adestramento (treinada):",adestramentoA),
        ("Atletismo:",atletismoA),
        ("Atuação:",atuacaoA),
        ("Cavalgar:",cavalgarA),
        ("Conhecimento (treinada):",conhecimentoA),
        ("Cura:",curaA),
        ("Diplomacia:",diplomaciaA),
        ("Enganação:",enganacaoA),
        ("Fortitude:",fortitudeA),
        ("Furtividade:",furtividadeA),
        ("Guerra (treinada):",guerraA),
        ("Iniciativa:",iniciativaA),
        ("Intimidação:",intimidacaoA),
        ("Intuição:",intuicaoA),
        ("Investigação:",investigacaoA),
        ("Jogatina (treinada):",jogatinaA),
        ("Ladinagem (treinada e penalidade por armadura):",ladinagemA),
        ("Luta:",lutaA),
        ("Misticismo:",misticismoA),
        ("Percepção:",percepcaoA),
        ("Pilotagem (treinada):",pilotagemA),
        ("Pontaria:",pontariaA),
        ("Reflexos:",reflexosA),
        ("Religião (Treinada):",religiaoA),
        ("Sobrevivência:",sobrevivenciaA),
        ("Vontade:",vontadeA)]
      for per in pericias:
        print(per)
        print("\n")
        t.sleep(1)
      acrobacia = ("Acrobacia (penalidade de armadura):",acrobaciaA),
      adestramento = ("Adestramento (treinada):",adestramentoA),
      atletismo = ("Atletismo:",atletismoA),
      atuacao = ("Atuação:",atuacaoA),
      cavalgar("Cavalgar:",calvalgarA),
      conhecimento = ("Conhecimento (treinada):",conhecimentoA),
      cura = ("Cura:",curaA),
      diplomacia = ("Diplomacia:",diplomaciaA)
      enganacao = ("Enganação:",enganacaoA)
      fortitude = ("Fortitude:",fortitudeA)
      furtividade = ("Furtividade:",furtividadeA)
      guerra = ("Guerra (treinada):",guerraA)
      iniciativa = ("Iniciativa:",iniciativaA)
      intimidacao = ("Intimidação:",intimidacaoA)
      intuicao = ("Intuição:",intuicaoA)
      investigacao = ("Investigação:",investigacaoA)
      jogatina = ("Jogatina (treinada):",jogatinaA)
      ladinagem = ("Ladinagem (treinada e penalidade por armadura):",ladinagemA)
      luta = ("Luta:",lutaA),
      misticismo = ("Misticismo:",misticismoA),
      percepcao = ("Percepção:",percepcaoA),
      pilotagem = ("Pilotagem (treinada):",pilotagemA),
      pontaria = ("Pontaria:",pontariaA),
      reflexos = ("Reflexos:",reflexosA),
      religiao = ("Religião (Treinada):",religiaoA),
      sobrevivencia = ("Sobrevivência:",sobrevivenciaA),
      vontade = ("Vontade:",vontadeA)
    elif perAprendida.lower() == "percepcao":
      misticismoA = int(2 + modI + niv/2)
      vontadeA = int(2 + modS + niv/2)
      conhecimentoA = int(0 + modI + niv/2)
      acrobaciaA = int(0 + modD + niv/2)
      adestramentoA = 0
      atletismoA = int(0 + modF+ niv/2)
      atuacaoA = int(0 + modCa + niv/2)
      cavalgarA = int(0 + modD + niv/2)
      curaA = int(0 + modS + niv/2)
      diplomaciaA = int(0 + modCa + niv/2 )
      enganacaoA = int(0+modCa+ niv/2)
      fortitudeA = int(0+modC+ niv/2)
      furtividadeA = int(0+modD+ niv/2)
      guerraA = 0
      iniciativaA = int(0+modD+ niv/2)
      intimidacaoA = int(0+modCa+ niv/2)
      intuicaoA = int(0+modS+niv/2)
      investigacaoA = int(0+modI+niv/2)
      jogatinaA = 0
      ladinagemA = 0
      lutaA = int(0+modF+niv/2)
      nobrezaA = 0
      percepcaoA = int(2+modS+niv/2)
      pilotagemA = 0
      pontariaA = int(0+modS+niv/2)
      reflexosA = int(0+modD+niv/2)
      religiaoA = 0
      sobrevivenciaA = int(0+modS+niv/2)
      pericias= [
        ("Acrobacia (penalidade de armadura):",acrobaciaA),
        ("Adestramento (treinada):",adestramentoA),
        ("Atletismo:",atletismoA),
        ("Atuação:",atuacaoA),
        ("Cavalgar:",cavalgarA),
        ("Conhecimento (treinada):",conhecimentoA),
        ("Cura:",curaA),
        ("Diplomacia:",diplomaciaA),
        ("Enganação:",enganacaoA),
        ("Fortitude:",fortitudeA),
        ("Furtividade:",furtividadeA),
        ("Guerra (treinada):",guerraA),
        ("Iniciativa:",iniciativaA),
        ("Intimidação:",intimidacaoA),
        ("Intuição:",intuicaoA),
        ("Investigação:",investigacaoA),
        ("Jogatina (treinada):",jogatinaA),
        ("Ladinagem (treinada e penalidade por armadura):",ladinagemA),
        ("Luta:",lutaA),
        ("Misticismo:",misticismoA),
        ("Percepção:",percepcaoA),
        ("Pilotagem (treinada):",pilotagemA),
        ("Pontaria:",pontariaA),
        ("Reflexos:",reflexosA),
        ("Religião (Treinada):",religiaoA),
        ("Sobrevivência:",sobrevivenciaA),
        ("Vontade:",vontadeA)]
      for per in pericias:
        print(per)
        print("\n")
        t.sleep(1)
      acrobacia = ("Acrobacia (penalidade de armadura):",acrobaciaA),
      adestramento = ("Adestramento (treinada):",adestramentoA),
      atletismo = ("Atletismo:",atletismoA),
      atuacao = ("Atuação:",atuacaoA),
      cavalgar("Cavalgar:",calvalgarA),
      conhecimento = ("Conhecimento (treinada):",conhecimentoA),
      cura = ("Cura:",curaA),
      diplomacia = ("Diplomacia:",diplomaciaA)
      enganacao = ("Enganação:",enganacaoA)
      fortitude = ("Fortitude:",fortitudeA)
      furtividade = ("Furtividade:",furtividadeA)
      guerra = ("Guerra (treinada):",guerraA)
      iniciativa = ("Iniciativa:",iniciativaA)
      intimidacao = ("Intimidação:",intimidacaoA)
      intuicao = ("Intuição:",intuicaoA)
      investigacao = ("Investigação:",investigacaoA)
      jogatina = ("Jogatina (treinada):",jogatinaA)
      ladinagem = ("Ladinagem (treinada e penalidade por armadura):",ladinagemA)
      luta = ("Luta:",lutaA),
      misticismo = ("Misticismo:",misticismoA),
      percepcao = ("Percepção:",percepcaoA),
      pilotagem = ("Pilotagem (treinada):",pilotagemA),
      pontaria = ("Pontaria:",pontariaA),
      reflexos = ("Reflexos:",reflexosA),
      religiao = ("Religião (Treinada):",religiaoA),
      sobrevivencia = ("Sobrevivência:",sobrevivenciaA),
      vontade = ("Vontade:",vontadeA)"""