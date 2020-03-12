# PRIMERA PRACTICA Arbol de BUSQUEDA
# SEGUNDA PRACTICA Machine learning, crear una red neuronal para resolver un determinado problema
# Tercera PrActica, Aprendizaje por refuerzo, ir aprendiendo con recompesas
import numpy as np
import tensorflow as tf
tf.print("hello gili")
x=[234324,4324324,34,33,3,3,3,3]
n=2
y=np.zeros((len(x), n))
print(y)
print("holamundo!!")
l=[1,2,3,4,5,6,7,8,9]
print(l)
l2=[(e**2,e**3) for e in l[::2]]
print(l2)
a = 1  # Enteros
b = 1.0  # Flotantes
c = 1.0+0.0j  # Complejos
d = "1"  # String Unicode
e = r"1"  # String raw
print(a)
print(b)
print(c)
print(d)
print(e)
u = u"Hola\n"
r = r"Hola\n"
print(u)
print(r)

#diccionarios
# se indexan por una clave
TCPIP = {"Telnet": 23, "SSH": 22, "FTP": 21, "HTTP": 80}

print(TCPIP["SSH"])
print(TCPIP["HTTP"])

a=66666
a
print(a)
a=35+3j+2j
print(a)
s="ja"
print(s+s)
print(s*5)
l[0]
len(l)
l[-1]
l[len(l)-1]
print(l[1:7])
print(l[1:])
print(l[3])

print(l[:])#print copia de la lista
print(l)#print la lista
l[3]=8934
l.append(666)
l.sort()
l.pop()

t=(1,2,3,4,5) #la tupla es inmutable, la lista es mutable. Vamos que la tupla es gija
t
print(t)

a=2
b=3
a,b=b,a #las comas es lo que definen las tuplas, intercambia los valores de a y b

var="FSI"
if var=="FSI2":#no hace falta abre llave y cierra llave, con dos puntos vale
    print("funciona sentencia de control")
print("Lo va a escribir igual")



l=[1,2,3,3,423,8,00,1,453,7677,88,4,5,6]
l2=[21,22,23,23,2423,28,200,21,2453,27677,288,24,25,26]
for e in l:
    print(e)

print("-------------\n")
for e in l[::2]:
    print(e)

print("-------------\n")
for e in l[::-2]:
    print(e)


print("-------------\n")
for e in l:
    print(e)

print("-------------\n")

for i in enumerate(l):
    print(i)

print("-------------\n")

for v1,v2 in zip(l,l2):
    print(v1,v2)

print("-------------\n")

lc=[]
for e in l:
    lc.append(e**2)
print(lc)

lc=[e**2 for e in l]#Compresión de listas, equivalente al código anterior
print(lc)

lc=[(e**2,e**3) for e in l]
print(lc)


def suma(a,b):
    return a+b
print (suma(3,4))

def suma_y_resta(a,b):
    return a+b,a-b
print (suma_y_resta(3,4))


print("-------------\n")
def suma(*a):
    aux=0
    for e in a:
        aux +=e
    return aux
print (suma(3,4,5,6))
print("-------------\n")
def suma2(*a):
    return sum(a)
print (suma2(3,4,5,63))
