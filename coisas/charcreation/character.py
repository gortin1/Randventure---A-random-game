from assets.funcs import digitar,getClass,clear, allclasse,allraces, getRace
from assets.charcreation.points import distribuirPericias,distribuirPontos
from assets.info.information import Describe



def charCreate():
    resists = {
        'veneno': False,
        'fogo': False,
        'gelo': False,
        'eletrico': False,
        'acido': False,
        'trovao': False,
        'radiante':False,
        'necrotico':False
    }
    clear()
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
                allclasse()
                classeChoose = int(input("Digite o numero que fica na frente da classe desejada: "))
                match classeChoose:
                    case 1:
                        getClass('barbaro',2)
                        input("Aperte Enter para continuar")
                        clear()
                    case 2:
                        getClass('bardo',2)
                        input("Aperte Enter para continuar")
                        clear()
                    case 3:
                        getClass('bruxo',2)
                        input("Aperte Enter para continuar")
                        clear()
                    case 4:
                        getClass('clerigo',2)
                        input("Aperte Enter para continuar")
                        clear()
                    case 5:
                        getClass('druida',2)
                        input("Aperte Enter para continuar")
                        clear()
                    case 6:
                        getClass('feiticeiro',2)
                        input("Aperte Enter para continuar")
                        clear()
                    case 7:
                        getClass('guerreiro',2)
                        input("Aperte Enter para continuar")
                        clear()
                    case 8:
                        getClass('ladino',2)
                        input("Aperte Enter para continuar")
                        clear()
                    case 9:
                        getClass('mago',2)
                        input("Aperte Enter para continuar")
                        clear()
                    case 10:
                        getClass('monge',2)
                        input("Aperte Enter para continuar")
                        clear()
                    case 11:
                        getClass('paladino',2)
                        input("Aperte Enter para continuar")
                        clear()
                    case 12:
                        getClass('patrulheiro',2)
                        input("Aperte Enter para continuar")
                        clear()
            digitar("Vamos escolher sua raça:")
            allraces()
            while True:
                race = int(input("Digite o numero indicado pela raça"))
                if race is not None:
                    match race:
                        case 1:
                            race = 'anao'
                            digitar("Voce escolheu a classe:",race,". Deseja continuar?")
                            yn = str(input("S para sim, N para nao")).lower
                            if yn == "s":
                                digitar("Classe escolhida:", race)
                                break
                            else: 
                                continue
                        case 2:
                            race = 'elfo'
                            digitar("Voce escolheu a classe:",race,". Deseja continuar?")
                            yn = str(input("S para sim, N para nao")).lower
                            if yn == "s":
                                digitar("Classe escolhida:", race)
                                break
                            else: 
                                continue
                        case 3:
                            race = 'halfling'
                            digitar("Voce escolheu a classe:",race,". Deseja continuar?")
                            yn = str(input("S para sim, N para nao")).lower
                            if yn == "s":
                                digitar("Classe escolhida:", race)
                                break
                            else: 
                                continue
                        case 4:
                            race = 'humano'
                            digitar("Voce escolheu a classe:",race,". Deseja continuar?")
                            yn = str(input("S para sim, N para nao")).lower
                            if yn == "s":
                                digitar("Classe escolhida:", race)
                                break
                            else: 
                                continue
                        case 5:
                            race = 'draconato'
                            digitar("Voce escolheu a classe:",race,". Deseja continuar?")
                            yn = str(input("S para sim, N para nao")).lower
                            if yn == "s":
                                digitar("Classe escolhida:", race)
                                break
                            else: 
                                continue
                        case 6:
                            race = 'gnomo'
                            digitar("Voce escolheu a classe:",race,". Deseja continuar?")
                            yn = str(input("S para sim, N para nao")).lower
                            if yn == "s":
                                digitar("Classe escolhida:", race)
                                break
                            else: 
                                continue
                        case 7:
                            race = 'meio-elfo'
                            digitar("Voce escolheu a classe:",race,". Deseja continuar?")
                            yn = str(input("S para sim, N para nao")).lower
                            if yn == "s":
                                digitar("Classe escolhida:", race)
                                break
                            else: 
                                continue
                        case 8:
                            race = 'meio-orc'
                            digitar("Voce escolheu a classe:",race,". Deseja continuar?")
                            yn = str(input("S para sim, N para nao")).lower
                            if yn == "s":
                                digitar("Classe escolhida:", race)
                                break
                            else: 
                                continue
                        case 9:
                            race = 'tiefling'
                            digitar("Voce escolheu a classe:",race,". Deseja continuar?")
                            yn = str(input("S para sim, N para nao")).lower
                            if yn == "s":
                                digitar("Classe escolhida:", race)
                                break
                            else: 
                                continue
                else:
                    digitar("Digite um numero valido!") 
                    continue
            clear()       
            digitar("Vamos escolher sua classe!")
            digitar(desc.allClasses())
            while True:
                classe = int(input("Digite o numero indicado classe"))
                if classe is not None:
                    match classe:
                        case 1:
                            classe = 'barbaro'
                            digitar("Voce escolheu a classe:",classe,". Deseja continuar?")
                            yn = str(input("S para sim, N para nao")).lower
                            if yn == "s":
                                digitar("Classe escolhida:", classe)
                                break
                            else: 
                                continue
                        case 2:
                            classe = 'bardo'
                            digitar("Voce escolheu a classe:",classe,". Deseja continuar?")
                            yn = str(input("S para sim, N para nao")).lower
                            if yn == "s":
                                digitar("Classe escolhida:", classe)
                                break
                            else: 
                                continue
                        case 3:
                            classe = 'bruxo'
                            digitar("Voce escolheu a classe:",classe,". Deseja continuar?")
                            yn = str(input("S para sim, N para nao")).lower
                            if yn == "s":
                                digitar("Classe escolhida:", classe)
                                break
                            else: 
                                continue
                        case 4:
                            classe = 'clerigo'
                            digitar("Voce escolheu a classe:",classe,". Deseja continuar?")
                            yn = str(input("S para sim, N para nao")).lower
                            if yn == "s":
                                digitar("Classe escolhida:", classe)
                                break
                            else: 
                                continue
                        case 5:
                            classe = 'druida'
                            digitar("Voce escolheu a classe:",classe,". Deseja continuar?")
                            yn = str(input("S para sim, N para nao")).lower
                            if yn == "s":
                                digitar("Classe escolhida:", classe)
                                break
                            else: 
                                continue
                        case 6:
                            classe = 'feiticeiro'
                            digitar("Voce escolheu a classe:",classe,". Deseja continuar?")
                            yn = str(input("S para sim, N para nao")).lower
                            if yn == "s":
                                digitar("Classe escolhida:", classe)
                                break
                            else: 
                                continue
                        case 7:
                            classe = 'guerreiro'
                            digitar("Voce escolheu a classe:",classe,". Deseja continuar?")
                            yn = str(input("S para sim, N para nao")).lower
                            if yn == "s":
                                digitar("Classe escolhida:", classe)
                                break
                            else: 
                                continue
                        case 8:
                            classe = 'ladino'
                            digitar("Voce escolheu a classe:",classe,". Deseja continuar?")
                            yn = str(input("S para sim, N para nao")).lower
                            if yn == "s":
                                digitar("Classe escolhida:", classe)
                                break
                            else: 
                                continue
                        case 9:
                            classe = 'mago'
                            digitar("Voce escolheu a classe:",classe,". Deseja continuar?")
                            yn = str(input("S para sim, N para nao")).lower
                            if yn == "s":
                                digitar("Classe escolhida:", classe)
                                break
                            else: 
                                continue
                        case 10:
                            classe = 'monge'
                            digitar("Voce escolheu a classe:",classe,". Deseja continuar?")
                            yn = str(input("S para sim, N para nao")).lower
                            if yn == "s":
                                digitar("Classe escolhida:", classe)
                                break
                            else: 
                                continue
                        case 11:
                            classe = 'paladino'
                            digitar("Voce escolheu a classe:",classe,". Deseja continuar?")
                            yn = str(input("S para sim, N para nao")).lower
                            if yn == "s":
                                digitar("Classe escolhida:", classe)
                                break
                            else: 
                                continue
                        case 12:
                            classe = 'patrulheiro'
                            digitar("Voce escolheu a classe:",classe,". Deseja continuar?")
                            yn = str(input("S para sim, N para nao")).lower
                            if yn == "s":
                                digitar("Classe escolhida:", classe)
                                break
                            else: 
                                continue
                        case _:
                            digitar("O numero digitado não esta listado, por favor digite um numero valido")
                            continue
                            
                else:
                    digitar("Por favor digite um numero valido!")
                    continue    
            clear()
            digitar("Vamos começar com a distribuição de pontos!")
            pontos = distribuirPontos(name, 1)
            clear()
            match race:
                case 'anao':
                    while True:
                        digitar("A raça na qual voce escolheu é", race)
                        digitar(getRace(race))
                        subRace = int(input("Escolha entre Anão da colina ou da montanha (Se quiser o anao da colina digite 1, anao da montanha digite 2)"))
                        match subRace:
                            case 1:
                                pontos['sabedoria'] += 1
                            case 2:
                                pontos['forca'] += 2
                            case _:
                                digitar("Digite um valor valido")
                                clear()
                                continue
                        resists["veneno"] = True
                case 'elfo':
                    while True:
                        digitar("")
                        digitar(getRace(race))
                        subRace = int(input(""))
                        