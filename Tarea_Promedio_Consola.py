# Actividad:
# Pedir 3 notas, calcular el promedio  e indicar si aprueba o no ( >4 aprueba). Indicar si reprueba o aprueba.

nota1 = float(input("Ingrese la primera nota: "))
nota2 = float(input("Ingrese la segunda nota: "))
nota3 = float(input("Ingrese la tercera nota: "))
promedio = ((nota1 + nota2 + nota3) / 3)
print(f"{promedio:.1f}")
if promedio >= 4:
    print("El estudiante APRUEBA ")
else:
    print("El estudiante REPRUEBA ")