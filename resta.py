"""
Módulo para realizar operaciones de resta.
Desarrollado con metodología TDD (Test Driven Development)
"""


def restar_numeros():
    """Solicita dos números al usuario y muestra su resta."""
    try:
        # Se capturan los datos como espera el test (monkeypatch)
        a = int(input("Ingresa el primer número: "))
        b = int(input("Ingresa el segundo número: "))

        resultado = a - b

        # El mensaje debe coincidir exactamente con el assert del test
        print(f"El resultado es: {resultado}")

    except ValueError:
        # El mensaje de error debe coincidir con el segundo test
        print("Error: Por favor, ingresa solo números enteros.")


if __name__ == "__main__":
    restar_numeros()
