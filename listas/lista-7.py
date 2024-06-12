import random

# 1. Dados os vetores v1 = [1,5,9,2,5], v2 = [7,4,13,21,6] e v3 = [8, −3,5,7,12], faça um programa que copie o conteúdo dos vetores dados para uma matriz de tamanho 3x5 de forma a obter o seguinte resultado:
M = []
v1 = [1, 5, 9, 2, 5]
v2 = [7, 4, 13, 21, 6]
v3 = [8, -3, 5, 7, 12]

M.append(v1)
M.append(v2)
M.append(v3)

for l in range(3):
    for c in range(5):
        print(M[l][c], end=' ')
    print('')


# 2. Faça a multiplicação de todos os elementos da matriz acima por 7
print(' ') # so pra separar no terminal
for l in range(3):
    for c in range(5):
        M[l][c] *= 7
        print(M[l][c], end=' ')
    print()
    

# 3. Matriz identidade, na matemática, também conhecida como matriz 𝐼𝐼 ou matriz unitária, é uma matriz quadrada em que a diagonal principal contém apenas elementos 1 (um) e todos os outros elementos são 0 (zero). Crie uma função que gere uma matriz identidade 4x4

# cria a matriz 4x4 so com 0s
MI = [[0 for i in range(4)] for i in range(4)]

 # define 1 a cada linha/coluna i
for i in range(4):
    MI[i][i] = 1
    
for l in range(4):
    for c in range(4):
        print(MI[l][c], end=' ')
    print()

# 4. Escreva um algoritmo que preenche uma matriz 4x6 com valores inteiros aleatórios entre -10 e 10. 

M = [[random.randint(-10, 10) for i in range(6)] for i in range(4)]

for l in range(4):
    for c in range(6):
        print(M[l][c], end=' ')
    print()

#    Calcule as somas:
    # a. dos elementos da segunda linha
print(sum(M[1]))

    # b. dos elementos da quinta coluna
print(sum(l[4] for l in M))

    # c. da multiplicação dos elementos da primeira linha pelos elementos da quarta linha
print(sum(M[0][c] * M[3][c] for c in range(6)))
   
    # d. dos elementos só das colunas com índices pares
print(sum(sum(M[l][c] for l in range(4)) for c in range(0, 6, 2)))
    
    # e. dos elementos só das linhas com índices ímpares
print(sum(sum(M[l][c] for c in range(6)) for l in range(1, 3, 5)))

# 5. Encontre o maior e o menor valor da matriz gerada no exercício anterior.
maior = float('-inf')   
menor = float('inf')    

for l in M:
    for i in l:
        if i > maior:
            maior = i
        if i < menor:
            menor = i

print(f"maior valor: {maior}. menor valor: {menor}")


# 6. Gere uma matriz 10x3 que contenha valores de notas de 10 alunos (cada linha contém a informação das notas de um aluno). Para isso, sorteie valores entre 0.0 e 10.0 na primeira e segunda colunas, e na terceira, calcule a média da Unisinos considerando as notas anteriores como nota do Grau A e do Grau B.
MNotas = []
for i in range(10):
    grauA = random.uniform(0.0, 10.0)
    grauB = random.uniform(0.0, 10.0)
    media = ((grauA + grauB*2)/3)
    MNotas.append([grauA, grauB, media])

for l in range(10):
    for c in range(3):
        print(f"{MNotas[l][c]:.1f}", end=' ')
    print()


# 7. Faça um programa que gere uma matriz de inteiros 5x5 e que transforme os números negativos em positivos e vice-versa. 
M = []
for i in range(5):
    l = [random.randint(-10, 10) for i in range(5)]
    M.append(l)

for l in range(5):
    for c in range(5):
        print(M[l][c], end=' ')
    print()

print( )

for i in range(len(M)):
    for j in range(len(M[i])):
        M[i][j] = -M[i][j]
        

for l in range(5):
    for c in range(5):
        print(M[l][c], end=' ')
    print()