#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr  9 16:24:11 2020

@author: david
"""

import tkinter as tk               #Se importa la libreria -tkinter- y se renombra -tk- por eficiencia al invocarla
import pandas as pd                #Se importa la libreria -pandas- y se renombra -pd- por eficiencia al invocarla
from PIL import Image              #Se importa -Image- de la libreria -PIL-
from os import listdir, getcwd     #Se imports -listdir- y -getcwd- de la libreria -os-
import re                          #Importa la libreria -re- 
from unidecode import unidecode    #Se importa -unidecode- de -unidecode- 




l1 = "*Recuerde, primero ingrese a la carpeta 'ProgrammingProyect' y ejecute desde allí el código* "
l2 = "si se encuentra en el directorio 'ProgrammingProyect' sólo presione ['Enter']:"

path =input(l1+"\n"+l2)

if path == '':
    path= getcwd()+'/'
    print(path)
else:
    path=path
    
data = pd.read_csv(path + 'data/ExtraInfoDiseases.csv')
df = pd.DataFrame(data)
    
#La entrada de datos principal de este modulo se ve de la siguiente forma:
        
    # diagnosis = [(False, 0.5, 'Nitrogeno'), (True, 0.7333333333333333, 'Azufre'),
    #             (False, 0.14285714285714285, 'Fósforo'), (False, 0.0, 'Silicio'),     
    #             (True, 0.75, 'Boro')]




def diagnosisWin(diagnosis): 
    """
    La función diagnosisWin() maneja los datos del proceso de seleción que realizo el usuario así 
    mismo crea otra ventana que retorna al usuario el diagnostico porcentual y que es nombrada -Diagnóstco-
    y en la que se agregaron botones para 1ro crear otra ventana en la cual se amplia la información que esta
    asignada a cada deficiencia y que es nombrada Información pero eso es en otra función, 2do en esa ventana 
    tambien se maneja un boton, pero en este caso el boton amplia la información de la deficiencia 
    graficamente con una o en algunos casos dos imagenes correspondientes a la información de la deficiencia, 
    esto también sucede más adelante en otra funcíon. 
    """
    
    
    
    #Creación función -diagnosisWin-
    #el parametro de entrada diagnosis es de la siguiente forma:
    
    #[(False, 0.5, 'Nitrogeno'), (False, 0.3333333333333333, 'Azufre'), 
    #(False, 0.14285714285714285, 'Fósforo'), 
    #(False, 0.0, 'Silicio'), (True, 0.75, 'Boro')]
    
    root_d = tk.Tk()                #Se crea el objeto de la clase -tk- y se nombra -root_d- 
    root_d.title("Diagnóstico")     #Se titula el objeto con el nombre de -Diagnostico- 
    
    
    disease = []                    #Se crea una lista vacia llamada -disease- va a contener
    row=0                           #Se define -row- como contador y se inciara en cero, 
#    bcount = 0
    
    ib = createInfoButtons(root_d)  #Se crea la lista de botones y se le asigna a la variable ib
    
    for indx, symp in enumerate(diagnosis):     
    #Se usa enumerate(diagnosis) para obtener una tupla asi: ("Numero de elemento","Elemento") 
        #Ej: (0,(False, 0.5, 'Nitrogeno'))
        
        #print(symp,"\n",indx,"\n") #(Codigo de prueba) 
        
        if symp[0] == True:                    
        #Si symp[0] es verdadero, es una deficiencia con alta probabilidad de acertar. 
         #Se ejecutara el if de lo contrario no. 
            disease.append(symp)              
            #disease contendra las deficiencias con la alta probabilidad acertada de ser reales.
            percentaje = round(symp[1]*100, 2)
            #Aqui en percentaje se transforma ese ratio a un porcentaje.
            
            label = tk.Label(root_d, 
            text='Detectada deficiencia de {0}, con {1}% de probabilidad'.format(symp[2],percentaje))
            #Basado en el nombre de la deficiencia y su percentaje se crea una etiqueta llamada label. 
        
            #print(indx) (Codigo de prueba)
            
            label.grid(row=row,column=0)        #Se usa el grid para posicionar la etiqueta.
            ib[indx].grid(row=row,column=1)     
            #Se posciciona el boton que da acceso a la información extra de la deficiencia 
            #nutritiva correspondiente esto nuevamente resulta simple por el orden usado en las 
            #bases de datos siempre es el mismo y se pueden remplazar nombre por numeros.
            
            row += 1                            #Aqui se aumenta el contador de filas en uno.
    
    root_d.bind("q", lambda q: root_d.destroy()) #permite cerrar la ventana
    
    root_d.mainloop()       #El rootWin.mainloop() Se usa para mantener ejecutando la ventana rootWin. 
    

    
    
def createInfoButtons(root): #Creación función -createInfoButtons-
    
    """
    La función createInfoButtons() se usa para la creación de los 27 botones y el manejo de la información
    con los archivos .csv ya que tienen un orden y es sencillo manejar de esta información remplazandola por
    indices numericos del 0 a 26 aclarando que estos botones nos dan acceso a la información desde readExtraInfo
    y luego de hacer este proceso los objetos botones los agregamos a una lista llamada ib. 
    """       
    
    #Aqui se estan creando los 27 botones que se necesitaron para proporcionar 
    #información extra respecto a una deficiencia.
    
    #En todos los archvios .csv se maneja el mismo orden de sintomas, 
    #con lo cual resulta mas secillo remplazar los nombres por indices numericos.
    
    #A estos botones se les asigno un valor desde 0 a 26 para darle el mejor manejo. 
    
    #Cada uno de estos botones nos esta dando acceso a la info. que esta almacenada en readExtraInfo. 
    
    ib1 = tk.Button(root, text='info', command=lambda: readExtraInfo(0), bg='blue')
    ib2 = tk.Button(root, text='info', command=lambda: readExtraInfo(1), bg='blue')
    ib3 = tk.Button(root, text='info', command=lambda: readExtraInfo(2), bg='blue')
    ib4 = tk.Button(root, text='info', command=lambda: readExtraInfo(3), bg='blue')
    ib5 = tk.Button(root, text='info', command=lambda: readExtraInfo(4), bg='blue')
    ib6 = tk.Button(root, text='info', command=lambda: readExtraInfo(5), bg='blue')
    ib7 = tk.Button(root, text='info', command=lambda: readExtraInfo(6), bg='blue')
    ib8 = tk.Button(root, text='info', command=lambda: readExtraInfo(7), bg='blue')
    ib9 = tk.Button(root, text='info', command=lambda: readExtraInfo(8), bg='blue')
    ib10 = tk.Button(root, text='info', command=lambda: readExtraInfo(9), bg='blue')
    ib11 = tk.Button(root, text='info', command=lambda: readExtraInfo(10), bg='blue')
    ib12 = tk.Button(root, text='info', command=lambda: readExtraInfo(11), bg='blue')
    ib13 = tk.Button(root, text='info', command=lambda: readExtraInfo(12), bg='blue')
    ib14 = tk.Button(root, text='info', command=lambda: readExtraInfo(13), bg='blue')
    ib15 = tk.Button(root, text='info', command=lambda: readExtraInfo(14), bg='blue')
    ib16 = tk.Button(root, text='info', command=lambda: readExtraInfo(15), bg='blue')
    ib17 = tk.Button(root, text='info', command=lambda: readExtraInfo(16), bg='blue')
    ib18 = tk.Button(root, text='info', command=lambda: readExtraInfo(17), bg='blue')
    ib19 = tk.Button(root, text='info', command=lambda: readExtraInfo(18), bg='blue')
    ib20 = tk.Button(root, text='info', command=lambda: readExtraInfo(19), bg='blue')
    ib21 = tk.Button(root, text='info', command=lambda: readExtraInfo(20), bg='blue')
    ib22 = tk.Button(root, text='info', command=lambda: readExtraInfo(21), bg='blue')
    ib23 = tk.Button(root, text='info', command=lambda: readExtraInfo(22), bg='blue')
    ib24 = tk.Button(root, text='info', command=lambda: readExtraInfo(23), bg='blue')
    ib25 = tk.Button(root, text='info', command=lambda: readExtraInfo(24), bg='blue')
    ib26 = tk.Button(root, text='info', command=lambda: readExtraInfo(25), bg='blue')
    ib27 = tk.Button(root, text='info', command=lambda: readExtraInfo(26), bg='blue')
    
    ib = [ib1,ib2,ib3,ib4,ib5,
          ib6,ib7,ib8,ib9,ib10,
          ib11,ib12,ib13,ib14,ib15,
          ib16,ib17,ib18,ib19,ib20,
          ib21,ib22,ib23,ib24,ib25,
          ib26,ib27]                   #ib es la lista donde se almacenan los objetos botones
    
    return ib                          #Retornamos ib



    
def readExtraInfo(indx):         #Creación función -createInfoButtons-
    
    """
    La función 'readExtraInfo()' se usa para la creación de la ventana que amplía la información de 
    las deficiencias nutricionales halladas, esta funcion es el comando que se ejecuta al oprimir
    cualquiera de los botones que se crearon en la función 'createInfoButtons()', e internamente se 
    puede decir que lo que hace es crear una ventana  nueva con esta información extra y un botón
    que da la posibilidad de acceder a imágenes de la deficiencia nutricional en concreto, para 
    ayudar al usuario a realizar un mejor veredicto sobre la deficiencia. Hay que recordar que como
    parámetro recibe un índice, que corresponde a un nombre de deficiencia nutritiva.
    """    
    
    
    
    rootWin = tk.Tk()            #Se crea el objeto de la clase -tk- y se nombra -rootWin- 
    rootWin.title("Información") #Se titula el objeto ventana clase -Tk- con el nombre de -Información- 
    
    rootWin.bind("q", lambda x: rootWin.destroy()) #permite cerrar la ventana
    rootWin.bind("h", lambda j: imgWin(indx)) #permite cerrar la ventana
    
    label= tk.Label(rootWin, text= df['extra info'].values[indx]) 
    #Se crea una etiqueta de la clase -Label- y se nombra -label- y se tomara como texto la informaciòn extra
    #relativa a la deficiencia seleccionada según .value[index], dado que en todo momento se mantiene el mismo
    #orden de deficiencias se puede decir que esto es equivalente a traer información extra sobre una u otra 
    #deficiencia determinada desde el archivo .csv nombrado antes.
    
    # print(indx, "en read extra info") -(Codigo de prueba)-
    
    label.grid(row=1,column=0)                 
    #Se define en que columna y fila queremos que aparezca esta etiqueta -label- en la vetana rootWin. 
    
    bimg = tk.Button(rootWin, text='mostrar imagen', command=lambda: imgWin(indx), bg='yellow')
    #Se crea un boton de la clase -Button- y se nombra -bimg- el cual dara ejecución a la funcion
    #que muestra la imagen de la deficiencia que se hallo según lo que ha sido escogido por el usuario. 

    bimg.grid(row = 2, column = 0)
    #Se define en que columna y fila queremos que aparezca este button -bquit- en la vetana rootWin.     
    
    rootWin.mainloop()    #El rootWin.mainloop() Se usa para mantener ejecutando la ventana rootWin. 



     
def imgWin(i):                         #Creación función -imgWin-
    
    """
    La función imgWin() Se encarga de dar acceso al usuario a imagenes orientativas a través de la 
    lectura de DataFrames, lectura de los elementos que componen el directorio de trabajo actual,
    transformaciones de texto y uso de expresiones regulares.
    """   
    
    
    matchTxt= df['deficiencia'].values[i] 
    #Toma el nombre de la deficiencia desde el data frame basado en csv que se nombra antes, cuando el 
    #usurio escoge ampliar la informacion en el boton imagen. 
    
    matchTxt = matchTxt.lower() 
    #Se usa lower para convertir en letras minusculas el texto nombre de la deficiencia.
    
    matchTxt = unidecode(matchTxt) 
    #En caso de que el string tenga acentos lo transforma a la representación ASCII posible más cercana
    #con -unidecode(matchTxt)-
    
    #print(matchTxt) (Codigo de prueba)
    
    reg = re.compile( matchTxt + "\_*"+ "\d*"+ "\.*" + "\w+") 
    #Se crea una expresion regular basada en el texto matchTxt para encontrar imagenes con el nombre de 
    #la forma matchTxt_"digitos"."cualquier tipo de archivo" ej: Dado matchTxt = nitrogeno la expresion 
    #regular va a ser de la forma nitrogeno.[tipo de imagen] o puede tambien ser de la forma 
    #nitrogeno_1.[tipo de imagen]  
        
    txt = " ".join(listdir(path+'imgs'))
    #Creación de cadena con los nombres de todos lo archivos dentro de la carpeta imagenes de 
    #-ProgrammingProyect- para posterior matcheo con la expresion regular creada.
    
    mo = reg.findall(txt) #Se encuentra el tipo de imagen/s con el nombre de la deficiencia. 
    
    for imgs in mo: 
        img = Image.open(path+'imgs/'+imgs)
        img.show()                  
    #Muestra las imagenes en la pantalla del Usario
    
    
#diagnosisWin(diagnosis) (Codigo de prueba)
