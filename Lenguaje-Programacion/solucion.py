# Programa Cine
# Para registrar las ventas de las entradas con sus descuentos

# Declaración de las listas
lista_nombres = [] # Lista para almacenar los nombres de los clientes
lista_apellidos = [] # Lista para almacenar los apellidos de los cliente
lista_cantidades = [] # Lista para almacenar la cantidad de entraas que compra cada cliente
lista_precios = [] # Lista para almacenar  el precio de cada entrada
lista_totales = [] # Lista para almacenar el total a pagar de cada cliente

# Como vamos a trabajar con el ciclo while
# es necesario solicitar al usuario
# la cantidad de ventas que va a registrar antes de iniciar

cantidad_ventas = int(input("Ingrese la cantidad de ventas que desea ingresar: "))

# Inicialización del contador en 0
contador = 0

# Ciclo While
while contador < cantidad_ventas: # Se va a repetir mientras el contador sea menor a la cantidad de ventas

    # Se solicitan los datos del cliente
    nombre = input("\nIngrese nombre: ") # Dato str
    apellido = input("Ingrese apellido: ") # Dato str
    cantidad_entradas = int(input("Ingrese cantidad de entradas: ")) # DATO str y se convierte a int
    precio = float(input("Ingrese precio unitario: ")) # Dato str y se convierte en float

    # Se calcula el subtotal con la formula (cantidad de entradas × precio unitario)
    subtotal = cantidad_entradas * precio

    # Cálcula del descuento según la cantidad de entradas
    # Por una entrada el descuento es del 10%
    if cantidad_entradas == 1:
        descuento = subtotal * 0.10
    else:
        # Por 2 y 3 entradas el descuento es del 20%
        if cantidad_entradas >= 2 and cantidad_entradas <= 3:
            descuento = subtotal * 0.20
        else:
            # Por 4 y 5 entradas el descuento es del 30%
            if cantidad_entradas >= 4 and cantidad_entradas <= 5:
                descuento = subtotal * 0.30
            else:
                # Por 6 o más entradas el descuento sería del 40%
                descuento = subtotal * 0.40

    # Ahora se calcula el total con el descuento aplicado
    total = subtotal - descuento

    # Se almacenan los datos en las listas
    lista_nombres.append(nombre) # Almacena los nombre ingresados
    lista_apellidos.append(apellido) # Almacena los apellidos ingresados
    lista_cantidades.append(cantidad_entradas) # Almacena las cantidades de entradas ingresadas
    lista_precios.append(precio) # Almacena los precios ingresados
    lista_totales.append(total) # Almacena los totales a pagar

    # Se incrementa el contador en 1
    contador = contador + 1

# Reporte Final
print("\n********** Reporte Final **********")

for i  in range(cantidad_ventas):

    print("Venta", i + 1) # Muestra el número de la venta registrada
    print("Nombre: ", lista_nombres[i]) # muestra el nombre correspondiente a la posición i
    print("Apellido: ", lista_apellidos[i]) # muestra el apellido correspondiente a la posición i
    print("Cantidad entradas: ", lista_cantidades[i]) # muestra la cantidad de entradas correspondiente a la posición i
    print("Precio unitario: ", lista_precios[i]) # muestra el precio correspondiente a la posición i
    print("Total a pagar: ", lista_totales[i]) # muestra el total a pagar correspondiente a la posición i
    print("**********************")

# Cálculo del promedio de las ventas (promedio de los totales)
promedio = 0

for i in range(cantidad_ventas): # Recorre todos los totales almacenados
    promedio = promedio + lista_totales[i] # Suma todos los totales al acumulador promedio

promedio = promedio / cantidad_ventas # Divide la suma total por la cantidad de ventas

# Determinar la venta mayor y la venta menor
# Se inicializan con el primer total registrado
mayor = lista_totales[0]
menor = lista_totales[0]

for i in range(cantidad_ventas):
    if lista_totales[i] > mayor: # Si el total actual es mayor que la variable mayor
                                 # se actualiza el valor de mayor
        mayor = lista_totales[i]

    if lista_totales[i] < menor: # Si el total actual es menor que la variable menor
                                 # se actualiza el valor de menor
        menor = lista_totales[i]

# Resultados finales
print("\nPromedio de ventas: ", promedio) #Muestra el promedio de ventas
print("Venta mayor: ", mayor) #Muestra la venta mayor
print("Venta menor: ", menor) #Muestra la venta menor
