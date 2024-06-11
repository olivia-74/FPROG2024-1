# arrays unidimensionais

import random

# 1. Criar um vetor de 10 números v e inicializá-lo sorteando valores de 10 a 90 para cada elemento.
v = []

for i in range(10):
    sorteio = random.randint(10, 90)
    v.append(sorteio)

# a. Imprimir o vetor
def imprimirVetor(v):
    print("Vetor:", v)
imprimirVetor(v)

# b. Verificar se existe o valor 50 neste vetor (apenas dizer se encontrou ou não)
def verificar50(v):
    if 50 in v:
        print("Existe o valor 50 neste vetor")
    else:
        print("Não existe o valor 50 neste vetor")
verificar50(v)

# c. Verificar o número de ocorrências do valor 50 neste vetor.
def contar50(v):
    print(f"Número de ocorrências do valor 50: {v.count(50)}") 
contar50(v)

# d. Calcular a média dos valores do vetor
def calcularMedia(v):
    print(f"Média dos valores do vetor: {sum(v) / len(v)}")
calcularMedia(v)

# e. Encontrar o maior e o menor valor dos elementos do vetor.
def maiorMenor(v):
    print(f"Maior valor: {max(v)}, Menor valor: {min(v)}") 
maiorMenor(v)

# f. Imprimir a soma e o produto acumulado dos valores dos elementos do vetor
def somaProduto(v):
    soma = sum(v)
    produto = 1
    for n in v:
        produto *= n
    print(f"Soma: {soma}, Produto: {produto}")
somaProduto(v)

# g. Imprimir o vetor em ordem inversa
def vetorInverso(v):
    print("Vetor inverso:", v[::-1])
vetorInverso(v)

# h. Copiar os elementos em ordem inversa para outro vetor.
def NovoVetorInverso(v):
    w = []
    for elemento in v:
        w.insert(0, elemento)
    print("Novo vetor W:", w)
NovoVetorInverso(v)

# i. Criar dois vetores vPares e vImpares com elementos pares e ímpares respectivamente
def paresImpares(v):
    pares = []
    impares = []

    for elemento in v:
        if elemento % 2 == 0:
            pares.append(elemento)
        else:
            impares.append(elemento)
    print(f"Elementos pares: {pares}, Elementos ímpares: {impares}")

paresImpares(v)

# 2. Faça um programa que leia 5 valores para dentro de um vetor e imprima o resultado de cada valor multiplicado pela sua posição no vetor. Por exemplo: 1, 2, 3, 4 e 5 imprimirá na tela 0, 2, 6, 12 e 20.
vetor = []

for i in range(5):
    valor = int(input(f"Digite o valor {i+1}: "))
    vetor.append(valor)

print("valor multiplicado pela posição:")
for i in range(len(vetor)):
    resultado = vetor[i] * i
    print(resultado)

# 3. Faça um programa para testar se um dado é viciado. Faça o lançamento N vezes (N é um número lido pelo usuário, pode ser um número bem grande), armazene cada valor que for sorteado em um array com 6 posições e ao final imprima o percentual do resultado de cada face
vetorDado = [0, 0, 0, 0, 0, 0]
nLancamento = int(input("Insira a quantidade de vezes que sera lancado o dado: "))

for i in range (nLancamento):
    vetorDado[random.randint(0,5)] += 1

for j in range (6):
    # porcentFaces.append((vetorDado[j] / nLancamento) * 100)
    print("porcentagem do resultado de cada face do dado")
    print(f"{j + 1}: {((vetorDado[j] / nLancamento) * 100):.2f}%")
