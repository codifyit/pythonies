#listas
#Las listas en Python son un tipo contenedor, compuesto,
#que se usan para almacenar conjuntos de elementos relacionados
#del mismo tipo o de tipos distintos.

#lista de números, mismos tipos
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(numeros)

#lista con valores de distintos tipos
elementos = [3, 'a', 8, 7.2, 'hola']
print(elementos)

#listas con listas
lista = [1, ['a', 'e', 'i', 'o', 'u'], 8.9, 'hola']
print(lista)

#crear una lista desde una cadena
vocales = list('aeiou')
print(vocales)

#crear listas vacías
lista_1 = []  # Opción 1
print(lista_1)
lista_2 = list()  # Opción 2
print(lista_2)

#acceder a los elementos de una lista
lista = ['a', 'b', 'd', 'i', 'j']
print(lista[0])  # Primer elemento de la lista. Índice 0 'a'
print(lista[3])  # Cuarto elemento de la lista. Índice 3 'i'

#acceso a listas con elementos de tipo lista
lista = ['a', ['d', 'b'], 'z']
print(lista[1][1]) # lista[1] hace referencia a la lista anidada 'b'

#acceso a elementos de la lista con índices negativos
vocales = ['a', 'e', 'i', 'o', 'u']
print(vocales[-1]) #'u'
print(vocales[-4]) #'e'

#acceso a subconjuntos de elementos en una lista
vocales = ['a', 'e', 'i', 'o', 'u']
print(vocales[2:3])  # Elementos desde el índice 2 hasta el índice 3-1 ['i']
print(vocales[2:4])  # Elementos desde el 2 hasta el índice 4-1 ['i', 'o']
print(vocales[:])  # Todos los elementos ['a', 'e', 'i', 'o', 'u']
print(vocales[1:])  # Elementos desde el índice 1 ['e', 'i', 'o', 'u']
print(vocales[:3])  # Elementos hasta el índice 3-1 ['a', 'e', 'i']

#acceso a elementos en pasos distintos
letras = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k']
print(letras[::2])  # Acceso a los elementos de 2 en 2 ['a', 'c', 'e', 'g', 'i', 'k']
print(letras[1:5:2])  # Elementos del índice 1 al 4 de 2 en 2 ['b', 'd']
print(letras[1:6:3])  # Elementos del índice 1 al 5 de 3 en 3 ['b', 'e']

