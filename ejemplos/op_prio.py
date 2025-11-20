#Al igual que ocurre en las matemáticas, los operadores en Python
#tienen un orden de prioridad. Este orden es el siguiente, de menos
#prioritario a más prioritario: asignación; operadores booleanos;
#operadores de comparación, identidad y pertenencia; a nivel de bits
#y finalmente los aritméticos
x = 5
y = 2
z = x + 3 * y  # El producto tiene prioridad sobre la suma
print(z) #11
z = (x + 3) * y  # Los paréntesis tienen prioridad
print(z) #16