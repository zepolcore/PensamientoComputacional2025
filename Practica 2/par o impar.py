"""
Crear un programa que solcite al usuario un entero y determine si es par o impar
mostrando por pantalla un mensaje que indique el resultado     
"""
numero = int(input("ingrese un numero y determinaremos si el mismo es par o impar "))
resultado = numero % 2
print("Si el resultado es 0 entonces es par, si el resultado es 1 es impar   --------->  El resultado es: "+ str(resultado) )
