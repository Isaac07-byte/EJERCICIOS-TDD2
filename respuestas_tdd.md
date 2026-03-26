# Taller TDD - Kata Suma y Resta

## Respuestas Técnicas y Reflexivas

---

## Evaluación SUMA

### ¿El test realmente falla?

**SÍ - La fase RED se cumple correctamente**

Al ejecutar el test antes de implementar la función `sumar()`, el test **falla** con el error:

```
ImportError: cannot import name 'sumar' from 'suma'
```

Esto sucede porque en la fase RED de TDD, primero escribimos un test que verifica el comportamiento esperado:

```python
def test_sumar_dos_numeros():
    from suma import sumar
    assert sumar(2, 3) == 5
```

El test falla porque la función `sumar()` aún no existe. Este error confirma que el test está correctamente diseñado y detecta la ausencia de la funcionalidad.

---

### ¿El código es mínimo?

**SÍ - Código mínimo en fase GREEN**

```python
def sumar(a, b):
    return a + b
```

Esta implementación contiene únicamente la lógica necesaria para que el test pase. No hay validaciones adicionales, ni estructuras complejas. Cumple con el principio de TDD: escribir la menor cantidad de código posible para cumplir el comportamiento esperado.

---

### ¿Se refactorizó o solo se dejó funcionando?

**SÍ - Se realizó refactorización**

Después de que el test pasó en GREEN, se mejoró la estructura sin cambiar el comportamiento:

```python
def sumar(a, b):
    """
    Retorna la suma de dos números.
    
    Args:
        a (int/float): Primer número
        b (int/float): Segundo número
    
    Returns:
        int/float: Resultado de a + b
    
    Raises:
        TypeError: Si los parámetros no son numéricos
    """
    if not isinstance(a, (int, float)):
        raise TypeError(f"El primer argumento debe ser número, no {type(a).__name__}")
    if not isinstance(b, (int, float)):
        raise TypeError(f"El segundo argumento debe ser número, no {type(b).__name__}")
    
    return a + b
```

Mejoras realizadas:
- Documentación con docstrings
- Validación de tipos
- Manejo de errores apropiado
- Código más mantenible

Los tests continúan pasando después de la refactorización.

---

## Evaluación RESTA

### ¿El test realmente falla?

**SÍ - La fase RED se cumple correctamente**

Al ejecutar el test antes de implementar la función `restar()`, el test **falla** con el error:

```
ImportError: cannot import name 'restar' from 'resta'
```

El test definido fue:

```python
def test_restar_dos_numeros():
    from resta import restar
    assert restar(10, 4) == 6
```

El test falla porque la función `restar()` aún no existe, confirmando que la metodología TDD se aplicó correctamente.

---

### ¿El código es mínimo?

**SÍ - Código mínimo en fase GREEN**

```python
def restar(a, b):
    return a - b
```

Esta implementación es la solución más simple posible que hace pasar el test. Solo contiene la operación esencial sin ninguna lógica adicional.

---

### ¿Se refactorizó o solo se dejó funcionando?

**SÍ - Se realizó refactorización**

```python
def restar(a, b):
    """
    Retorna la resta de dos números (a - b).
    
    Args:
        a (int/float): Primer número (minuendo)
        b (int/float): Segundo número (sustraendo)
    
    Returns:
        int/float: Resultado de a - b
    
    Raises:
        TypeError: Si los parámetros no son numéricos
    """
    if not isinstance(a, (int, float)):
        raise TypeError(f"El primer argumento debe ser número, no {type(a).__name__}")
    if not isinstance(b, (int, float)):
        raise TypeError(f"El segundo argumento debe ser número, no {type(b).__name__}")
    
    return a - b
```

La refactorización incluyó:
- Documentación completa de la función
- Validación de tipos de datos
- Manejo de errores con TypeError
- Mejora en la legibilidad y mantenimiento

Los tests siguen pasando después de la refactorización, confirmando que el comportamiento no cambió.

---

## Conclusión

Para ambas operaciones (suma y resta), se siguió correctamente la metodología TDD:

1. **RED**: Se wrote un test que falla porque la función no existe
2. **GREEN**: Se implementó código mínimo para que el test pase
3. **REFACTOR**: Se mejoró la estructura sin cambiar el comportamiento

La importancia de TDD radica en que los tests actúan como especificación del comportamiento y protección ante regresiones durante refactorizaciones.