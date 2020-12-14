

def encontrar_vertice_min(valores_distancia, vertices_restantes):
    """ Función para encontrar el vértice con la distancia mínima
        en la lista de vertices que aún no se ha procesado"""

    # De esta forma se representa infinito en Python
    dist_minima = float("inf")
    index_del_minimo = -1  # Por ahora no se selecciona ningun indice

    for i in range(len(valores_distancia)):
        """
        Se recorre la lista de distancias y se empieza a escoger el mínimo
        y se guarda el índice donde se encuentre el mínimo siempre y cuando
        aún esté en los vértices disponibles.
        """
        if ((valores_distancia[i] < dist_minima) and (i in 
                                                      vertices_restantes)):

            dist_minima = valores_distancia[i]
            index_del_minimo = i
    
    return index_del_minimo


def imprimir_camino_corto(arbol_menor_longitud, vertice):
    """ 
    Función para imprimir el camino del origen a un vértice dado.
    """
    # Este sería si es el origen
    if arbol_menor_longitud[vertice] == -1:
        print(vertice, "-", end="")
    else:
        # Ahora se busca el siguiente vértice
        imprimir_camino_corto(arbol_menor_longitud,
                              arbol_menor_longitud[vertice])
        print(vertice, "-", end="")


def algoritmo_dijkstra(grafo, vertice_origen): 
    """
    Función que aplica el algoritmo dijkstra para encontrar el 
    camino más corto a todos los vértices dado un origen
    """
    
    # Recordemos que nuestro grafo es una  matriz de adyacencia
    columnas = len(grafo[0])
    filas = len(grafo)
    
    """ Paso 1: Creamos la lista de vértices no procesados que en un inicio debe
    tener todos los vértices del grafo"""

    vertices_restantes = []
    for vertice in range(filas):
        vertices_restantes.append(vertice)
    
    """Lista de vértices procesados"""

    vertices_procesados = []

    """Esta lista obtendrá las distancias más cortas que  forman el árbol
        desde el origen con todos los caminos más cortos a cada vértice"""
    arbol_menor_longitud = filas * [-1]

    """ Paso 2: Inicialmente todas las distancias y costos son infinito para
        cada vértice"""
    valores_distancia = filas*[float("inf")]

    """Inicializamos la distancia del origen al origen en 0 (no hay
    distancia entre él mismo)"""
    valores_distancia[vertice_origen] = 0
 
    # Paso 3: Mientras la lista de vertices restantes no esté vacía:
            
    while len(vertices_restantes) != 0:

        """ 3.a) Escoger el vértice u con la distancia mínima de la lista de 
            vértices restantes."""

        vertice_u = encontrar_vertice_min(valores_distancia, 
                                          vertices_restantes)

        """ 3.b) Remover el vértice u de la lista de vertices restantes, agregarlo
        a la lista de vértices procesados"""

        vertices_restantes.remove(vertice_u)
        vertices_procesados.append(vertice_u)

        """ 3.c) Actualizar el valor de la distancia de los vértices adyacentes,
        seleccionando el valor menor entre el existente y el nuevo valor"""

        """Como nuestro grafo está representado por matriz de adyacencia,
        cada fila es un vértice y las columnas los vecinos, necesitamos
        recorrer las columnas de la fila que tiene al vértice u"""

        """Se analizan los vértices vecinos que aún no están en la lista de
           vértices procesados"""
        
        for i in range(columnas):
            if grafo[vertice_u][i] and i not in vertices_procesados:
                distancia_actual = valores_distancia[i]
                distancia_nueva = (valores_distancia[vertice_u] + 
                                   grafo[vertice_u][i])

            # vamos a comparar la distancia actual con la nueva
                if distancia_actual > distancia_nueva:
                    distancia_menor = distancia_nueva
                    valores_distancia[i] = distancia_menor
                    # actualizamos la lista de costos
                    arbol_menor_longitud[i] = vertice_u

    print("Vértice origen     -   Vértice destino", "\t",
          "Distancia mínima", "\t", "Camino más corto", "\n")

    for vertice in range(0, len(valores_distancia)):
        print("\t", vertice_origen, "\t", " - ", "\t", vertice, "\t\t\t",
              valores_distancia[vertice], "\t\t\t", end="")
        imprimir_camino_corto(arbol_menor_longitud, vertice)
        print("\n")


"""grafo = [[0, 4, 0, 0, 0, 0, 0, 8, 0],
         [4, 0, 8, 0, 0, 0, 0, 11, 0],
         [0, 8, 0, 7, 0, 4, 0, 0, 2],
         [0, 0, 7, 0, 9, 14, 0, 0, 0],
         [0, 0, 0, 9, 0, 10, 0, 0, 0],
         [0, 0, 4, 14, 10, 0, 2, 0, 0],
         [0, 0, 0, 0, 0, 2, 0, 1, 6],
         [8, 11, 0, 0, 0, 0, 1, 0, 7],
         [0, 0, 2, 0, 0, 0, 6, 7, 0]]"""


grafo = [[0, 1, 2, 0, 0, 0],
         [1, 0, 3, 9, 0, 0],
         [2, 3, 0, 5, 8, 3],
         [0, 9, 5, 0, 4, 0],
         [0, 0, 8, 4, 0, 0],
         [0, 0, 3, 0, 0, 0]]


algoritmo_dijkstra(grafo, 3)

 
