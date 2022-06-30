from estructuras import *
from manejo_archivos import *


if __name__ == "__main__":

    lista_restaurants = []

    # Primero poblamos los datos de las estructuras
    lista_input = manejar_input()
    N = lista_input[0]
    i = 0
    # Poblar los restaurantes
    for i in range(int(N)):
        lista_mesas = []
        # Poblar las mesas
        for j in  range(int(lista_input[i+1])):
            mesa = inicializar_mesas(j)
            lista_mesas.append(mesa)
        restaurante = inicializar_restaurantes(i, lista_input[i+1], lista_mesas)
        lista_restaurants.append(restaurante)        

