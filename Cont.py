print("Hola, escriba su nombre: ")
nombre= input()
print("es un placer conocerte,",nombre)

n1 = float(input("Ingrese el primer número: " ))
n2 = float(input("ingrese el segundo número: "))
n3 = float (input("ingrese el tercer número: "))

if n2 < n1 > n3 :
    print("El numero mayor es el primer número. Número,",n1)
elif n1 < n2 > n3:
    print ("El número mayor es el segundo número. Número,",n2)
elif n1 < n3 > n2:
    print ( "El número mayor es el tercer número. Numero,",n3)

