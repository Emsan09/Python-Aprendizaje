#ejercicio 9
contador = 10
while contador > 0:
    print(contador)
    contador -= 1
print("¡Despegue!")

#ejercicio 10
numero_usuario = int(input("Ingrese un numero"))
while numero_usuario > 0:
    print(numero_usuario)
    numero_usuario -= 1
print("Fin")

#ejercicio 11
numero_par= 2
while numero_par < 22:
    print(numero_par)
    numero_par += 2

#ejercicio 12
numero_par2= 1
while numero_par2 <= 20:
    if numero_par2%2 == 0:
        print(numero_par2)
    numero_par2 += 1

#ejercicio 13
numero_impar = 1
while numero_impar <= 20:
    if numero_impar%2 == 1:
        print(numero_impar)
    numero_impar += 1

#ejercicio 14 
multiplo_5 = 1
while multiplo_5 <= 50:
    if multiplo_5%5 == 0:
       print(multiplo_5)
    multiplo_5 += 1

#ejrcicio 14
numeros = 1
while numeros <= 100:
    if numeros%3 == 0 and numeros%5 == 0:
        print("FizzBuzz")
    elif numeros%3 == 0:
        print("Fizz")
    elif numeros%5 == 0:
        print("Buzz")
    else:
        print()
    numeros +=1

#ejercicio 15
for i in range(1,11):
    print(i)

#ejercicio 16

for i in range (2,21,2):
    print(i)

#ejercicio 17
for i in range (20,0, -1):
    print(i)

#ejercicio 18
for i in range (1,55):
    if i%5 == 0:
        print(i)

#ejercicio 19
for i in range (1,101):
    if i%2 == 0:
        print(f"{i} par")
    elif i%2 == 1:
        print(f"{i} impar")