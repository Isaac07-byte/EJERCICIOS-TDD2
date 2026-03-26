"""Pruebas para la funcion ``sumar_numeros``."""

from funcionalidades.suma import sumar_numeros

def test_sumar_numeros_exito(monkeypatch, capsys):
    """Prueba una suma exitosa con entradas válidas."""
    # Simulamos las entradas del usuario: "5" y luego "3"
    respuestas = iter(["5", "3"])
    monkeypatch.setattr("builtins.input", lambda _: next(respuestas))

    sumar_numeros()

    # Capturamos la salida de la consola
    capturado = capsys.readouterr()
    assert "El resultado es: 8" in capturado.out


def test_suma_entrada_invalida(monkeypatch, capsys):
    """Prueba el manejo de error cuando no se ingresan enteros en suma."""
    # Simulamos una entrada no numérica "abc"
    respuestas = iter(["abc", "5"])
    monkeypatch.setattr("builtins.input", lambda _: next(respuestas))

    sumar_numeros()

    capturado = capsys.readouterr()
    assert "Error: Por favor, ingresa solo números enteros." in capturado.out
