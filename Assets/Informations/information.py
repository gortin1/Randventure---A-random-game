class Describe:
    def __init__(self):
        pass

    def descricaoRaca(self, raceasked: str):
        match raceasked.lower():
            case "humano":
                return [
                    "Atributos: +1 em todos os valores de habilidade.",
                    "Idade: Adultos no final da adolescencia; vivem menos de 100 anos.",
                    "Tendencia: Variada, sem inclinacao predominante.",
                    "Tamanho: Medio (entre 1,50 m e 1,80 m).",
                    "Idiomas: Comum e um idioma adicional a escolha."
                ]
            case "elfo":
                return [
                    "Atributos: +2 em Destreza.",
                    "Idade: Adultos por volta dos 100 anos; vivem ate 750 anos.",
                    "Tendencia: Tendem ao Caotico e geralmente sao bons.",
                    "Tamanho: Medio (entre 1,50 m e 1,80 m).",
                    "Idiomas: Comum e Elfico."
                ]
            case "anao":
                return [
                    "Atributos: +2 em Constituicao.",
                    "Idade: Adultos por volta dos 50 anos; vivem mais de 400 anos.",
                    "Tendencia: Tendem ao Leal, geralmente bons.",
                    "Tamanho: Medio (cerca de 1,20 m de altura).",
                    "Idiomas: Comum e Anao."
                ]
            case "orc":
                return [
                    "Atributos: +2 em Forca, +1 em Constituicao.",
                    "Idade: Adultos por volta dos 14 anos; vivem ate cerca de 75 anos.",
                    "Tendencia: Tendem ao Caotico; podem ser bons ou maus.",
                    "Tamanho: Medio (entre 1,80 m e 2,10 m).",
                    "Idiomas: Comum e Orc."
                ]
            case _:
                return ["Raca nao encontrada."]

    def descricaoClasse(self, classaked: str):
        match classaked.lower():
            case "druida":
                return[
                    "Dado de Vida: 8.",
                    "Armaduras: Armaduras leves e medias (sem metal), escudos de madeira.",
                    "Testes de Resistencia: Inteligencia, Sabedoria.",
                    "Pericias: Escolha duas entre Arcanismo, Intuicao, Medicina, Natureza, Percepcao, Religiao e Sobrevivencia.",
                    "Forma Selvagem: Pode se transformar em animais (nivel 2 em diante).",
                    "Atributo principal: Sabedoria."
                ]
            case "barbaro":
                return[
                    "Dado de Vida: 12.",
                    "Testes de Resistencia: Forca, Constituicao.",
                    "Pericias: Escolha duas entre Atletismo, Intimidacao, Natureza, Percepcao, Sobrevivencia e Animais.",
                    "Furia: Pode entrar em estado de furia, ganhando bonus em dano e resistencia a dano fisico.",
                    "Atributo principal: Forca (Constituicao e muito importante tambem)."
                ]
            case "mago":
                return[
                    "Dado de Vida: 6.",
                    "Testes de Resistencia: Inteligencia, Sabedoria.",
                    "Pericias: Escolha duas entre Arcanismo, Historia, Intuicao, Investigacao, Medicina e Religiao.",
                    "Conjuracao: Usa Inteligencia para conjurar magias, com foco em magias arcanas.",
                    "Atributo principal: Inteligencia."
                ]
            case "guerreiro":
                return[
                    "Dado de Vida: 10.",
                    "Testes de Resistencia: Forca, Constituicao.",
                    "Pericias: Escolha duas entre Atletismo, Intimidacao, Percepcao, Sobrevivencia, Historia, Intuicao e Acrobacia.",
                    "Estilo de Combate: Ganha bonus ao escolher um estilo, como defesa, arquearia ou luta com duas armas.",
                    "Atributo principal: Forca ou Destreza (depende do estilo de luta)."
                ]

