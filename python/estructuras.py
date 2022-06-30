



class Restaurant:

    def __init__(self):
        self.id = 0
        self.mesas = []


class Mesas:

    def __init__(self):
        self.abierta = False
        self.capacidad = None

class Menu:

    def __init__(self):
        pass

class Persona:
    
    def __init__(self):
        pass

def inicializar_restaurantes(id, capacidad, lista_mesas):
    restaurante = Restaurant()
    restaurante.id = id
    restaurante.capacidad = capacidad
    restaurante.mesas = lista_mesas
    return restaurante

def inicializar_mesas(id):
    mesa = Mesas()
    mesa.id = id
    return mesa
