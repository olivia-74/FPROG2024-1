# import random
# import math

# # Funções relacionadas às ações do jogo

# def JogarDado():
#     resultado = random.randint(1, 6)
#     print(f"resultado do dado: {resultado}")
#     return resultado

# def MoverJogador(nJogador, casa):
#     input("Jogador, pressione Enter para jogar o dado...")
#     dado = JogarDado()
#     if dado != 3 and dado != 6:
#         posJogador += dado
#         print(f"Você avançou {dado} casa(s).")
#     elif dado == 3:
#         posJogador -= 1
#         print("Voce voltou uma casa")
#     elif dado == 6:
#         print("rodada anulada")
#         pass
#     print(f"Jogador {nJogador}: Você chegou à casa {posJogador}{tabuleiro[casa]}")

# def Morrer(nJogador, status_jogador):
#     status = status_jogador[nJogador]
#     print(f"{nJogador} morreu! Game Over! Status: {status}")

# def DesafioMatematico(nJogador):
#     """Executa um desafio matemático."""
#     print(f"{nJogador}: Desafio matemático! Jogue o dado e decida que funcao executar: \n1- mostrar na tela os numeros primos ate 100. \n2- fazer o somatorio dos numeros de 1 ate 100. \n3- imprimir a serie de fibonacci ate o decimo elemento. \n4- calcular a area de um circulo com raio de 2.5. \n5- imprimir o fatorial de 5. \n6- imprimir os 5 primeiros numeros divisiveis por 2 e por 5.")
#     input("Jogador, pressione Enter para jogar o dado...")
#     resultado = JogarDado()

#     if resultado == 1:
#         Primos(100)
#     elif resultado == 2:
#         Somatorio(1, 100)
#     elif resultado == 3:
#         Fibonacci(10)
#     elif resultado == 4:
#         AreaCirculo(2.5)
#     elif resultado == 5:
#         Fatorial(5)
#     else: 
#         Divisao(2, 5)
        
#     # Primos(100)
#     def Primos(x):
#         nPrimos = []
#         n = 2
#         while n <= x:
#             primo = True
#             for i in range(2, n):
#                 if n % i == 0:
#                     primo = False
#                     break
#             if primo:
#                 nPrimos.append(n)
#             n += 1 
#         print(f"1) números primos até {x}: {' '.join(map(str, nPrimos))}") # mapeia e converte cada elemento da lista em strings para poder juntar elas usando join

#     # Somatorio(1,100)
#     def Somatorio(inicio,final):
#         somatorio = 0
#         for i in range(inicio, final + 1):
#             somatorio += i
#         print("2) somatorio dos numeros de 1 ate 100: {somatorio}")

#     # Fibonacci(10)
#     def Fibonacci(n):
#         serie = [0, 1]
#         while len(serie) < n:
#             elemento = serie[-1] + serie[-2]
#             serie.append(elemento)
#         print(f"3) série de Fibonacci até o {n}º elemento e: {' '.join(map(str, serie))}")

#     # AreaCirculo(2.5)
#     def AreaCirculo(r):
#         A = math.pi * (r * r)
#         print(f"4) a area de um circulo com raio de {r} e: {A}")

#     # Fatorial(5)
#     def Fatorial(n):
#         fatorial = 1  # comeca com 1 pq o fatorial de 0 é 1
#         for i in range(1, n + 1):  # loop
#             fatorial *= i  # multiplica o resultado pelo número atual do loop
#         print(f"5) o fatorial de {n} e: {fatorial}")

#     # Divisao(2, 5)
#     def Divisao(valor1, valor2):
#         divisiveis = []
#         num = 1
#         while len(divisiveis) < 5:
#             if num % valor1 == 0 and num % valor2 == 0: 
#                 divisiveis.append(num)  
#             num += 1
#         print(f"6) os 5 primeiros numeros divisiveis por {valor1} e por {valor2} sao: {', '.join(map(str, divisiveis))}")

# def Formatura(nJogador):
#     print("se formou!!! Jogue o dado e decida cursos para os 6 possiveis valores.\n 1- medicina \n 2- ciencia da computacai \n 3- veterinaria \n 4- direito \n 5- pedagogia \n 6- administracao")
#     input("pressione Enter para jogar o dado...")
#     resultado = JogarDado()
#     if resultado == 1:
#         print("curso: medicina")
#     elif resultado == 2:
#         print("curso: ciencia da computacao")
#     elif resultado == 3:
#         print("veterinaria")
#     elif resultado == 4:
#         print("curso: direito")
#     elif resultado == 5:
#         print("pedagogia")
#     else:
#         print("administracao")

# def TerFilho(nJogador):
#     """Simula ter filhos."""
#     print(f"Jogador {nJogador}: Você teve um filho!")
#     print("teve filho!!! jogue o dado e se sair o numero 5, sao gemeos!!! Nos outros casos, apenas 1 filho.")
#     input("Jogador, pressione Enter para jogar o dado...")
#     resultado = JogarDado()
#     if resultado == 5:
#         nJogador[filhos] += 2
#     else:
#         nJogador[filhos] += 1

# def Casar(nJogador):
#     print(f"casamento!")
#     if jogador[estadoCivil] != "Casado":
#         nJogador[estadoCivil] = "Casado"
#     else:
#         print("o jogador ja e casado")
#         pass

# def FicarFamoso(nJogador):
#     print(f"Jogador {nJogador}: Você ficou famoso!")
#     # Atualizar o status de fama do jogador aqui...

# def Divorciar(nJogador):
#     if nJogador[estadoCivil] == "casado":
#         nJogador[estadoCivil] = "divorciado"
#         print(f"Jogador {nJogador}: Você se divorciou!")
#     else:
#         pass

# def Loteria(nJogador):
#     premios = {
#         1: 'Ganha R$ 2,50 no bolão',
#         2: 'Ganha R$ 5.000,00',
#         3: 'Ganha R$ 50.000,00',
#         4: 'Ganha R$ 500.000,00',
#         5: 'Ganha R$ 5.000.000,00',
#         6: 'Ganha R$ 100.000.000,00'
#     }
#     premio = premios[JogarDado()]
#     print(f"Jogador {nJogador}: {premio}")
#     # Atualizar o estado financeiro do jogador aqui...

# def Resetar(nJogador):
#     jogador[casa] == 0
#     jogador[filhos] == 0
#     jogador[estadoCivil] = "solteiro"

# # Dicionário com as ações associadas a cada casa do tabuleiro
# tabuleiro = {
#     0: '👶- Iniciou a Jornada ',
#     1: '🎲- Lancar o dado',
#     2: '💀- Morrer',
#     3: '🎲- Lancar o dado',
#     4: '🧮- Desafio matematico ',
#     5: 'Formatura 🎓',
#     6: 'Ter filho 🍼',
#     7: 'Casar 💍 ',
#     8: 'Morrer 💀',
#     9: 'Ter filho 🍼',
#     10: 'Lancar o dado 🎲',
#     11: 'Desafio matematico 🧮',
#     12: 'Divorcio 💔',
#     13: 'Ter filho 🍼',
#     14: 'Ganhar na loteria 💰',
#     15: 'Ficar famoso🕺',
#     16: 'Casar 💍',
#     17: 'Lancar o dado 🎲',
#     18: 'Morrer 💀',
#     19: 'Desafio matematico 🧮',
#     20: 'Resetar ⌛',
#     21: 'Teve uma vida longa e prospera 🖖',
# }



# # Função principal do jogo
# def main():
#     while True:
#         qtdJogadores = int(input("Quantos jogadores? (1 ou 2): "))
#         if qtdJogadores == 1 or qtdJogadores == 2:
#             break
#         else:
#             print("insira apenas 1 ou 2 como número de jogadores")
    
#     # Inicialização das variáveis do jogo

#     jogador1 = {posJogador: 0, filhos: 0, estadoCivil: "solteiro", vivo: True}

#     nJogador = {
#         jogador1,
#         jogador2
#     }

#     # Loop principal do jogo
#     while True:
#         MoverJogador(1, posJogador)

#         if posJogador == 1:
#             MoverJogador(nJogador, posJogador)

#         elif posJogador == 2:
#             Morrer(nJogador)
        
#         elif posJogador == 3:
#             MoverJogador(nJogador, posJogador)
        
#         elif posJogador == 4:
#             DesafioMatematico(nJogador)
        
#         elif posJogador == 5:
#             Formatura(nJogador)

#         elif posJogador == 6:
#             TerFilho(nJogador)
        
#         elif posJogador == 7:
#             Casar(nJogador)
        
#         elif posJogador == 8:
#             Morrer(nJogador)

#         elif posJogador == 9:
#             TerFilho(nJogador)

#         elif posJogador == 10:
#             MoverJogador(nJogador, posJogador)

#         elif posJogador == 11:
#             DesafioMatematico(nJogador)
        
#         elif posJogador == 12:
#             Divorciar(nJogador)
        
#         elif posJogador == 13:
#             TerFilho(nJogador)

#         elif posJogador == 14:
#             Loteria(nJogador)

#         elif posJogador == 15:
#             FicarFamoso(nJogador)
        
#         elif posJogador == 16:
#             Casar(nJogador)

#         elif posJogador == 17:
#             MoverJogador(nJogador, posJogador)

#         elif posJogador == 18:
#             Morrer(nJogador)

#         elif posJogador == 19:
#             DesafioMatematico(nJogador)
        
#         elif posJogador == 20:
#             Resetar(nJogador)

#         if posJogador >= 21:
#             print(tabuleiro[21])
#             break

        

# # Iniciar o jogo
# main()



import random
import math

# Global variables
posJog1 = 0
posJog2 = 0
filhosJog1 = 0
filhosJog2 = 0
ecJog1 = "solteiro"
ecJog2 = "solteiro"
forJog1 = None
forJog2 = None
dinJog1 = 0
dinJog2 = 0
statusJog1 = "normal"
statusJog2 = "normal"
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

# Function to handle dice rolling for both players
def JogarDado(posJogX):
    input(f"Jogador, pressione Enter para jogar o dado: ")
    dado = random.randint(1, 6)
    print(f"Resultado do dado: {dado}")
    if dado in [1, 2, 4, 5]:
        posJogX += dado
        print(f"O jogador andou mais {dado} casas")
    elif dado == 3:
        posJogX -= 1
        print("O jogador voltou 1 casa")
    print(f"O jogador está na casa {posJogX}")
    return posJogX

# Function to handle the "Morrer" event
def Morrer(posJogX):
    print(f"O jogador morreu! Game Over!")
    print()
    return 21  # Return position 21, the last position on the board

# Function to handle the "Desafio Matemático" event
def DesafioMatematico():
    print("Desafio matemático! Jogue o dado e decida que função executar:\n"
          "1- Mostrar na tela os números primos até 100.\n"
          "2- Fazer o somatório dos números de 1 até 100.\n"
          "3- Imprimir a série de Fibonacci até o décimo elemento.\n"
          "4- Calcular a área de um círculo com raio de 2.5.\n"
          "5- Imprimir o fatorial de 5.\n"
          "6- Imprimir os 5 primeiros números divisíveis por 2 e por 5.")
    input("Jogador, pressione Enter para jogar o dado...")
    dado = random.randint(1, 6)
    print("Resultado do dado: ", dado)
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

# Function to handle the "Formatura" event
def Formatura(forJogX):
    print("Se formou!!! Jogue o dado e decida cursos para os 6 possíveis valores.\n"
          "1- Medicina\n"
          "2- Ciência da Computação\n"
          "3- Veterinária\n"
          "4- Direito\n"
          "5- Pedagogia\n"
          "6- Administração")
    input("Pressione Enter para jogar o dado...")
    dado = random.randint(1, 6)
    print("Resultado do dado: ", dado)
    cursos = {
        1: "medicina",
        2: "ciência da computação",
        3: "veterinária",
        4: "direito",
        5: "pedagogia",
        6: "administração"
    }
    forJogX = cursos.get(dado)
    print(f"Parabéns! Você se formou em {forJogX}")
    return forJogX

# Function to handle the "Ter Filho" event
def TerFilho(filhosJogX):
    print("Teve filho!!! Jogue o dado e, se sair o número 5, são gêmeos!!! Nos outros casos, apenas 1 filho.")
    input("Jogador, pressione Enter para jogar o dado...")
    dado = random.randint(1, 6)
    print("Resultado do dado: ", dado)
    if dado == 5:
        filhosJogX += 2
        print("Parabéns! São gêmeos")
    else:
        filhosJogX += 1
        print("Parabéns! Você teve um filho")
    return filhosJogX

# Function to handle the "Casar" event
def Casar(ecJogX):
    if ecJogX != "casado":
        print("Parabéns! Você se casou")
        ecJogX = "casado"
    else:
        print("Você já é casado 🤨")
    return ecJogX

# Function to handle the "Divorciar" event
def Divorciar(ecJogX):
    if ecJogX == "casado":
        print("Você agora está divorciado")
        ecJogX = "divorciado"
    else:
        print("Você precisa ser casado para poder se divorciar")
    return ecJogX

# Function to handle the "Ganhar na Loteria" event
def Loteria(dinJogX):
    print("Ganhou na loteria!! Jogue o dado para ver quanto ganhou:\n"
          "1- Ganha R$ 2,50 no bolão\n"
          "2- Ganha R$ 5.000\n"
          "3- Ganha R$ 50.000\n"
          "4- Ganha R$ 500.000\n"
          "5- Ganha R$ 5.000.000\n"
          "6- Ganha R$ 10.000.000")
    input("Jogador, pressione Enter para jogar o dado...")
    dado = random.randint(1, 6)
    print("Resultado do dado: ", dado)
    premios = {1: 2.50, 2: 5000, 3: 50000, 4: 500000, 5: 5000000, 6: 10000000}
    ganho = premios.get(dado, 0)
    dinJogX += ganho
    print(f"Você ganhou R${ganho}")
    return dinJogX

# Function to handle the "Ficar Famoso" event
def Fama(statusJogX):
    statusJogX = "famoso"
    print("Você ficou famoso!")
    return statusJogX

# Function to reset player stats
def Resetar():
    global posJog1, posJog2, filhosJog1, filhosJog2, ecJog1, ecJog2, forJog1, forJog2, dinJog1, dinJog2, statusJog1, statusJog2
    posJog1 = 0
    posJog2 = 0
    filhosJog1 = 0
    filhosJog2 = 0
    ecJog1 = "solteiro"
    ecJog2 = "solteiro"
    forJog1 = None
    forJog2 = None
    dinJog1 = 0
    dinJog2 = 0
    statusJog1 = "normal"
    statusJog2 = "normal"

# Function to check winning condition
def VerificarVencedor():
    global vencedor
    if posJog1 == 21:
        vencedor = 1
    elif posJog2 == 21:
        vencedor = 2
    elif posJog1 == 21 and posJog2 == 21:
        vencedor = 3

# Game loop
while vencedor == 0:
    qtdJogadores = int(input("Quantos jogadores? (1 ou 2): "))
    if qtdJogadores not in [1, 2]:
        print("Insira apenas 1 ou 2 como número de jogadores")
        continue

    posJog1 = JogarDado(posJog1)
    if posJog1 in [2, 8, 18]:
        posJog1 = Morrer(posJog1)
        print(f"RIP jogador 1: \nQuantidade de filhos: {filhosJog1} \nEstado civil: {ecJog1} \nFormação: {forJog1} \nDinheiro: {dinJog1} \nStatus social: {statusJog1}")
        vencedor = 2
        break
    elif posJog1 in [4, 11, 19]:
        DesafioMatematico()
    elif posJog1 == 5:
        forJog1 = Formatura(forJog1)
    elif posJog1 in [6, 9, 13]:
        filhosJog1 = TerFilho(filhosJog1)
    elif posJog1 in [7, 16]:
        ecJog1 = Casar(ecJog1)
    elif posJog1 == 12:
        ecJog1 = Divorciar(ecJog1)
    elif posJog1 == 14:
        dinJog1 = Loteria(dinJog1)
    elif posJog1 == 15:
        statusJog1 = Fama(statusJog1)
    elif posJog1 == 20:
        Resetar()

    VerificarVencedor()

    if qtdJogadores == 2:
        posJog2 = JogarDado(posJog2)
        if posJog2 in [2, 8, 18]:
            posJog2 = Morrer(posJog2)
            print(f"RIP jogador 2: \nQuantidade de filhos: {filhosJog2} \nEstado civil: {ecJog2} \nFormação: {forJog2} \nDinheiro: {dinJog2} \nStatus social: {statusJog2}")
            vencedor = 1
            break
        elif posJog2 in [4, 11, 19]:
            DesafioMatematico()
        elif posJog2 == 5:
            forJog2 = Formatura(forJog2)
        elif posJog2 in [6, 9, 13]:
            filhosJog2 = TerFilho(filhosJog2)
        elif posJog2 in [7, 16]:
            ecJog2 = Casar(ecJog2)
        elif posJog2 == 12:
            ecJog2 = Divorciar(ecJog2)
        elif posJog2 == 14:
            dinJog2 = Loteria(dinJog2)
        elif posJog2 == 15:
            statusJog2 = Fama(statusJog2)
        elif posJog2 == 20:
            Resetar()

        VerificarVencedor()

if vencedor == 1:
    print("Jogador 1 venceu")
elif vencedor == 2:
    print("Jogador 2 venceu")
elif vencedor == 3:
    print("Empate!")
