n = int(input("Introduce la altura del triángulo (entero positivo): "))
for i in range(n,0,-1):
    for j in range(i):
        print("*", end="")
    print("")