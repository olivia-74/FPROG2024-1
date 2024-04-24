import os
import random

# 1. Faça uma função que verifique se um número inteiro é primo ou não, retornando: True ou False.

def VerificarPrimo(n):
    if n > 1:
        for i in range(2, n): #qualquer numero e divisivel por 1 e por ele mesmo
            if n % i == 0: #saber se e divisivel por algum outro numero ("o resultado será um número natural e o resto será igual a zero")
                return False
                break
            else:
                return True
    else:
        return False
    
# print(VerificarPrimo(10))

# 2. Faça um programa que leia números inteiros até que o usuário digite 0. No final, imprima a porcentagem de números positivos, negativos, divisíveis por 2, divisíveis por 5 e números primos lidos.

pos = 0
neg = 0
div2 = 0
div5 = 0
primos = 0
total = 0

# def VerificarPrimo(n):
#     if n > 1:
#         for i in range(2, n): 
#             if n % i == 0: 
#                 return False
#                 break
#             else:
#                 return True
#     else:
#         return False

while True:
    n = int(input("Digite um número inteiro ou 0 para parar: "))
    if n == 0:
        break
    if VerificarPrimo(n):
        primos += 1 
    if n > 0:
        pos += 1 
    if n < 0:
        neg += 1 
    if n % 2 == 0:
        div2 += 1 
    if n % 5 == 0:
        div5 += 1 
    total += 1
        
os.system('cls' if os.name == 'nt' else 'clear') 
 
if total == 0:
    print("fim do programa")
else:
    print(f"positivos: {(pos / total) * 100:.2f}%")
    print(f"negativos: {(neg / total) * 100:.2f}%")
    print(f"divisíveis por 2: {(div2 / total) * 100:.2f}%")
    print(f"divisíveis por 5: {(div5 / total) * 100:.2f}%")
    print(f"primos: {(primos / total) * 100:.2f}%")

# 3. Escreva um trecho de código que verifique e mostre na tela os 10 primeiros números primos.

nPrimos = []
n = 2
while n <= 10:
    primo = True
    for i in range(2, n):
        if n % i == 0:
            primo = False
            break
    if primo:
        nPrimos.append(n)
    n += 1 
print(' '.join(map(str, nPrimos))) # mapeia e converte cada elemento da lista em strings para poder juntar elas usando join

# 4. Faça um programa que sorteie um   número de 1 a 10 e peça para o usuário tentar adivinhar. O usuário tem 3 chances de acertar. Indique se o usuário acertou ou errou a cada tentativa.

sorteio = random.randint(1, 10)

print("tente adivinhar o numero sorteado")

for i in range (3):
    vez = i + 1
    tentativa = int(input(f"tentativa {vez}: " ))
    if tentativa == sorteio:
        print(f"parabens! voce acertou na {vez} tentativa")
    else:
        print("errou!")
    if vez == 3:
        print("o numero sorteado era", sorteio)

#  3) Faça um programa que simule uma máquina de café e permita, através de um menu principal, executar as funções descritas nos itens (a, b, c e d)abaixo, e só termine quando o usuário escolhe a função desligar (d). A máquina prepara 3 opções de café: preto, com leite e cappuccino. Dentro dela, ela possui 4 compartimentos que armazenam até 1kg/1l dos ingredientes: café, água, leite e mistura para cappuccino. Cada compartimento recebe um refil de 1kg (sólidos) ou 1l (líquidos) dos ingredientes, e a máquina possui medidores eletrônicos que estimam a quantidade existente de cada um deles. Portanto, a qualquer momento, ela pode mostrar quanto ainda resta de cada um deles. As ações que podem ser feitas com a máquina são: 
    # a) Trocar o refil, indicando como parâmetro qual o tipo de ingrediente que deve ter o compartimento preenchido. Após fazer a troca, o compartimento fica com a quantidade máxima do produto.
    # b) Consultar a quantidade de um ingrediente. Para isso, é necessário informar como parâmetro o tipo do ingrediente e a máquina retorna no visor a quantidade dele.
    # c) Preparar café, recebendo como parâmetro o tipoIng do café (preto, com leite ou cappuccino) e o pagamento (os cafés custam R$1,00, R$1,50 e R$2,00, respectivamente) e retornando a bebida (em nosso programa, apenas uma mensagem na tela: CAFÉ PRONTO, RETIRE SUA BEBIDA!) e o troco correto do cliente. A compra é bem-sucedida (faz a bebida e retorna o troco, se necessário) se o pagamento fornecido para a opção for maior ou igual ao preço do café e:
        # i. Para a compra do café preto, houver 15g de café e 250ml de água na máquina
        # ii. Para a compra do café com leite, houver 20g de café e 250ml de leite na máquina
        # iii. Para a compra do cappuccino, houver 40g de mistura de cappuccino e 300ml de água na máquina.
        # iv. Caso não exista a quantidade suficiente de algum dos ingredientes do café a ser comprado, a máquina “devolve” o pagamento do cliente e imprime o aviso: PRODUTO INDISPONÍVEL, pagamento DEVOLVIDO.
    # d) Desligar, que encerra o programa.
    # OBS.: Assuma que a máquina sempre vai ter o troco correto, não estamos levando em conta a arrecadação.
 
 
# dicionario ompartimentos
compartimentos = {
    "cafe": 1000,  
    "agua": 1000,  
    "leite": 1000,  
    "cappuccino": 1000  
}

def trocarRefil(compartimentos, tipoIng):
    if tipoIng in compartimentos:
        compartimentos[tipoIng] = 1000 #atualiza a qtd do ingrediente no dicio compartimento
        print("Pronto!")
    else:
        print("Ingrediente inválido!")

def consultarQuantidade(compartimentos, tipoIng):
    if tipoIng in compartimentos:
        return compartimentos[tipoIng] #consulta a chave e retorna o valor ("chave": valor)
    else:
        print("Ingrediente inválido!")

def prepararCafe(compartimentos, tipoCafe, pagamento):
    preco = 0
    if tipoCafe == "1":
        tipoCafe = "preto"
        preco = 1.00
        if compartimentos["cafe"] >= 15 and compartimentos["agua"] >= 250: #verifica se tem qtd suficiente
            compartimentos["cafe"] -= 15 #atualiza o valor no dicionario
            compartimentos["agua"] -= 250
        else:
            print("Produto indisponível, dinheiro devolvido.")
            return
    elif tipoCafe == "2":
        tipoCafe = "com leite"
        preco = 1.50
        if compartimentos["cafe"] >= 20 and compartimentos["leite"] >= 250:
            compartimentos["cafe"] -= 20
            compartimentos["leite"] -= 250
        else:
            print("Produto indisponível, dinheiro devolvido.")
            return
    elif tipoCafe == "3":
        tipoCafe = "cappuccino"
        preco = 2.00
        if compartimentos["cappuccino"] >= 40 and compartimentos["agua"] >= 300:
            compartimentos["cappuccino"] -= 40
            compartimentos["agua"] -= 300
        else:
            print("Produto indisponível, dinheiro devolvido.")
            return
    else:
        print("Opção de café inválida!")
        return

    if pagamento >= preco:
        troco = pagamento - preco
        print("Café pronto, retire sua bebida!")
        print("Troco: R$", troco)
    else:
        print("Pagamento insuficiente, pagamento devolvido.")

def main():
    while True: #loop ate desligar
        acao = input("\nMenu: \n1- Trocar o refil \n2- Consultar a quantidade de um ingrediente \n3- Preparar café \n4- Desligar \nInsira o número correspondente à ação que deseja realizar: \n")
        
        if acao == "1":
            refil = input("compartimento a preencher:\n1- Café\n2- Água\n3- Leite\n4- Cappuccino\nOpção: ")
            if refil in ["1", "2", "3", "4"]:
                tipoIng = ["cafe", "agua", "leite", "cappuccino"]
                trocarRefil(compartimentos, tipoIng[int(refil) - 1])
            else:
                print("Opção inválida!")

        elif acao == "2":
            consulta = input("ingrediente a consultar:\n1- Café \n2- Água \n3- Leite \n4- Cappuccino \nOpção: ")
            if consulta in ["1", "2", "3", "4"]: #verifica se o input ta na lista de possibilidades
                tipoIng = ["cafe", "agua", "leite", "cappuccino"] #lista de ingredientes
                print("Quantidade:", consultarQuantidade(compartimentos, tipoIng[int(consulta) - 1]))
            else:
                print("Opção inválida!")

        elif acao == "3":
            cafe = input("café desejado: \n1- Preto \n2- Com leite \n3- Cappuccino \nOpção: ")
            pagamento = float(input("Pagar com (valor): "))
            if cafe in ["1", "2", "3"]:
                prepararCafe(compartimentos, cafe, pagamento) #puxa a funcao que verifica e atualiza as quantidades
            else:
                print("Opção inválida!")
                
        elif acao == "4":
            print("Desligando...")
            break
        else:
            print("Opção inválida, tente novamente.")

main()


    





