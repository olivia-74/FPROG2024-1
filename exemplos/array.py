#matrizes
# matriz 3x4
M = [ [1 , 2, 3, 4], #0
      [5, 6, 7, 8], #1
      [9, 10, 11]] #2

#numero de elementos da lista
print(len(M))

#percorrer
for l in range (nLinhas):
    for c in range(nColunas):
        print(M[l],[c], end=' ')
    print()

#primeiro elemento da primeira linha:
print(M[0][0])

#segundo elemento da terceira linha:
print(M[2][1])

#ultimo elemento da segunda linha:
print(M[1][3])
print(M[1][-1])