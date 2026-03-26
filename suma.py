"""
Módulo para realizar operaciones de suma.
Desarrollado con metodología TDD (Test Driven Development)
"""


def sumar_numeros():
    """
    Solicita dos números al usuario y muestra su suma con validación de entrada.
    Cumple con los requisitos de los tests de éxito y error.
    """
    try:
        # Captura de datos inyectados por el test
        a = int(input("Ingresa el primer número: "))
        b = int(input("Ingresa el segundo número: "))

        resultado = a + b

        # Formato exacto para test_sumar_numeros_exito
        print(f"El resultado es: {resultado}")

    except ValueError:
        # Mensaje exacto para test_suma_entrada_invalida
        print("Error: Por favor, ingresa solo números enteros.")


if __name__ == "__main__":
    sumar_numeros()
