""""
Escribir un programa que le pida a un usuario su año de nacimiento y otro año, y le diga que edad teia el 
usuario en el año ingresado
"""

nacimiento = int(input("ingrese su año de nacimiento: "))
fecha = int(input("Ingrese la fecha deseada para calcular su edad en ese momento: "))

"""
para poder realizar la operacion hay que convertir los input a int, sino me toma la entrada como String
"""
resultado = fecha - nacimiento
print("Tu edad es: " + str(resultado))