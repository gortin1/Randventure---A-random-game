from assets.funcs import digitar
from assets.info.information import magias

def chooseMagias(classe,nome,genero):
    match genero:
        case 1:
            match classe:
                case 'bardo':
                    digitar("Bem vinda!", nome)
                    digitar("Vamos escolher suas magias iniciais?")
                    digitar("Antes vamos dar uma leve explicação sobre como funiciona as magias!")
                    digitar("Cada magia é divida em niveis onde começam do nivel 0 e vai ate o nivel 9!")
                    digitar("Sendo magias de nivel 0 (ou tambem chamados Truques), magias fracas enquanto as de nivel 9 magias extremamente fortes")
                    digitar("Sua classe:", classe,"Voce pode escolher 2 truques e 2 magias de nivel 1 no começo")
                    digitar("As suas magias disponiveis são as seguinte:")
                    digitar(magias.magiasDisponiveis('bardo',0))
                    while True:
                        magia0 = 2
                        if magia0 > 0:
                            digitar("Restam",magia0,"Truques para escolher ainda!")
                            spells = {
                                'spells0':{
                                    'Amizade ': False,
                                    'Ataque Certeiro ': False,
                                    'Consertar ': False,
                                    'Globos de Luz ': False,
                                    'Ilusão Menor ': False,
                                    'Luz ': False,
                                    'Mãos Mágicas ': False,
                                    'Mensagem ': False,
                                    'Prestidigitação ': False,
                                    'Zombaria Viciosa ': False
                                },
                                'spells1':{
                                    'coisa':False
                                }
                            }
                            spellChoosed = str(input("Digite a magia que deseja aprender!"))
                    
        case 2:
            digitar()