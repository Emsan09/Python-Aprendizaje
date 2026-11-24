#ejercicio 1
edad= 17
nombre = "Emanuel"
pais = "Colombia"
print (f"Hola, me llamo {nombre}, tengo {edad} años y vivo en {pais}")

#ejercicio 2 
frase = "Estoy aprendiendo python"
frase_mayuscula = frase.upper()
frase_minuscula = frase.lower()
frase_caracteres = len(frase)
print (f"frase en mayuscula: {frase_mayuscula}")
print (f"frase en minuscula: {frase_minuscula}")
print (f"número de caracteres: {frase_caracteres}")

#ejercicio 3
nombre_completo = "Emanuel Sanchez"
nombre = nombre_completo[:7]
apellido = nombre_completo[8:]
print (f"Nombre: {nombre}")
print (f"Apellido: {apellido}")

#ejercicio 4
Nombre = input ("ingrese su nombre:")
Apellido = input("ingrese su apellido:")
Edad = int(input ("Ingrese su edad: "))
nombre_completo_caracteres = len(Nombre) + len(Apellido)
print (f"Hola {Nombre} {Apellido}")
print (f"Tienes {Edad} años")
print (f"Tu nombre completo tiene {nombre_completo_caracteres} caracteres")

#ejercicio 5
año_nacimiento = int(input("¿En qué año naciste? "))
año_actual = 2026 
edad = año_actual - año_nacimiento
print (f"Tienes aproximadamente {edad} años")
