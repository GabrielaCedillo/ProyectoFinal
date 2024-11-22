def caminos_posibles_ramificacion_y_poda(m, n):
    def explorar(x, y, camino, visitados):
        # Si llegamos al destino
        if (x, y) == (m - 1, n - 1):
            return [camino]

        # Lista para almacenar caminos válidos
        caminos = []

        # Movimiento hacia la derecha
        if y + 3 < n and (x, y + 3) not in visitados:
            caminos.extend(explorar(x, y + 3, camino + [(x, y + 3)], visitados | {(x, y + 3)}))

        # Movimiento hacia abajo
        if x + 2 < m and (x + 2, y) not in visitados:
            caminos.extend(explorar(x + 2, y, camino + [(x + 2, y)], visitados | {(x + 2, y)}))

        return caminos

    # Llamada inicial
    return explorar(0, 0, [(0, 0)], {(0, 0)})


# Ejemplo de uso
m, n = 11, 7  # Tablero de 11 filas x 7 columnas
resultados = caminos_posibles_ramificacion_y_poda(m, n)
print(f"Total caminos encontrados (Ramificación y Poda): {len(resultados)}")
for idx, camino in enumerate(resultados):
    print(f"Camino {idx + 1}: {camino}")