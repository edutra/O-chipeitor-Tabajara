import math
import random
import sys

matriz = []
size = 0
fios = []

#dicionario = {0: (0, 0), 1: (0, 1), 2: (0, 2), 3: (0, 3), 4:(1, 0), 5:(1, 1), 6:(1, 2), 7: (1, 3), 8:(2, 0)}


def gera_matriz(size):
    global matriz
    posicao = (0, 0)
    for x in range(size**2):

        matriz.append(posicao)
        posicao = pula_um(posicao[0], posicao[1])

    #print(matriz)

def distance(x1, y1, x2, y2):
    return math.sqrt((x1 - x2)**2 + (y1 - y2)**2)

def pula_um(x, y):
  #  print(y)
    global size
    if(y ==  size-1):
        return (x+1, 0)
    else:
        return (x, y+1)
def calcula_dist_tudo(aux):
    
    soma = 0
    for x in fios:
        
        #print(aux[x[0]])
        primeiro_chip = aux[x[0]]
        
        segundo_chip = aux[x[1]]
     #   print(primeiro_chip)
     #   print(segundo_chip)
        

        soma = soma + distance(primeiro_chip[0], primeiro_chip[1], segundo_chip[0], segundo_chip[1])

    return soma
def inverte_uma_parte():
    global matriz
    aux = matriz.copy()
    #print("antes")
    #print(aux)
    valor1 = random.randint(0, int(len(matriz)/2))
    valor2 = random.randint(valor1, len(matriz))
    if valor2 == valor1:
        valor2 = valor2+1
    #print("==============================================")
    #print(valor1)
    #print(valor2)
    parte = aux[valor1:valor2].copy()
    #print(parte)
    parte = parte[::-1]
    aux = aux[:valor1] + parte.copy() + aux[valor2:]
    #print("depois")
    #print(aux)
    
    #aux = aux[len(aux)/2:] + aux[:len(aux)/2]  
    dist_aux = calcula_dist_tudo(aux)
    dist_dic = calcula_dist_tudo(matriz)

   # print(dist_aux)
   # print(dist_dic)
   # print("--------------")
    if(dist_aux <= dist_dic):
        #print("True")
        return aux.copy()
   # print(dicionario) 
    return matriz.copy()

def inverte_diagonal():
    global matriz
    aux = matriz.copy()

    valor = random.randint(0, len(aux)-1)

    for x in range(len(aux) - 1):
        if (aux[x][0] == aux[valor][0]-1 or aux[valor][0] + 1 == aux[x][0]) and (aux[x][1] == aux[valor][1]-1 or aux[valor][1] + 1 == aux[x][1]):
            aux[x], aux[valor] = aux[valor], aux[x]

    dist_aux = calcula_dist_tudo(aux)
    dist_dic = calcula_dist_tudo(matriz)

   # print(dist_aux)
   # print(dist_dic)
   # print("--------------")
    if(dist_aux <= dist_dic):
        #print("True")
        return aux.copy()
   # print(dicionario) 
    return matriz.copy()



def troca_os_canto():
    global matriz
    aux = matriz.copy()
    
    for x in aux:
        if(x == (0,0)):
            x = (int(math.sqrt(len(matriz)) -1), int(math.sqrt(len(matriz)) -1))
        elif(x == (0, int(math.sqrt(len(matriz)) -1))):
            x = (0, 0)
        elif(x == (int(math.sqrt(len(matriz)) -1), 0)):
            x = (int(math.sqrt(len(matriz)) -1), 0)
        elif(x == (int(math.sqrt(len(matriz)) -1), int(math.sqrt(len(matriz)) -1))):
            x = (0, int(math.sqrt(len(matriz)) -1))


    dist_aux = calcula_dist_tudo(aux)
    dist_dic = calcula_dist_tudo(matriz)

    if(dist_aux <= dist_dic):

        return aux.copy()

    return matriz.copy()

def inverte_coluna():
    global matriz

    aux = matriz.copy()
    coluna = random.randint(0, int(math.sqrt(len(aux))-1))
    dicionario_aux = {}
    for x in range(len(aux) -1):
        if(aux[x][0] == coluna):
            dicionario_aux[x] = aux[x]
    i = int(math.sqrt(len(matriz)) -1)
    for x in dicionario_aux:
        aux[x] = (i, coluna)
        i = i - 1

    dist_aux = calcula_dist_tudo(aux)
    dist_dic = calcula_dist_tudo(matriz)


    if(dist_aux <= dist_dic):

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
        print("Random")
        aux = random_swap()
    elif choose == 1:
        print("inverte linha")
    
        aux = inverte_linha()
    elif choose == 2:
        print("inverte coluna")
        aux = inverte_coluna()
    elif choose == 3:
        print("troca diagonal")
        aux = inverte_diagonal()
    elif choose == 4:
        print("troca metade")
        aux = inverte_uma_parte()
    else:
        print("troca canto")
        aux = troca_os_canto()

    return aux

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

   
    while(0 == 0):

        
        aux = modificador()
        print(calcula_dist_tudo(matriz))    

     
        matriz = aux.copy()
     



main()
