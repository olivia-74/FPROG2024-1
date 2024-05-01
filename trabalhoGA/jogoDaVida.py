# variaveis
import math
import random

# filhos = 0
# estadoCivil = "solteiro"
# casa = 0

tabuleiro = {1: Mover(), 2: Morrer(), 3: Mover(), 4: DesafioMatematico(), } 

jogador1 = {casa: 0, filhos: 0, estadoCivil: "solteiro", vivo: True}

# jogador2 = {casa: 0, filhos: 0, estadoCivil: "solteiro"}



# funcoes

# 🎲: "rode a roleta" - se parar no 1, avance uma casa; se parar no 3, volte uma casa; se parar no 6, perde uma rodada no jogo em dupla
def JogarDado ():
    resultado = random.randint(1,6)
    print(f"Resultado do dado: {resultado}")
    return resultado

def ExecutarRegras (jogador, casa):
    sa#pega o dicionario tabuleiro


# Mover(jogador, casa)        
def Mover(jogador, casa):
    JogarDado()
    if resultado < 3 or 3 > resultado < 6:
        resultado = jogarDado()
        jogador[casa] += resultado
        print(f"{jogador1} avançou   {resultado} casa.")
    elif resultado == 3:
        jogador[casa] -= 3
    elif resultado == 6:
        pass

#💀: morreu - dar print dos dados dos jogadores e dizer quem ganhou (!!!)
def Morrer (jogador):
    print(jogador, "morreu")
    jogador1[vivo] = False


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
# Formatura(jogador)
def Formatura(jogador):
    print("se formou!!! Jogue o dado e decida cursos para os 6 possiveis valores./n 1- medicina /n 2- ciencia da computacai /n 3- veterinaria /n 4- direito /n 5- pedagogia /n 6- administracao")
    print(JogarDado())
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

# TerFilho(jogador, filhos) 
def TerFilho(jogador, filhos):
    print("teve filho!!! jogue o dado e se sair o numero 5, sao gemeos!!! Nos outros casos, apenas 1 filho.")
    JogarDado()
    if resultado == 5:
        jogador[filhos] += 2
    else:
        jogador[filhos] += 1

# Casar(jogador1)
def Casar(estadoCivil, jogador):
    print("casamento!")
    if jogador[estadoCivil] != "Casado":
        jogador1[estadoCivil] = "Casado"
    else:
        print("o jogador ja e casado")
        pass

# Fama(jogador)
def Fama(jogador):
    print("o jogador ficou famoso")

# Divorciar(jogador)
def Divorciar(jogador):
    if jogador1[estadoCivil] == "casado":
        jogador1[estadoCivil] = "divorciado"
    else:
        pass

# Loteria(jogador)
def Loteria(jogador):
    JogarDado()
    if resultado == 1:
        print("ganha R$ 2,50 no Bolao")
    elif resultado == 2:
        print("ganha R$ 5.000,00")
    elif resultado == 3:
        print("ganha 50.000,00")
    elif resultado == 4:
        print("ganha 500.000,00")
    elif resultado == 5:
        print("ganha 5.000.000,00")
    else:
        print("ganha R$ 10.000.000")

def Resetar(jogador):
    jogador[casa] == 0
    jogador[filhos] == 0
    jogador[estadoCivil] = "solteiro"


# quantidade de jogadores
while True:
    nJogadores = int(input("Número de jogadores (1 ou 2): "))
    if nJogadores == 1 or nJogadores == 2:
        break
    else:
        print("insira apenas 1 ou 2 como número de jogadores")



print("O jogador", jogadores_restantes, "venceu!")


# -----------------------------------------------------
import math
import random

# variáveis
filhos = 'filhos'
estadoCivil = 'estadoCivil'
vivo = 'vivo'

# dicionário do tabuleiro
tabuleiro = {
    0: '👶- Iniciou a Jornada ',
    1: '🎲- Lancar o dado',
    2: '💀- Morrer',
    3: '🎲- Lancar o dado',
    4: 'Desafio matematico 🧮',
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

# jogadores
jogador = {casa: 0, filhos: 0, estadoCivil: "solteiro", vivo: True}
# jogador2 = {casa: 0, filhos: 0, estadoCivil: "solteiro", vivo: True}

# função para jogar o dado
def JogarDado():
    resultado = random.randint(1, 6)
    print(f"resultado do dado: {resultado}")
    return resultado

# função para mover o jogador
def Mover(jogador, casas):
    resultado = JogarDado()
    if resultado == 1:
        jogador[casa] += 1
    elif resultado == 2:
        jogador[casa] += 2
    elif resultado == 3:
        jogador[casa] -= 1
    elif resultado == 4:
        jogador[casa] += 4
    elif resultado == 5:
        jogador[casa] += 5
    else:
        pass


# função para indicar que o jogador morreu
def Morrer(jogador, jogador_numero):
    print(f"jogador {jogador_numero} morreu. Status: Estado civil: {jogador[estadoCivil]}, Filhos: {jogador[filhos]}")
    jogador[vivo] = False

# função para desafio matemático
def DesafioMatematico():
    resultado = JogarDado()
    print(f"Resultado do dado: {resultado}")
    print("Executando Desafio Matemático...")

def ExecutarRegras():
    if jogador[casa] == 1:
        print(tabuleiro[1])
        print(f"{jogador}: aperte Enter para jogar o dado")
        # Mover(jogador, 1)
        break
    if jogador[casa] == 2:
        print(tabuleiro[2])
        Morrer(jogador)
    if jogador[casa] == 3:
        print(tabuleiro[3])
    if jogador[casa] == 4:
        print(tabuleiro[4])

# função principal
def main():
    print(f"jogador: aperte Enter para jogar o dado")

    if jogador[casa] == 0:
        print(tabuleiro[0])
        # Mover(jogador, 0)
        break
    

    

    
        

    for casa, acao in tabuleiro.items():
        if acao == 'Mover':
            Mover(jogador1, 1)
            if nJogadores == 2:
                Mover(jogador2, 2)
        elif acao == 'Morrer':
            Morrer(jogador1, 1)
            if not jogador1[vivo]:
                break
            if nJogadores == 2:
                Morrer(jogador2, 2)
            if not jogador2[vivo]:
                break
        elif acao == 'DesafioMatematico':
            DesafioMatematico()
            if nJogadores == 2:
                DesafioMatematico()


# quantidade de jogadores
while True:
    nJogadores = int(input("Número de jogadores (1 ou 2): "))
    if nJogadores == 1 or nJogadores == 2:
        break
    else:
        print("Insira apenas 1 ou 2 como número de jogadores")

# rodada
main()
if jogador1[vivo]:
    print("O jogador 1 venceu!")
elif jogador2[vivo]:
    print("O jogador 2 venceu!")
else:
    print("Empate!")
