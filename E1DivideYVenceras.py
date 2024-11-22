def caminos_posibles_divide_y_venceras(m, n):
    def explorar(x, y):
        # Si llegamos al destino
        if (x, y) == (m - 1, n - 1):
            return [[(x, y)]]

        # Si salimos de los límites, no hay caminos
        if x >= m or y >= n:
            return []

        # Resolver subproblemas: derecha y abajo
        caminos_derecha = explorar(x, y + 3)
        caminos_abajo = explorar(x + 2, y)

        # Combinar soluciones de los subproblemas
        return [[(x, y)] + camino for camino in caminos_derecha + caminos_abajo]

    # Llamada inicial
    return explorar(0, 0)

# Ejemplo de uso
m, n = 11, 7  # Tablero de 11 filas x 7 columnas
resultados = caminos_posibles_divide_y_venceras(m, n)
print(f"Total caminos encontrados (Divide y Vencerás): {len(resultados)}")
for idx, camino in enumerate(resultados):
    print(f"Camino {idx + 1}: {camino}")