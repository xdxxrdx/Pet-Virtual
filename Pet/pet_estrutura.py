class bichinho:
    nome = input('Digite um nome para seu bichinho:')
    idade = 0
    saude = 50
    fome = 50
    status = saude - (fome/2)
    if status >= 25:
        humor = 'Feliz'
        print(humor)

    elif status < 25:
        humor = 'Triste'
        print(humor)


    def __init__(self):
        pass


    def alimentar(self=None, fome=None):
        fome = bichinho.fome
        saude = bichinho.saude

        print('')
        print('''
        1 PARA PIRULITO (-1 de saúde -1 de fome)
        2 PARA VITAMINA DE BANANA (+1 de saúde -2 de fome)
        3 PARA MACARRÃO (+2 de saúde -3 de fome)
        4 PARA ENERGÉTICO (-5 de saúde -5 de fome''')
        print('')
        resposta = int(input('Digite um número para alimentar'))

        if resposta == 1:
            fome -= 1
            saude -= 1
            print(fome, saude)

        elif resposta == 2:
            fome -= 2
            saude += 1
            print(fome, saude)

        elif resposta == 3:
            fome -= 3
            saude += 2
            print(fome, saude)

        elif resposta == 4:
            fome -= 5
            saude -= 5
            print(fome, saude)

        else:
            print('Número inválido')






nome = bichinho()

interface = True

while interface:
    print('')
    print(bichinho.nome, 'está com', bichinho.idade, 'anos!')
    print(bichinho.nome, 'está', bichinho.humor)
    print('')
    print('''DIGITE:
1 - para alimentar
2 - para jogar Pedra, papel e tesoura
3 - para jogar o Jogo do Balde''')
    ok = int(input('Insira o numero'))
    bichinho.idade +=1
    bichinho.fome -=1

    if ok == 1:
        bichinho.alimentar()

    elif ok ==2:
        from games import pedra_papel_tesoura
        pedra_papel_tesoura.PedraPapelETesoura()

    elif ok == 3:
        from games import jogo_do_balde
        jogo_do_balde.JogoDoBalde()
