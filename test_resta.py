"""Pruebas para la funcion ``restar_numeros``."""

from resta import restar_numeros

def test_restar_numeros_exito(monkeypatch, capsys):
    """Prueba una resta exitosa con entradas válidas."""
    # Simulamos las entradas del usuario: "10" y luego "4"
    respuestas = iter(["10", "4"])
    monkeypatch.setattr("builtins.input", lambda _: next(respuestas))

    restar_numeros()

    capturado = capsys.readouterr()
    assert "El resultado es: 6" in capturado.out


def test_resta_entrada_invalida(monkeypatch, capsys):
    """Prueba el manejo de error cuando no se ingresan enteros en resta."""
    # Simulamos una entrada inválida
    respuestas = iter(["10", "xyz"])
    monkeypatch.setattr("builtins.input", lambda _: next(respuestas))

    restar_numeros()

    capturado = capsys.readouterr()
    assert "Error: Por favor, ingresa solo números enteros." in capturado.out
