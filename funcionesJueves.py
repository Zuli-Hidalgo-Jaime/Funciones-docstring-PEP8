# Este script está diseñado para practicar las funciones con uso de
# parámetros y retornos. También se trabaja el uso de docstring y 
# una buena práctica utilizando PEP 8

# Ejemplo 1: Crear una calculadora que tenga las funciones principales
# como suma, resta, multiplicación y division usando funciones que 
# reciben parámetros y retornan el resultado

'''
def suma(a, b):
    """
    Se hace la suma de dos números.

    Parámetros:
    a (float): Número 1.
    b (float): Número 2.

    Retorna:
    float: resultado de la suma.
    """
    resultado = a + b
    return resultado


def resta(a, b):
    """
    Realiza la resta entre dos números.

    Parámetros:
    a (float): Número 1.
    b (float): Número 2.

    Retorna:
    float: resultado de la resta.
    """
    resultado = a - b
    return resultado


def multiplicacion(a, b):
    """
    Realiza la multiplicación de dos números.

    Parámetros:
    a (float): Número 1.
    b (float): Número 2.

    Retorna:
    float: Resultado de la multiplicación.
    """
    resultado = a * b
    return resultado


def division(a, b):
    """
    Realiza la división entre dos números.

    Parámetros:
    a (float): Número 1.
    b (float): Número 2.

    Retorna:
    float: Resultado de la división.
    """
    resultado = a / b
    return resultado


def elegir_numeros():
    """
    Solicita al usuario dos números y los convierte a números float.

    Retorna:
    tupla: Una tupla con los dos números ingresados (numero1, numero2).
    """
    numero1 = float(input("Digite el primer número: "))
    numero2 = float(input("Digite el segundo número: "))
    return numero1, numero2


def menu_de_operaciones():
    """
    Muestra el menú de operaciones.
    """
    print("1. Suma")
    print("2. Resta")
    print("3. Multiplicación")
    print("4. División")
    print("5. Salir")


# Bucle principal del programa
while True:
    menu_de_operaciones()
    opcion = input("Elige la opción que deseas: ")

    if opcion == "1":
        numero1, numero2 = elegir_numeros()
        print(f"El resultado de la suma es: {suma(numero1, numero2)}")

    elif opcion == "2":
        numero1, numero2 = elegir_numeros()
        print(f"El resultado de la resta es: {resta(numero1, numero2)}")

    elif opcion == "3":
        numero1, numero2 = elegir_numeros()
        print(f"El resultado de la multiplicación es: {multiplicacion(numero1, numero2)}")

    elif opcion == "4":
        numero1, numero2 = elegir_numeros()
        if numero2 == 0:
            print("Error: No se puede dividir entre cero.")
        else:
            print(f"El resultado de la división es: {division(numero1, numero2)}")

    elif opcion == "5":
        print("Hasta pronto.")
        break

    else:
        print("Hubo un error. Intente de nuevo.")

#----------------------------------------------------------------------
'''
#Ejemplo 2: 

def mostrar_menu_principal():
    """
    Se muestra el menú con los empleados.
    """
    print("Selecciona un empleado:")
    for i, nombre in enumerate(empleados.keys(), start=1): # La función keys() sirve para obtener las llaves o claves de
        #cada elemento que hay en el diccionario, en este caso el diccionario de empleados
        print(f"{i}. {nombre}")
    print("4. Salir")


def mostrar_menu_empleado(nombre):
    """
    Se muestra el menú de acciones para el empleado que se elija.

    Parámetros:
    nombre (str): Nombre del empleado.
    """
    print("\n")
    print("1. Agregar un pendiente")
    print("2. Consultar pendientes")
    print("3. Eliminar un pendiente")
    print("4. Volver al menú principal")


def agregar_pendiente(nombre):
    """
    Agrega un pendiente al empleado.

    Parámetros:
    nombre (str): Nombre del empleado.

    Retorna:
    str: Mensaje de confirmación.
    """
    pendiente = input("Escribe el pendiente: ")
    empleados[nombre].append(pendiente)
    return "Pendiente agregado exitosamente."


def consultar_pendientes(nombre):
    """
    Muestra los pendientes actuales del empleado.

    Parámetros:
    nombre (str): Nombre del empleado.
    """
    pendientes = empleados[nombre]
    if not pendientes:
        print("No hay pendientes.")
    else:
        print("\nPendientes:")
        for i, pendiente in enumerate(pendientes, start=1):
            print(f"{i}. {pendiente}")


def eliminar_pendiente(nombre):
    """
    Elimina un pendiente del empleado seleccionado.

    Parámetros:
    nombre (str): Nombre del empleado.
    """
    pendientes = empleados[nombre]
    if not pendientes:
        print("No hay pendientes para eliminar.")
        return

    consultar_pendientes(nombre)
    try:
        indice = int(input("Ingresa el número del pendiente a eliminar: ")) - 1
        if 0 <= indice < len(pendientes):
            eliminado = pendientes.pop(indice)
            # Elimina el pendiente en la posición indicada y guarda el valor eliminado en la variable 'eliminado'.
            # pop() remueve y retorna el elemento en el índice especificado de una lista.
            print(f"Pendiente eliminado: {eliminado}")
        else:
            print("Índice inválido.")
    except ValueError:
        print("Entrada inválida. Debe ser un número.")


# Diccionario de empleados con lista de pendientes
empleados = {
    "Hazael Pérez": [],
    "Diana Fernández": [],
    "Zuli Hidalgo": []
}

# Programa principal
while True:
    mostrar_menu_principal()  # Muestra el menú de empleados
    opcion = input("Elige un empleado: ")

    # Verifica si la opción seleccionada corresponde a un número válido de empleado
    if opcion in ["1", "2", "3"]:
        # Obtiene el nombre del empleado correspondiente a la opción elegida
        empleado_seleccionado = list(empleados.keys())[int(opcion)]

        # Bucle interno: menú de acciones específicas para el empleado seleccionado
        while True:
            mostrar_menu_empleado(empleado_seleccionado)  # Muestra el menú del empleado
            accion = input("Elige una opción: ")  # Pide al usuario que elija una acción

            if accion == "1":
                # Llama a la función para agregar un pendiente y muestra el resultado
                print(agregar_pendiente(empleado_seleccionado))
            elif accion == "2":
                # Llama a la función para consultar los pendientes del empleado
                consultar_pendientes(empleado_seleccionado)
            elif accion == "3":
                # Llama a la función para eliminar un pendiente del empleado
                eliminar_pendiente(empleado_seleccionado)
            elif accion == "4":
                # Sale del menú del empleado y regresa al menú principal
                break
            else:
                # Maneja una opción inválida dentro del menú del empleado
                print("Opción inválida, intenta de nuevo.")

    # Opción para salir del programa
    elif opcion == "4":
        print("¡Hasta luego!")
        break  # Rompe el bucle principal y finaliza el programa

    else:
        # Maneja una opción inválida en el menú principal
        print("Opción inválida, intenta de nuevo.")

