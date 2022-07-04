

def manejar_input():
    with open('../TEST-T0/tests/easy/A_02.txt','r') as stop_words: 
        lineas = [linea.strip() for linea in stop_words]
        return lineas

def imprimir_status(locationID, tableID, capacidad_total, capacidad_restante, lista_cliente):
    print(f"ESTADO MESA: Restaurante: {locationID} : Mesa: {tableID}")
    print(f"CAPACIDAD TOTAL {capacidad_total}")
    print(f"CAPACIDAD RESTANTE {capacidad_restante}")
    print(f"CLIENTES: ")
    for i in range(capacidad_total):
        if lista_cliente[i] != 0:
            print(f"ID_CLIENTE {lista_cliente[i].id}")
        else:
            print("_")

        
    print("FIN ESTADO")

# def sumar_capacidad_total(lista_mesas):
#     capacidad_total = 0
#     for i in lista_mesas:
#         capacidad_total += i.capacidad
#     return capacidad_total

if __name__ == "__main__":
    
    lista = manejar_input()

    for linea in lista:
        print(linea)