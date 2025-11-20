#formatear strings
#operador % en la cadena se define un lugar
#(en el que se especifica un marcador de tipo)
#que será sustituido posteriormente por un valor
nombre = 'J2logo'
#%s para variables de tipo cadena
print('Hola %s' % nombre) #'Hola J2logo'

#%i para variables de tipo entero
x=1
y=2
print('El resultado de sumar %i y %i es: %i' % (x, y, x+y)) #El resultado de 1 e 2 es: 3'

#formatear con la función format()
var1 = 'J2logo'
var2 = 'Hola'
print('{} {}, ¿cómo estás?'.format(var2, var1))

#se puede especificar el nombre de las variables
v1 = 'J2logo'
v2 = 'Hola'
print('{var2} {var1}, ¿cómo estás?'.format(var1=v1, var2=v2))

#también se puede usar el índice de las variables
print('{1} {0}, ¿cómo estás?'.format(v1, v2))

#concatenar listas de cadenas
cadenas = ['Hola', 'j2logo', ',', '¿cómo', 'estás?']
print(' '.join(cadenas)) #une las cadenas de la lista añadiendo entre ellas un espacio

#con números
numeros = ['1', '2', '3']
print(', '.join(numeros)) #une los números y añade entre ellos , y espacio



