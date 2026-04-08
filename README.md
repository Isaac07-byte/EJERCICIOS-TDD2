# 📦 Taller TDD - Desarrollo Guiado por Pruebas

> **Metodología Test-Driven Development (TDD)** - Aplicada en todas las actividades

---

## 🏢 Información Institucional

```
ANÁLISIS Y DESARROLLO DE SOFTWARE
CENTRO PARA LA INDUSTRIA PETROQUÍMICA 
SENA - REGIONAL BOLÍVAR

APRENDICES:
ISAAC CHICO                 MICHAEL VERGARA

FICHA: 2995985
INSTRUCTORA: MARA SOFÍA CABRALES
FECHA: 23/03/2026
CARTAGENA – COLOMBIA
```

---

## 📋 Tabla de Contenidos

1. [Actividad 1: Kata Sencillo (Suma y Resta)](#-actividad-1-kata-sencillo)
2. [Actividad 2: Sistema de Gestión de Inventario](#-actividad-2-sistema-de-gestión-de-inventario)
3. [Actividad 3: Diseño de Casos de Prueba](#-actividad-3-diseño-de-casos-de-prueba)

---

## 🔴🟢🟡 Actividad 1: Kata Sencillo

### Descripción
Cada integrante desarrolló un kata sencillo siguiendo el ciclo TDD:
- **Escribir un test que falle (RED)**
- **Ejecutar**
- **Escribir código mínimo (GREEN)**
- **Refactorizar**
- **Ejecutar nuevamente**

> [!NOTE]
> No se permite escribir código funcional sin que exista primero un test fallido.

---

### 📊 Evaluación SUMA

#### ¿La prueba realmente falla? (Fase RED)
**SÍ** - La fase RED se cumple correctamente.

Al ejecutar el test antes de implementar la función `sumar()`, el test **falla** con el error:

```
ImportError: cannot import name 'sumar' from 'suma'
```

El test definido fue:
```python
def test_sumar_dos_numeros():
    from suma import sumar
    assert sumar(2, 3) == 5
```

El test falla porque la función `sumar()` aún no existe. Este error confirma que el test está correctamente diseñado y detecta la ausencia de la funcionalidad.

#### ¿El código es mínimo? (Fase GREEN)
**SÍ** - Código mínimo en fase GREEN

```python
def sumar(a, b):
    return a + b
```

Esta implementación contiene únicamente la lógica necesaria para que el test pase. No hay validaciones adicionales, ni estructuras complejas. Cumple con el principio de TDD: escribir la menor cantidad de código posible para cumplir el comportamiento esperado.

#### ¿Se refactorizó o solo se dejó funcionando? (Fase REFACTOR)
**SÍ** - Se realizó refactorización

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

> [!IMPORTANT]
> **Mejoras del Refactor:**
> - Manejo de errores: Se añadió validación de tipos
> - Documentación: Se agregaron docstrings completos
> - Cumplimiento de contrato: El código es más robusto

---

### 📊 Evaluación RESTA

#### ¿La prueba realmente falla? (Fase RED)
**SÍ** - La fase RED se cumple correctamente.

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

#### ¿El código es mínimo? (Fase GREEN)
**SÍ** - Código mínimo en fase GREEN

```python
def restar(a, b):
    return a - b
```

Esta implementación es la solución más simple posible que hace pasar el test. Solo contiene la operación esencial sin ninguna lógica adicional.

#### ¿Se refactorizó o solo se dejó funcionando? (Fase REFACTOR)
**SÍ** - Se aplicó una mejora estructural

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

> [!TIP]
> La refactorización incluyó validación de tipos, documentación completa y manejo de errores, manteniendo la consistencia con el módulo de suma.

---

### ✅ Resultado de Tests

```
test_sumar_numeros_exito PASSED
test_restar_numeros_exito PASSED  
test_entrada_invalida PASSED
```

---

## 📦 Actividad 2: Sistema de Gestión de Inventario

### Descripción
Sistema simplificado de gestión de inventario desarrollado con metodología TDD, utilizando estructuras de datos en memoria.

**Funcionalidades implementadas:**
- ✅ Registrar un producto en el inventario
- ✅ Actualizar la cantidad disponible de un producto
- ✅ Consultar la información de un producto
- ✅ Listar los productos registrados

---

### 🔧 Análisis de Funcionalidades

| # | Funcionalidad | Descripción | Validación |
|---|---------------|-------------|-------------|
| 1 | **Registrar Producto** | Agregar un nuevo producto con nombre, cantidad y precio | Asignar ID único automáticamente |
| 2 | **Consultar Producto** | Buscar producto mediante ID | Retornar datos o None si no existe |
| 3 | **Actualizar Cantidad** | Modificar el stock disponible | Lanzar error si ID no es válido |
| 4 | **Listar Inventario** | Obtener lista completa de productos | Verificar cantidad de registros |

---

### 🔄 Ciclo TDD Aplicado

Para cada funcionalidad se respetó estrictamente el flujo:

1. **Fase RED:** Se escribió la prueba unitaria antes de que la lógica existiera. Se ejecutó `pytest` y se confirmó el fallo.
2. **Fase GREEN:** Se implementó el código mínimo necesario para que la prueba pasara.
3. **Fase REFACTOR:** Se optimizó el código (uso de `@dataclass`, diccionarios, manejo de excepciones) asegurando que los tests se mantuvieran en verde.

> [!WARNING]
> No se permite escribir código funcional sin que exista primero un test fallido.

---

### 📂 Estructura del Proyecto

```
EJERCICIOS TDD2/
├── funcionalidades/           # Lógica de la aplicación
│   ├── inventario.py        # Clase y lógica de inventario (Actividad 2)
│   ├── suma.py             # Funciones de suma (Actividad 1)
│   ├── resta.py            # Funciones de resta (Actividad 1)
│   └── pedido.py           # Sistema de pedidos (Actividad 3)
├── test/                    # Pruebas automatizadas (Pytest)
│   ├── test_actualizar_cantidad.py
│   ├── test_agregar_producto.py
│   ├── test_agregar_producto_invalido.py
│   ├── test_calcular_total.py
│   ├── test_consultar_producto.py
│   ├── test_crear_pedido.py
│   ├── test_descuento_invalido.py
│   ├── test_descuento_valido.py
│   ├── test_listar_productos.py
│   ├── test_multiples_productos.py
│   ├── test_sin_productos.py
│   ├── test_suma.py
│   ├── test_resta.py
│   └── conftest.py          # Configuración de pytest
├── README.md                # Documentación del proyecto
├── requirements.txt         # Dependencias (pytest==9.0.1)
└── .gitignore              # Archivos excluidos
```

---

### 📝 Bitácora Reflexiva

#### Micro-funcionalidad: Registrar un producto en el inventario

**RED:**
-Qué se esperaba: validar que el método `registrar_producto` exista y permita almacenar correctamente un producto.
-Qué falló: la prueba falló porque el método aún no estaba implementado.
-Mensaje de pytest: la prueba indicó que la funcionalidad no existía.

**GREEN:**
-Qué se implementó: se creó el método `registrar_producto` con la lógica mínima necesaria.
-Código mínimo aplicado: inserción del producto en una estructura interna (diccionario) y asignación de un ID autoincremental.

**REFACTOR:**
-Qué se mejoró: se reorganizó la lógica separando la creación del producto, la asignación de ID y el almacenamiento.
-Mejoras: uso de `@dataclass` para estructura de Producto.

---

#### Micro-funcionalidad: Consultar la información de un producto

**RED:**
-Qué se esperaba: validar el comportamiento del método `consultar_producto` para IDs válidos e inválidos.
-Qué falló: la prueba falló porque el método no existía inicialmente.

**GREEN:**
-Qué se implementó: se creó el método `consultar_producto` utilizando acceso directo al diccionario interno.
-Código mínimo aplicado: `self._productos.get(producto_id)`.

**REFACTOR:**
-Qué se mejoró: se documentó el método y se definió claramente su comportamiento ante datos inexistentes.
-Mejoras: validación de tipo para el identificador.

---

#### Micro-funcionalidad: Actualizar la cantidad disponible

**RED:**
-Qué se esperaba: validar que el método `actualizar_cantidad` modifique correctamente el stock.
-Qué falló: la prueba falló porque el método no existía.

**GREEN:**
-Qué se implementó: se añadió la lógica para ubicar el producto por ID y actualizar únicamente su cantidad.

**REFACTOR:**
-Qué se mejoró: se incorporaron validaciones para evitar cantidades negativas y manejar productos inexistentes mediante excepciones.

---

#### Micro-funcionalidad: Listar los productos registrados

**RED:**
-Qué se esperaba: verificar que el método `listar_productos` existiera y retornara una colección de productos.
-Qué falló: la prueba falló porque el método no estaba implementado.

**GREEN:**
-Qué se implementó: se creó el método `listar_productos` para retornar los productos almacenados en memoria.

**REFACTOR:**
-Qué se mejoró: se revisó la estructura de retorno para mantener consistencia, ordenando por ID.

---

## 📋 Actividad 3: Diseño de Casos de Prueba

### Descripción del Sistema
El sistema de gestión de pedidos permite:
- Crear pedidos de clientes
- Agregar productos al pedido con precio y cantidad
- Calcular el total del pedido
- Aplicar descuentos sobre el total

El sistema valida entradas incorrectas, como precios o cantidades menores o iguales a cero, y descuentos fuera del rango permitido.

---

### 📑 Escenarios de Prueba

| Escenario | Descripción | Entrada | Salida Esperada |
|-----------|-------------|---------|-----------------|
| 1 | Crear pedido | Nombre del cliente | Pedido creado con lista vacía |
| 2 | Agregar producto válido | Nombre producto, precio >0, cantidad >0 | Producto agregado (True) |
| 3 | Agregar producto inválido | Precio ≤0 o cantidad ≤0 | Producto no agregado (False) |
| 4 | Calcular total con productos | Lista de productos | Total correcto (suma de precio*cantidad) |
| 5 | Calcular total sin productos | Lista vacía | None |
| 6 | Aplicar descuento válido | Porcentaje entre 0 y 100 | Total con descuento aplicado |
| 7 | Aplicar descuento inválido | Porcentaje <0 o >100 | None |

---

### 🧪 Casos de Prueba Detallados

| ID | Escenario | Entrada | Resultado Esperado |
|----|-----------|---------|-------------------|
| CP01 | Crear pedido | "Juan" | Pedido creado con lista vacía |
| CP02 | Agregar producto válido | ("Producto1", 10000, 2) | True |
| CP03 | Agregar producto inválido (precio) | ("Producto2", -100, 1) | False |
| CP04 | Agregar producto inválido (cantidad) | ("Producto3", 1000, 0) | False |
| CP05 | Calcular total | Producto1:10000x2, Producto2:5000x3 | 35000 |
| CP06 | Múltiples productos | Producto1:10000x3, Producto2:5000x4 | 50000 |
| CP07 | Sin productos | [] | None |
| CP08 | Descuento válido 10% | Total=100000, porcentaje=10 | 90000 |
| CP09 | Descuento 0% | Total=100000, porcentaje=0 | 100000 |
| CP10 | Descuento 100% | Total=100000, porcentaje=100 | 0 |
| CP11 | Descuento inválido >100 | Total=100000, porcentaje=150 | None |
| CP12 | Descuento inválido negativo | Total=100000, porcentaje=-10 | None |

---

### 🎯 Casos Borde

> [!CAUTION]
> Los siguientes casos deben ser probados para asegurar la robustez del sistema:

- Precio = 0
- Cantidad = 0
- Pedido sin productos
- Descuento = 0%
- Descuento = 100%
- Descuento negativo
- Descuento > 100%

---

### ✓ Validaciones del Sistema

- ✅ No se permiten precios menores o iguales a 0
- ✅ No se permiten cantidades menores o iguales a 0
- ✅ El descuento debe estar entre 0 y 100
- ✅ No se puede calcular el total sin productos

---

### 🚀 Configuración y Ejecución

### Requisitos Técnicos
- **Lenguaje:** Python 3.13+
- **Framework de Pruebas:** Pytest 9.0.1
- **Control de Versiones:** Git

### Instalación
```bash
# Clonar el repositorio
git clone https://github.com/Isaac07-byte/EJERCICIOS-TDD2.git

# Activar entorno virtual (Windows)
.venv\Scripts\activate

# Instalar dependencias
pip install -r requirements.txt
```

### Ejecutar Pruebas
```bash
python -m pytest -v
```

---

## 🎓 Aprendizajes Clave

> [!TIP]
> Principios fundamentales aplicados en el taller:

1. **TDD permite detectar errores antes de implementar funcionalidades**
2. **El código mínimo en fase GREEN debe ser simple y funcional**
3. **La refactorización mejora la calidad sin afectar el comportamiento validado**
4. **El uso de diccionarios optimiza el acceso por ID**
5. **Los casos borde deben definirse desde las pruebas**
6. **Las pruebas automatizadas permiten detectar errores tempranos**
7. **Validar datos de entrada previene fallos en ejecución**
8. **El ciclo RED–GREEN–REFACTOR fortalece la disciplina de desarrollo**

---

## 📊 Conclusiones

### Actividad 1 (Kata)
- Se siguió correctamente la metodología TDD
- Los tests actúan como especificación del comportamiento
- La refactorización mejora la mantenibilidad sin alterar la funcionalidad

### Actividad 2 (Inventario)
- El sistema fue desarrollado de manera incremental
- Cada funcionalidad pasó por las tres fases de TDD
- Se logró un código robusto y testeable

### Actividad 3 (Casos de Prueba)
- El diseño de casos de prueba permite validar el correcto funcionamiento
- Se cubrieron escenarios normales y casos borde
- Se garantizó el manejo de entradas inválidas

---

*Documento desarrollado como parte del proceso de formación en Análisis y Desarrollo de Software - SENA Regional Bolívar*
