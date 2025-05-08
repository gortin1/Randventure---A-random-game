from colorama import just_fix_windows_console, Fore, Style
class racesAndClasses:
    def allClasses():
        return '\n'.join([
            '1- Barbaro',
            '2- Bardo',
            '3- Bruxo',
            '4- Clerigo',
            '5- Druida',
            '6- Feiticeiro',
            '7- Guerreiro',
            '8- Ladino',
            '9- Mago',
            '10- Monge',
            '11- Paladino',
            '12- Patrulheiro'
        ])
    def allRaces():
        return '\n'.join([
            '1- Anao',
            '2- elfo',
            '3- Halfling',
            '4- Humano',
            '5- Draconato',
            '6- Gnomo',
            '7- Meio-elfo',
            '8- Meio-orc',
            '9- Tiefling'
        ])
    def classXrace(classe: str):
        perfect = (Fore.GREEN + "Combinação perfeita."+ Style.RESET_ALL)
        good = (Fore.BLUE + "Combinação boa."+ Style.RESET_ALL)
        neutral = (Fore.WHITE + "Combinação neutra."+ Style.RESET_ALL)
        bad = (Fore.RED + "Combinação ruim."+ Style.RESET_ALL)
        just_fix_windows_console()
        match classe.lower():
            case 'barbaro':
                return '\n'.join([
                    'Barbaro X Anao = ' + good,
                    'Barbaro X elfo = ' + neutral,
                    'Barbaro X Halfling = ' + good,
                    'Barbaro X Humano = ' + neutral,
                    'Barbaro X Draconato = ' + good,
                    'Barbaro X Gnomo = ' + good,
                    'Barbaro X Meio-elfo = ' + neutral,
                    'Barbaro X Meio-Orc = ' + perfect,
                    'Barbaro X Tiefling = ' + bad
                ])
            case 'bardo':
                return '\n'.join([
                    'Bardo X Anao = ' + neutral,
                    'Bardo X elfo = ' + good,
                    'Bardo X Halfling = ' + neutral,
                    'Bardo X Humano = ' + neutral,
                    'Bardo X Draconato = ' + good,
                    'Bardo X Gnomo = ' + neutral,
                    'Bardo X Meio-elfo = ' + perfect,
                    'Bardo X Meio-Orc = ' + bad,
                    'Bardo X Tiefling = ' + bad 
                ])
            case 'bruxo':
                return '\n'.join([
                    'Bruxo X Anao = ' + bad,
                    'Bruxo X elfo = ' + good,
                    'Bruxo X Halfling = ' + bad,
                    'Bruxo X Humano = ' + neutral,
                    'Bruxo X Draconato = ' + good,
                    'Bruxo X Gnomo = ' + neutral,
                    'Bruxo X Meio-elfo = ' + good,
                    'Bruxo X Meio-Orc = ' + bad,
                    'Bruxo X Tiefling = ' + perfect 
                ])
            case 'clerigo':
                return '\n'.join([
                    'Clerigo X Anao = ' + good,
                    'Clerigo X elfo = ' + good,
                    'Clerigo X Halfling = ' + neutral,
                    'Clerigo X Humano = ' + neutral,
                    'Clerigo X Draconato = ' + neutral,
                    'Clerigo X Gnomo = ' + neutral,
                    'Clerigo X Meio-elfo = ' + perfect,
                    'Clerigo X Meio-Orc = ' + neutral,
                    'Clerigo X Tiefling = ' + bad 
                ])
            case 'druida':
                return '\n'.join([
                    'Druida X Anao = ' + good,
                    'Druida X elfo = ' + good,
                    'Druida X Halfling = ' + neutral,
                    'Druida X Humano = ' + neutral,
                    'Druida X Draconato = ' + neutral,
                    'Druida X Gnomo = ' + neutral,
                    'Druida X Meio-elfo = ' + perfect,
                    'Druida X Meio-Orc = ' + neutral,
                    'Druida X Tiefling = ' + bad 
                ])
            case 'feiticeiro':
                return '\n'.join([
                    'Feiticeiro X Anao = ' + bad,
                    'Feiticeiro X elfo = ' + good,
                    'Feiticeiro X Halfling = ' + bad,
                    'Feiticeiro X Humano = ' + neutral,
                    'Feiticeiro X Draconato = ' + good,
                    'Feiticeiro X Gnomo = ' + neutral,
                    'Feiticeiro X Meio-elfo = ' + good,
                    'Feiticeiro X Meio-Orc = ' + bad,
                    'Feiticeiro X Tiefling = ' + perfect 
                ])
            case 'guerreiro':
                return '\n'.join([
                    'Guerreiro X Anao = ' + bad,
                    'Guerreiro X elfo = ' + good,
                    'Guerreiro X Halfling = ' + bad,
                    'Guerreiro X Humano = ' + neutral,
                    'Guerreiro X Draconato = ' + good,
                    'Guerreiro X Gnomo = ' + neutral,
                    'Guerreiro X Meio-elfo = ' + good,
                    'Guerreiro X Meio-Orc = ' + bad,
                    'Guerreiro X Tiefling = ' + perfect 
                    #arrumar
                ])
            case 'ladino':
                return '\n'.join([
                    'Ladino X Anao = ' + bad,
                    'Ladino X elfo = ' + good,
                    'Ladino X Halfling = ' + bad,
                    'Ladino X Humano = ' + neutral,
                    'Ladino X Draconato = ' + good,
                    'Ladino X Gnomo = ' + neutral,
                    'Ladino X Meio-elfo = ' + good,
                    'Ladino X Meio-Orc = ' + bad,
                    'Ladino X Tiefling = ' + perfect 
                    #arrumar
                ])
            case 'mago':
                return '\n'.join([
                    'Mago X Anao = ' + bad,
                    'Mago X elfo = ' + good,
                    'Mago X Halfling = ' + bad,
                    'Mago X Humano = ' + neutral,
                    'Mago X Draconato = ' + good,
                    'Mago X Gnomo = ' + neutral,
                    'Mago X Meio-elfo = ' + good,
                    'Mago X Meio-Orc = ' + bad,
                    'Mago X Tiefling = ' + perfect 
                    #arrumar
                ])
            case 'monge':
                return '\n'.join([
                    'Monge X Anao = ' + bad,
                    'Monge X elfo = ' + good,
                    'Monge X Halfling = ' + bad,
                    'Monge X Humano = ' + neutral,
                    'Monge X Draconato = ' + good,
                    'Monge X Gnomo = ' + neutral,
                    'Monge X Meio-elfo = ' + good,
                    'Monge X Meio-Orc = ' + bad,
                    'Monge X Tiefling = ' + perfect 
                    #arrumar
                ])
            case 'paladino':
                return '\n'.join([
                    'Paladino X Anao = ' + bad,
                    'Paladino X elfo = ' + good,
                    'Paladino X Halfling = ' + bad,
                    'Paladino X Humano = ' + neutral,
                    'Paladino X Draconato = ' + good,
                    'Paladino X Gnomo = ' + neutral,
                    'Paladino X Meio-elfo = ' + good,
                    'Paladino X Meio-Orc = ' + bad,
                    'Paladino X Tiefling = ' + perfect 
                    #arrumar
                ])
            case 'patrulheiro':
                return '\n'.join([
                    'Patrulheiro X Anao = ' + bad,
                    'Patrulheiro X elfo = ' + good,
                    'Patrulheiro X Halfling = ' + bad,
                    'Patrulheiro X Humano = ' + neutral,
                    'Patrulheiro X Draconato = ' + good,
                    'Patrulheiro X Gnomo = ' + neutral,
                    'Patrulheiro X Meio-elfo = ' + good,
                    'Patrulheiro X Meio-Orc = ' + bad,
                    'Patrulheiro X Tiefling = ' + perfect 
                    #arrumar
                ])      
    def descricaoRaca(raceasked: str):
        match raceasked:
            case "anao":
                return '\n'.join([
                    "Atributos: +2 em Constituicao.",
                    "Tendencia: Tendem ao Leal, geralmente bons.",
                    "Tamanho: Medio (cerca de 1,20 m de altura).",
                    "Idiomas: Comum e Anao.",
                    "Visao no Escuro: Voce tem visão na penumbra e na noite.",
                    "Resiliencia Anã: Voce possui resistencia contra veneno e dano de veneno.",
                    "Sub raça: Voce deve escolher uma das duas sub-raças. Escolha entre Anão da colina e Anão da montanha.",
                    "\n",
                    "Anão da colina:",
                    "Atributo: +1 em sabedoria.",
                    "Tenacidade anã: Seu maximo de vida aumenta em 1, e sempre que sobe de nivel aumenta em mais 1 ponto adicional de vida",
                    "\n",
                    "Anão da montanha:",
                    "Atributo: +2 em força."
                ])
            case "elfo":
                return'\n'.join([
                    "Atributos: +2 em Destreza.",
                    "Tendencia: Tendem ao Caotico e geralmente sao bons.",
                    "Tamanho: Medio (entre 1,50 m e 1,80 m).",
                    "Idiomas: Comum e Elfico."
                    "Visao no Escuro: Voce tem visao na penumbra e no escuro"
                    "Sentidos aguçados: Voce tem a pericia Percepção",
                    "Ancestral Feérico: Voce não pode ser colocado para dormir e Voce tem resistencia contra ser enfeitiçados",
                    "Sub-Racas: alto elfo, elfo da floresta e elfo negro",
                    "\n",
                    "Alto elfo",
                    "Atributos: +1 em inteligencia",
                    "Truque: Voce conhece um truque de mago (Atributo usado Inteligencia)",
                    "Idioma adicional: Você pode ler, falar e escrever em um idioma a sua escolha",
                    "\n",
                    "Elfo da floresta",
                    "Atributos: +1 sabedoria",
                    "Pericia: Voce tem a pericia Sobrevivencia",
                    "\n",
                    "Elfo Negro",
                    "Atributos: +1 em Carisma",
                    "Visão no Escuro Superior: Voce tem visao no escuro",
                    "Sensibilidade a luz solar: Voce tem desvantagem em ataques quando exposto a luz solar direto",
                    "Magia Drow: Você possui o truque "
                ])
            case "halfling":
                return '\n'.join([
                    "Atributo: +2 em destreza.",
                    "Tendencia: Tendem ao leal e bom.",
                    "Tamanho: Pequeno (cerca de 0,90 m)",
                    "Idiomas: comum e halfling"
                    "Sortudo:"
                ])
            case "humano":
                return '\n'.join([
                    "Atributos: +1 em todos os valores de habilidade.",
                    "Tendencia: Variada, sem inclinacao predominante.",
                    "Tamanho: Medio (entre 1,50 m e 1,80 m).",
                    "Idiomas: Comum e um idioma adicional a escolha."
                ])
            case "meio-orc":
                return '\n'.join([
                    "Atributos: +2 em Forca, +1 em Constituicao.",
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
class magias:
    def magiasDisponiveisTruques(classe):
        match classe:
            case 'bardo':
                return'\n'.join([
                    'Amizade (encantamento)',
                    'Ataque Certeiro (adivinhação)',
                    'Consertar (transmutação)',
                    'Globos de Luz (evocação)',
                    'Ilusão Menor (ilusão) ',
                    'Luz (evocação)',
                    'Mãos Mágicas (conjuração)',
                    'Mensagem (transmutação)',
                    'Prestidigitação (transmutação)',
                    'Proteção contra Lâminas (abjuração)',
                    'Zombaria Viciosa (encantamento)'
            ])
            case 'bruxo':
                return '\n'.join([
                    'Amizade (encantamento)',
                    'Ataque Certeiro (adivinhação)',
                    'Ilusão Menor (ilusão)', 
                    'Mãos Mágicas (conjuração)', 
                    'Prestidigitação (transmutação)', 
                    'Proteção contra Lâminas (abjuração)', 
                    'Rajada de Veneno (conjuração)', 
                    'Rajada Mística (evocação)', 
                    'Toque Arrepiante (necromancia)' 
                ])
            case 'clerigo':
                return '\n'.join([
                    'Chama Sagrada (evocação)', 
                    'Consertar (transmutação)', 
                    'Estabilizar (necromancia)', 
                    'Luz (evocação)', 
                    'Orientação (adivinhação)',
                    'Resistência (abjuração)',
                    'Taumaturgia (transmutação)'
                ])
            case 'druida':
                return '\n'.join([
                    'Bordão Místico (transmutação)' 
                    'Chicote de Espinhos (transmutação)' 
                    'Consertar (transmutação)' 
                    'Criar Chamas (conjuração)' 
                    'Druidismo (transmutação)' 
                    'Orientação (adivinhação) '
                    'Rajada de Veneno (conjuração)'
                ])
            case 'feiticeiro':
                return '\n'.join([
                    'Amizade (encantamento)',
                    'Ataque Certeiro (adivinhação)' ,
                    'Consertar (transmutação)', 
                    'Espirro Ácido (conjuração)' ,
                    'Globos de Luz (evocação)',
                    'Ilusão Menor (ilusão)', 
                    'Luz (evocação)' ,
                    'Mãos Mágicas (conjuração)' ,
                    'Mensagem (transmutação)' ,
                    'Prestidigitação (transmutação)' ,
                    'Proteção contra Lâminas (abjuração)', 
                    'Raio de Fogo (evocação)' ,
                    'Raio de Gelo (evocação)' ,
                    'Rajada de Veneno (conjuração)' ,
                    'Toque Arrepiante (necromancia)' ,
                    'Toque Chocante (evocação)'
                ])     
                     
