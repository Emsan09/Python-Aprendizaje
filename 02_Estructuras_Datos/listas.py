animales = ["perro", "gato", "conejo", "loro"]
animales[1] = "tigre"
animales[3] = "aguila"
print(animales)

video_juegos = ["Roblox","Free Fire","Fifa"]
video_juegos.append("Clash royale")
video_juegos.append("Pes")
print(video_juegos)
print(len(video_juegos))

comidas = ["pizza", "hamburguesa", "pasta", "arroz", "pollo"]
comidas.remove ("pasta")
comidas.remove ("arroz")
comidas.append ("lasagna")
print(comidas)
print(len(comidas))

estudiantes= ["Emanuel","Samuel","Diana", "Marcela", "Monica"]
Eliminado = estudiantes.pop(2)
print(Eliminado)
print(estudiantes)

numeros = [15, 3, 28, 7, 12, 1, 20]
numeros.sort()
print(numeros)
print(len(numeros))

numeros_reversa = [12, 45, 3, 89, 21, 7, 56]
numeros_reversa.sort(reverse=True)
print(numeros_reversa)
print(numeros_reversa[0])

juegos = ["Minecraft", "Roblox", "FIFA", "Free Fire"]
print( "Minecraft" in juegos)
print("GTA" in juegos)
print("GTA" not in juegos)

notas = [2.8, 3.6, 4.2, 2.1, 5.0, 1.9]
print(notas)
notas.append(3.5)
notas.remove(3.6)
notas.sort()
print(notas[0])
print(notas[-1])
print(len(notas))
print(notas)

Notas = [2.5, 4.0, 3.2, 1.8, 4.7, 2.9]
for i in Notas:
    if i >= 3.0:
        print(i)

Aprobadas = []
Notas = [2.5, 4.0, 3.2, 1.8, 4.7, 2.9]
for i in Notas:
    if i >= 3.0:
        Aprobadas.append(i)
print(Aprobadas)

Numeros = [3, 8, 12, 5, 17, 20, 7, 14]
Pares = []
for i in Numeros:
    if i%2 == 0:
        Pares.append(i)
print(Pares)

notas = [2.5, 4.0, 3.2, 1.8, 4.7, 2.9]
print(sum(notas))
print(max(notas))
print(min(notas))
promedio = sum(notas)/len(notas)
print(promedio)

notas = [2.5, 4.0, 3.2, 1.8, 4.7, 2.9]
promedio = sum(notas)/len(notas)
contador = 0
for i in notas:
    if i >= 3.0:
        contador += 1
print(contador)
print(promedio)
print(max(notas))
print(min(notas))
print(len(notas))