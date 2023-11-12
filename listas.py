# > LISTAS

# ANTES
nota1 = 7.9
nota2 = 9.7
nota3 = 8.2

# com lista 
notas = [7.9, 9.7, 8.2]



# criando listas 
lista = []
lista = list()
lista = [26, "rodrigo", 3.14159, False]
lista_de_listas = [10, [1, 2, 3]]

# indexacao e slices ( fatiamento )

lista = [10, "rodrigo", 3.14159, True] 

print(lista[0])
print(lista[1])
print(lista[2])
print(lista[3])
print(lista[-1])
# slices 

lista = [10, 50, 30, 40, 25, 60, 5]

print(lista[0:3])    # intervalo de 03 numeros 
print(lista[3:6])    # intervalo de 3 a 6
print(lista[3:])     # intervalo de 3 ate o final da tabela
print(lista[2:6:2])  # intervalo de 02 numeros ate o maximo de 06  

# interações com FOR

# 1. utilizando os proprios elementos da lista 

for elemento in lista:
    print(elemento)

# 2. utlizando os indices 

print("Comprimento da lista:", len(lista))

for i in range(len(lista)):
    print(lista[i])
    
# metodos de lista 

lista = [1, 3, 12, 8, 2]    

# append

print("Antes do append:", lista)

lista.append(3)

print("Depois do append:", lista)

# insert 

lista.insert(2, 10)

print("Depois do insert:", lista)


# extend

lista2 = [1, 2, 3]    

lista.extend(lista2)

print("Depois do extend:", lista)

# pop

lista.pop() # lista vazia elimina o ultimo elemento

print("Lista após o pop:", lista)

lista.pop(0) # elimina o elemento na posicao 0 

print("Lista após o pop:", lista)


# remove

lista.remove(3) # remove o primeiro elemento 3 que ele encontrar 

print("Depois do remove:", lista)


# count

print("Quantidade de 2 na lista:", lista.count(2)) # junta a lista e lista2 

# index 

print("Indice do elemento 12:", lista.index(12)) # diz em qual posicao o elemento 12 está 

# sort 

lista.sort() # coloca a lista em posicao crescente 

print(lista)

lista.sort(reverse=True) #  coloca a lista em posicao decrescente

print(lista)

# funçoes para listas 


# 1. len 

print(len(lista))

# 2. sun

print(sum(lista))

# max

print("Maior elemento da lista:", max(lista))

# 3. min

print("Menor elemento da lista:", min(lista))





