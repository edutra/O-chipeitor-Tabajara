import math
import random
import sys

matriz = []
size = 0
fios = []



# Reponsavel por popular a matriz com a coordenada de cada chip.
# A matriz gerada possui apenas uma dimensão
# O indice (0 até len(matriz) -1 ) representa o "nome" de cada componente
# o conteúdo da matriz é a posição (i, j) de cada componente.
def gera_matriz(size):
    global matriz
    
    posicao = (0, 0)
    for x in range(size**2):

        matriz.append(posicao)
        posicao = pula_um(posicao[0], posicao[1])
    

# Calcula a distancia euclidiana entre 2 coordenadas
# x1, y1 representam a posição de um componente
# x2, y2 também
def distance(x1, y1, x2, y2):
    return math.sqrt((x1 - x2)**2 + (y1 - y2)**2)


# Funçãozinha para auxiliar na criação da matriz
def pula_um(x, y):
    global size
    if(y ==  size-1):
        return (x+1, 0)
    else:
        return (x, y+1)

# calcula o comprimento total dos fios que conectam os componentes
def calcula_dist_tudo(aux):
    
    soma = 0
    for x in fios:
        
        primeiro_chip = aux[x[0]]
        segundo_chip = aux[x[1]]

        soma = soma + distance(primeiro_chip[0], primeiro_chip[1], segundo_chip[0], segundo_chip[1])

    return soma


# Seleciona, aleatoriamente, dois valores.
# Pega a parte do array entre esses dois valores, e inverte.
def inverte_uma_parte():
    global matriz
    aux = matriz.copy()
    
    valor1 = random.randint(0, len(matriz)-2)
    valor2 = random.randint(valor1, len(matriz)-1)
    if valor2 == valor1:
        valor2 = valor2+1
    
    parte = aux[valor1:valor2].copy()
    
    parte = parte[::-1]
    aux = aux[:valor1] + parte.copy() + aux[valor2:]

    dist_aux = calcula_dist_tudo(aux)
    dist_dic = calcula_dist_tudo(matriz)

    if(dist_aux < dist_dic):
        
        return aux.copy()
    
    return matriz.copy()


# Seleciona um indice, aleatoriamente
# Troca o valor o valor deste indice por um valor que estaria na sua diagonal, caso o array fosse 2D

# matriz[3], por exemplo, é igual (2, 3)
# Essa função vai procurar pelos indices que possuem valor igual a (1, 3), (3, 3), (2, 4) ou (3, 4), e vai inverter, por exemplo, matriz[3], matriz[x] = matriz[x], matriz[3]
# tal que o valor de matriz[x] é um destes "(1, 3), (3, 3), (2, 4) ou (3, 4)"
def inverte_diagonal():
    global matriz
    aux = matriz.copy()

    valor = random.randint(0, len(aux)-1)

    for x in range(len(aux) - 1):
        # Compara pra ver se fica na diagonal
        if (aux[x][0] == aux[valor][0]-1 or aux[valor][0] + 1 == aux[x][0]) and (aux[x][1] == aux[valor][1]-1 or aux[valor][1] + 1 == aux[x][1]):
            aux[x], aux[valor] = aux[valor], aux[x]

    dist_aux = calcula_dist_tudo(aux)
    dist_dic = calcula_dist_tudo(matriz)

   
    if(dist_aux < dist_dic):
        
        return aux.copy()
   
    return matriz.copy()


# Troca os componentes que se localizam nos extremos (0, 0), (0, tamanho de um lado), (tamanho de um lado, 0), (tamanho_lado, tamanho_lado)
def troca_os_canto():
    global matriz
    aux = matriz.copy()
    
    for x in aux:
        if(x == (0,0)):
            x = (int(math.sqrt(len(matriz)) -1), 0)
        elif(x == (0, int(math.sqrt(len(matriz)) -1))):
            x = (0, 0)
        elif(x == (int(math.sqrt(len(matriz)) -1), 0)):
            x = (int(math.sqrt(len(matriz)) -1), int(math.sqrt(len(matriz)) -1))
        elif(x == (int(math.sqrt(len(matriz)) -1), int(math.sqrt(len(matriz)) -1))):
            x = (0, int(math.sqrt(len(matriz)) -1))


    dist_aux = calcula_dist_tudo(aux)
    dist_dic = calcula_dist_tudo(matriz)

    if(dist_aux < dist_dic):

        return aux.copy()

    return matriz.copy()



def remonta_coluna_invertida():
    global matriz
    
    aux = matriz.copy()
    
    coluna = random.randint(0, int(math.sqrt(len(aux))-1))
    dicionario_aux = {}
    for x in range(len(aux) -1):
        if(aux[x][1] == coluna):
            dicionario_aux[x] = aux[x]
    i = int(math.sqrt(len(matriz)) -1)
    for x in dicionario_aux:
        
        aux[x] = (i, coluna)
        i = i - 1

    distancianova = calcula_dist_tudo(aux)
    distanciavelha = calcula_dist_tudo(matriz)


    if(distancianova < distanciavelha):

        return aux.copy()

    return matriz.copy()

def inverte_linha():
    global matriz
    
    aux = matriz.copy()
    linha = random.randint(0, int(math.sqrt(len(aux))-1))
    dicionario_aux = []
    for x in range(len(aux) -1):
        if(aux[x][0] == linha):
            dicionario_aux.append((x, aux[x]))
    
    i = 0
    for x in dicionario_aux:
        aux[x[0]] = (linha, dicionario_aux[len(dicionario_aux) -1 - i][1][1])
        i = i + 1
    
    dist_aux = calcula_dist_tudo(aux)
    dist_dic = calcula_dist_tudo(matriz)

    if(dist_aux <= dist_dic):

        return aux.copy()

    return matriz.copy()

def random_swap():
    global matriz
    global size
    aux = matriz.copy()
    x, y = random.randint(0, size-1), random.randint(0, size-1)

    aux[x], aux[y] = aux[y], aux[x]

    dist_aux = calcula_dist_tudo(aux)
    dist_dic = calcula_dist_tudo(matriz)

    if(dist_aux < dist_dic):

        return aux.copy()

    return matriz.copy()



    
def modificador():
    choose = random.randint(0, 5)
    aux = []
    if choose == 0:
      #  print("Random")
        aux = random_swap()
    elif choose == 1:
      #  print("inverte linha")
    
        aux = inverte_linha()
    elif choose == 2:
       # print("inverte coluna")
        aux = remonta_coluna_invertida()
    elif choose == 3:
        #print("troca diagonal")
        aux = inverte_diagonal()
    elif choose == 4:
        #print("troca metade")
        aux = inverte_uma_parte()
    else:
        #print("troca canto")
        aux = troca_os_canto()

    return aux.copy()

def _1d_to_2d(arr):
    array_aux = arr.copy()

    side_size = int(math.sqrt(len(array_aux)))

    matrix =  [[0 for x in range(side_size)] for y in range(side_size)]
    #print(array_aux)
    for x in range(len(array_aux)):
        
        matrix[array_aux[x][0]][array_aux[x][1]] = x
    

    return matrix.copy()



    

def main():
    global size
    global matriz  
    global fios

    
    filename = sys.argv[1]

    arq = open(filename, "r")
    text = arq.readline()
    
    text = text.split()

    size = int(text[0])
    conexoes = int(text[1])
    for x in range(size):
        text = arq.readline()

    

    aux_fios = []
    for x in range(conexoes):
        text = arq.readline()
        text = text.split()
        aux_fios.append( ( int(text[0])  , int(text[1]) ) )

    

    fios = aux_fios.copy()
    
    gera_matriz(size)
    
    i = 0
   
    while(0 == 0):

        
        aux = modificador()
        

     
        matriz = aux.copy()
        #print(f"Tamanho total = {calcula_dist_tudo(matriz)} \n {_1d_to_2d(matriz.copy())}", end="\r")
        print(f"Tamanho total = {calcula_dist_tudo(matriz)}", end="\r")
        

        i = i + 1

main()
