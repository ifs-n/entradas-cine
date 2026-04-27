import os
os.system("cls")


DESCUENTO_NINO = 0.50      # menores de 12 años
DESCUENTO_ADULTO_MAYOR = 0.30  # 60 años o más
DESCUENTO_MARTES = 0.20
RECARGO_FIN_SEMANA = 0.15
IVA = 0.19

dias = ["lunes", "martes", "viernes", "sabado", "domingo"]

try:
    cliente = input("Ingrese nombre del cliente: \n")
    edad = int(input("Ingrese la edad del cliente: \n"))
    while edad <= 0:
        edad = int(input("El valor ingresado no es una edad válido, ingrese la edad nuevamente: \n"))
    entradas = int(input("Ingrese la cantidad de entradas: \n"))
    while entradas < 0:
        entradas = int(input("La cantidad de entradas no puede ser 0, ingrese la cantidad de entradas nuevamente: \n"))
    precio_entradas = float(input("Ingrese el valor de las entradas: \n"))
    while precio_entradas <= 0:
        precio_entradas = int(input("El valor ingresado no es válido, ingrese el valor de las entradas nuevamente: \n"))
    dia_funcion = input("Ingrese el dia de la función (lunes, martes, viernes, sabado o domingo): \n").lower()
    while dia_funcion not in dias:
        dia_funcion = input("El dia ingresado no tiene funciones, ingrese un dia válido:").lower()

    subtotal = precio_entradas * entradas

    if edad < 12:
        descuento_edad = subtotal * DESCUENTO_NINO
        edad_mensaje = "Niño"
    elif edad >= 60:
        descuento_edad = subtotal * DESCUENTO_ADULTO_MAYOR
        edad_mensaje = "Adulto mayor"
    else:
        descuento_edad = 0
        edad_mensaje = "Adulto"

    if dia_funcion == "martes":
        descuento_dia = subtotal * DESCUENTO_MARTES
    else:
        descuento_dia = 0

    if dia_funcion == "sabado" or dia_funcion == "domingo":
        recargo_finde = subtotal * RECARGO_FIN_SEMANA
    else:
        recargo_finde = 0

    total = subtotal - descuento_dia - descuento_edad + recargo_finde

    subtotal_iva = total * IVA

    total_final = total + subtotal_iva

    if total_final <= 10000:
        mensaje = "Compra ecónomica"
    elif total_final in range(10001, 30001):
        mensaje = "Compra normal"
    else:
        mensaje = "Compra alta"

    os.system("cls")

    print(f"Nombre del cliente: {cliente}")
    print(f"Edad: {edad}")
    print(f"Tipo cliente: {edad_mensaje}")
    print(f"Total a pagar: {round(total_final, 2)}")
    print(f"Clasificación de la compra: {mensaje}")


except:
    print("Los datos ingresado no son números.")