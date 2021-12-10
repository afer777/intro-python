def lee_numero_entero():
    while True:
        a = input("Ingrese un número entero: ")
        try:
            a = int(a)
            return a
        except ValueError:
            print ("debe de ingresar un numero entero")
a=lee_numero_entero()
b=lee_numero_entero()
if a < b:
    print('a es menor que b')
elif a > b:
    print('a es mayor que b')
else:
    print('a y b son iguales')