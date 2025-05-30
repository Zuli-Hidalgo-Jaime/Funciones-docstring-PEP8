###Funciones con uso de parámetros y retornos

## Propósito

El objetivo de este proyecto es crear 2 ejemplos utilizando diferentes elementos en Python para comprender
y utilizar buenas prácticas al momento de la codificación, entre dichos elementos están:

- Uso de diccionarios, listas, tuplas, etc
- Documentación con docstrings y formato PEP8
- Uso de funciones
- Uso de parámetros en funciones y retornos

## Tecnologías
Visual Studio Code v 1.92.2 instalado
Python v 3.11.9 instalado

## Ejecución

1. Descargar archivo funcionesJueves.py
2. Abrir terminal
3. Buscar la dirección del archivo
4. ejecutar con comando
	Python funcionesJueves.py

# Ejemplo de uso
## Ejemplo 2

Al iniciar el programa se mostrará en consola lo siguiente:
  Selecciona un empleado:
  1. Hazael Pérez
  2. Diana Fernández
  3. Zuli Hidalgo
  4. Salir
  Elige un empleado:

Al elegir un empleado se desplegará el siguiente menú:

1. Agregar un pendiente
2. Consultar pendientes
3. Eliminar un pendiente
4. Volver al menú principal

Si se seleccionó numero 3 (Zuli Hidalgo) y después opción 1 (Agregar pendiente, por ejemplo "Preparar Trasformaciones Coneptuales")

Al elegir la opción 2 (Consultar pendientes) se observará:
1. Preparar reporte mensual

Con la opción 3 (Eliminar un pendiente) se muestra la lista de pendientes y se debe elegir el número del pendiente a eliminar.

Al elegir la opción número 3 se devuelve al menú principal, donde están los nombres de empleados

#Estructura del código

mostrar_menu_principal() – Muestra los empleados disponibles.

mostrar_menu_empleado(nombre) – Muestra opciones para el empleado seleccionado.

agregar_pendiente(nombre) – Permite agregar un nuevo pendiente.

consultar_pendientes(nombre) – Lista los pendientes actuales del empleado.

eliminar_pendiente(nombre) – Permite eliminar un pendiente por número.

Diccionario empleados – Contiene los nombres y listas de pendientes.
