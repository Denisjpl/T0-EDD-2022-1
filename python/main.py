from estructuras import *
from manejo_archivos import *


if __name__ == "__main__":

    lista_restaurants = []

    # Primero poblamos los datos de las estructuras
    lista_input = manejar_input()
    N = lista_input[0]
    # Poblar los restaurantes
    for i in range(int(N)):
        lista_mesas = []
        # Poblar las mesas
        for j in  range(int(lista_input[i+1])):
            mesa = inicializar_mesas(j)
            lista_mesas.append(mesa)
        restaurante = inicializar_restaurantes(i, lista_input[i+1], lista_mesas)
        lista_restaurants.append(restaurante)        

total_input =  int(lista_input[int(N)+1])
iteracion = int(N) + 2

#For que abre cada una de las mesas
for i in range(total_input):
    input = lista_input[iteracion].split(" ")
    lista_restaurants[int(input[1])].mesas[int(input[2])].abierta = True
    lista_restaurants[int(input[1])].mesas[int(input[2])].capacidad = int(input[3])


    iteracion += 1

total_input = int(lista_input[iteracion])
iteracion += 1

menu = Menu()

# for que agrega los menus de la carta
for i in range(total_input):
    input = lista_input[iteracion].split(" ")
    plato = inicializar_plato(int(input[1]), int(input[2]))
    menu.platos.append(plato)
    iteracion += 1






        
