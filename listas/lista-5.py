# 1. Implemente uma função cumprimentar que receba como parâmetro o nome de uma pessoa e escreva a mensagem “Olá, <nome_da_pessoa>!”

def cumprimentar(nome):
    print("Olá,", nome)
cumprimentar("Olivia")

# 2. Implemente uma função tabuada que receba como parâmetro um número inteiro e escreva a tabuada desse número.
def tabuada(n):
    for i in range(11):
      print(f"{n} X {i} = {n * i}")
tabuada(5)

# 3. Implemente uma função mediaUnisinos que receba como parâmetro as notas do Grau A e do Grau B e retorne o resultado do grau final.

def mediaUnisinos(grauA, grauB):
    media = (grauA + grauB * 2) / 3
    return media

# 4. Implemente uma função sorteio que receba o intervalo de valores inteiros início e fim como parâmetro e sorteie um número dentro do intervalo (considerando intervalo fechado [início, fim])

import random
def sorteio(inicio, fim):
    n = random.randint(inicio, fim)
    return n

# 5. Utilizando o template de menus mostrado em aula, faça um programa que simule uma calculadora simples, mostrando ao usuário as opções somar, subtrair, multiplicar e dividir dois números reais. Cada 
# uma das operações deve ser executada em funções que recebam como parâmetro os dois números, lidos do usuário. As funções devem retornar o resultado para o programa principal, que o exibirá na tela. 
# OBS.: Apenas chame a função de dividir se o divisor for diferente de zero (divisão por zero não existe!).

def menu():
    print('1 - Somar')
    print('2 - Subtrair')
    print('3 - Multiplicar')
    print('4 - Dividir')
    print('0 - Sair\n')
    item = input('Escolha uma opção: ')
    return item

def Somar(x, y):
    print('\nOpção escolhida: 1\n')
    print(x + y)

def Subtrair(x, y):
    print('\nOpção escolhida: 2\n')
    print(x - y)

def Multiplicar(x, y):
    print('\nOpção escolhida: 3\n')
    print(x * y)

def Dividir(x, y):
    print('\nOpção escolhida: 4\n')
    if y != 0:
        print(x / y)
    else:
        print("Divisão por zero não existe!")

escolha = ''
while escolha != '0':
    escolha = menu()
    if escolha != '0':
        x, y = map(int, input("Insira dois valores: ").split())
        if escolha == '1':
            Somar(x, y)
        elif escolha == '2':
            Subtrair(x, y)
        elif escolha == '3':
            Multiplicar(x, y)
        elif escolha == '4':
            Dividir(x, y)
        else:
            print('\nOpção desconhecida!\n')
        input('Pressione ENTER para continuar')
    else:
        print('\nSaindo...\n')


# 6. Utilizando o template de menus mostrado em aula, faça um programa que simule um sistema de lootbox simples. As opções para o usuário são abrir uma caixa e consultar itens coletados. Ao abrir uma caixa, o
# usuário irá receber 1 item comum, raro ou lendário, conforme a probabilidade da tabela abaixo:
# Tipo de item Probabilidade de obtenção
# Comum 80 %
# Raro 19%
# Lendário 1%

# Ao obter o item, deverá se atualizar o inventário do jogador contabilizando o número de itens comuns,
# raros e lendários que ele possui. Ao consultar os itens coletados, deverá ser mostrado ao usuário a
# quantidade de itens de cada tipo que ele possui.
# Exemplos de tela:
# 1 – Abrir uma caixa
# 2 – Consultar itens
# 0 - Sair

# Escolha uma opção: 1
# Você coletou 1 item comum!
# 1 – Abrir uma caixa
# 2 – Consultar itens
# 0 - Sair
# -----
# Escolha uma opção: 2
# Itens comuns: 9
# Itens raros: 2
# Itens lendários: 0

itemComum = 0
itemRaro = 0
itemLendario = 0

def abrirCaixa():
    global itemComum, itemRaro, itemLendario  # Declarando as variáveis como globais
    prob = random.randint(1, 100)
    if prob <= 80:
        print("Você coletou 1 item comum!")
        itemComum += 1
    elif prob <= 99:
        print("Você coletou 1 item raro!")
        itemRaro += 1
    else:
        print("Você coletou 1 item lendário!")
        itemLendario += 1
    
def Consultar():
    print("Itens comuns:", itemComum)
    print("Itens raros:", itemRaro)
    print("Itens lendários:", itemLendario)

def menu():
    print()
    print("1 - Abrir uma caixa")
    print("2 - Consultar itens")
    print("0 - Sair")
    escolha = input('Escolha uma opção: ')
    return escolha

while True:
    escolha = menu()
    if escolha == "1":
        abrirCaixa()
    elif escolha == "2":
        Consultar()
    elif escolha == "0":
        print("Saindo...")
        break
    else:
        print("Opção inválida! Por favor, escolha uma opção válida.")
