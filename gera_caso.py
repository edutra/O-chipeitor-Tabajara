import random

#print("Qual o valor de n?")
tamanho = input()
#print("Quantos fios vai ter?")
qtd_fios = input()
tam_int = int(tamanho)
qtd_fios_int = int(qtd_fios)
arr = ""
fios = ""
#arr não importa
for x in range(tam_int -1):
    arr = arr + "0  \n"

arr = arr + "0"
for x in range(qtd_fios_int):
    #x = 
    fios = fios + str(random.randint(0, tam_int)) + " " + str(random.randint(0, tam_int)) + "\n"


print(tamanho + " " + qtd_fios)
print(arr)
print(fios)
