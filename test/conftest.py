
"""Fixtures compartidas para las pruebas del modulo de inventario."""

import pytest
from funcionalidades.inventario import Inventario

@pytest.fixture
def mi_inventario():
    """Proporciona una instancia limpia de Inventario para cada test."""
    return Inventario()
