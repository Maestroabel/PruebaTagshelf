# Este script convierte el modelo de color RGB al HSV de manera aproximada, utilizando branchless (Sin evaluar condiciones). Para ello, 
# le pide al usuario el modelo de color RGB, el programa encuentra el modulo del input otorgado para que se encuentre en el rango 0...255 
# y luego lo divide entre 255 para que se encuentre entre 0...1. Luego de esto, calcula mediante formulas el modelo de color HSV.

# OJO: Por favor, limitarse solamente a colocar numeros entero. El programa obviamente explota 
# si se le coloca otros tipos de datos, ya que no los maneja.

r = ((int(input("Escriba el R: "))%255)/255)
g = ((int(input("Escriba el G: "))%255)/255)
b = ((int(input("Escriba el B: "))%255)/255)

# Para diseñar las formulas, se tomo como guia los diversos metodos que indica: https://www.rapidtables.com/convert/color/rgb-to-hsv.html

max = max(r, g, b)
min = min(r, g, b)
delta = max - min

h = round(((((g - b) / delta) % 6) * (max == r) + ((b - r) / delta + 2) * (max == g) + ((r - g) / delta + 4) * (max == b) + (delta == 0))*60)
s = round(delta / max,3)*100
v = round(max,3)*100

print(f"\nMatiz: {h}")
print(f"Saturacion: {s}%")
print(f"Brillo: {v}%")