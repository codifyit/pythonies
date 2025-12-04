# capitalize()
# El método capitalize() se aplica sobre una cadena y la devuelve con su primera letra en mayúscula.

s = "mi cadena"
print(s.capitalize()) #Mi cadena

print(len(s)) #longitud de la cadena

# lower()
# El método lower() convierte todos los caracteres alfabéticos en minúscula.

s = "MI CADENA"
print(s.lower()) #mi cadena

# swapcase()
# El método swapcase() convierte los caracteres alfabéticos con mayúsculas en minúsculas y viceversa.

s = "mI cAdEnA"
print(s.swapcase()) #Mi CaDeNa

# upper()
# El método upper() convierte todos los caracteres alfabéticos en mayúsculas.

s = "mi cadena"
print(s.upper())

# count(<sub>[, <start>[, <end>]])
# El método count() permite contar las veces que otra cadena se encuentra dentro de la primera. Permite también dos parámetros opcionales que indican donde empezar y acabar de buscar.

s = "el bello cuello "
print(s.count("llo")) #2

# isalnum()
# El método isalnum() devuelve True si la cadena esta formada únicamente por caracteres alfanuméricos, False de lo contrario. Caracteres como @ o & no son alfanumericos.

s = "correo@dominio.com"
print(s.isalnum())

# isalpha()
# El método isalpha() devuelve True si todos los caracteres son alfabéticos, False de lo contrario.

s = "abcdefg"
print(s.isalpha())

# strip([<chars>])
# El método strip() elimina a la izquierda y derecha el carácter que se le introduce. Si se llama sin parámetros elimina los espacios. Muy útil para limpiar cadenas.

s = "  abc  "
print(s.strip()) #abc

# zfill(<width>)
# El método zfill() rellena la cadena con ceros a la izquierda hasta llegar a la longitud pasada como parámetro.

s = "123"
print(s.zfill(5)) #00123

# join(<iterable>)
# El método join() devuelve la primera cadena unida a cada uno de los elementos de la lista que se le pasa como parámetro.

s = " y ".join(["1", "2", "3"])
print(s) #1 y 2 y 3

# split(sep=None, maxsplit=-1)
# El método split() divide una cadena en subcadenas y las devuelve almacenadas en una lista. La división es realizada de acuerdo a el primer parámetro, y el segundo parámetro indica el número máximo de divisiones a realizar.

s = "Python,Java,C"
print(s.split(",")) #['Python', 'Java', 'C']

# invertir una cadena
texto = "Hola a todos"
palabras = texto.split()
for palabra in palabras:
    print(palabra[::-1], end = ' ')
