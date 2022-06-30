

def manejar_input():
    with open('../TEST-T0/tests/easy/A_02.txt','r') as stop_words: 
        lineas = [linea.strip() for linea in stop_words]
        return lineas

if __name__ == "__main__":
    
    lista = manejar_input()

    for linea in lista:
        print(linea)