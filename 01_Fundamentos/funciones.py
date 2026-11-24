def presentacion():
    print("Hola, estoy aprendiendo python")
presentacion()

def despedida():
    print("Gracias por aprender python conmigo")
despedida()

def presentacion_2(Nombre, Edad):
    print(f"Hola {Nombre}, tienes {Edad} años")
presentacion_2("Emanuel", 17)

def suma(numero1, numero2):
    print(numero1 + numero2)
suma(10,5)

def multiplicar(num1, num2):
    print (num1 * num2)
multiplicar(5,3)

def resta(num3,num4):
    return num3 - num4
resultado = resta(15,5)
print(resultado)

def calcular_edad(año_actual,año_nacimiento):
    return año_actual - año_nacimiento
edad = calcular_edad(2026,2007)
print(edad)

def es_mayor_de_edad (Edad):
    if Edad >= 18:
        return True
    else:
        return False
edad_mayor = es_mayor_de_edad (16)
print (edad_mayor)

def mayor_de_edad (Edad):
    if Edad >= 18:
        return "Eres mayor de edad"
    else:
        return "Eres menor de edad"
ed = mayor_de_edad(25)
print(ed)

def calculadora(numero1, numero2, operacion):
    if operacion == "suma":
        return numero1 + numero2
    elif operacion == "resta":
        return numero1 - numero2
    elif operacion == "multiplicacion":
        return numero1 * numero2
    else:
        return "Operacion no valida"
operaciones = calculadora(3,4,"suma")
print(operaciones)

def es_par (numero):
    if numero%2 == 0:
        return "Es par"
    else:
        return "Es impar"
num = es_par(15)
print(num)

def analizar_numero(numero):
    if numero > 0:
        return "Positivo"
    elif numero < 0:
        return "Negativo"
    else:
        return "Es cero"
an = analizar_numero (-2)
print(an)

def calcular_promedio(nota1,nota2,nota3):
    return (nota1 + nota2 + nota3) / 3
promedio = calcular_promedio(3.1, 2.9, 4.0)
print(promedio)
if promedio >= 3.0:
    print("Aprobaste")
else:
    print("Reprobaste")

def numero_mayor(n1, n2, n3):
    if n1 > n2 and n1 > n3:
        return n1 
    elif n2 > n1 and n2 > n3:
        return n2
    else:
        return n3
mayor = numero_mayor(10,9,14)
print(mayor)

def contar_vocales(Palabra):
    vocales = "aeiou"
    contador = 0
    for letra in Palabra:
        if letra in vocales: 
            contador += 1
    return contador
num_vocales = contar_vocales("emanuel")
print(num_vocales)

def contar_pares(lista):
    contador = 0
    for i in lista:
        if i%2 == 0:
            contador +=1
    return contador
pares = contar_pares([2,40,22,3,5])
print(pares)