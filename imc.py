nombre = input("¿Cómo te llamas? ")
apellido = input("¿Cuál es tu apellido? ")
edad = int(input("¿Cuántos años tienes? "))
peso = float(input("¿Cuánto pesas en kg? "))
estatura = float(input("¿Cuánto mides en metros? (ej. 1.70) "))

imc = peso / estatura ** 2

print("===== RESUMEN =====")
print(f"Nombre: {nombre.title()} {apellido.title()}")
print(f"Edad: {edad} años")
print(f"Peso: {peso} kg")
print(f"Estatura: {estatura} m")
print(f"IMC: {imc:.2f}")