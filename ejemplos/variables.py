#variables, referencias y direcciones de memoria
a=1
b=1
print('Dirección de memoria de 1')
print(id(1))
print('Dirección de memoria de a')
print(id(a))
print('Dirección de memoria de b')
print(id(b))
#si cambio el valor de b también cambia su dirección de memoria
#que será distinta a la de a
b=2
print('Dirección de memoria de b después de cambiar su valor')
print(id(b))
