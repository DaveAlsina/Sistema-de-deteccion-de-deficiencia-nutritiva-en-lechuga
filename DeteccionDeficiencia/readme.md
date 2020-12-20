#Guia de uso
---------------------------

Para poder efectivamente ejecutar el código:
asegúrese de que el directorio de trabajo actual desde el que está ejecutando el cógido
sea el de 'DeteccionDeficiencia', de lo contrario no podrá ejecutar el código.

Habrán casos en que la interfaz al ejecutarse no funciona o se ve buggeada, en este caso 
mate la ejecución del código y vuelva a repetir el proceso de ejecutarlo. 

Finalmente ejecute y disfrute de la asistencia en diagnóstico que ofrece este sistema :).

##precausiones con los datos
------------------------------


Esta carpeta contiene los códigos base "diagnosticar.py"
y "infoWin.py" necesarios para ejecutar la ayuda en diagnósico
que ofrece este código, en las carpetas "data" e "imgs" encontrará
bases de datos en formato "csv" para el la primera carpeta y 
en la segunda series de imágenes en formato "png" y "jpg"

***Por favor no los altere sin antes asegurarse de que sabe lo que
está haciendo, en otro caso podría llegar a dañar la funcionalidad
de la solución de código y se vería obligado a reinstalarlo***.


##fuentes y manejo de los datos
------------------------------

Todas las imágenes usadas y la información que se da sobre síntomas
y diagnóstico están respaldadas con el respectivo link de donde se han 
obtenido y en el caso de la información de deficiencias, esta se encuentra
citada en el documento "Datos Deficiencias Nutricionales.pdf" en la carpeta
'fuentes _ y _ documentación'.


##disclaimer
-----------------------

Esta solución implementada en python no pretende ser una guia absoluta 
sobre las deficiencias de las plantas, pretende ser solo orientativa y 
de fines didácticos, para así lograr diagnosticar mejor las plantas, 
los creadores de este cógido no se hacen responsables por las acciones que
se tomen a partir del uso de este código y sus diagnósticos. El uso que se 
de a este cógido es total responsabilidad del usuario.




##Documentación
---------------



#### Archivo ‘Diagnosticar 

Este archivo lo primero que hace es importar las librerías ‘re’, ‘pandas’, ‘tkinter’, la función ‘zeros’ de ‘numpy’,  el módulo ‘InfoWin’, la función ‘getcwd’ de ‘os’, la clase de ‘PIL’ llamada ‘Image’, e importa finalmente ‘sys’.

Tras realizar estas importaciones empieza el proceso más importante de este módulo que es la creación de la clase ‘Deficiency’ y sus métodos:

 En primer lugar se ejecuta el método ‘__init__()’ en el que se crea un DataFrame de pandas basado en la lectura del archivo ‘síntomas.csv’(archivo que contiene una serie de síntomas de las deficiencias agrupados por categorías) y se lo asigna a un atributo de la clase, cuidando reemplazar los valores que están en ‘NaN’ con ceros, para más adelante poder omitirlos a la hora de fijar síntomas en la interfaz,  además se recibe un objeto de la clase Tk(), es decir una de ventana de tkinter a la cual se le harán una serie de transformaciones, y para hacer fácil su uso se lo asigna a un atributo de la clase, tras esto se ejecutan varios métodos de la clase que se encargaran de crear los botones que se añaden a la ventana (‘createButtons()’), se ejecutan métodos que se encargan de relacionar los distintos botones en la interfaz con los distintos síntomas correspondientes a enfermedades (‘diseaseButton()’), también se ejecutan ‘createLeftLabels()’ y ‘createRightLabels()’ métodos que respectivamente, ponen las etiquetas que se ven en la sección izquierda de la interfaz y en la sección derecha de la interfaz de usuario.

En segundo lugar se define el método ‘diseaseButton()’, inicialmente se lee el archivo ‘deficiencia_items.csv’ (archivo que contiene los nombres de las deficiencias y junto a estos una lista de números que corresponden a los botones de la interfaz gráfica, contados de arriba a abajo, partiendo primero por la sección izquierda y luego la derecha, esto con el fin de relacionar los botones de los síntomas con las enfermedades que los causan), a partir del cual se crea un DataFrame para obtener comodidad de acceso a los datos, sin embargo, este DataFrame que ha sido generado aún no puede ser correctamente utilizado para relacionar los botones ordenados por números con las distintas deficiencias nutritivas, ya que una de las columnas del DataFrame en concreto tiene los datos pero en formato String, y lo que se requiere es usar números para relacionar el índice numérico del botón con su enfermedad, luego lo que viene a continuación es la definición de la función ‘toInt()’ que se encarga de convertir los dígitos en String que fueron encontrados, a dígitos en valores enteros numéricos que puedan ser usados, tras esta tarea se crea un nuevo DataFrame que contiene los datos en un formato correcto para su uso, y se le asigna a un atributo para su fácil acceso. (para ilustrar mejor el problema anterior se muestra este ejemplo): 

inicialmente sucedía esto (el DataFrame lucía similar):

\#notamos que los números son un solo string

Deficiencia | Botones
-------------- | --------------
Nitrógeno	|	['0, 9, 10, 4'] 

*después de capturar los dígitos con expresiones regulares se obtiene:*

\#cada dígito es un string

Deficiencia | Botones
-------------- | --------------
Nitrógeno	|	[‘0’, ‘9’, ‘10’, ‘4’] 


después de pasar por la función ‘toInt()’:


\#cada digito ya se ha convertido a entero

Deficiencia |	Botones
--------------	|	--------------
Nitrógeno	|	[0, 9, 10, 4] 

Saltando a la documentación de la función ‘monitorButtons()’ notamos que recibe como parámetro un índice, el cual corresponde al índice único de cada botón, basado en este índice único ‘monitorButtons()’ cambia el estado de ese botón en la lista que almacena los estados de los botones, lo cambia a ‘0’ si estaba en ‘1’ o a ‘1’ si estaba en ‘0’, y con ello el color del botón, para indicar que no está presionado lo pone azul, para indicar que está presionado lo pone en rojo, (tener en cuenta las listas con las que accede a los estados de los botones, y la lista con la que accede a los botones fueron creadas en la función ‘createButtons()’).     

	Tratando el método ‘graphicGuide()’ tenemos que es uno bastante sencillo, encargado de abrir dos imágenes que sirven como orientación al usuario, cuando este da click en el botón ‘Guía Gráfica’ (que fue creado en ‘createButtons()’), o cuando presiona la tecla ‘h’.


Pasando a la documentación del método ‘createButtons()’ tenemos que se crean 33 botones exactamente iguales excepto porque difieren en el valor que pasan a la función ‘monitorButtons()’ en el ‘command’ del botón, partiendo de  ‘monitorButtons(0)’ hasta ‘monitorButton(32)’, esto es porque cada botón tiene su índice único, que generará ciertos cambios en una lista que almacena los estados de los botones, ejemplo: dado que son 32 botones hay que vigilar 32 estados, sean ‘0’ para no oprimido y ‘1’ para presionado, el índice ‘0’ en esa lista me daría acceso al registro del estado de ese botón (del primer botón), tal cual se ha explicado en la documentación de la función ‘monitorButtons()’, continuando con la idea de que hay 32 botones que vigilar y que se debe acceder a ellos con comodidad, se empaquetaron en una lista todos estos objetos botón, y se creó otra lista rellena con tantos ceros como botones habían en la lista anterior, para mantener así el registro del estado de estos botones, finalmente estas listas fueron asignadas a atributos de la clase, por otra parte también se crearon los botones ‘Diagnosticar’ (encargado de habilitar el diagnóstico con el método ‘diagnosis()’) y ‘Guía gráfica’ (encargado de ejecutar el método ‘graphicGuide()’).

Respecto a los métodos ‘createRightLabels()’ y ‘createLeftLabels()’ en primer lugar hay que decir que son métodos prácticamente idénticos, por lo que se ha decidido juntar la explicación de ambos, en este bloque, inicialmente en ‘createLeftLabels()’ se crea el contador para las filas (con el fin de que no se pongan unas etiquetas encima de otras), y se crea un contador para los botones (con el fin de que no se repitan botones y se causen errores en la interfaz gráfica), después de esto se revisa en el DataFrame que fue creado con base al documento ‘sintomas.csv’ y basado en si las columnas del DataFrame son columnas de índice par, se empiezan a pegar en la interfaz todos los textos de los síntomas que están en esa columna del DataFrame, con su respectivo botón al lado para monitorear si se presenta o no ese síntoma, al acabar, la cuenta de los botones usados se guarda en un atributo, que será la base para el contador de botones del método ‘createRightLabels()’, que hace lo mismo que  ‘createLeftLabels()’ sólo que en lugar de las columnas pares, este método pega los síntomas de las columnas impares, junto con sus botones de vigilancia.

En lo relativo al método ‘makeDiagnosis()’, tenemos que aquí es donde se efectúa el diagnóstico basado en los estados de los botones que fueron modificados por el usuario, en primer lugar se acude al DataFrame que fue creado en base al archivo ‘deficiencia_items.csv’ (archivo que contiene los nombres de las deficiencias y junto a estos una lista de números que corresponden a los botones de la interfaz gráfica, contados de arriba a abajo, partiendo primero por la sección izquierda y luego la derecha, esto con el fin de relacionar los botones de los síntomas con las enfermedades que los causan),  con este DataFrame como base se empiezan a revisar los estados de los botones relevantes a cada deficiencia, se suman sus estados, y se dividen en la cantidad de botones que eran relevantes para esa deficiencia, obteniéndose la probabilidad de padecer la deficiencia nutritiva, la probabilidad y el nombre de la respectiva deficiencia son pasados a una función ‘map()’ que se encarga de establecer unas comparaciones y organización de los datos para producir una lista de tuplas que se ve como la siguiente: [(True, 0.7, ‘Nitrógeno’), … ,(False, 0.66, ‘Azufre’)] la cual corresponde finalmente al diagnóstico, este diagnóstico se guarda en un atributo para su fácil uso.

El método por sobrecarga de operadores: ‘__str__()’ se encarga básicamente de retornar un texto junto con la lista de los resultados del diagnóstico.

El método ‘diagnosis()’ sirve para crear una variable booleana atributo, que anuncia que se puede realizar un diagnóstico, también se encarga de cerrar la pestaña principal de los síntomas, este método suele ser llamado o al presionar el botón ‘Diagnosticar’ o al oprimir ‘d’.

El método ‘kill()’, se encarga de cerrar la pestaña principal de síntomas, y de terminar la ejecución del programa, este es llamado cuando presionan la ‘q’ en la interfaz de la ventana principal.




#### Archivo ‘InfoWin’

Este archivo lo primero que hace es importar las librerías ‘tkinter’, ‘pandas’ y ‘re’, la clase de ‘PIL’ llamada ‘Image’,  la función ‘getcwd’ y ‘listdir’ de ‘os’ e importa finalmente la función ‘unidecode’ de ‘unidecode’.

Tras realizar estas importaciones empieza el proceso más importante de este módulo que es la creación de la función ‘diagnosisWin()’ y sus métodos.
lo primero que hace esta función es crear el objeto de la clase ‘Tk()’ que se nombra ‘root_d’ y se titula ‘Diagnostico’, una vez creado el objeto es posible dar atributos y etiquetas, para ello se crea primero un contador llamado ‘row’ que se usará para contar las filas en la venta y cada vez que el proceso se repite cambia de fila en aumento de una a la vez (que sirve para evitar la superposición de textos en una misma fila), seguido por el proceso de crear la lista de botones (gracias a la función ‘createInfoButtons()’), así se le asigna dicha lista a la variable ‘ib’ que se usará con la ventana ‘root_win’, ahora pasamos al for en donde se usa ‘enumerate(diagnosis)’ para obtener una tupla así: ("Número de elemento", "Elemento"), por ejemplo: ( 0, (False, 0.5, 'Nitrógeno') ).

 Luego del For, sigue la parte del if en donde si ‘symp[0]’ es verdadero, es una deficiencia con alta probabilidad de acertar y de este modo se ejecuta el if de lo contrario no. El if modifica  a  la lista ‘disease’ agregándole las deficiencias con la alta probabilidad de ser reales, por otra parte se calcula ‘percentaje’ variable que guarda el ratio anterior, convertido a porcentaje. De esta forma hemos llegado a la parte nombrada hace un momento en donde se crean las etiquetas para  esta ventana y que se nombran ‘label’, de la clase ‘Label()’, las cuales tienen por texto: el nombre de la deficiencia y el porcentaje, posteriormente  se posicionan las etiquetas con ‘.grid()’ y a su vez se posiciona un botón con el index correspondiente a la deficiencia para dar acceso al usuario a la ventana que contiene la información extra sobre la deficiencia usando la función ‘readExtraInfo()’,  finalizando este proceso encontramos el row += 1, que como dijimos anteriormente aumenta un valor cada vez que se itera a través del for.

Así es como llegamos la función ‘createInfoButtons()’ que se usa para la creación de 27 botones los cuales serán los tendrán conexión con el manejo de la información de los archivos .csv, debido a que se les asignó un índice numérico que reemplaza el nombre de las deficiencias nutritivas, índice con el cual se puede acceder a los cuadros de datos y a la información específica que contienen, aclarando que estos botones nos dan acceso a la información desde ‘readExtraInfo(‘index’)’.  También cabe mencionar que esta serie de botones se agruparon en una lista, la cual permite su fácil acceso y uso a través de índices.

Pasamos ahora a la función ‘readExtraInfo()’ la cual es usada para la creación de la ventana que amplía la información de las deficiencias halladas luego de que se efectuase el diagnóstico con las entradas dadas por el usuario en ‘Diagnosticar.py’, basado en el DataFrame construido a partir de la lectura de ‘ExtraInfoDiseases.csv’, se agrega la respectiva etiqueta con el texto relativo a la información extra sobre la deficiencia nutritiva, esta viene nombrada indirectamente por el índice que le es pasado a la función (como se ha explicado antes se usan índices en lugar de nombres), finalmente se agrega el botón ‘mostrar imagen’, que se encarga de ejecutar la función ‘imgWin()’ al ser clicado.

La función ‘imgWin()’ se usa para el manejo de las imágenes ayudando al fácil acceso ya que cada deficiencia tiene una y a veces dos imagenes que mostrar (estas distintas imágenes tienen  nombres ligeramente diferentes pero con patrones comunes, fueron pensados de esta manera), lo primero en hacerse es transformar el nombre de la deficiencia nutritiva (al que se accedió haciendo uso del DataFrame construido en base al documento ‘ExtraInfoDiseases.csv’) a uno que coincida con el formato de los nombres de las imágenes, usando el código ASCII se convierte todo el texto en uno sin caracteres especiales como tildes y demás, también se deja todo el texto en minúscula usando el método de Strings ‘lower()’ .

Así mismo se usa ‘re.compile( “nombre de la deficiencia” + "\_*"+ "\d*"+ "\.*" + "\w+")’, para crear una expresión regular basada en el  nombre de la deficiencia nutritiva, que permita encontrar imágenes con el nombre de  la forma:
“nombre de la deficiencia nutritiva”_"dígitos"."cualquier tipo de archivo", otro ejemplo sería: 

Dado nombre de la deficiencia igual a: “nitrógeno” la expresión regular va a encontrar texto de la forma:  
“nitrogeno.[tipo de imagen]” o puede también ser de la forma “nitrogeno_1.[tipo de imagen]”.

	La siguiente etapa es leer el directorio actual, en concreto migrando hacia la carpeta de imágenes titulada ‘imgs’, en la cual se encuentran todas las imágenes, una vez leído el directorio con ‘listdir()’ se obtendrá una lista de nombres de los archivos de las imágenes, estos nombres serán unidos para crear una gran línea de texto a la cual se le puede aplicar la expresión regular para encontrar los archivos que nos interesan, el texto se unirá a través de la función ‘.join()’, y se encontrarán los textos que cumplen la descripción de la expresión regular a través del ‘.findall()’, después de encontrados se abren los distintos archivos de imagen.


