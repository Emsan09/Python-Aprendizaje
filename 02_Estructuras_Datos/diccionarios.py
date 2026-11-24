persona = {"nombre":"Carlos",
"edad": 20,
"profesion":"Programador"
}
print(persona["nombre"])
print(persona["edad"])
print(persona["profesion"])

computador = {"marca": "Lenovo",
"ram":"8GB", 
"precio": 2000000
}
computador["marca"] = "HP"
computador["ram"] = "16GB"
computador["procesador"] = "Intel i5"
print(computador)

celular = {
    "marca": "Samsung",
    "modelo": "Galaxy S24",
    "precio": 3000000,
    "color": "negro"
}
color_eliminado = celular.pop("color")
print(color_eliminado)
print(celular)


estudiante = {
    "nombre": "Carlos",
    "edad": 17,
    "curso": "Programación",
    "nota": 4.5
}
claves_valores = estudiante.items()
print(claves_valores)
for clave, valor in estudiante.items():
    print(f"{clave}: {valor}")

estudiante = {
    "nombre": "Carlos",
    "edad": 17,
    "curso": "Programación",
    "nota": 4.5
}
print(estudiante.keys())
print(estudiante.values())
for i in estudiante.keys():
    print(i)

productos = {
    "arroz": 5000,
    "leche": 4000,
    "pan": 2000,
    "huevos": 12000,
    "aceite": 9000
}
contador = 0
for producto, valor in productos.items():
    if valor > 5000:
       print(f"{producto} : {valor}")
       contador += 1
print(contador)

productos = {
    "arroz": 5000,
    "leche": 4000,
    "pan": 2000,
    "huevos": 12000,
    "aceite": 9000
}
total = 0
for i in productos.values():
    total += i
print(total)

inventario = {
    "camiseta": 35000,
    "pantalon": 70000,
    "zapatos": 120000,
    "gorra": 25000,
    "chaqueta": 150000
}
print(inventario)
contador = 0
total = 0
for producto, valor in inventario.items():
    if valor > 50000:
        print(f"{producto}:{valor}")
        contador += 1
print(contador)
for i in inventario.values():
    total += i 
print(total)

nombre = input("ingresa tu nombre")
edad =  int(input("ingresa tu edad"))
ciudad = input("ingresa la ciudad donde vives")
datos_personales = {"nombre": nombre,
    "edad": edad,
    "ciudad": ciudad}
print(datos_personales)

nombre = input("Ingresa tu nombre")
edad = int(input("Ingresa tu edad"))
nota1 = float(input("Ingresa 1 nota"))
nota2 = float(input("Ingresa 1 nota"))
nota3 = float(input("Ingresa 1 nota"))
lista_notas = [nota1, nota2, nota3]
prom = {"nombre": nombre,
    "edad": edad,
"notas": lista_notas
}
promedio1 = sum(lista_notas)/ len(lista_notas)
prom["promedio"] = promedio1
print(prom)
if promedio1 >= 3.0:
    print("Aprobo")
else:
    print("Reprobo")

curso = {
    "nombre": "Python",
    "estudiantes": ["Ana", "Carlos", "Emanuel", "Sofia"],
    "notas": [4.0, 2.8, 3.5, 4.7]
}
print(len(curso["estudiantes"]))
promedio = sum(curso["notas"])/ len(curso["notas"])
estudiantes_aprobaron = 0
for i in range(len(curso["notas"])):
    if curso["notas"][i]>= 3.0:
       print(curso["estudiantes"][i])
       estudiantes_aprobaron += 1
print(promedio)
print(estudiantes_aprobaron)
nota_mayor = max(curso["notas"])
posicion = curso["notas"].index(nota_mayor)
print(curso["estudiantes"][posicion])