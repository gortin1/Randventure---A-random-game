from Assets.funcs import wait

def distribuir(name):
    while True:
        print(f"Bem-Vindo {name} a distribuição de pontos do Randventure!")
        wait()
        print(f"Iremos fazer a distribuição de pontos do seu personagem")
        wait()
        print(f"Quer saber quais são os melhores tipo de distribuição para o seu personagem?")
        wait()
        answer1 = str(input("(Escreva S para sim ou N para não) \n"))
        if answer1.lower == "n":
            pass
        else:
            wait()
            print("Qual seria a raça?")
            wait()
            raceasked = str(input())
            informations.descricao(raceasked)
            

            
        
        