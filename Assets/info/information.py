from colorama import just_fix_windows_console, Fore, Style
class Describe:
    def allClasses():
        return '\n'.join([
            '1- barbaro',
            '2- bardo',
            '3- bruxo',
            '4- clerigo',
            '5- druida',
            '6- feiticeiro',
            '7- guerreiro',
            '8- ladino',
            '9- mago',
            '10- monge',
            '11- paladino',
            '12- patrulheiro'
        ])
    def allRaces():
        return '\n'.join([
            '1- Anao',
            '2- Elfo',
            '3- Halfling',
            '4- Humano',
            '5- Draconato',
            '6- Gnomo',
            '7- Meio-elfo',
            '8- Meio-orc',
            '9- Tiefling'
        ])
    def classXrace(classe: str):
        just_fix_windows_console()
        match classe.lower():
            case 'barbaro':
                return '\n'.join([
                    'Barbaro X Anao = ' + Fore.BLUE + "Combinação boa."+ Style.RESET_ALL,
                    'Barbaro X Elfo = ' + Fore.WHITE + "Combinação neutra."+ Style.RESET_ALL,
                    'Barbaro X Halfling = ' + Fore.BLUE + "Combinação boa."+ Style.RESET_ALL,
                    'Barbaro X Humano = ' + Fore.BLUE + "Combinação boa."+ Style.RESET_ALL,
                    'Barbaro X Draconato = ' + Fore.BLUE + "Combinação boa."+ Style.RESET_ALL,
                    'Barbaro X Gnomo = ' + Fore.BLUE + "Combinação boa."+ Style.RESET_ALL,
                    'Barbaro X Meio-Elfo = ' + Fore.WHITE + "Combinação neutra."+ Style.RESET_ALL,
                    'Barbaro X Meio-Orc = ' + Fore.GREEN + "Combinação perfeita."+ Style.RESET_ALL,
                    'Barbaro X Tiefling = ' + Fore.WHITE + "Combinação neutra."+ Style.RESET_ALL
                ])
            #terminar o resto dasa classes
    def descricaoRaca(raceasked: str):
        match raceasked:
            case "humano":
                return '\n'.join([
                    "Atributos: +1 em todos os valores de habilidade.",
                    "Idade: Adultos no final da adolescencia; vivem menos de 100 anos.",
                    "Tendencia: Variada, sem inclinacao predominante.",
                    "Tamanho: Medio (entre 1,50 m e 1,80 m).",
                    "Idiomas: Comum e um idioma adicional a escolha."
                ])
            case "elfo":
                return'\n'.join([
                    "Atributos: +2 em Destreza.",
                    "Idade: Adultos por volta dos 100 anos; vivem ate 750 anos.",
                    "Tendencia: Tendem ao Caotico e geralmente sao bons.",
                    "Tamanho: Medio (entre 1,50 m e 1,80 m).",
                    "Idiomas: Comum e Elfico."
                ])
            case "anao":
                return '\n'.join([
                    "Atributos: +2 em Constituicao.",
                    "Idade: Adultos por volta dos 50 anos; vivem mais de 400 anos.",
                    "Tendencia: Tendem ao Leal, geralmente bons.",
                    "Tamanho: Medio (cerca de 1,20 m de altura).",
                    "Idiomas: Comum e Anao."
                ])
            case "meio-orc":
                return '\n'.join([
                    "Atributos: +2 em Forca, +1 em Constituicao.",
                    "Idade: Adultos por volta dos 14 anos; vivem ate cerca de 75 anos.",
                    "Tendencia: Tendem ao Caotico; podem ser bons ou maus.",
                    "Tamanho: Medio (entre 1,80 m e 2,10 m).",
                    "Idiomas: Comum e Orc."
                ])
            case _:
                return print("Raca nao encontrada.")
        


    def descricaoClasse( classaked: str):
        match classaked:
            case "druida":
                return'\n'.join([
                    "Vida: 8",
                    "Testes de Resistencia: Inteligencia, Sabedoria",
                    "Atributo principal: Sabedoria."
                ])
            case "barbaro":
                return'\n'.join([
                    "Dado de Vida: 12",
                    "Testes de Resistencia: Forca, Constituicao.",
                    "Atributo principal: Forca (Constituicao e muito importante tambem)."
                ])
            case "mago":
                return'\n'.join([
                    "Dado de Vida: 6",
                    "Testes de Resistencia: Inteligencia, Sabedoria.",
                    "Atributo principal: Inteligencia."
                ])
            case "guerreiro":
                return'\n'.join([
                    "Dado de Vida: 10",
                    "Testes de Resistencia: Forca, Constituicao.",
                    "Atributo principal: Forca ou Destreza (depende do estilo de luta)."
                ])
    def descricaoPericias(classe: str):
        match classe:
            case 'druida':
                return '\n'.join([
                     'arcanismo',
                     'adestrar animais',
                     'intuicao',
                     'medicina',
                     'natureza',
                     'percepcao',
                     'religiao',
                     'sobrevivencia'
                     ])
            
            case 'mago':
                return '\n'.join(['arcanismo',
                        'historia',
                        'intuicao',
                        'investigacao',
                        'medicina',
                        'religiao'
                        ])
            case 'barbaro':
                return '\n'.join([
                        'adestrar animais',
                        'atletismo',
                        'intimidacao',
                        'natureza',
                        'percepcao',
                        'sobrevivencia'
                        ])
            case 'guerreiro':
                return '\n'.join([
                        'acrobacia',
                        'adestrar animais',
                        'atletismo',
                        'historia',
                        'intuicao',
                        'intimidacao',
                        'percepcao',
                        'sobrevivencia'
                        ])