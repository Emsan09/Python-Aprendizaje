#ejercicio 6
edad = int(input("Ingrese su edad"))
if edad >= 18:
    print("Eres mayor de edad")
else:
    print ("Eres menor de edad")

#ejercicio 7 
notas = int(input("Ingrese una nota entre 00 y 100"))
if notas >= 90:
    print ("Excelente")
elif 70 <= notas <=89:
    print("Aprobaste")
elif 60 <= notas <= 69:
    print("Debes mejorar")
else:
    print("Reprobaste")

#ejercicio 8 
dinero_persona = int(input("¿Cuanto dinero tienes?"))
if dinero_persona >= 100000:
    print("Puedes comprar el producto")
elif dinero_persona >= 50000:
    print("Puedes comprar un producto mas ecomico")
else:
    print("No tienes suficiente dinero")