from estructuras import *
from manejo_archivos import *


if __name__ == "__main__":

    lista_input = manejar_input()
    N = lista_input[0]
    lista_restaurants = []

    #Primero llenamos la tabla de mesas con puros 0
    for j in range(int(lista_input[0])):
        lista_restaurants.append(0)

    # Poblar los restaurantes
    for i in range(int(N)):
        lista_mesas = []
        #Primero llenamos la tabla de mesas con puros 0
        for j in range(int(lista_input[i+1])):
            lista_mesas.append(0)

        # Poblar las mesas
        for j in  range(int(lista_input[i+1])):
            mesa = inicializar_mesas(j, )
            lista_mesas[j] = mesa
        restaurante = inicializar_restaurantes(i, lista_mesas)
        lista_restaurants[i] = restaurante

    total_input =  int(lista_input[int(N)+1])
    iteracion = int(N) + 2

    #For que abre cada una de las mesas
    for i in range(total_input):
        input = lista_input[iteracion].split(" ")
        lista_restaurants[int(input[1])].mesas[int(input[2])].abierta = True
        lista_restaurants[int(input[1])].mesas[int(input[2])].capacidad = int(input[3])
        # Poblamos cada asientos con 0 para
        for j in range(lista_restaurants[int(input[1])].mesas[int(input[2])].capacidad):
                lista_restaurants[int(input[1])].mesas[int(input[2])].asientos.append(0)

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

    while lista_input[iteracion] != "END":
        input = lista_input[iteracion].split(" ")

        if input[0] == "CUSTOMER":
            if lista_restaurants[int(input[1])].mesas[int(input[2])].asientos_ocupados == lista_restaurants[int(input[1])].mesas[int(input[2])].capacidad:
                print("No quedan mas asientos disponibles")
            else:
                persona = inicializar_personas(input[3])
                lista_restaurants[int(input[1])].mesas[int(input[2])].asientos[lista_restaurants[int(input[1])].mesas[int(input[2])].asientos_ocupados] = persona
                lista_restaurants[int(input[1])].mesas[int(input[2])].asientos_ocupados += 1       
        elif input[0] == "TABLE-STATUS":
            # print(lista_restaurants[int(input[1])].mesas[int(input[2])].capacidad)
            capacidad_total = lista_restaurants[int(input[1])].mesas[int(input[2])].capacidad
            restante = lista_restaurants[int(input[1])].mesas[int(input[2])].capacidad - lista_restaurants[int(input[1])].mesas[int(input[2])].asientos_ocupados
            lista_clientes = lista_restaurants[int(input[1])].mesas[int(input[2])].asientos
            imprimir_status(int(input[1]), int(input[2]), capacidad_total, restante, lista_clientes)

        
        iteracion += 1
            

        
    # print(lista_restaurants[39].mesas[47].asientos[0].id)             
    # print(lista_restaurants[39].mesas[47].asientos_ocupados)             
    # print(lista_restaurants[39].mesas[47].capacidad)             






        
