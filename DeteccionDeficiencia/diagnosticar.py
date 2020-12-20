#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr  7 13:34:59 2020

@author: david
"""
import re
import pandas as pd
import tkinter as tk
from numpy import zeros
import infoWin as iw
from os import getcwd
from PIL import Image
import sys

l1 = "*Recuerde, primero ingrese a la carpeta 'ProgrammingProyect' y ejecute desde allí el código* "
l2 = "si se encuentra en el directorio 'ProgrammingProyect' sólo presione ['Enter']:"

path =input(l1+"\n"+l2)

if path == '':
    path= getcwd()+'/'
    print(path)
else:
    path=path



class Deficiency:
    
    """Clase que crea una ventana de interacción con el usuario para que este
    Seleccione los síntomas de deficiencias nutritivas que presenta la planta
    Y se haga un diagnóstico basado en estos síntomas.
    """
    
    def __init__(self, root):

        """__init__ (self, root), Función inicial que recibe un objeto de la clase Tk(), y que
        lee el documento csv (Síntomas), con el construye un dataframe de la librería pandas, 
        se llaman algunas funciones dentro de la clase, con las que se construye la ventana
        principal."""
        
        #reads the csv and stores the readings into data
        data = pd.read_csv(path + 'data/' +'sintomas.csv')  
        
        self.df = pd.DataFrame(data)    #creates a pd dataframe based on 'data'
        self.df = self.df.fillna(0)     #fills the NaN values of the 'DataFrame' object with 0
        self.root = root                #takes the tk window and assigns it as an attribute
        
        self.createButtons()        #creates all the buttons 
        
        self.diseaseButton()        #creates the data structure that allows to 
                                    #link the different buttons and its indexes with the 
                                    #different diseases, ex: [buttons 0,3,4,7 are buttons 
                                    #that correspond to symptoms that are related with Nitrogen
                                    #deficiency]
                                    
        self.createLeftLabels()     #creates the labels containing the symptoms text 
                                    #for the left side of the inteface, and appends next to that 
                                    #the corresponding button for tracking its state wheter is 
                                    #'pressed for afirmation of having he symptom' or
                                    #'not pressed for negative of having the symptom' 
                                    
        self.createRightLabels()    #creates the labels containing the symptoms text 
                                    #for the right side of the inteface, and appends next to that 
                                    #the corresponding button for tracking its state wheter is 
                                    #'pressed for afirmation of having he symptom' or
                                    #'not pressed for negative of having the symptom' 
        
#        print(data.iloc[1][2]) #for debugging 
#        print(len(data.iloc[1]),"\n\n") #for debugging
        
        
    def diseaseButton(self):

        """Se lee el archivo csv (deficiencia_items), y basado en este se crea un DataFrame
        que permite relacionar los botones de los síntomas de la interfaz con las distintas
        deficiencias nutritivas que presenta la planta. Contiene la función 'toInt(x)' que 
        juega un rol muy importante (se recomienda leer su documentación).
        """
        
        number = re.compile('\d+')  #creates a object that matches numbers
        deficiency =[]              #creates a lists where the digit matches can be storted
        
        
        data = pd.read_csv(path + 'data/' + 'deficiencia_items.csv') #reads the csv file
        df = pd.DataFrame(data) #converts it into a pandas 'DataFrame'
        
        
        #print(df['Deficiencia'].values)    #for better understanding of the code
        #print(df['items'].values)          #for better understanding of the code
        
        
        for i in df['items'].values:        #gets the values of the columm 'items'
                                            #which are a series of strings in a list 
                                            #that look like this: ['0, 9, 10, 4', ... ,'12 ,13']
                                            
            deficiency.append(number.findall(i))  #finds all the digits and appends the match to 
                                                  #deficiency
                                                  
        #print(defitiency)      #for better understanding
        
        def toInt(x):           #converts the match list to list of integers

            """Convierte los números de la función anterior (los cuales se encuentran en forma 
            string) en enteros para que así crear un nuevo dataframe con los números en enteros."""
            
            new=[]  #list where the converted to int elements of the subsets are stored 
            
            final=[] #list where the subsets converted to int are storted
            
            for Set in x:  #access the lists in the list 'x'
                
                
                for element in Set:             #access the elements in the list 'Set'
                    new.append(int(element))    #appends the converted element to the list
                                
                    
                final.append(new)       #appends the converted new lists to the final list
                new=[]                  #resets new in order to be able to store the other lists
                
            return final                #gives the converted list of lists 
        
        
        
        
        
        deficiency = toInt(deficiency)  #list of strings is converted to list of lists of integers
        
        #print(defitiency)          #for better understanding
        
        
        #actualices the 'DataFrame'  'df' with the values of the new defitiency list
        #and new labels for the columns
        
        df = pd.DataFrame(list(zip(df['Deficiencia'].values, deficiency)),
                          columns= ['defitiency','buttons']) 
                     
                     
        #print(df)                  #for better understanding
        
        self.df_Disease = df        #assigns the transformed 'DataFrame' to the atribute
                                    #'self.df_Disease' in order to get general access
        
        return self.df_Disease
        
        
        
    def monitorButtons(self,index):

        """Aquí se tiene control del estado de los botones; así, al oprimirlo, éste cambia 
        de 0 a 1, y si se vuelve a oprimir volverá a 0. Adicionalmente se da el cambio de 
        color al oprimirlo."""
        
        
        if self.buttonStates[index] == 0:       #if the index was originally 0
            self.b[index].configure(bg='red')   #changes the button color to red
            self.buttonStates[index] = 1        #changes the button state value to 1
            
        else:                                   #if the index was originally 1
            self.b[index].configure(bg='blue')  #restores the button color to blue
            self.buttonStates[index] = 0        #restores the button state value to 0
                   
     


         
        
    def createLeftLabels(self):

        """En esta función se ubican los síntomas en la sección izquierda de la interfaz gráfica, 
        a partir del dataframe basado en el csv (Sintomas). Si la etiqueta corresponde a texto se 
        colocará, si hay un cero en lugar de texto, no. Si se crea la etiqueta con un sintoma, 
        también se coloca un botón al lado teniendo la precaución de que no quede uno encima de 
        otro y que no se repita el uso de botones."""
        
        buttonIndex=0   #counts in what button index we're in in order
                        #to not repeat button use.
                        
        row=0           #counts the row we're in when applying grid.
        
                
        for col,coln in zip(self.df.columns[1:],range(len(self.df.columns[1:]))):
        
            if coln%2 == 0:      #only for even index columns
                
                label = tk.Label(self.root,text=col, fg = 'blue')  #creates a label for
                                                                   #the column symptom label
                label.grid(row=row,column=0)    #applies the label to the user interface
                row +=1                       #increments the row counter by one
                                            #just when the label is plotted to the interface
                
                
                
                for s in self.df[col]:  #gets the values inside every column
                    
                    
                                    
                    if type(s)==str:    #prooves if the sympt in the column is a valid one
                                        #or a empty space NaN or Zero
                        
                        label = tk.Label(self.root,text=s)  #creates a label for the valid symptom
                        label.grid(row=row,column=0)        #puts the label in the interface
                        
                        self.b[buttonIndex].grid(row=row, column=1) #adds a button next to the label
                        
                        row +=1             #increases the row counter
                        buttonIndex += 1    #increases the button counter 
                
                
                separator = tk.Label(self.root,text='- - -')    #creates a separator label
                                                                #for stetic reasons
                separator.grid(row=row,column=0)                #appends it just below the last
                                                                #label that was added
                row +=1                             #increases the row count by 1
                
        self.buttonIndex = buttonIndex   #stores the actual remaining buttons
                                         #indicated by the index
                
      
        
        
        
    def createRightLabels(self):

        """En esta función se ubican los síntomas en la sección derecha de la interfaz gráfica, 
        a partir del dataframe basado en el csv (Sintomas). Si la etiqueta corresponde a texto 
        se colocará, si hay un cero en lugar de texto, no. Si se crea la etiqueta con un sintoma, 
        también se coloca un botón al lado teniendo la precaución de que no quede uno encima de
        otro y que no se repita el uso de botones."""
        
        buttonIndex= self.buttonIndex   #counts in what button index we're in in order
                                        #to not repeat button use
                        
        row=0           #counts the row we're in when applying grid
        
                
        for col,coln in zip(self.df.columns[1:],range(len(self.df.columns[1:]))):
        
            if coln%2 != 0:      #only for odd index columns
                
                label = tk.Label(self.root,text=col, fg = 'blue')  #creates a label for
                                                                   #the column symptom label
                label.grid(row=row,column=3)    #applies the label to the user interface
                row +=1                       #increments the row counter by one
                                            #just when the label is plotted to the interface
                
                
                
                for s in self.df[col]:  #gets the values inside every column
                    
                    
                                    
                    if type(s)==str:    #prooves if the sympt in the column is a valid one
                                        #or a empty space NaN or Zero
                        
                        label = tk.Label(self.root,text=s)  #creates a label for the valid symptom
                        label.grid(row=row,column=3)    #puts the label in the interface
                        
                        self.b[buttonIndex].grid(row=row, column=4) #adds a button next to the label
                        
                        row +=1            #increases the row counter
                        buttonIndex += 1   #increases the button counter 
                
                
                separator = tk.Label(self.root,text='- - -')#creates a separator label
                                                            #for stetic reasons
                separator.grid(row=row,column=3)   #applies the label to the user interface
                row +=1                            #increments the row counter by one
                                         #just when the label is plotted to the interface
        
        
    def makeDiagnosis(self):

        """Ejecuta un diagnóstico al leer el estado de los botones dado por el método 
        "monitorButtons", con lo cual crea una lista de tuplas de la forma 
        (True/False, porcentaje de incurrencia de síntomas, nombre de la deficiencia de nutrición).
         se la asigna al atributo: 'self.r'"""
        
        diagnosis = []  #stores the results of the probability calculation of having
                        #a nutrient deficiency, for every nutrient deficiency
                        
        result=0    #stores the calculation of the probability of having a nutrient 
                    #deficiency, before it gets storted in the list 'diagnosis'
        
        for buttonList in self.df_Disease['buttons']:      
            
            for button in buttonList:
                result += self.buttonStates[button] #sums the values of the found button states
                
            result = result/len(buttonList) #gets the mean 
            diagnosis.append(result)    #appends the mean to the lists
            result = 0                  #resets the 'result' value to zero
                                        #in order to be able to use the variable again for 
                                        #other calculations 
        
        
        #the iterable given to the lambda function in map is a tuple given by enumerate 
        #which looks like follows: (index,value), lambda takes the tuple and compares 
        #if one of the values is greater than 70%, puts the number of % next to it
        #and finally adds the corresponding label of disease, so the output of lambda looks like:
        #('True/False', 'x %', 'label')
        
        r = map(lambda data: (data[1]>0.7, data[1], self.df_Disease['defitiency'][data[0]])
        , enumerate(diagnosis)) 
        
        #The result of the previous map function use is converted to a list and storted in the 
        #atribute 'self.r' for better access.
        self.r = list(r)
                
    
    def graphicGuide(self, keypressb):
        
        """Función que muestra una imagen de guía para el usuario."""
        
        img = Image.open(path+'imgs/'+'guia.png')       #opening fist help image
        img2 = Image.open(path+'imgs/'+'guia_2.png')    #opening second help image
        
        #showing both images into the screen
        img.show()  
        img2.show()                 
        
        
    def createButtons(self):

        """Se crean todos los botones colocados al lado de los síntomas, se empaquetan en la lista 'b' 
        y se crea el atributo 'self.b' que contiene todos los botones. Además se crea la lista
        buttonStates (que es la encargada de guardar los estados de los botones, que pueden ser: 
        oprimido/ no oprimido) y se le asigna el atributo 'self.buttonStates'."""
        
        #creation of all the buttons for every symptom that was found in the 'sintomas.csv' file 
            
        b1 = tk.Button(root, text='', command=lambda: self.monitorButtons(0) , bg='blue')
        b2 = tk.Button(root, text='', command=lambda: self.monitorButtons(1) , bg='blue')
        b3 = tk.Button(root, text='', command=lambda: self.monitorButtons(2) , bg='blue')
        b4 = tk.Button(root, text='', command=lambda: self.monitorButtons(3) , bg='blue')
        b5 = tk.Button(root, text='', command=lambda: self.monitorButtons(4), bg='blue')
        b6 = tk.Button(root, text='', command=lambda: self.monitorButtons(5), bg='blue')
        b7 = tk.Button(root, text='', command=lambda: self.monitorButtons(6), bg='blue')
        b8 = tk.Button(root, text='', command=lambda: self.monitorButtons(7) , bg='blue')
        b9 = tk.Button(root, text='', command=lambda: self.monitorButtons(8), bg='blue')
        b10 = tk.Button(root, text='', command=lambda: self.monitorButtons(9) , bg='blue')
        b11 = tk.Button(root, text='', command=lambda: self.monitorButtons(10), bg='blue')
        b12 = tk.Button(root, text='', command=lambda: self.monitorButtons(11), bg='blue')
        b13 = tk.Button(root, text='', command=lambda: self.monitorButtons(12), bg='blue')
        b14 = tk.Button(root, text='', command=lambda: self.monitorButtons(13) , bg='blue')
        b15 = tk.Button(root, text='', command=lambda: self.monitorButtons(14), bg='blue')
        b16 = tk.Button(root, text='', command=lambda: self.monitorButtons(15), bg='blue')
        b17 = tk.Button(root, text='', command=lambda: self.monitorButtons(16), bg='blue')
        b18 = tk.Button(root, text='', command=lambda: self.monitorButtons(17), bg='blue')
        b19 = tk.Button(root, text='', command=lambda: self.monitorButtons(18), bg='blue')
        b20 = tk.Button(root, text='', command=lambda: self.monitorButtons(19), bg='blue')
        b21 = tk.Button(root, text='', command=lambda: self.monitorButtons(20), bg='blue')
        b22 = tk.Button(root, text='', command=lambda: self.monitorButtons(21), bg='blue')
        b23 = tk.Button(root, text='', command=lambda: self.monitorButtons(22), bg='blue')
        b24 = tk.Button(root, text='', command=lambda: self.monitorButtons(23), bg='blue')
        b25 = tk.Button(root, text='', command=lambda: self.monitorButtons(24), bg='blue')
        b26 = tk.Button(root, text='', command=lambda: self.monitorButtons(25), bg='blue')
        b27 = tk.Button(root, text='', command=lambda: self.monitorButtons(26), bg='blue')
        b28 = tk.Button(root, text='', command=lambda: self.monitorButtons(27), bg='blue')
        b29 = tk.Button(root, text='', command=lambda: self.monitorButtons(28), bg='blue')
        b30 = tk.Button(root, text='', command=lambda: self.monitorButtons(29), bg='blue')
        b31 = tk.Button(root, text='', command=lambda: self.monitorButtons(30), bg='blue')
        b32 = tk.Button(root, text='', command=lambda: self.monitorButtons(31), bg='blue')
        b33 = tk.Button(root, text='', command=lambda: self.monitorButtons(32), bg='blue')
        
        #creation of the button 'Diagnosticar' and its display in the main window
        #this button allows to make the diagnosis process 
        bd = tk.Button(root, text='Diagnosticar', command=self.diagnosis, bg='orange')
        bd.grid(row=30,column=2)
        
        #creation of the button 'Guia gráfica' ands its display in the main window
        #this button allows to have access to a graphic guide for the user in the interface
        gb = tk.Button(root, text='Guia gráfica', command=self.graphicGuide, bg='yellow')
        gb.grid(row=28,column=2)
    
        self.b = [b1,b2,b3,b4,b5,
                  b6,b7,b8,b9,b10,
                  b11,b12,b13,b14,b15,
                  b16,b17,b18,b19,b20,
                  b21,b22,b23,b24,b25,
                  b26,b27,b28,b29,b30,
                  b31,b32,b33]          #list with all the created buttons 
            
            
        self.buttonStates = zeros(len(self.b)) #list filled with as many zeros as buttons in 'self.b'
        #for the purpose of keeping track of every button state, all of them begin in 'no pressed state'
        #which can be translated to '0', that's why the list is filled with zeros in the first place
        
        
    def __str__(self):

        """Se le añade un formato de impresión en el que se muestra el resultado"""
        
        return "Diagnosis after all the process is: "+ "\n"+ str(self.r)
            
    def diagnosis(self, keypress=0):
        
        """Habilita la relaización de un diagnóstico y cierra la ventana principal"""
        
        self.enableDiag=True #creates the atribute responsible of enabling the diagnosis process
        self.root.destroy()  #closes the main window
        
    def kill(self, keypress=0):
        
        """Cierra la ventana principal y acaba la ejecución del programa"""
        self.root.destroy() #closes the main window
        sys.exit() #kills the program execution




#creates a root for the welcome to the user
welcome = tk.Tk()

txt_ = "Bienvenido :), Este programa busca ayudarte en la tarea de conocer\n \
        el estado de tus plantas tratando en específico el tema de deficiencias nutritivas y sus síntomas.\n\n\
        Lo primero que verás serán una serie de síntomas con botones a su lado, oprímelos si\n \
        tus plantas presentan alguno de estos, si en algún momento te sientes perdido puedes\n \
        presionar \"h\" para obtener una guía gráfica que te oriente mejor, o directamente pulsar en\n\
        \"guía gráfica\", una vez hayas acabado de seleccionar síntomas, presiona \"Diagnosticar\" o oprime \"d\".\n\
        Éxitos con tu diagnóstico, si decides salir del programa puedes presionar 'q' o cerrar la pestaña.\n\n\
        Buscando la exactitud para tí solo mostramos diagnósticos con más del 70% de probabilidad de ser acertados :).\n"

#label with the welcome text 
Wlabel = tk.Label(welcome, text=txt_, font=("Times", "12", "bold italic"), bg="pink")
Wlabel.grid(row=0, column=0)

#allows to close the window with the key press 'q'
welcome.bind("q", lambda x: welcome.destroy())
welcome.mainloop()



#creates an object of the class 'Tk()', basically a window widget       
root= tk.Tk()       

#adds a title to that window
root.title("Sistema de ayuda en detección de deficiecias nutritivas en plantas")


d = Deficiency(root)        #passes the window to the Deficiency class in order to be modified and 
                            #transformed to the actual main window that's displayed in the beggining

root.bind("q", d.kill)      #sets a keypress event for killing the program when 'q' is pressed

root.bind("d", d.diagnosis) #sets a keypress event for enabling diagnosis process when 'd' is pressed

root.bind("h", d.graphicGuide)  #sets a keypress event for showing a graphic guide for the user
                                #to get better understanding when 'h' is pressed

root.mainloop()

if d.enableDiag == True:
    
    d.makeDiagnosis()    #makes the diagnosis based on the inputs given to the user interface
    
    iw.diagnosisWin(d.r) #the result of the diagnosis is passed to diagnosisWin()
                         #which creates a window that allows to see the results and get
                         #some extra information around the found diseases
    print (d)            #for debuggin and seeing how this works

else:
    sys.exit() #in case that there was no habilitation of diagnosis and the window was destroyed
