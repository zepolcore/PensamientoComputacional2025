
# Crear un programa que le solicite al usuario un entero y lo imprima por pantalla.
# Recordá que podés usar las funciones input (para solicitar información) y print para mostrar
# información.

print("ingrese un entero")
entero = int(input())
    # me castea el input a int, si ingreso un valor no numerico como un char o un String me da un error.
    # solo puede castear a int valores nnumericos
print ("El numero ingresado fue: " )
print(entero)


-------------------------------------------------------------------------------------------------------

# Si desglosamos la funcion, vemos el input al cual le pasamos como parametro un String
# esto es como si pusieramos un print("ingrese un entero"), pero ademas selecciona un espacio en memoria 
# para el ingreso de un dato, y lo guarda en la variable numero.
numero = int(input("Ingrese un numero entero: "))
# La funcion que envuelte a input es una funcion de casteo, fuerza o convierte el dato ingresado en el 
# tipo de dato que le indiquemos. Una vez teniendo todo enpaqueado, recien se guarda en numero

print("El numero ingresado es: " + str(numero))
# Aca vemos que hay un casteo nuevamente, esto se debe a que no puedo concatenar un int con un String

----------------------------------------------------------------------------------------------------
