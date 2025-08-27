# diferencias de listas
lista_vacia = []
lista_numeros =[1, 2, 3, 4, 5]
listas_strings = ["manzana", "pera", "uva"]
lista_mixto = ["hola", 1, True]

# metodos basicos python
listas_strings = ["manzana", "pera", "uva"]
listas_strings.append("pera")

# agrega item a la lista segun su indice
listas_strings.insert(1, "guinda")
print(listas_strings)

#remover elemento
listas_strings.remove("manzana")
print(listas_strings)

# metodos de busqueda
numeros = [10, 20, 30, 40, 50, 30, 20]
indice = numeros.index(30)
print("El indice de 30", indice)

# para saber el total de elementos en una lista
total = len(numeros)
print(total)

# metodo de ordenaminto
ordenar_num = [60, 16, 40, 20, 15]
ordenar_num.sort() 
print("Lista ordenada ascendente", ordenar_num)
ordenar_num.sort(reverse=True)
print("Lista ordenada ascendente", ordenar_num)


###########################

# combinar listas
frutas = ["manzana", "uva", "pera"]
verduras = ["apio", "cebolla", "lechuga"]
print("fruta - verdura")
for i in range(len(frutas)):
    print(f"{frutas[i]} - {verduras[i]}")
    
#comparar elementos
lista1 = [5, 8, 3, 9, 2]
lista2 = [5, 7, 3, 10, 2]
print("comparando elementos: ")
for i in range(len(lista1)):
    if lista1[i] == lista2[i]:
        print(f"indice {i}: {lista1[i]} == {lista2[i]} ")
