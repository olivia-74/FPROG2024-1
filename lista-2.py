# 1. Faça um algoritmo que leia uma quantidade de tempo em minutos e escreva o tempo equivalente em segundos na tela.

minutos = input("insira a quantidade de tempo em minutos: ")
segundos = minutos * 60
print(f"{minutos} minutos equivale a {segundos} segundos")


# 2. Um turista deseja comprar dólares em uma casa de câmbio. Escreva um programa que leia a cotação do dólar para real, 
# a quantidade de dólares que o turista deseja comprar, e calcule o valor total em reais que ele precisará pagar.

cotacaoDolar = float(input("cotação do Dólar para Real hoje: "))
quantidadeDolar = float(input("quantidade de Dólares desejada: "))
pagar = cotacaoDolar * quantidadeDolar
print(f"o turista deverá pagar {pagar} Reais para conseguir {quantidadeDolar} Dólares")


# 3. Um restaurante de buffet a quilo cobra R$ 40,00 por quilo. Escreva um programa que leia o peso do prato do cliente 
# e calcule o valor a ser pago.

peso = float (input ("Peso do prato do cliente kg: "))
valor = 40 * peso
print (f"o valor a ser pago é {valor}")

# 4. Faça um algoritmo que permita ao aluno calcular a sua média final na Unisinos. Leia a nota do grau A e do grau B 
# e escreva o resultado na tela. Lembrando que o Grau A vale 1/3 e o Grau B 2/3.

grauA = float(input("insira a nota do grau A: "))
grauB = float(input("insira a nota do grau B: "))
mediaFinal = ((grauA + grauB*2)/3)
print(f"a média final será: {format(mediaFinal, '.2f')}")

# 5. Um motorista deseja encher o tanque do seu carro com gasolina. Escreva um algoritmo para ler o preço do litro da 
# gasolina e o valor que o motorista tem disponível para abastecer. Calcule quantos litros ele conseguiu colocar no 
# tanque e exiba na tela.

precoGasolina = float(input("insira o preço da gasolina: "))
valorDisponivel = float(input("insira o valor disponível para abastecer: "))
qtdAbastecer = valorDisponivel/precoGasolina
print(f"é possível abastecer {qtdAbastecer:.2f} litros")

# 6. A loja de eletrônicos TechMundo vende uma certa quantidade de smartphones e uma quantidade de tablets a cada dia. 
# Cada smartphone custa R$ 1000,00 e cada tablet custa R$ 1500,00. Ao final do dia, o dono quer saber quanto arrecadou 
# com a venda dos smartphones e dos tablets. Escreva um programa que leia o número de smartphones e tablets vendidos em 
# um dia e calcule o total arrecadado.




# 7. Um criador de pássaros deseja saber a quantidade de ração diária necessária para alimentar seus pássaros. Cada 
# pássaro consome 30 gramas de ração por dia. Escreva um programa que leia o número de pássaros que o criador possui e 
# calcule a quantidade total de ração necessária por dia.


# 8. Um usuário deseja converter a temperatura de Celsius para Fahrenheit. Escreva um programa que leia a temperatura em
# Celsius e exiba a temperatura equivalente em Fahrenheit.


# 9. Durante uma liquidação uma loja resolveu dar quinze por cento de desconto nas compras feitas pelos clientes. Faça um 
# programa que leia o valor da compra e escreva o valor da compra com o desconto.


# 10. O lojista gostou tanto do seu programa anterior que encomendou outro. Dessa vez ele quer que você calcule quanto 
# cada cliente gastou na loja apenas informando o número de camisetas, calças e cintos comprados. As camisetas custam 
# R$ 25,00, as calças cem reais e os cintos 40 reais. Some o valor da compra e ao final dê um desconto de 10 por cento 
# sobre o total. Exiba na tela o valor do desconto e o valor da compra.
