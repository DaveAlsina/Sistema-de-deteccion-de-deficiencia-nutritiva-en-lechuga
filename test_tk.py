#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr  5 12:08:39 2020

@author: david
"""
import tkinter as t
from numpy import zeros

root = t.Tk()
#creating a label widget
l0 = t.Label(root, text="Sistema de ayuda")


#creating the set of symptomps labels
l1 = t.Label(root, text="Amarillamiento de las hojas viejas cercanas a la base de la planta: ")
l2 = t.Label(root, text="Crecimiento desacelerado o detenido: ")
l3 = t.Label(root, text="Tallos marcadamente delgados o leñosos: ")
l4 = t.Label(root, text="Coloración purpura en hojas o tallos:  ")

#creating the buttons for those labels
l_b = t.Label(root, text="Click al boton si tiene el síntoma")
l_b.grid(row=0, column=1)   #putting the label in the window grid

l = [l0,l1,l2,l3,l4]

def buttonState(index, bState):
    if bState[index] == 0:
        bState[index] = 1
        
    else: 
        bState[index] = 0
        
    state = t.Label(root, text=str(int(bState[index])))
    state.grid(row=index+1, column= 2)
    
    
bState = zeros(len(l)-1)  #creates a state saver for the button







#for selecting the color it can be used the #adfff00 system Hex-Color-Code

b1 = t.Button(root, text='', command=lambda: buttonState(0,bState), bg='blue')
b2 = t.Button(root, text='', command=lambda: buttonState(1,bState), bg='blue')
b3 = t.Button(root, text='', command=lambda: buttonState(2,bState), bg='blue')
b4 = t.Button(root, text='', command=lambda: buttonState(3,bState), bg='red')

b = [l_b,b1,b2,b3,b4]
  

for label, row, button in zip(l, range( len(l) ), b):
    label.grid(row=row, column=0)  #putting the label in the window grid
    button.grid(row=row, column=1) #putting the button in the window grid

    



root.mainloop()