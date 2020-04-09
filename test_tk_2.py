#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr  5 12:08:39 2020

@author: david
"""
import tkinter as t
from numpy import zeros
import pandas as pd 

####Ver si es posible que creemos un icono y agreagarlo
#
#
#data = pd.read_csv("sintomas.csv")
#print(data)
#
#df = pd.DataFrame(data[:2])


root = t.Tk()
#creating a label widget
l0 = t.Label(root, text="Sistema de ayuda")

symptoms = ["Amarillamiento de las hojas viejas cercanas a la base de la planta: ",
            "Amarillamiento de las hojas maduras y jóvenes: ",
            "Coloramiento verde oscuro en las hojas: ",
            "Coloración purpura en hojas o tallos: ",
            
            "Pequeños puntos negros en la hoja, o partes de tejido muerto: ",
            "puntos negros necróticos en  las puntas de las yemas: ",
            "puntos negros necróticos en la base de la hoja: ", 
            "Muerte de hojas viejas: ", 
            
            "Hoja inusualmente rígida y quebradiza: ", 
            
            "Crecimiento desacelerado o detenido: ",
            "Tallos marcadamente delgados o leñosos: ",
            "Maduración de la planta retrasada: ",
            "Plantas débiles y más propensas a irse de lado: ",
            "Plantas atacadas fácilmente por hongos en las hojas: ",
            "Planta altamente ramificada y con ápices necróticos: "
            ]

buttonStates = zeros(len(symptoms))

def createSympLabels():
    for symptom, row in zip(symptoms, range(len(symptoms))):
        label = t.Label(root, text=symptom)
        label.grid(row=row+1,column=0 )
        


def buttonState(index, bState):
    if bState[index] == 0:
        bState[index] = 1
        
    else: 
        bState[index] = 0
        
    state = t.Label(root, text=str(int(bState[index])))
    state.grid(row=index+1, column= 2)


def createSympButton():
    b1 = t.Button(root, text='', command=lambda: buttonState(0,buttonStates), bg='blue')
    b2 = t.Button(root, text='', command=lambda: buttonState(1,buttonStates), bg='blue')
    b3 = t.Button(root, text='', command=lambda: buttonState(2,buttonStates), bg='blue')
    b4 = t.Button(root, text='', command=lambda: buttonState(3,buttonStates), bg='blue')
    b5 = t.Button(root, text='', command=lambda: buttonState(4,buttonStates), bg='blue')
    b6 = t.Button(root, text='', command=lambda: buttonState(5,buttonStates), bg='blue')
    b7 = t.Button(root, text='', command=lambda: buttonState(6,buttonStates), bg='blue')
    b8 = t.Button(root, text='', command=lambda: buttonState(7,buttonStates), bg='blue')
    b9 = t.Button(root, text='', command=lambda: buttonState(8,buttonStates), bg='blue')
    b10 = t.Button(root, text='', command=lambda: buttonState(9,buttonStates), bg='blue')
    b11 = t.Button(root, text='', command=lambda: buttonState(10,buttonStates), bg='blue')
    b12 = t.Button(root, text='', command=lambda: buttonState(11,buttonStates), bg='blue')
    b13 = t.Button(root, text='', command=lambda: buttonState(12,buttonStates), bg='blue')
    b14 = t.Button(root, text='', command=lambda: buttonState(13,buttonStates), bg='blue')
    b15 = t.Button(root, text='', command=lambda: buttonState(14,buttonStates), bg='blue')


    b = [b1,b2,b3,b4,b5,b6,b7,b8,b9,b10,b11,b12,b13,b14,b15]

    for button, bindex in zip(b, range(len(b))):
        button.grid(row=bindex+1, column= 1)
    
#
#def evaluateInputs():
#    #evalua según los botones que fueron pulsados o no la probabilidad de 
#    #que sea esta o aquella deficiencia nutritiva
#    
#    #la sintaxis "A If B else C" podría ser linda de usar acá
#    #de igual manera la función map() podría ser útil, o el usar lambda functions
#    
#    #cada boton es un sintoma y tiene su respectivo índice
#    #la base para el funcionamiento correcto de esta evaluación es que haya una función
#    #que toma todos los síntomas que respectan a enfermedad, suma los estados del botón
#    #sea 0 o sea 1, los promedia
#    #finalmente dentro de "evaluate inputs se escupen las enfermedades que tengan score
#    #superior a 70% de posibilidad de estar enfermas
    
#def createFunctButton():
#    #crea los botones "especiales de la intefaz de usuario"
#    
#    bResult = t.Button(root, text='Diagnosticar', command=lambda: x, bg='blue')
#    bInfo = t.Button(root, text='info', command=lambda: x, bg='blue')
#    
#    bF = [bResult, bInfo]
#        
createSympLabels()
createSympButton()

print("\n",buttonStates)





root.mainloop()
print(buttonStates)
