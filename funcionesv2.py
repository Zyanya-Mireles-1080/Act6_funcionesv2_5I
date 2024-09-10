print("Mas sobre funciones")
# Aqui se escriben las funciones
def suma_ab(a,b):
    s = a + b
    return s

def resta_ab(c,d):
    r = c - d
    return r

def mult_ab(e,f):
    x = e*f
    return x

def div_ab(g,h):
    z = g/h
    return z

# Llamadas a las funciones
print("Calculando suma")
n1 = int(input("Ingresa el primer Numero  "))
n2 = int(input("Ingresa el segundo Numero  "))
suma = suma_ab(n1,n2)
print(f"La suma de {n1} + {n2} es igual a: {suma} \n")

print("Calculando resta")
n3 = int(input("Ingresa el primer Numero  "))
n4 = int(input("Ingresa el segundo Numero  "))
resta = resta_ab(n3,n4)
print(f"La resta de {n3} - {n4} es igual a: {resta} \n")

print("Calculando multiplicación")
n5 = int(input("Ingresa el primer Numero  "))
n6 = int(input("Ingresa el segundo Numero  "))
mult = mult_ab(n5,n6)
print(f"La multiplicación de {n5} * {n6} es igual a: {mult} \n")

print("Calculando división")
n7 = int(input("Ingresa el primer Numero  "))
n8 = int(input("Ingresa el segundo Numero  "))
div = div_ab(n7,n8)
print(f"La division de {n7} / {n8} es igual a: {div} \n")