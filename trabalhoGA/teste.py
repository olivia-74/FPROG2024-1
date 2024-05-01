import random
import math

# Funções relacionadas às ações do jogo

def JogarDado():
    resultado = random.randint(1, 6)
    print(f"resultado do dado: {resultado}")
    return resultado

def MoverJogador(nJogador, casa):
    input("Jogador, pressione Enter para jogar o dado...")
    dado = JogarDado()
    if dado != 3 and dado != 6:
        posJogador += dado
        print(f"Você avançou {dado} casa(s).")
    elif dado == 3:
        posJogador -= 1
        print("Voce voltou uma casa")
    elif dado == 6:
        print("rodada anulada")
        pass
    print(f"Jogador {nJogador}: Você chegou à casa {posJogador}{tabuleiro[casa]}")

def Morrer(nJogador, status_jogador):
    status = status_jogador[nJogador]
    print(f"{nJogador} morreu! Game Over! Status: {status}")

def DesafioMatematico(nJogador):
    """Executa um desafio matemático."""
    print(f"{nJogador}: Desafio matemático! Jogue o dado e decida que funcao executar: \n1- mostrar na tela os numeros primos ate 100. \n2- fazer o somatorio dos numeros de 1 ate 100. \n3- imprimir a serie de fibonacci ate o decimo elemento. \n4- calcular a area de um circulo com raio de 2.5. \n5- imprimir o fatorial de 5. \n6- imprimir os 5 primeiros numeros divisiveis por 2 e por 5.")
    input("Jogador, pressione Enter para jogar o dado...")
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

def Formatura(nJogador):
    print("se formou!!! Jogue o dado e decida cursos para os 6 possiveis valores.\n 1- medicina \n 2- ciencia da computacai \n 3- veterinaria \n 4- direito \n 5- pedagogia \n 6- administracao")
    input("pressione Enter para jogar o dado...")
    resultado = JogarDado()
    if resultado == 1:
        print("curso: medicina")
    elif resultado == 2:
        print("curso: ciencia da computacao")
    elif resultado == 3:
        print("veterinaria")
    elif resultado == 4:
        print("curso: direito")
    elif resultado == 5:
        print("pedagogia")
    else:
        print("administracao")

def TerFilho(nJogador):
    """Simula ter filhos."""
    print(f"Jogador {nJogador}: Você teve um filho!")
    print("teve filho!!! jogue o dado e se sair o numero 5, sao gemeos!!! Nos outros casos, apenas 1 filho.")
    input("Jogador, pressione Enter para jogar o dado...")
    resultado = JogarDado()
    if resultado == 5:
        nJogador[filhos] += 2
    else:
        nJogador[filhos] += 1

def Casar(nJogador):
    print(f"casamento!")
    if jogador[estadoCivil] != "Casado":
        nJogador[estadoCivil] = "Casado"
    else:
        print("o jogador ja e casado")
        pass

def FicarFamoso(nJogador):
    print(f"Jogador {nJogador}: Você ficou famoso!")
    # Atualizar o status de fama do jogador aqui...

def Divorciar(nJogador):
    if nJogador[estadoCivil] == "casado":
        nJogador[estadoCivil] = "divorciado"
        print(f"Jogador {nJogador}: Você se divorciou!")
    else:
        pass

def Loteria(nJogador):
    premios = {
        1: 'Ganha R$ 2,50 no bolão',
        2: 'Ganha R$ 5.000,00',
        3: 'Ganha R$ 50.000,00',
        4: 'Ganha R$ 500.000,00',
        5: 'Ganha R$ 5.000.000,00',
        6: 'Ganha R$ 100.000.000,00'
    }
    premio = premios[JogarDado()]
    print(f"Jogador {nJogador}: {premio}")
    # Atualizar o estado financeiro do jogador aqui...

def Resetar(nJogador):
    jogador[casa] == 0
    jogador[filhos] == 0
    jogador[estadoCivil] = "solteiro"

# Dicionário com as ações associadas a cada casa do tabuleiro
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



# Função principal do jogo
def main():
    while True:
        qtdJogadores = int(input("Quantos jogadores? (1 ou 2): "))
        if qtdJogadores == 1 or qtdJogadores == 2:
            break
        else:
            print("insira apenas 1 ou 2 como número de jogadores")
    
    # Inicialização das variáveis do jogo

    jogador1 = {posJogador: 0, filhos: 0, estadoCivil: "solteiro", vivo: True}

    nJogador = {
        jogador1,
        jogador2
    }

    # Loop principal do jogo
    while True:
        MoverJogador(1, posJogador)

        if posJogador == 1:
            MoverJogador(nJogador, posJogador)

        elif posJogador == 2:
            Morrer(nJogador)
        
        elif posJogador == 3:
            MoverJogador(nJogador, posJogador)
        
        elif posJogador == 4:
            DesafioMatematico(nJogador)
        
        elif posJogador == 5:
            Formatura(nJogador)

        elif posJogador == 6:
            TerFilho(nJogador)
        
        elif posJogador == 7:
            Casar(nJogador)
        
        elif posJogador == 8:
            Morrer(nJogador)

        elif posJogador == 9:
            TerFilho(nJogador)

        elif posJogador == 10:
            MoverJogador(nJogador, posJogador)

        elif posJogador == 11:
            DesafioMatematico(nJogador)
        
        elif posJogador == 12:
            Divorciar(nJogador)
        
        elif posJogador == 13:
            TerFilho(nJogador)

        elif posJogador == 14:
            Loteria(nJogador)

        elif posJogador == 15:
            FicarFamoso(nJogador)
        
        elif posJogador == 16:
            Casar(nJogador)

        elif posJogador == 17:
            MoverJogador(nJogador, posJogador)

        elif posJogador == 18:
            Morrer(nJogador)

        elif posJogador == 19:
            DesafioMatematico(nJogador)
        
        elif posJogador == 20:
            Resetar(nJogador)

        if posJogador >= 21:
            print(tabuleiro[21])
            break

        

# Iniciar o jogo
main()



