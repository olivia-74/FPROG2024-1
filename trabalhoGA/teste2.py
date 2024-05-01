import random

posjog1 = 0
posjog2 = 0

vencedor = 0

tabuleiro = {
    0: '👶- Iniciou a Jornada ',
    1: '🎲- Lancar o dado',
    2: '💀- Morrer',
    3: '🎲- Lancar o dado',
    4: '🧮- Desafio matematico ',
    5: 'Formatura 🎓',
    6: 'Ter filho 🍼',
    7: 'Casar 💍 ',
    8: 'Morrer 💀',
    9: 'Ter filho 🍼',
    10: 'Lancar o dado 🎲',
    11: 'Desafio matematico 🧮',
    12: 'Divorcio 💔',
    13: 'Ter filho 🍼',
    14: 'Ganhar na loteria 💰',
    15: 'Ficar famoso🕺',
    16: 'Casar 💍',
    17: 'Lancar o dado 🎲',
    18: 'Morrer 💀',
    19: 'Desafio matematico 🧮',
    20: 'Resetar ⌛',
    21: 'Teve uma vida longa e prospera 🖖',
}

def JogarDado(posjogX):
    while posjogX == 1 or posjogX == 3 or posjogX == 10 or posjogX == 17: 
        input(f"jogador, aperte enter para jogar o dado: ")
        dado = random.randint(1,6)
        print(f"resultado do dado: {dado}")
        if dado == 1:
            posjogX += 1
            print(f"o jogador andou mais 1 casa")
        elif dado == 2:
            posjogX += 2
            print(f"o jogador andou mais 2 casas")
        elif dado == 3: 
            posjogX -= 1
            print(f"o jogador voltou 1 casa")
        elif dado == 4:
            posjogX += 4
            print(f"o jogador andou mais 4 casas")
        elif dado == 5:
            posjogX += 5
            print(f"o jogador andou mais 5 casas")
        else:
            print(f"o jogador continua no mesmo lugar")
            break
        print(f"o jogador esta na casa {posjogX}")
        pass

def Morrer(posjogX):
    print(f"{posjogX} morreu! Game Over!")
    vencedor = 2

while vencedor == 0:

# JOGADOR 1 AAAAAAAAAAA
    input("Jogador 1, aperte enter para jogar o dado: ")
    dado = random.randint(1,6)
    print(f"resultado do dado: {dado}, o jogador andou {dado} casas")
    posjog1 += dado
    casa = posjog1
    print(f"casa {casa}: {tabuleiro[casa]}")
    if casa == 1:
        JogarDado(posjog1)
    elif casa == 2:
        Morrer(posjog1)
    elif casa == 3:
        JogarDado(posjog1)
    else:
        break
    

    print()

    if posjog1 < 0: #nao existe posicao negativa
        posjog1 = 0
    if posjog1 > 21: #21 e o limite
        posjog1 = 21

# JOGADOR 2
    input("Jogador 2, aperte enter para jogar o dado: ")
    dado = random.randint(1,6)
    print(f"resultado do dado: {dado}")
    if dado == 1:
        posjog2 += 1
        print(f"jogador 2 andou 1 casa")
    elif dado == 2:
        posjog2 += 2
        print(f"jogador 2 andou 2 casas")
    elif dado == 3: 
        posjog2 -= 1
        print(f"jogador 2 voltou 1 casa")
    elif dado == 4:
        posjog2 += 4
        print(f"jogador 2 andou 4 casas")
    elif dado == 5:
        posjog2 += 5
        print(f"jogador 2 andou 5 casas")
    else:
        print(f"jogador 2 perde uma rodada no jogo em dupla")
        pass
    
    casa = posjog2
    print(f"casa {casa}: {tabuleiro[posjog2]}")
    print()

    if posjog2 < 0: #nao existe posicao negativa
        posjog2 = 0
    if posjog2 > 21: #21 e o limite
        posjog2 = 21

    if posjog1 == 21: 
        vencedor = 1
    if posjog2 == 21:
        vencedor = 2 
    if posjog1 == 21 and posjog2 == 21: 
        vencedor = 3 #empate


    print()
    print("Jogador 1:", end=' ')
    for i in range (posjog1):
        print("*", end= ' ')
    print()
    print("Jogador 2:", end=' ')
    for i in range (posjog2):
        print("*", end= ' ')

if vencedor == 1:
    print("Jogador 1 venceu")
elif vencedor == 2:
    print("Jogador 2 venceu")
else:
    print("empate!")
