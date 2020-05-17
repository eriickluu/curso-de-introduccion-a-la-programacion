def saludar(nombre):
    return "Hola {} bienvenido al juego de Cody.".format(nombre) 

print("Ingresa tu nombre:")
nombre = input()

print(saludar(nombre))