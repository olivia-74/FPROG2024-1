# import random

# def JogarDado():
#     resultado = random.randint(1, 6)
#     print(f"Resultado do dado: {resultado}")
#     return resultado

# # Função para executar as regras do jogo
# def ExecutarRegras(jogador, casa):
#     jogada = JogarDado()  # Realiza a jogada do dado
    
#     if jogada < 3 or jogada == 6:
#         casa += jogada
#         print(f"{jogador} avançou {jogada} casa.")
#     elif jogada == 3:
#         casa -= 1
#         print(f"{jogador} voltou 1 casa.")
    
#     return casa

# # Quantidade de jogadores
# while True:
#     nJogadores = int(input("Número de jogadores (1 ou 2): "))
#     if nJogadores == 1 or nJogadores == 2:
#         break
#     else:
#         print("Insira apenas 1 ou 2 como número de jogadores")

# # Tabuleiro com 21 casas
# casa_jogador1 = 0
# casa_jogador2 = 0

# # Loop do jogo
# while True:
#     input("Jogador 1 - jogue o dado") 
#     casa_jogador1 = ExecutarRegras("Jogador 1", casa_jogador1)
#     if casa_jogador1 >= 21:
#         print("Jogador 1 venceu!")
#         break
    
#     if nJogadores == 2:
#         input("Jogador 2 - jogue o dado")
#         casa_jogador2 = ExecutarRegras("Jogador 2", casa_jogador2)
#         if casa_jogador2 >= 21:
#             print("Jogador 2 venceu!")
#             break



# variaveis
import math
import random
casa = 0
tabuleiro = []

# quantidade de jogadores
while True:
    nJogadores = int(input("Número de jogadores (1 ou 2): "))
    if nJogadores == 1 or nJogadores == 2:
        break
    else:
        print("insira apenas 1 ou 2 como número de jogadores")

# funcoes

# 🎲: "rode a roleta" - se parar no 1, avance uma casa; se parar no 3, volte uma casa; se parar no 6, perde uma rodada no jogo em dupla
def JogarDado ():
    resultado = random.randint(1,6)
    print(f"Resultado do dado: {resultado}")
    return resultado

def ExecutarRegras (jogador, casa):

    if jogada < 3 or 3 > jogada < 6:
        jogada = jogarDado()
        casa += jogada
        print(f"{jogador} avançou {jogada} casa.")
    
    elif jogada == 3:
        casa -= 1
    elif jogada == 6:
        pass


#💀: morreu - dar print dos dados dos jogadores e dizer quem ganhou (!!!)
def Morrer (jogador):
    print(jogador, "venceu")


#🧮: desafio matematico - jogar o dado e chamar uma das funcoes: 
    #  1 = mostrar na tela os numeros primos ate 100 (Primos(100)). 
    # 2 = fazer o somatorio dos numeros de 1 ate 100 (Somatorio(ini, fim)). 
    # 3 = imprimir a serie de fibonacci ate o decimo elemento (Fibo(n)). 
    # 4 = calcular a area de um circulo com raio de 2.5 (AreaCirculo(r)). 
    # 5 = imprimir o fatorial de 5 (fatorial(n)). 
    # 6 = imprimir os 5 primeiros numeros divisiveis por 2 e por 5 (Div25(n)).
# DesafioMatematico()
def DesafioMatematico():
    resultado = JogarDado()
    if resultado == 1:
        Primos(100)
    elif resultado == 2:
        Somatorio(1, 100)
    elif resultado == 3:
        Fibonacci(10)
    elif resultado == 4:
        AreaCirculo(2.5)
    elif resultado == 5:
        Fatorial(5)
    else: 
        Divisao(2, 5)
        
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
    print("2) somatorio dos numeros de 1 ate 100: {somatorio}")

# Fibonacci(10)
def Fibonacci(n):
    serie = [0, 1]
    while len(serie) < n:
        elemento = serie[-1] + serie[-2]
        serie.append(elemento)
    print(f"3) série de Fibonacci até o {n}º elemento e: {' '.join(map(str, serie))}")

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
    print(f"6) os 5 primeiros numeros divisiveis por {valor1} e por {valor2} sao: {', '.join(map(str, divisiveis))}")


#🎓: formatura - jogue o dado e decida os 6 possiveis valores:
    #  1 = medicina 
    #  2 = ciencia da computacao 
    #  3 = veterinaria
    #  4 = direito
    #  5 = pedagogia
    #  6 = administracao
def Formatura(jogador):



# rodada
def main():
    for i in range (nJogadores):
        JogarDado(jogador)

while nJogadores > 1:
    main()


print("O jogador", jogadores_restantes, "venceu!")