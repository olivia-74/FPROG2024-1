# 1. (4.0 pt) Correção de provas objetivas: faça um programa que permita cadastrar um vetor com o gabarito de uma prova objetiva contendo 10 questões, cujos resultados podem ser de ‘a’ a ‘f’ (veja exemplo abaixo). Depois disso, permita ao usuário a opção de entrar com as respostas dadas por um estudante. 
#     a) Contabilizar o número de respostas certas e dar a pontuação final, de 0 a 10
#     b) Durante o processo de correção, imprimir na tela quais questões foram acertadas e quais o estudante errou. Neste caso, deve-se imprimir a resposta correta. 

gabarito =  ['a', 'f', 'c', 'd', 'd', 'a', 'e', 'e', 'b', 'a']
respostasEstudante = ['a', 'f', 'a', 'd', 'f', 'a', 'e', 'e', 'c', 'a']
pontuacao = 0

for i in range(len(gabarito)):
    if respostasEstudante[i] == gabarito[i]:
        print(f'Questão {i+1}: resposta correta.')
        pontuacao += 1
    else:
        print(f'Questão {i+1}: resposta incorreta. A resposta correta é {gabarito[i]}.')

print(f'A pontuação do estudante é {pontuacao}/{len(gabarito)}')

# 2. (6.0 pts) Batalha naval simplificada (apenas 1 jogador): considere um programa de jogo de batalha naval
# para 1 jogador, que possui um tabuleiro 8x8 onde devese alocar 5 navios (1 porta-aviões, 1 navio de 4 canos, 1
# navio de 3 canos, 1 navio 2 canos e um submarino). A figura abaixo mostra como seria a estrutura do tabuleiro
# e uma possível configuração dos navios. O programa deve permitir, no início, a entrada da matriz
# com a configuração dos navios. Vamos chamá-la de matriz de controle. Depois disso, na tela, deve-se exibir o tabuleiro apenas
# com quadrados vazios (ou algum caractere indicativo). Esta será a matriz de exibição, que deverá ser atualizada
# em cada jogada. Enquanto o jogador não tiver acertado todos os navios, ele precisa dizer a posição de um
# quadrado do tabuleiro, da maneira como mostra a figura (por exemplo “A 5”).
# O programa verifica na matriz de controle se aquela posição possui algum navio ou não, e mostra para jogador o que possui naquela posição 
# (atualizando a matriz de exibição). Se possui um navio, o programa ainda escreve na tela uma onomatopeia de explosão 
# (exibe uma mensagem "BOOOM" na tela). Se não possui, ele exibe um som de “SPLASH” na água. 
# No momento que um navio todo foi atingido, o programa toca um som de navio afundando (mensagem "GLUB GLUB GLUB"). 
# Ao final(quando o jogador acertou todos os navios), ele mostra o número de jogadas e parabeniza o jogador.

def batalhaNaval():
    a


tabuleiro = []

# Ler do usuário o nro de linhas e colunas que a matriz terá
nLinhas = random.randint(1, 10)  #int(input('Digite o nro de linhas: '))
nColunas = random.randint(1, 10) #int(input('Digite o nro de colunas: '))

for l in range(nLinhas):
    novaLinha = []
    for c in range(nColunas):
        novoValor = random.randint(0, 100)
        novaLinha.append(novoValor) #adicionando o novo valor na linha auxiliar (nova linha)
    tabuleiro.append(novaLinha)

imprimirMatriz(tabuleiro)
print()