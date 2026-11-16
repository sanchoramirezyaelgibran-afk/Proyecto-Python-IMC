edad = int(input("¿Cuántos años tienes? "))
peso = float(input("¿Cuánto pesas en kg? "))
estatura = float(input("¿Cuánto mides en metros? (ej. 1.70) "))

imc = peso / estatura ** 2

print(f"Tienes {edad} años.")
print(f"Tu IMC es: {imc:.2f}")