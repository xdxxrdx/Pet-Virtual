import random


class JogoDoBalde:
    capacidade = 100
    volume_inicial = random.randint(1, 50)



ciclo = True
while ciclo:
    quantidade = random.randint(1, 25)
    print('''
    1 PARA ADICIONAR
    2 PARA DESCARTAR''')
    print('Deseja adicionar?')
    resposta = int(input())
    if resposta == 1:

        JogoDoBalde.volume_inicial += quantidade

        if JogoDoBalde.volume_inicial > JogoDoBalde.capacidade:
            print('Você perdeu!')
            print(JogoDoBalde.volume_inicial)
            break

        elif JogoDoBalde.volume_inicial == JogoDoBalde.capacidade:
            print('Você ganhou!')
            print(JogoDoBalde.volume_inicial)
            break

        elif JogoDoBalde.volume_inicial < JogoDoBalde.capacidade:
            print(JogoDoBalde.volume_inicial)

if __name__ == '__main__':
    JogoDoBalde()
