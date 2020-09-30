import random

class jogo_da_velha():
    ponto_do_pc = 0
    ponto_do_usuario = 0
    PEDRA = 1
    PAPEL = 2
    TESOURA = 3

    def jogar(self):


        ponto_pc = 0
        ponto_usuario = 0
        PEDRA = 1
        PAPEL = 2
        TESOURA = 3

a = True


resposta_do_computador = random.randint(1,3)
if resposta_do_computador == 1:
    escolhapc = 'Pedra'

elif resposta_do_computador == 2:
    escolhapc = 'Papel'

elif resposta_do_computador == 3:
    escolhapc = 'Tesoura'

while a:

    print('''
    JOGO DA VELHA!
    1 - PEDRA
    2 - PAPEL
    3 - TESOURA
    4 - SAIR''')

    print('Pontos do bichinho:', jogo_da_velha.ponto_do_pc, 'Pontos do usuário:', jogo_da_velha.ponto_do_usuario)

    resposta = int(input('Insira um número'))




    if resposta_do_computador == 1 and resposta == 1:
        print(escolhapc)
        print('Empate')
        print('Bichinho:', jogo_da_velha.ponto_do_pc, 'Você:', jogo_da_velha.ponto_do_usuario)

    elif resposta_do_computador ==1 and resposta ==2:
        print(escolhapc)
        jogo_da_velha.ponto_do_usuario += 1
        print('Bichinho:', jogo_da_velha.ponto_do_pc, 'Você:', jogo_da_velha.ponto_do_usuario)
    elif resposta_do_computador == 1 and resposta == 3:
        print(escolhapc)
        jogo_da_velha.ponto_do_pc += 1
        print('Bichinho:', jogo_da_velha.ponto_do_pc, 'Você:', jogo_da_velha.ponto_do_usuario)
    elif resposta_do_computador == 2 and resposta == 1:
        print(escolhapc)
        jogo_da_velha.ponto_do_pc += 1
        print('Bichinho:', jogo_da_velha.ponto_do_pc, 'Você:', jogo_da_velha.ponto_do_usuario)
    elif resposta_do_computador == 2 and resposta == 2:
        print(escolhapc)
        print('Empate')
        print('Bichinho:', jogo_da_velha.ponto_do_pc, 'Você:', jogo_da_velha.ponto_do_usuario)
    elif resposta_do_computador== 2 and resposta == 3:
        print(escolhapc)
        jogo_da_velha.ponto_do_usuario += 1
        print('Bichinho:', jogo_da_velha.ponto_do_pc, 'Você:', jogo_da_velha.ponto_do_usuario)
    elif resposta_do_computador == 3 and resposta == 1:
        print(escolhapc)
        jogo_da_velha.ponto_do_usuario +=1
        print('Bichinho:', jogo_da_velha.ponto_do_pc, 'Você:', jogo_da_velha.ponto_do_usuario)
    elif resposta_do_computador == 3 and resposta == 2:
        print(escolhapc)
        jogo_da_velha.ponto_do_pc += 1
        print('Bichinho:', jogo_da_velha.ponto_do_pc, 'Você:', jogo_da_velha.ponto_do_usuario)
    elif resposta_do_computador == 3 and resposta == 3:
        print(escolhapc)
        print('Empate')
        print('Bichinho:', jogo_da_velha.ponto_do_pc, 'Você:', jogo_da_velha.ponto_do_usuario)

    elif resposta == 4:
        break

    else:
        print('Número inválido')

if __name__ == '__main__':
    jogo_da_velha()
