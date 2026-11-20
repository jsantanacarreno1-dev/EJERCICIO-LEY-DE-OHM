###Calculo de circuitos electricos" 

import tkinter as tk
import Operaciones
from Operaciones import division
from Operaciones import multiplicacion

while True:

 print(" Que desea calcular")
 print ("1 = RESISTENCIA")
 print ("2 = VOLTIOS")
 print ("3 = AMPERAJE")
 print("4 = SALIR")

 Opciones = int (input ("SELECCIONA TU OPCION:"))
 if Opciones == 1:
    print ("Calcular resistencia")
    voltaje = float(input(" Valor voltaje:"))
    amperaje = float(input("Valor amperaje:"))
    resultado = Operaciones.division (voltaje,amperaje)
    print("La resistencia es",resultado)
 elif Opciones == 2:
    print("Calcular Voltaje")
    amperaje = float(input("Valor amperaje:"))
    resistencia = float(input("Valor resistencia:"))
    resultado = Operaciones.multiplicacion (resistencia,amperaje)
    print("El voltaje es",resultado)
 elif Opciones == 3:
    print("Calcular amperaje")
    voltaje = float(input(" Valor voltaje:"))
    resistencia = float(input("Valor resistencia:"))
    resultado = Operaciones.division (voltaje,resistencia)
    print("El amperaje es",resultado)

 elif Opciones == 4:
    print("Programa finalizado.")
    break
 else:
    print("Opción no válida")

