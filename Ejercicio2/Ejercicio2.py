def busqueda_binaria(arr, elemento_actual, inicio, fin):
    # Función de búsqueda binaria que devuelve la posición donde insertar elemento_actual en arr.
    # `inicio` es el índice inicial y fin es el índice final del rango de búsqueda.

    while inicio < fin:
        medio = (inicio + fin) // 2
        if arr[medio] < elemento_actual:
            inicio = medio + 1
        else:
            fin = medio
    return inicio


def insertion_sort_busqueda_binaria(arr):
    for i in range(1, len(arr)):
        elemento_actual = arr[i]

        # Encuentra la posición de inserción usando la búsqueda binaria
        pos = busqueda_binaria(arr, elemento_actual, 0, i)

        # Mueve los elementos a la derecha para hacer espacio para el elemento actual
        arr = arr[:pos] + [elemento_actual] + arr[pos:i] + arr[i + 1:]

    return arr


def insertion_sort_normal(arr):
    # Recorre cada elemento de la lista a partir del segundo
    for i in range(1, len(arr)):
        # Guarda el valor del elemento actual
        elemento_actual = arr[i]
        # Inicializa j como el índice del elemento anterior
        j = i - 1

        # Mueve los elementos de la lista que sean mayores que el elemento actual una posición a la derecha
        while j >= 0 and arr[j] > elemento_actual:
            arr[j + 1] = arr[j]
            j -= 1

        # Coloca el elemento actual en su posición correcta
        arr[j + 1] = elemento_actual

    return arr


ejemplo = [12, 11, 13, 5, 6, 1, 4]
print("Arreglo original:", ejemplo)
arreglo_ordenado = insertion_sort_busqueda_binaria(ejemplo)
print("Arreglo ordenado:", arreglo_ordenado)
arreglo_ordenado_2 = insertion_sort_normal(ejemplo)
print("Arreglo con i_normal:", arreglo_ordenado_2)