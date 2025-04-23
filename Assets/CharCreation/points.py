from assets.funcs import wait, showClasse, getClass, digitar, showPericias

def distribuirPontos(name):
    while True:
        digitar(f"Bem-Vindo {name} a distribuição de pontos do Randventure!")
        wait.smallwait()
        digitar(f"Iremos fazer a distribuição de pontos do seu personagem")
        digitar(f"Quer saber quais são os melhores tipo de distribuição para o seu personagem?")
        wait.smallwait()
        answer1 = str(input("(Escreva S para sim ou N para não) \n"))
        while True:
            if answer1.lower() == "n":
                break   
            else:
                showClasse()
                digitar("Deseja saber de outra classe?")
                answer2 = str(input("(Escreva S para sim ou N para não) \n"))
                if answer2.lower() == "n":
                    break
                else:
                    continue
        digitar("Bem, vamos começar com a distribuição de pontos!")
        
        forca, destreza, constituicao, inteligencia, sabedoria, carisma = 0,0,0,0,0,0
        pontosdisponiveis = 10
                
        while pontosdisponiveis > 0:
            digitar("Voce tem ", pontosdisponiveis, " pontos disponiveis, digite qual o atributo que deseja aumentar")
            wait.smallwait()
            digitar(
                "1- Força = ",forca,
                "\n2- Destreza = ",destreza,
                "\n3- Constituição = ",constituicao,
                "\n4- Inteligencia = ",inteligencia,
                "\n5- Sabedoria = ", sabedoria,
                "\n6- Carisma = ", carisma,
            )
            wait.mediumwait()
            choose = int(input("\nDigite qual você deseja aumentar (use os numeros indicados na frente do atributo!)\n"))
            match choose:
                case 1:
                    print("\n\n")
                    wait.smallwait()
                    digitar("Atributo escolhido: (força)")
                    wait.smallwait()
                    add = int(input("Digite a quantidade de pontos que deseja adicionar: "))
                    if add <= pontosdisponiveis:
                        pass
                    else:
                        digitar("Erro ao adicionar! pontos insuficientes")
                        continue 
                    forca = forca + add
                    pontosdisponiveis -= add
                    print("\n\n\n\n\n\n\n")
                    wait.mediumwait()
                    continue
                case 2:
                    print("\n\n")
                    wait.smallwait()
                    digitar("Atributo escolhido: (Destreza)")
                    wait.smallwait()
                    add = int(input("Digite a quantidade de pontos que deseja adicionar: "))
                    if add <= pontosdisponiveis:
                        pass
                    else:
                        digitar("Erro ao adicionar! pontos insuficientes")
                        continue
                    destreza = destreza + add
                    pontosdisponiveis -= add
                    print("\n\n\n\n\n\n\n")
                    wait.mediumwait()
                    continue
                case 3:
                    print("\n\n")
                    wait.smallwait()
                    digitar("Atributo escolhido: (Constituição)")
                    wait.smallwait()
                    add = int(input("Digite a quantidade de pontos que deseja adicionar: "))
                    if add <= pontosdisponiveis:
                        pass
                    else:
                        digitar("Erro ao adicionar! pontos insuficientes")
                        continue
                    constituicao = constituicao + add
                    pontosdisponiveis -= add
                    print("\n\n\n\n\n\n\n")
                    wait.mediumwait()
                    continue
                case 4:
                    print("\n\n")
                    wait.smallwait()
                    digitar("Atributo escolhido: (Inteligencia")
                    wait.smallwait()
                    add = int(input("Digite a quantidade de pontos que deseja adicionar: "))
                    if add <= pontosdisponiveis:
                        pass
                    else:
                        digitar("Erro ao adicionar! pontos insuficientes")
                        continue
                    inteligencia = inteligencia + add
                    pontosdisponiveis -= add
                    print("\n\n\n\n\n\n\n")
                    wait.mediumwait()
                    continue
                case 5:
                    print("\n\n")
                    wait.smallwait()
                    digitar("Atributo escolhido: (Sabedoria)")
                    wait.smallwait()
                    add = int(input("Digite a quantidade de pontos que deseja adicionar: "))
                    if add <= pontosdisponiveis:
                        pass
                    else:
                        digitar("Erro ao adicionar! pontos insuficientes")
                        continue
                    sabedoria = sabedoria + add
                    pontosdisponiveis -= add
                    print("\n\n\n\n\n\n\n")
                    wait.mediumwait()
                    continue
                case 6:
                    print("\n\n")
                    wait.smallwait()
                    digitar("Atributo escolhido: (Carisma)")
                    wait.smallwait()
                    add = int(input("Digite a quantidade de pontos que deseja adicionar: "))
                    if add <= pontosdisponiveis:
                        pass
                    else:
                        digitar("Erro ao adicionar! pontos insuficientes")
                        continue
                    carisma = carisma + add
                    pontosdisponiveis -= add
                    print("\n\n\n\n\n\n\n")
                    wait.mediumwait()
                    continue
                case _:
                    print("\n\n")
                    wait.smallwait()
        return {'forca': forca, 
                'destreza':destreza, 
                'constituicao':constituicao, 
                'inteligencia':inteligencia, 
                'sabedoria':sabedoria, 
                'carisma':carisma}  
                                  
def distribuirPericias(classe):
    
    match classe:
        case "druida":
            digitar("Bem vindo! iremos fazer a escolha de pericias!\n")
            wait.smallwait()
            digitar("A raça que você escolheu anteriormente foi: ", classe)
            wait.smallwait()
            digitar("Gostaria de rever algumas coisas sobre a classe")
            answer1 = str(input("(Escreva S para sim ou N para não) \n"))
            while True:
                if answer1.lower() == "n":
                    break   
                else:
                    getClass(classe)
                    answer2 = str(input("(Escreva S para sim ou N para não) \n"))
                    if answer2.lower() == "n":
                        break
                    else:
                        continue
        
            dictpericias ={
                'pericias': {
                    'arcanismo': False,
                    'adestrar_animais': False,
                    'intuicao': False,
                    'medicina': False,
                    'natureza': False,
                    'percepcao': False,
                    'religiao': False,
                    'sobrevivencia': False
                }
            }
            i = 2
            digitar("Você pode escolher ", i," pericias entre as listadas abaixo\n",showPericias(classe))
            while i > 0:
                digitar("Aviso! ao escolher as pericias apenas atraves de subida de nivel é possivel adicionar outras pericias!")
                digitar("Escolhas disponiveis: ", i)
                periciaescolhida = str(input('digite a pericia que deseja aprender\n'))
                if periciaescolhida in dictpericias['pericias']:
                    if not dictpericias['pericias'][periciaescolhida]:
                        dictpericias['pericias'][periciaescolhida] = True
                        digitar(f"A perícia '{periciaescolhida}' foi adicionada com sucesso!")
                        i -= 1
                    else:
                        digitar("Você já escolheu essa perícia. Tente outra.")
                else:
                    digitar("Perícia inválida. Digite exatamente como mostrado na lista.")
            for chave in dictpericias['pericias']:
                if dictpericias['pericias'][chave]:
                    dictpericias['pericias'][chave] = 2
                else:
                    dictpericias['pericias'][chave] = 0
            
            return dictpericias
        
        case 'guerreiro':
            digitar("Bem vindo! iremos fazer a escolha de pericias!\n")
            wait.smallwait()
            digitar("A raça que você escolheu anteriormente foi: ", classe)
            wait.smallwait()
            digitar("Gostaria de rever algumas coisas sobre a classe")
            answer1 = str(input("(Escreva S para sim ou N para não) \n"))
            while True:
                if answer1.lower() == "n":
                    break   
                else:
                    getClass(classe)
                    answer2 = str(input("(Escreva S para sim ou N para não) \n"))
                    if answer2.lower() == "n":
                        break
                    else:
                        continue
            dictpericias ={
                'pericias': {
                    'acrobacia': False,
                    'adestrar_animais': False,
                    'atletismo': False,
                    'historia': False,
                    'intuicao': False,
                    'intimidacao': False,
                    'percepcao': False,
                    'sobrevivencia': False
                }
            }
            i = 2
            digitar("Você pode escolher ", i," pericias entre as listadas abaixo\n",showPericias(classe))
            while i > 0:
                digitar("Aviso! ao escolher as pericias apenas atraves de subida de nivel é possivel adicionar outras pericias!")
                digitar("Escolhas disponiveis: ", i)
                periciaescolhida = str(input('digite a pericia que deseja aprender\n'))
                if periciaescolhida in dictpericias['pericias']:
                    if not dictpericias['pericias'][periciaescolhida]:
                        dictpericias['pericias'][periciaescolhida] = True
                        digitar(f"A perícia '{periciaescolhida}' foi adicionada com sucesso!")
                        i -= 1
                    else:
                        digitar("Você já escolheu essa perícia. Tente outra.")
                else:
                    digitar("Perícia inválida. Digite exatamente como mostrado na lista.")
            for chave in dictpericias['pericias']:
                if dictpericias['pericias'][chave]:
                    dictpericias['pericias'][chave] = 2
                else:
                    dictpericias['pericias'][chave] = 0
                    
            return dictpericias     
                    
            
        case 'mago':
            
            digitar("Bem vindo! iremos fazer a escolha de pericias!\n")
            wait.smallwait()
            digitar("A raça que você escolheu anteriormente foi: ", classe)
            wait.smallwait()
            digitar("Gostaria de rever algumas coisas sobre a classe")
            answer1 = str(input("(Escreva S para sim ou N para não) \n"))
            while True:
                if answer1.lower() == "n":
                    break   
                else:
                    getClass(classe)
                    answer2 = str(input("(Escreva S para sim ou N para não) \n"))
                    if answer2.lower() == "n":
                        break
                    else:
                        continue
            
            dictpericias ={
                'pericias': {
                    'arcanismo': False,
                    'historia': False,
                    'intuicao': False,
                    'investigacao': False,
                    'medicina': False,
                    'religiao': False
                }
            }
            i = 2
            digitar("Você pode escolher ", i," pericias entre as listadas abaixo\n",showPericias(classe))
            while i > 0:
                digitar("Aviso! ao escolher as pericias apenas atraves de subida de nivel é possivel adicionar outras pericias!")
                digitar("Escolhas disponiveis: ", i)
                periciaescolhida = str(input('digite a pericia que deseja aprender\n'))
                if periciaescolhida in dictpericias['pericias']:
                    if not dictpericias['pericias'][periciaescolhida]:
                        dictpericias['pericias'][periciaescolhida] = True
                        digitar(f"A perícia '{periciaescolhida}' foi adicionada com sucesso!")
                        i -= 1
                    else:
                        digitar("Você já escolheu essa perícia. Tente outra.")
                else:
                    digitar("Perícia inválida. Digite exatamente como mostrado na lista.")
            for chave in dictpericias['pericias']:
                if dictpericias['pericias'][chave]:
                    dictpericias['pericias'][chave] = 2
                else:
                    dictpericias['pericias'][chave] = 0
                    
            return dictpericias          
        case 'barbaro':
            digitar("Bem vindo! iremos fazer a escolha de pericias!\n")
            wait.smallwait()
            digitar("A raça que você escolheu anteriormente foi: ", classe)
            wait.smallwait()
            digitar("Gostaria de rever algumas coisas sobre a classe")
            answer1 = str(input("(Escreva S para sim ou N para não) \n"))
            while True:
                if answer1.lower() == "n":
                    break   
                else:
                    getClass(classe)
                    answer2 = str(input("(Escreva S para sim ou N para não) \n"))
                    if answer2.lower() == "n":
                        break
                    else:
                        continue
            
            dictpericias ={
                'pericias': {
                    'adestrar_animais': False,
                    'atletismo': False,
                    'intimidacao': False,
                    'natureza': False,
                    'percepcao': False,
                    'sobrevivencia': False
                }
            }
            i = 2
            digitar("Você pode escolher ", i," pericias entre as listadas abaixo\n",showPericias(classe))
            while i > 0:
                digitar("Aviso! ao escolher as pericias apenas atraves de subida de nivel é possivel adicionar outras pericias!")
                digitar("Escolhas disponiveis: ", i)
                periciaescolhida = str(input('digite a pericia que deseja aprender\n'))
                if periciaescolhida in dictpericias['pericias']:
                    if not dictpericias['pericias'][periciaescolhida]:
                        dictpericias['pericias'][periciaescolhida] = True
                        digitar(f"A perícia '{periciaescolhida}' foi adicionada com sucesso!")
                        i -= 1
                    else:
                        digitar("Você já escolheu essa perícia. Tente outra.")
                else:
                    digitar("Perícia inválida. Digite exatamente como mostrado na lista.")
            for chave in dictpericias['pericias']:
                if dictpericias['pericias'][chave]:
                    dictpericias['pericias'][chave] = 2
                else:
                    dictpericias['pericias'][chave] = 0
            
            return dictpericias
        
def getpericia(dictpericias, namepericia):
    return dictpericias['pericias'].get(namepericia)