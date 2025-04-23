from assets.CharCreation.points import distribuirPericias, distribuirPontos, getpericia
from assets.funcs import rolaracao
name = str(input("Digite seu nome "))
classe = str(input("Digite sua classe " ))
pericias = distribuirPericias(classe)
atributos = distribuirPontos(name)
listPericia = {

    'Atletismo': atributos['forca'],
    'acrobacia': atributos['destreza'],
    'furtividade': atributos['destreza'],
    'ladinagem' : atributos['destreza'],
    'arcanismo': atributos['inteligencia'],
    'historia': atributos['inteligencia'],
    'investigacao': atributos['inteligencia'],
    'natureza': atributos['inteligencia'],
    'religiao': atributos['inteligencia'],
    'adestrar_animais': atributos['sabedoria'],
    'intuicao': atributos['sabedoria'],
    'medicina': atributos['sabedoria'],
    'percepcao': atributos['sabedoria'],
    'sobrevivencia': atributos['sabedoria'],
    'atuacao': atributos['carisma'],
    'engancao': atributos['carisma'],
    'intimidacao': atributos['carisma'],
    'persuasao': atributos['carisma']
}
bonusPericia = getpericia(pericias)
acao = rolaracao(getpericia(pericias,'arcanismo'), listPericia['arcanismo'])

if acao <= 10:
    print("Falha critica")
else:
    print("acertou!")
    