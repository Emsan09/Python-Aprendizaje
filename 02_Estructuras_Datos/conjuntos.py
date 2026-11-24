colores = {"rojo", "azul", "amarillo", "rojo", "verde", "azul"}
print(colores)
colores.add("negro")
colores.remove("verde")
print(colores)
print(len(colores))

grupo_a = {"Ana", "Carlos", "Emanuel", "Sofia"}
grupo_b = {"Carlos", "Sofia", "Daniel", "Laura"}

print(grupo_a & grupo_b)
print(grupo_a | grupo_b)
print(grupo_a - grupo_b)

python = {"Ana", "Carlos", "Emanuel", "Sofia"}
java = {"Carlos", "Daniel", "Sofia", "Laura"}
print("Emanuel" in python)
print("Laura" in java)
print("Daniel" in python)