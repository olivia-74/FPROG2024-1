# 10/04

def funcaoComParametros(p1, p2, p3):
    print("p1: ", p1)
    print("p2: ", p2)
    print("p3: ", p3)

funcaoComParametros(1, 2, 3)
funcaoComParametros(1, 2.2, "C")

a = "oie"
b = input("digite:")

funcaoComParametros(a,b,True)

def cumprimentar (nome):
    print ("ola", nome)
    
# nome1 = input("nome: ")
# cumprimentar(nome1)

# nome2 = input("nome: ")
# cumprimentar(nome2)
qtd = int(input("quantidade de usuarios: "))
for i in range(qtd):
    print("ola usuario", i+1, end ="")
    nome = input(", digite seu nome ")
    cumprimentar(nome)
    
    
def tabuada(n):
    for i in range(1, 11):
        print(n, "x", i, "=", n * i)

for i in range(1, 11):
    tabuada(i) 
    print("")

def musicaElefantes(n):
    for i in range(1, n):
        print(i, "daniel incomoda muita gente, ")
        print(i+1, "daniel ", end="")
        for j in range(0, i+1):
            print("incomodam, ", end="")
        print("muito mais")
        
musicaElefantes(10)


def mediaUnisinos(grauA, grauB):
    media = (grauA + 2*grauB) / 3 
    return media
    
    grauA = float(input("grau A: "))
    grauB = float(input("grau B: "))
    grauFinal = mediaUnisinos(grauA,grauB)
    print("grau final é ", grauFinal)






