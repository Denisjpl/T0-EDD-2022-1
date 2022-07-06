



class Restaurant:

    def __init__(self):
        self.id = 0
        self.mesas = []


class Mesas:

    def __init__(self):
        self.id = None
        self.abierta = False
        self.capacidad = 0
        self.asientos_ocupados = 0
        self.asientos = []

class Menu:

    def __init__(self):
        self.platos = []

class Persona:
    
    def __init__(self):
        self.id = None
        self.cuenta = []

class Plato:

    def __init__(self):
        self.id = None
        self.price = 0

def inicializar_restaurantes(id, lista_mesas):
    restaurante = Restaurant()
    restaurante.id = id
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

def inicializar_personas(id):
    persona = Persona()
    persona.id = id
    return persona
