# Ordenamiento por Selección (Selection Sort)
def selection_sort(lista):
    for i in range(len(lista)):
        indice_minimo = i
        # Encuentra el índice del elemento mínimo en la sublista no ordenada
        for j in range(i + 1, len(lista)):
            if lista[j] < lista[indice_minimo]:
                indice_minimo = j
        # Intercambia el elemento mínimo encontrado con el primer elemento de la sublista no ordenada
        lista[i], lista[indice_minimo] = lista[indice_minimo], lista[i]
    return lista


# Ordenamiento por Inserción (Insertion Sort)
def insertion_sort(lista):
    for i in range(1, len(lista)):
        clave = lista[i]
        j = i - 1

        # Mueve los elementos mayores al elemento actual hacia la derecha
        while j >= 0 and clave < lista[j]:
            lista[j + 1] = lista[j]
            j -= 1
        lista[j + 1] = clave
    return lista


# Ordenamiento Burbuja (Bubble Sort)
def bubble_sort(lista):
    n = len(lista)
    for i in range(n):
        for j in range(0, n - i - 1):
            # Intercambia si el elemento actual es mayor que el siguiente
            if lista[j] > lista[j + 1]:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]
    return lista


# Ordenamiento por Mezcla (Merge Sort)
def merge_sort(lista):
    if len(lista) <= 1:
        return lista

    # Divide la lista en dos mitades
    mitad = len(lista) // 2
    izquierda = merge_sort(lista[:mitad])
    derecha = merge_sort(lista[mitad:])

    # Combina las dos mitades ordenadas
    return combinar(izquierda, derecha)


def combinar(lista_izquierda, lista_derecha):
    lista_ordenada = []
    i = j = 0
    # Combina los elementos de ambas listas en orden
    while i < len(lista_izquierda) and j < len(lista_derecha):
        if lista_izquierda[i] < lista_derecha[j]:
            lista_ordenada.append(lista_izquierda[i])
            i += 1
        else:
            lista_ordenada.append(lista_derecha[j])
            j += 1
    # Agrega los elementos restantes de ambas listas
    lista_ordenada.extend(lista_izquierda[i:])
    lista_ordenada.extend(lista_derecha[j:])
    return lista_ordenada


import random
import time

# Generamos arreglo con 10 elementos
arreglo_10 = list(range(10))
random.shuffle(arreglo_10)
# Generamos arreglo con 100 elementos
arreglo_100 = list(range(100))
random.shuffle(arreglo_100)
# Generamos arreglo con 1000
arreglo_1000 = list(range(1000))
random.shuffle(arreglo_1000)
# Generamos arreglo con 10000
arreglo_10000 = list(range(10000))
random.shuffle(arreglo_10000)
# Generamos arreglo con 100000
arreglo_100000 = list(range(100000))
random.shuffle(arreglo_100000)

ejemplo = arreglo_100000

elementos = len(ejemplo)

# Tiempo selection sort
tiempo_inicio = time.perf_counter()
arreglo_ordenado = selection_sort(ejemplo)
tiempo_final = time.perf_counter()
tiempo_ejecucion = (tiempo_final - tiempo_inicio)
print("SELECTION SORT")
# print("Arreglo ordenado:", arreglo_ordenado )
print(f"El tiempo de ejecucion para {elementos} elementos es de: {tiempo_ejecucion:.8f} segundos")
print("-----------------------------------------------------")

# Tiempo insertion sort
tiempo_inicio3 = time.perf_counter()
arreglo_ordenado3 = insertion_sort(ejemplo)
tiempo_final3 = time.perf_counter()
tiempo_ejecucion3 = (tiempo_final3 - tiempo_inicio3)
print("INSERTION SORT")
# print("Arreglo ordenado:", arreglo_ordenado3)
print(f"El tiempo de ejecucion para {elementos} elementos es de: {tiempo_ejecucion3:.8f} segundos")
print("-----------------------------------------------------")

# Tiempo bubble sort
tiempo_inicio5 = time.perf_counter()
arreglo_ordenado5 = bubble_sort(ejemplo)
tiempo_final5 = time.perf_counter()
tiempo_ejecucion5 = (tiempo_final5 - tiempo_inicio5)
print("BUBBLE SORT")
# print("Arreglo ordenado:", arreglo_ordenado5 )
print(f"El tiempo de ejecucion para  {elementos} elementos es de: {tiempo_ejecucion5:.8f} segundos")
print("-----------------------------------------------------")

# Tiempo Merge sort
tiempo_inicio7 = time.perf_counter()
arreglo_ordenado7 = merge_sort(ejemplo)
tiempo_final7 = time.perf_counter()
tiempo_ejecucion7 = (tiempo_final7 - tiempo_inicio7)
# print("Arreglo ordenado:", arreglo_ordenado7 )
print("MERGE SORT")
print(f"El tiempo de ejecucion para {elementos} elementos es de: {tiempo_ejecucion7:.8f} segundos")
print("-----------------------------------------------------")