def camino_existe_fuerza_bruta(m, n):
    # Comienza en la casilla (0,0)
    x, y = 0, 0
    destino = (m - 1, n - 1)
    visitados = set()  # Para evitar visitar la misma casilla más de una vez
    visitados.add((x, y))

    # Lista de posiciones a explorar
    posiciones = [(x, y)]

    while posiciones:
        x, y = posiciones.pop(0)

        # Si llegamos al destino, regresamos True
        if (x, y) == destino:
            return True

        # Intentamos movernos a la derecha
        if y + 3 < n and (x, y + 3) not in visitados:
            posiciones.append((x, y + 3))
            visitados.add((x, y + 3))

        # Intentamos movernos hacia abajo
        if x + 2 < m and (x + 2, y) not in visitados:
            posiciones.append((x + 2, y))
            visitados.add((x + 2, y))

    return False


# Ejemplo de uso
m, n = 3, 4  # Tablero de 3 filas x 4 columnas
existe = camino_existe_fuerza_bruta(m, n)
print("¿Existe un camino?", "Sí" if existe else "No")


def caminos_posibles_fuerza_bruta(m, n):
    x, y = 0, 0
    destino = (m - 1, n - 1)
    caminos = []
    visitados = set()  # Para evitar visitar la misma casilla más de una vez
    visitados.add((x, y))

    # Lista de posiciones a explorar
    posiciones = [([(0, 0)], (x, y))]

    while posiciones:
        camino, (x, y) = posiciones.pop(0)

        # Si llegamos al destino, guardamos el camino
        if (x, y) == destino:
            caminos.append(camino)
            continue

        # Movimientos hacia la derecha: avanzar 3 casillas, solo si es posible
        if y + 3 < n and (x, y + 3) not in visitados:
            posiciones.append((camino + [(x, y + 3)], (x, y + 3)))
            visitados.add((x, y + 3))

        # Movimientos hacia abajo: avanzar 2 casillas, solo si es posible
        if x + 2 < m and (x + 2, y) not in visitados:
            posiciones.append((camino + [(x + 2, y)], (x + 2, y)))
            visitados.add((x + 2, y))

    return caminos


# Ejemplo de uso
m, n = 11, 7  # Tablero de 11 filas x 7 columnas
resultados = caminos_posibles_fuerza_bruta(m, n)
print(f"Total caminos encontrados: {len(resultados)}")
for idx, camino in enumerate(resultados):
    print(f"Camino {idx + 1}: {camino}")