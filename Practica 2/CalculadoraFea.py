"""
Crear un programa que le solicite al usuario dos numeros enteros y luego imprima por pantalla:
- La suma de los dos numeros
- La resta de los dos numeros
- La multiplicacion de los dos numeros
- La division entera de los dos numeros
- El resto 
"""

print("Ingrese dos numeros enteros")
numero1 = int(input("Inrese el pimer numero: "))
numero2 = int(input("Ingrese el segundo numero: "))

suma = numero1 + numero2
print("el resultado de la suma es: " + str(suma))

resta = numero1 - numero2
print("el resultado de la resta es: " + str(resta))

multiplicacion = numero1 * numero2
print("el resultado de la multiplicacion es: " + str(multiplicacion))

division = numero1 / numero2
print("El resultado de la division es: " + str(int(division)))

resto = numero1 / numero2
print("El resultado del resto es: " + str(int(resto)))