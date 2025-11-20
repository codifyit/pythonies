#todo valor que pueda ser asignado a una variable tiene asociado un tipo de dato.
'''
Así que los tipos de datos serían las clases (donde se
definen las propiedades y qué se puede hacer con ellas) 
y las variables serían las instancias (objetos) de los tipos
de datos.
'''
#tipo de datos numérico, entero
a = -1 # a es de tipo int y su valor es -1
b = a + 2 # b es de tipo int y su valor es 1
print("b es de tipo numérico y su valor es:")
print(b)
#tipo de datos punto flotante, decimal
a,b,suma=1.1,2.2,0
print('la suma de a más b es de tipo float y su valor es:')
suma=a+b
#formatear el valor de una variable de tipo decimal
#con dos decimales
print(f'{suma:.2f}')
'''
En Python está permitido realizar una operación aritmética con números de distinto tipo. En este caso, el tipo
numérico «más pequeño» se convierte al del tipo «más grande», de manera que el tipo del resultado siempre es el
del tipo mayor.
'''
#la suma de un entero y un float se almacena en el tipo de mayor
#representación, el float
a=1 #entero
b=3.3 #float
suma=a+b #suma es de tipo float
print(suma)
#Otro tipo básico de Python, e imprescindible, son las secuencias o cadenas de caracteres. Este tipo es conocido
#como string
#Para crear un string, simplemente tienes que encerrar entre comillas simples '' o dobles "" una secuencia de
#caracteres.
saludo1 = 'Hola "Pythonies" esto es una cadena de caracteres con comillas dobles'
print(saludo1)
saludo2 = 'Hola \'Pythonies\', esto es una cadena de caracteres con comillas simples'
print(saludo2)

#tipo de datos booleano, las variables de este tipo pueden tomar el valor:True o False
respuesta = True
print(respuesta)

#Conocer el tipo de una variable
#función type()
print(type(saludo1))
#función isinstance()
print(isinstance(saludo1,str))
print(isinstance(True,bool))
print(type(respuesta))

#conversión de tipos de datos
edadStr='25'
#no podemos sumar 1 a la variable edad porque no es de tipo numérico
#convertimos al tipo int y sumamos
edad=int(edadStr) + 1
print(edadStr)
print(type(edadStr))
print(edad)
print(type(edad))
edadFloat = float(edad)
print(type(edadFloat))
print(edadFloat)