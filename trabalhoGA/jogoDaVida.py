import random
import math

posJog1 = 0
posJog2 = 0

#status
filhosJog1 = 0
filhosJog2 = 0
ecJog1 = "solteiro" #ec = estado civil 
ecJog2 = "solteiro"
forJog1 = None #formacao
forJog2 = None
dinJog1 = 0
dinJog2 = 0 #dinheiro
statusJog1 = "normal"
statusJog2 = "normal"

# ideia:  j1 = {nome: "nome", pos: 0, filhos: 0, relacionamento: "solteiro"}
# jog1 = j1
vencedor = 0

tabuleiro = {
    0: '👶 Iniciou a Jornada 👶',
    1: '🎲 Lançar o dado 🎲',
    2: '💀 Morrer 💀',
    3: '🎲 Lancar o dado',
    4: '🧮 Desafio matematico ',
    5: '🎓 Formatura 🎓',
    6: '🍼 Ter filho 🍼',
    7: '💍 Casar 💍 ',
    8: '💀 Morrer 💀',
    9: '🍼 Ter filho 🍼',
    10: '🎲 Lançar o dado 🎲',
    11: '🧮 Desafio matematico 🧮',
    12: '💔 Divorcio 💔',
    13: '🍼 Ter filho 🍼',
    14: '💰 Ganhar na loteria 💰',
    15: '🕺 Ficar famoso 🕺',
    16: '💍 Casar 💍',
    17: '🎲 Lançar o dado 🎲',
    18: '💀 Morrer 💀',
    19: '🧮 Desafio matematico 🧮',
    20: '⌛ Resetar ⌛',
    21: '🖖 Teve uma vida longa e prospera 🖖',
}

#funcoes do desafio matematico

# Primos(100)
def Primos(x):
    nPrimos = []
    n = 2
    while n <= x:
        primo = True
        for i in range(2, n):
            if n % i == 0:
                primo = False
                break
        if primo:
            nPrimos.append(n)
        n += 1 
    print(f"1) números primos até {x}: {' '.join(map(str, nPrimos))}") # mapeia e converte cada elemento da lista em strings para poder juntar elas usando join

# Somatorio(1,100)
def Somatorio(inicio,final):
    somatorio = 0
    for i in range(inicio, final + 1):
        somatorio += i
    print(f"2) somatorio dos numeros de 1 ate 100: {somatorio}")

# Fibonacci(10)
def Fibonacci(n):
    serie = [0, 1]
    while len(serie) < n:
        elemento = serie[-1] + serie[-2]
        serie.append(elemento)
    print(f"3) série de Fibonacci até o {n}º elemento: {' '.join(map(str, serie))}")

# AreaCirculo(2.5)
def AreaCirculo(r):
    A = math.pi * (r * r)
    print(f"4) a area de um circulo com raio de {r} e: {A}")

# Fatorial(5)
def Fatorial(n):
    fatorial = 1  # comeca com 1 pq o fatorial de 0 é 1
    for i in range(1, n + 1):  # loop
        fatorial *= i  # multiplica o resultado pelo número atual do loop
    print(f"5) o fatorial de {n} e: {fatorial}")

# Divisao(2, 5)
def Divisao(valor1, valor2):
    divisiveis = []
    num = 1
    while len(divisiveis) < 5:
        if num % valor1 == 0 and num % valor2 == 0: 
            divisiveis.append(num)  
        num += 1
    print(f"6) os 5 primeiros numeros divisiveis por {valor1} e por {valor2} são: {', '.join(map(str, divisiveis))}")


# funcoes das casas

def JogarDado(posJogX):
    while posJogX == 1 or posJogX == 3 or posJogX == 10 or posJogX == 17: 
        input(f"jogador, aperte Enter para jogar o dado: ")
        dado = random.randint(1,6)
        print(f"resultado do dado: {dado}")
        if dado == 1:
            posJogX += 1
            print(f"o jogador andou mais 1 casa")
        elif dado == 2:
            posJogX += 2
            print(f"o jogador andou mais 2 casas")
        elif dado == 3: 
            posJogX -= 1
            print(f"o jogador voltou 1 casa")
        elif dado == 4:
            posJogX += 4
            print(f"o jogador andou mais 4 casas")
        elif dado == 5:
            posJogX += 5
            print(f"o jogador andou mais 5 casas")
        else:
            print(f"o jogador continua no mesmo lugar")
            break
        print(f"o jogador está na casa {posJogX}")
        pass

def Morrer(posJogX):
    print(f"o Jogador morreu! Game Over!")
    print()

def DesafioMatematico():
    print("Desafio matemático! Jogue o dado e decida que funcao executar: \n1- mostrar na tela os numeros primos ate 100. \n2- fazer o somatorio dos numeros de 1 ate 100. \n3- imprimir a serie de fibonacci ate o decimo elemento. \n4- calcular a area de um circulo com raio de 2.5. \n5- imprimir o fatorial de 5. \n6- imprimir os 5 primeiros numeros divisiveis por 2 e por 5.")
    input("Jogador, pressione Enter para jogar o dado...")
    dado = random.randint(1,6)
    print("resultado do dado: ", dado)

    if dado == 1:
        Primos(100)
    elif dado == 2:
        Somatorio(1, 100)
    elif dado == 3:
        Fibonacci(10)
    elif dado == 4:
        AreaCirculo(2.5)
    elif dado == 5:
        Fatorial(5)
    else: 
        Divisao(2, 5)

def Formatura(forJogX):
    global forJog1, forJog2
    print("se formou!!! Jogue o dado e decida cursos para os 6 possiveis valores.\n 1- medicina \n 2- ciencia da computacai \n 3- veterinaria \n 4- direito \n 5- pedagogia \n 6- administracao")
    input("pressione Enter para jogar o dado:")
    dado = random.randint(1,6)
    print("resultado do dado: ", dado)    
    if dado == 1:
        forJogX = "medicina"
    elif dado == 2:
        forJogX = "ciencia da computacao"
    elif dado == 3:
        forJogX = "veterinaria"
    elif dado == 4:
        forJogX = "direito"
    elif dado == 5:
        forJogX = "pedagogia"
    else:
        forJogX = "administracao"
    print(f"parabens! voce se formou em {forJogX}")
    return forJogX
 
def TerFilho(filhosJogX):
    global filhosJog1, filhosJog2
    print("teve filho!!! jogue o dado e se sair o numero 5, são gêmeos!!! Nos outros casos, apenas 1 filho.")
    input("Jogador, pressione Enter para jogar o dado:")
    dado = random.randint(1,6)
    print("resultado do dado: ", dado)     
    if dado == 5:
        filhosJogX += 2
        print("parabens! são gêmeos")
    else:
        filhosJogX += 1
        print("parabens! voce teve um filho")
    return filhosJogX

def Casar(ecJogX):
    global ecJog1, ecJog2
    print(f"casamento!")
    if ecJogX != "casado":
        print("parabens! voce se casou")
        ecJogX = "casado"
    else:
        print("voce ja é casado 🤨")
        pass
    return ecJogX

def Divorciar(ecJogX):
    global ecJog1, ecJog2
    if ecJogX == "casado":
        print("voce agora é divorciado")
        ecJogX = "divorciado"
    else:
        print("voce precisa ser casado poder se divorciar")
        pass
    return ecJogX

def Loteria(dinJogX):
    global dinJog1, dinJog2
    print("Ganhou na loteria!! Jogue o dado para ver quanto ganhou: \n1-Ganha R$ 2,50 no bolão \n2- Ganha RS 5.000 \n3- Ganha R$ 50.000 \n4- Ganha R$ 500.000 \n5- Ganha R$ 5.000.000 \n6- Ganha RS 10.000.000")
    input("Jogador, pressione Enter para jogar o dado:")
    dado = random.randint(1,6)
    print("resultado do dado: ", dado)   

    if dado == 1:
        dinJogX += 2,50
        print("ganha R$ 2,50 no Bolao")
    elif dado == 2:
        dinJogX += 5000
        print("ganha R$ 5.000,00")
    elif dado == 3:
        dinJogX += 50000
        print("ganha 50.000,00")
    elif dado == 4:
        dinJogX += 500000
        print("ganha 500.000,00")
    elif dado == 5:
        dinJogX += 5000000
        print("ganha 5.000.000,00")
    else:
        dinJogX += 10000000
        print("ganha R$ 10.000.000")
    return dinJogX

def Fama(statusJogX):
    global statusJog1, statusJog2
    statusJogX = "famoso"
    print(f"Você ficou famoso!")
    return statusJogX

def Resetar(posJogX, filhosJogX, ecJogX, forJogX, dinJogX, statusJogX):
    global posJog1, posJog2, filhosJog1, filhosJog2, ecJog1, ecJog2, forJog1, forJog2, dinJog1, dinJog2, statusJog1, statusJog2
    posJogX = 0
    filhosJogX = 0
    ecJogX == "solteiro"
    forJogX = None
    dinJogX = 0
    statusJogX = "normal"


while True:
    qtdJogadores = int(input("Quantos jogadores? (1 ou 2): "))
    if qtdJogadores == 1 or qtdJogadores == 2:
        break
    else:
        print("insira apenas 1 ou 2 como número de jogadores")

while vencedor == 0:

# JOGADOR 1 AAAAAAAAAAA
    input("Jogador 1, aperte enter para jogar o dado: ")
    dado = random.randint(1,6)
    print(f"resultado do dado: {dado}, o jogador andou {dado} casas")
    posJog1 += dado

    if posJog1 < 0: #nao existe posicao negativa
        posJog1 = 0
    if posJog1 > 21: #21 e o limite
        posJog1 = 21

    casa = posJog1
    print(f"casa {casa}: {tabuleiro[casa]}")
    if casa == 1 or casa == 3 or casa == 10 or casa == 17:
        JogarDado(posJog1)
    elif casa == 2 or casa == 8 or casa == 18:
        Morrer(posJog1)
        print(f"RIP jogador 1: \nquantidade de filhos: {filhosJog1} \nestado civil: {ecJog1} \nformacao: {forJog1} \ndinheiro: {dinJog1} \nstatus social: {statusJog1}")
        vencedor = 2
        break
    elif casa == 4 or casa == 11 or casa == 19:
        DesafioMatematico()
    elif casa == 5:
        forJog1 = Formatura(forJog1)
    elif casa == 6 or casa == 9 or casa == 13:
        filhosJog1 = TerFilho(filhosJog1)
    elif casa == 7 or casa == 16:
        ecJog1 = Casar(ecJog1)
    elif casa == 12:
        ecJog1 = Divorciar(ecJog1)
    elif casa == 14:
        dinJog1 = Loteria(dinJog1)
    elif casa == 15:
        statusJog1 = Fama(statusJog1)
    elif casa == 20:
        Resetar(posJog1, filhosJog1, ecJog1, forJog1, dinJog1, statusJog1)
    elif casa == 21:
        vencedor = 1
        break
    print()

    


    if qtdJogadores == 2:
# JOGADOR 2
        input("Jogador 2, aperte enter para jogar o dado: ")
        dado = random.randint(1,6)
        print(f"resultado do dado: {dado}, o jogador andou {dado} casas")
        posJog2 += dado
        
        if posJog2 < 0: #nao existe posicao negativa
            posJog2 = 0
        if posJog2 > 21: #21 e o limite
            posJog2 = 21

        casa = posJog2
        print(f"casa {casa}: {tabuleiro[casa]}")
        if casa == 1 or casa == 3 or casa == 10 or casa == 17:
            JogarDado(posJog2)
        elif casa == 2 or casa == 8 or casa == 18:
            Morrer(posJog2)
            print(f"RIP jogador 2: \nquantidade de filhos: {filhosJog2} \nestado civil: {ecJog2} \nformacao: {forJog2} \ndinheiro: {dinJog2} \nstatus social: {statusJog2}") #NAO TA MUDANDO O VALOR DA VARIAVEL AAAAAAAAA
            vencedor = 1
            break
        elif casa == 4 or casa == 11 or casa == 19:
            DesafioMatematico()
        elif casa == 5:
            forJog2 = Formatura(forJog2)
        elif casa == 6 or casa == 9 or casa == 13:
            filhosJog2 = TerFilho(filhosJog2)
        elif casa == 7 or casa == 16:
           ecJog2 = Casar(ecJog2)
        elif casa == 12:
            ecJog2 = Divorciar(ecJog2)
        elif casa == 14:
            dinJog2 = Loteria(dinJog2)
        elif casa == 15:
            statusJog2 = Fama(statusJog2)
        elif casa == 20:
            Resetar(posJog2, filhosJog2, ecJog2, forJog2, dinJog2, statusJog2)
        elif casa == 21:
            vencedor == 2
            pass
        print()
        
    else:
        pass


if vencedor == 1:
    print("Jogador 1 venceu")
elif vencedor == 2:
    print("Jogador 2 venceu")

