curso = {"nombre":"Python",
"estudiantes":["Ana","Carlos","Emanuel","Sofia"],
"notas":[4.0,2.5,3.8,4.5],
"dias_clase": ("lunes","miercoles", "viernes")
}
print(curso["nombre"])
print(len(curso["estudiantes"]))
promedio = sum(curso["notas"])/len(curso["notas"])
print(promedio)
reprobados = 0
for i in range(len(curso["notas"])):
    if curso["notas"] [i] >= 3.0:
        print(curso["estudiantes"][i])
    if curso["notas"][i] < 3.0:
        reprobados += 1
print(reprobados)
print(round(promedio,2))


ventas = {
    "enero": 150000,
    "febrero": 230000,
    "marzo": 180000,
    "abril": 310000,
    "mayo": 120000,
    "junio": 270000
}
print(ventas)
total = sum(ventas.values())
print(total)
promedio_ventas = sum(ventas.values())/len(ventas.values())
print(promedio_ventas)
mes_mayor = max(ventas.values())
for mes, valor in ventas.items():
    if valor == mes_mayor:
        print(mes)
contador = 0
for i in ventas.values():
    if i > 200000:
        contador += 1
print(contador)

ventas = {
    "enero": 150000,
    "febrero": 230000,
    "marzo": 180000,
    "abril": 310000,
    "mayo": 120000,
    "junio": 270000,
    "julio": 90000,
    "agosto": 350000
}
promedio = sum(ventas.values())/len(ventas.values())
print(promedio)
contador = 0
for mes, valor in ventas.items():
    if valor > promedio:
        contador += 1
        print(mes)
print("meses_menores")
for mes, valor in ventas.items():
    if valor < promedio:
        print(mes)
print(contador)
mes_menor = min(ventas.values())
for mes, valor in ventas.items():
    if valor == mes_menor:
        print(mes)

notas = [2.5, 4.0, 3.2, 1.8, 4.7, 2.9, 3.8]
aprobadas = [i for i in notas if i>= 3.0]
print(aprobadas)

numeros = [1, 2, 3, 4, 5, 6, 7, 8]
dobles = [i*2 for i in numeros if i%2 == 0]
print(dobles)

ventas = {
    "enero": 150000,
    "febrero": 230000,
    "marzo": 180000,
    "abril": 310000,
    "mayo": 120000
}
ventas_altas = [i for i in ventas.values() if i > 200000]
print(ventas_altas)

ventas = {
    "enero": 150000,
    "febrero": 230000,
    "marzo": 180000,
    "abril": 310000,
    "mayo": 120000
}
meses_altas = [mes for mes, valor in ventas.items() if valor > 200000]
print(meses_altas)

estudiantes = {
    "Ana": 4.5,
    "Carlos": 2.8,
    "Emanuel": 3.7,
    "Sofia": 4.8,
    "Daniel": 2.5,
    "Laura": 3.2,
    "Mateo": 1.9
}
promedio = sum(estudiantes.values())/len(estudiantes.values())
Aprobados = [nombre for nombre, nota in estudiantes.items() if nota >= 3.0]
print(Aprobados)
Reprobados = [nombre for nombre, nota in estudiantes.items() if nota < 3.0]
print(Reprobados)
notas_altas = [nota for nota in estudiantes.values() if nota >= 4.0]
print(notas_altas)
contador = 0
for nombre, nota in estudiantes.items():
    if nota >= 3.0:
        contador += 1
print(contador)