temperaturas = (22, 25, 19, 28, 24)
print(temperaturas)
print(temperaturas[0])
print(temperaturas[4])
print(len(temperaturas))
print(sum(temperaturas)/len(temperaturas))

colores = ("rojo", "azul", "verde")
colores[1] = "Amarillo" #Da error las tuplas no se pueden modificar

ventas = (15000, 23000, 18000, 31000, 12000, 27000)
total_ventas = sum(ventas)
menor = min(ventas)
mayor = max(ventas)
promedio = sum(ventas)/len(ventas)
for i in ventas:
    if i >= 20000:
        print(i)
print(total_ventas)
print(menor)
print(mayor)
print(promedio)

productos = ("arroz", "leche", "pan", "huevos")
print(len(productos))
print(productos[0])
print(productos[3])
for i in productos:
    print(i)