# Este script convierte el modelo de color HSV al RGB de manera aproximada, utilizando branchless (Sin evaluar condiciones). Para ello, 
# le pide al usuario el modelo de color HSV, el programa encuentra el modulo del input otorgado para que se encuentre entre 
# los rangos del h [0..360] y entre los rangos del S y V [0..100]. Luego de esto, calcula mediante formulas el modelo de color RGB.

# OJO: Por favor, limitarse solamente a colocar numeros entero. El programa obviamente explota 
# si se le coloca otros tipos de datos, ya que no los maneja.

h = (int(input("Escriba el H: "))%360)
s = ((int(input("Escriba el S: "))%101)/100)
v = ((int(input("Escriba el V: "))%101)/100)

# Para diseñar las formulas, se tomo como guia los diversos metodos que indica: https://www.rapidtables.com/convert/color/hsv-to-rgb.html

C = s * v
X = C * (1 - abs((h / 60) % 2 - 1))
m = v - C

rdelta = (C * (h >= 0 and h < 60)) + (X * (h >= 60 and h < 120)) + (0 * (h >= 120 and h < 240)) + (X * (h >= 240 and h < 300)) + (C * (h >= 300 and h < 360))
gdelta = (X * (h >= 0 and h < 60)) + (C * (h >= 60 and h < 120)) + (C * (h >= 120 and h < 180)) + (X * (h >= 180 and h < 240)) + (0 * (h >= 240 and h < 360))
bdelta = (0 * (h >= 0 and h < 120)) + (X * (h >= 120 and h < 180)) + (C * (h >= 180 and h < 300)) + (X * (h >= 300 and h < 360))

r = round((rdelta+m)*255)
g = round((gdelta+m)*255)
b = round((bdelta+m)*255)

print(f"\nr = {r}")
print(f"g = {g}")
print(f"b = {b}")