def pedir_numero(mensaje):
    """Pide un número y repite hasta que sea válido."""
    while True:
        valor = input(mensaje).strip()

        if valor == "":  # campo vacío
            print("Error: el campo no puede estar vacío.")
            continue

        try:
            numero = float(valor)  # falla si hay letras
        except ValueError:
            print("Error: escribe solo números.")
            continue

        if numero <= 0:
            print("Error: el valor debe ser mayor que 0.")
            continue

        return numero


edad = pedir_numero("Edad: ")
peso = pedir_numero("Peso (kg): ")
estatura = pedir_numero("Estatura (m): ")

imc = peso / (estatura ** 2)       
print(f"A los {int(edad)} años, tu IMC es: {imc:.2f}")