



class Restaurant:

    def __init__(self):
        self.id = 0
        self.mesas = []


class Mesas:

    def __init__(self):
        self.abierta = False
        self.capacidad = None
        self.capacidad = 0
        self.asientos = []

class Menu:

    def __init__(self):
        self.platos = []

class Persona:
    
    def __init__(self):
        pass

class Plato:

    def __init__(self):
        self.id = None
        self.price = 0

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

def inicializar_plato(id, price):
    plato = Plato()
    plato.id = id
    plato.price = price
    return plato
