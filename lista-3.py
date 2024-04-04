# 1) Escreva um programa que leia dois números e efetue uma divisão, mas somente se o divisor for diferente de zero; quando isto ocorrer, é mostrada uma mensagem de erro apropriada.

while True:

    dividendo = float(input("insira o valor a ser dividido: "))
    divisor = float(input("insira o valor do divisor: "))
    
    if divisor != 0:
        quociente = dividendo / divisor
        print(f"o quociente será {quociente}")
        break
    else:
        print("erro: o divisor precisa ser diferente de 0")
    

# 2) Faça um algoritmo que leia os valores A, B, C e imprima na tela se a soma de A + B é menor que A + C.
    
    A, B, C = input("Insira três valores: ").split()

    AB = A + B
    AC = A + C

    if AB < AC :
        print("A soma de A + B é menor que a soma de A + C")
    elif AB == AC : 
        print("A soma de A + B é igual a soma de A + C")
    else:
        print("A soma de A + B é maior que a soma de A + C")


# 3) Encontrar o dobro de um número caso ele seja positivo e o seu triplo caso seja negativo, imprimindo o resultado.
    valor = float(input("insira um valor: "))

    if valor > 0:
        print(f"o dobro de {valor} é {2 * valor}")
    elif valor < 0:
        print(f"o triplo de {valor} é {3 * valor}")


# 4) Crie um programa que verifica se um número inteiro informado pelo usuário é divisível por 3.

    valor = int(input("insira um valor inteiro: "))

    if valor % 3 == 0:
        print(f"{valor} é divisivel por 3")
    else:
        print(f"{valor} não é divisivel por 3")

# 5) Faça um algoritmo para receber um número qualquer do usuário e informar na tela se é par ou se é ímpar.
    
    valor = float(input("insira um valor: "))

    if valor % 2 == 0:
        print(f"{valor} é par")
    else:
        print(f"{valor} é ímpar")
        
# 6) Brincadeira do PAR ou ÍMPAR. Pergunte para o usuário se ele aposta em PAR ou ÍMPAR. Depois disso, peça para ele digitar um número de 0 a 5 (como se fosse mostrar os dedos da mão). Sorteie um número de 0 a 5 e some com o que o usuário digitou. Se o usuário escolheu PAR e o valor da soma for par OU se ele escolheu ÍMPAR e o valor da soma é ímpar, diga que ele venceu. Senão, diga que o programa venceu. 

import random
possibilidades = [0, 1, 2, 3, 4, 5]
while True:
    aposta = input("aposte par ou impar: ")
    if (aposta == "par") or (aposta == "impar"):
        valor = int(input("digite um número de 0 a 5: "))
        if 0 <= valor <= 5:
            sorteio = (random.choice(possibilidades))
            resultado = sorteio + valor
            print(f"par ou ímpar: {valor} + {resultado}")
            if resultado % 2 == 0 and aposta == "par" or resultado % 2 != 0 and aposta == "impar":
                print("você venceu")
            else:
                print("eu venci 😎😎😎😎😎😎😎😎😎")
            break
        else:
            break
    else:
        continue
    
        
# 7) Implementar um programa que calcula o desconto previdenciário de um funcionário. O programa deve, dado um salário retornar o valor do desconto proporcional ao mesmo. O cálculo de desconto segue a regra: o desconto deve 11% do valor do salário. Entretanto, o valor máximo de desconto é 318,20. Sendo assim, ou o método retorna 11% sobre o salário ou 318,20.

salario = float(input("insira seu salário: "))
desconto = salario * 0.11
maximo = 318.20

if desconto < maximo:
    print(f"será descontado {desconto} reais do seu salário")
elif desconto >= maximo:
    print(f"será descontado {maximo} reais do seu salário")


# 8) Um comerciante comprou um produto e quer vendê-lo com lucros diferentes dependendo do valor da compra. Ele quer um lucro de 45% se o valor da compra for menor que R$ 20,00, 35% se o preço for de até 50 reais e lucro de 25% se valor for maior. Entrar com o valor do produto e imprimir na tela o valor de venda.

valorCompra = float(input("insira o valor do produto: "))

if valorCompra < 20:
    lucro = 0.45
elif valorCompra < 50:
    lucro = 0.35
else:
    lucro = 0.25
    
valorVenda = (1 + lucro) * valorCompra

print(f"o valor da venda deve ser: {valorVenda}")

# 9) Faça um conversor de câmbio de reais/dólar/euro. O usuário deve informar inicialmente a cotação de cada moeda em relação ao real. Depois apresente o seguinte menu:
#     1) Converter de Real para Euro
#     2) Converter de Real para Dólar
#     3) Converter de Euro para Dólar
#     4) Converter de Euro para Real
#     5) Converter de Dólar para Euro
#     6) Converter de Dólar para Real
# Leia o valor a ser convertido na moeda de origem e imprima na tela a quantidade na moeda destino.

   realEuro = float(input("insira a cotacao do Real para o Euro: "))
realDolar = float(input("insira a cotacao do Real para o Dolar: "))
euroDolar = float(input("insira a cotacao do Euro para o Dolar: "))

print("Menu:")
print("1) Converter de Real para Euro")
print("2) Converter de Real para Dólar")
print("3) Converter de Euro para Dólar")
print("4) Converter de Euro para Real")
print("5) Converter de Dólar para Euro")
print("6) Converter de Dólar para Real")

opcao = int(input("escolha uma opcao: "))

if opcao == 1:
    valor = float(input("insira o valor em Reais: "))
    conversao = valor * realEuro
    print(f"valor em Euro: {conversao}")
    
elif opcao == 2:
    valor = float(input("insira o valor em Reais: "))
    conversao = valor * realDolar
    print(f"valor em Dólar: {conversao}")
    
elif opcao == 3:
    valor = float(input("insira o valor em Euro: "))
    conversao = valor * euroDolar
    print(f"valor em Dólar: {conversao}")
    
elif opcao == 4:
    valor = float(input("insira o valor em Euro: "))
    conversao = valor / realEuro
    print(f"valor em Reais: {conversao}")
    
elif opcao == 5:
    valor = float(input("insira o valor em Dólar: "))
    conversao = valor / euroDolar
    print(f"valor em Euro: {conversao}")
    
elif opcao == 6:
    valor = float(input("insira o valor em Dólar: "))
    conversao = valor / realDolar
    print(f"valor em Reais: {conversao}")
    
else:
    print("erro") 


# 10) Dados não precisam ser tão “quadrados”, ou cúbicos para ser mais exato. Faça um programa que simule dados de 4, 6, 8, 10, 12 ou 16 faces (apenas estes valores). Peça para o usuário informar no começo do programa quantas faces quer, para depois fazer o sorteio.

import random

while True:
    
    qtdFaces = int(input("insira a quantidade de faces do dado (4, 6, 8, 10, 12 e 16): "))
    
    if qtdFaces in [4, 6, 8, 10, 12, 16]:
        resultado = random.randint(1, qtdFaces)
        print(f"o valor sorteado foi: {resultado}")
        break
    else:
        print("quantidade de faces inválida. Escolha entre 4, 6, 8, 10, 12 e 16")



# 11) Crie um programa para informar quais e quantas notas são necessárias para entregar o mínimo de cédulas para um determinado valor informado pelo usuário considerando notas de R$ 100, R$ 50, R$ 20, R$ 10 e R$ 5 e R$ 1. Seu programa deve mostrar apenas as notas utilizadas. Por exemplo, ao solicitar R$18, o programa deve informar apenas a seguinte informação (note que não foram exibidas informações sobre as demais cédulas):
#     1 nota(s) de R$ 10.
#     1 nota(s) de R$ 5.
#     3 nota(s) de R$ 1.

valor = int(input("Digite o valor desejado: "))
arrayNotas = [100, 50, 20, 10, 5, 1]
resultado = {}

print("Notas utilizadas:")
for nota in arrayNotas:
    if valor >= nota:
        qtdNotas = valor // nota
        resultado[nota] = qtdNotas
        valor -= qtdNotas * nota
        print(f"{qtdNotas} nota(s) de R$ {nota}")


# 12) A confederação brasileira de natação irá promover eliminatórias para o próximo mundial. Fazer um algoritmo que receba a idade de um nadador e imprima a sua categoria segundo a tabela a seguir: 
#     Categoria Idade
#         Infantil A 5-7 anos
#         Infantil B 8-10 anos
#         Juvenil A 11-13 anos
#         Juvenil B 14-17 anos
#         Sênior Maiores de 18 anos

if 5 <= idade <= 7:
    categoria = "Infantil A"
elif 8 <= idade <= 10:
    categoria = "Infantil B"
elif 11 <= idade <= 13:
    categoria = "Juvenil A"
elif 14 <= idade <= 17:
    categoria = "Juvenil B"
else:
    categoria = "Sênior"

print(f"sua categoria é: {categoria}")


# 13) Faça um programa que leia a nota do Grau A e do Grau B do aluno e calcule a média final conforme as regras da Unisinos. Imprima a média final na tela e diga se o aluno passou por média ou se ficou em recuperação (grau C). Se o aluno ficou em recuperação, pergunte se ele quer substituir o Grau A ou o Grau B (ele deve digitar ‘a’ ou ‘b’). Leia a nota do Grau C, recalcule a média de acordo com o grau substituído e imprima na tela o resultado, informando se ele foi aprovado ou reprovado.

grauA = float(input("insira a nota do grau A: "))
grauB = float(input("insira a nota do grau B: "))
mediaFinal = ((grauA + grauB*2)/3)

print(f"a média final será: {format(mediaFinal, '.2f')}")

if mediaFinal >= 6:
    print("o aluno passou por media")
else:
    print("o aluno ficou em recuperacao")
    grauC = float(input("insira a nota do grau C: "))
    substituir = input("substituir a nota do grau A (A) ou do grau B (B)? ").upper()
    
    if substituir == "A":
        mediaFinal = ((grauC + grauB*2)/3)
    elif substituir == "B":
        mediaFinal = ((grauA + grauC*2)/3)
    else: 
        print("erro")
        
    if mediaFinal >= 6:
        print("media o aluno foi aprovado com média", format(mediaFinal, '.2f'))
    else:
        print("o aluno foi reprovado com média", format(mediaFinal, '.2f'))

###DUVIDA
# 14) Criar um programa para identificar o valor a ser pago por um plano de saúde dada a idade do conveniado considerando que todos pagam R$ 300 e mais um adicional (se tiver dependentes) conforme a seguinte tabela:
#     a) crianças com menos de 10 anos pagam R$100;
#     b) dependentes com idade entre 10 e 30 anos pagam R$220;
#     c) dependentes com idade entre 31 e 60 anos pagam R$ 395; e
#     d) dependentes com mais de 60 anos pagam R$ 480.

valorAdicional = 0

idadeConveniado = int(input("insira a idade do conveniado: "))
qtdDependentes = int(input("insira a quantidade de dependentes: "))

if idadeConveniado < 10:
    valorAdicional += 100
    
elif 10 <= idadeConveniado <= 30:
    valorAdicional += 220
    
elif 31 <= idadeConveniado <= 60:
    valorAdicional += 395
    
else:
    valorAdicional += 480

for i in range(qtdDependentes):
    idadeDependente = int(input(f"insira a idade do dependente {i + 1}: "))
    
    if idadeDependente < 10:
        valorAdicional += 100
        
    elif 10 <= idadeDependente <= 30:
        valorAdicional += 220
        
    elif 31 <= idadeDependente <= 60:
        valorAdicional += 395
        
    else:
        valorAdicional += 480

valorTotal = 300 + (valorAdicional * qtdDependentes)

print(f"o valor do plano de saúde sera: R${valorTotal:.2f}")


# 15) Elabore um algoritmo que calcule o que deve ser pago por um produto, considerando o preço
# normal de etiqueta e a escolha da condição de pagamento. Utilize os códigos da tabela a seguir
# para ler qual a condição de pagamento escolhida e efetuar o cálculo adequado.
#     1 - À vista em dinheiro, recebe 15% de desconto
#     2 - À vista no cartão de crédito, recebe 10% de desconto
#     3 - Em duas vezes, preço normal de etiqueta sem juros
#     4 - Em três vezes, preço normal de etiqueta mais juros de 10%
# Leia o valor a ser convertido na moeda de origem e imprima na tela a quantidade na moeda
# destino.

precoProduto = float(input("insira o preco do produto: "))

print("Formas de pagamento:")
print("1 - à vista em dinheiro")
print("2 - à vista no cartão de crédito")
print("3 - em duas vezes")
print("4 - em três vezes")

pagamento = int(input("escolha uma opcao: "))

if pagamento == 1:
    valorFinal = precoProduto * 0.85  
    
elif pagamento == 2:
    valorFinal = precoProduto * 0.90  
    
elif pagamento == 3:
    valorFinal = precoProduto  
    
elif pagamento == 4:
    valorFinal = precoProduto * 1.10  
    
else:
    valorFinal = "erro"

print(f"O valor a ser pago pelo produto é: R${valorFinal:.2f}")
