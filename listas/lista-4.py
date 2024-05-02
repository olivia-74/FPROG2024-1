# 1. Faça um algoritmo para:
#   a. Gerar e escrever todos os números inteiros do intervalo [0,100].
n = 0
while n <= 100:
  print(n)
  n = n + 1

  # b. Gerar e escrever os números pares do intervalo [20,50].
n = 20
while n <= 50:
    print(n)
    n = n + 2
  
  # c. Gerar e escrever os números inteiros do intervalo [25,70] em ordem decrescente.
n = 70
while n >= 25:
    print(n)
    n = n - 1
    
  # d. Gerar e escrever os números ímpares do intervalo [25,95] em ordem decrescente.
n = 95
while n >= 25:
    print(n)
    n = n - 2
    
  # e. Ler 15 números e escrever a soma e a média dos números lidos.
soma = 0
for i in range (15):
  n = int(input("insira um numero: "))
  soma += n
media = soma/15
print("A soma é:", soma)
print("A média é:", media)


  # f. Ler 10 números inteiros e escrever a quantidade de números pares e a quantidade de números ímpares lidos.
pares = 0
impares = 0

for i in range (10):
  n = int(input("insira um numero: "))
  if n % 2 == 0:
    pares += 1
  else:
    impares += 1
  
print(f"quantidade de números pares: {pares}; quantidade de números ímpares: {impares}")


  # g. Sortear 20 números inteiros entre -10 e 10 e imprimi-los acompanhados da mensagem “POSITIVO”, “NEGATIVO”, ou “NULO”, conforme o caso. No final, imprimir a quantidade de números positivos e negativos lidos.
import random

positivos = 0
negativos = 0
nulos = 0

for i in range(20):
  n = random.randint(-10, 10)
  if n > 0:
    positivos += 1
    print(n, "positivo")
  elif n < 0:
    negativos += 1
    print(n, "negativo")
  else:
    nulos += 1
    print(n, "nulo")

print(f"{positivos} positivos; {negativos} negativos; {nulos} nulos")


  # h. Ler n números e imprimir no final a soma dos números lidos (obs.: n é a quantidade de números que deverão ser lidos e também deve ser lido do teclado)

soma = 0
n = int(input())
for i in range(n):
  n = int(input())
  soma += n
print(soma)

 
# 2. Implemente um programa que sorteia um número de 1 a 10 e dá ao usuário 3 tentativas de acertá-lo. A cada tentativa errada, o programa informa se o número a adivinhar está abaixo ou acima.

resposta = random.randint(1, 10)
tentativas = 0

while tentativas < 3:
    n = int(input("tente adivinhar o numero sorteado: "))
    if n == resposta:
        print(f"voce acertou com {tentativas} tentativas")
        tentativas = 3
    elif n > resposta:
        print(f"errou! o numero sorteado é menor que {n}")
        tentativas += 1
    elif n < resposta:
        print(f"errou! o numero sorteado é maior que {n}")
        tentativas += 1


# 3. Elabore um programa que lê um número de 1 a 9 e mostra a tabuada de multiplicação do número. Exemplo de tela de saída:
#   Entre com um número: 5
#   5 x 1 = 5
#   5 x 2 = 10
#   ...
#   5 x 10 = 50
#   Calcular outro número (s/n)? n

while True:
  n = int(input("insira um numero de 1 a 9: "))
  if n >= 1 and n <= 9:
    for i in range(11):
      print(f"{n} X {i} = {n * i}")
    resposta = input("Calcular outro número (s/n)? ")
    if resposta == "s":
      pass
    if resposta == "n":
      break
  else:
    print("sua resposta precisa ser um numero de 1 a 9")
  

# 4. Escrever um programa que calcule todos os números divisíveis por certo valor indicado pelo usuário (o resto da divisão por este número deve ser igual a zero), compreendidos em um intervalo também
# especificado pelo usuário. O usuário deve entrar com um primeiro valor correspondente ao divisor e após ele vai fornecer o valor inicial do intervalo, seguido do valor final deste intervalo. Exemplo de tela de saída:
# Entre com o valor do divisor: 3 
# Início do intervalo: 17
# Final do intervalo: 29
# Números divisíveis por 3 no intervalo de 17 a 29:
# 18 21 24 27

divisor = int(input("valor do divisor: "))
inicio = int(input("início do intervalo: "))
fim = int(input("fim do intervalo: "))

print("números divisíveis por", divisor, "no intervalo de", inicio, "a", fim, ":")
for n in range(inicio, fim + 1):
    if n % divisor == 0:
        print(n, end=" ")


# 5. Para x alunos da Unisinos, ler as notas do grau A e grau B e calcular a média considerando o sistema de notas da Unisinos. Se o aluno estiver aprovado escrever “APROVADO”. Caso contrário, ler o grau C
# e pedir qual o grau que deve ser substituído (A ou B, maiúsculo ou minúsculo), recalcular a média. Se estiver aprovado, escrever “APROVADO”, caso contrário escrever “REPROVADO”. No final escrever a média geral dos alunos.

x = int(input("insira a quantidade de alunos: "))
somaMF = 0

for i in range(x):
    print(f"aluno {i+1}")
    grauA = float(input("insira a nota do grau A: "))
    grauB = float(input("insira a nota do grau B: "))
    mediaFinal = ((grauA + grauB*2)/3)

    print(f"a média final será: {format(mediaFinal, '.2f')}")
    if mediaFinal >= 6:
        print("APROVADO")
    else:
        grauC = float(input("insira a nota do grau C: "))
        substituir = input("substituir a nota do grau A (A) ou do grau B (B)? ").upper()
        if substituir == "A":
            mediaFinal = ((grauC + grauB*2)/3)
        elif substituir == "B":
            mediaFinal = ((grauA + grauC*2)/3)
        else: 
            print("erro")
        if mediaFinal >= 6:
            print("APROVADO")
        else:
            print("REPROVADO")

    somaMF += mediaFinal

print(f"media geral dos {x} alunos: {format(somaMF/x, '.2f')}")

# 6. Crie um algoritmo que sorteie 5 valores entre 0 e 100 e depois imprima o menor, o maior e a média dos valores sorteados.

listaValores = []

for i in range(5):
    n = random.randint(0, 100)
    listaValores.append(n)

media = sum(listaValores) / 5

print("Valores sorteados:", listaValores)
print("Menor valor sorteado:", min(listaValores))
print("Maior valor sorteado:", max(listaValores))
print("Média dos valores sorteados:", media)


# 7. Descubra, dentre cinco nomes informados pelo usuário, qual o primeiro em ordem alfabética.

nomes = []
for i in range(5):
    nome = input(f"{i+1}: Insira um nome: ")
    nomes.append(nome)

nomes.sort()

print(f"primeiro nome em ordem alfabética: {nomes[0]}")


# 8. Fazer um programa que calcule e imprima o fatorial de um número fornecido pelo usuário. Repetir a execução do programa tantas até o usuário responder não. O fatorial de um número inteiro positivo é
# definido como o número multiplicado por ele menos 1, menos 2, etc até o valor 1. Por exemplo, o fatorial de 4 é 4x3x2x1=24. Exemplo de tela de saída:
# Entre com um número: 5
# O fatorial de 5 é 120
# Calcular outro número (s/n)? n

fatorial = 1
while True:
  n = int(input("Entre com um número: "))
  for i in range(1, n + 1): 
    fatorial *= i
  print(f"fatorial de {n}: {fatorial}")

  resposta = input("Calcular outro número (s/n)? ")
  if resposta == "s":
    pass
  if resposta == "n":
    break


# 9. Escrever um programa que produza a saída abaixo na tela, para n linhas e usando um caractere lido do teclado.
# Exemplo de tela de saída, para n = 5 e caracter = `*`:
# Entre com um número: 5
# Entre com um caracter: *
# *
# * *
# * * *
# * * * *
# * * * * *

n = int(input("Entre com um número: "))
c = input("Entre com um caractere: ")

for i in range(1, n + 1):
    for j in range(i):
        print(c, end=" ")

