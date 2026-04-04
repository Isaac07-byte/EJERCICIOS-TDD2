# 📦 Sistema de Gestión de Inventario (TDD) - Actividad 2

Este proyecto implementa un sistema de inventario simplificado utilizando la metodología **TDD (Test-Driven Development)**, desarrollado como parte de la formación en **Análisis y Desarrollo de Software (ADSO)** en el SENA - Regional Bolívar.

## 👥 Aprendices
* **Isaac Chico**
* **Michael Vergara**
* **Ficha:** 2995985
* **Instructora:** Mara Sofía Cabrales

---

## 🛠️ 1. Análisis de Funcionalidades
Antes de iniciar la codificación, se identificaron las operaciones esenciales que el sistema debe soportar para garantizar un diseño incremental y robusto:

1.  **Registrar Producto:** * *Descripción:* Agregar un nuevo producto al sistema con un nombre, cantidad y precio.
    * *Validación:* El sistema debe asignar un ID único automáticamente.
2.  **Consultar Producto:** * *Descripción:* Buscar un producto específico mediante su ID único.
    * *Validación:* Retornar los datos del producto o un valor nulo si no existe.
3.  **Actualizar Cantidad:** * *Descripción:* Modificar el stock disponible de un producto existente.
    * *Validación:* Debe lanzar un error (ValueError) si el ID del producto no es válido.
4.  **Listar Inventario:** * *Descripción:* Obtener una lista completa de todos los productos registrados.
    * *Validación:* Verificar que el tamaño de la lista coincida con el número de registros realizados.

---

## 🚀 2. Configuración del Entorno

### Requisitos Técnicos
* **Lenguaje:** Python 3.13+
* **Framework de Pruebas:** Pytest 9.0.1
* **Control de Versiones:** Git

### Instalación y Ejecución
1.  **Clonar el repositorio:**
    ```bash
    git clone <https://github.com/Isaac07-byte/EJERCICIOS-TDD2.git>
    cd "EJERCICIOS TDD2"
    ```
2.  **Activar entorno virtual:**
    ```bash
    # Windows
    .venv\Scripts\activate
    ```
3.  **Instalar dependencias:**
    ```bash
    pip install -r requirements.txt
    ```
4.  **Ejecutar Pruebas Automatizadas (Ciclo TDD):**
    ```bash
    python -m pytest -v
    ```

---

## 🔄 3. Ciclo TDD Aplicado
Para cada funcionalidad se respetó estrictamente el flujo:

* **Fase RED:** Se escribió la prueba unitaria en la carpeta `test/` antes de que la lógica existiera. Se ejecutó `pytest` y se confirmó el fallo (Estandarización del error).
* **Fase GREEN:** Se implementó el código mínimo necesario en `src/inventario.py` para que la prueba pasara.
* **Fase REFACTOR:** Se optimizó el código (uso de `@dataclass`, diccionarios para búsquedas rápidas y manejo de excepciones) asegurando que los tests se mantuvieran en verde.

---

## 📂 4. Estructura del Proyecto

EJERCICIOS TDD2/
├── funcionalidades/      # Lógica de la aplicación
│   ├── inventario.py    # Clase y lógica de inventario
│   ├── suma.py          # Lógica de suma
│   └── resta.py         # Lógica de resta
├── test/                # Pruebas automatizadas (Pytest)
│   ├── test_actualizar_cantidad.py
│   ├── test_agregar_producto.py
│   ├── test_consultar_producto.py
│   ├── test_listar_productos.py
│   ├── test_suma.py
│   └── test_resta.py
├── .gitignore          # Archivos excluidos del control de versiones
├── README.md           # Documentación del proyecto
└── requirements.txt    # Dependencias (pytest==9.0.1)
---

Aquí tienes tu **bitácora completamente corregida, coherente con tu código real y lista para copiar/pegar en Word** 👇

---

## 📝 5. Bitácora Reflexiva

### Micro-funcionalidad: Registrar un producto en el inventario

**Objetivo:** Verificar que el sistema permita crear y almacenar un producto con nombre, cantidad, precio e identificador.

**RED**

* Qué se esperaba: validar que el método `registrar_producto` exista y permita almacenar correctamente un producto.
* Qué falló: la prueba falló porque el método aún no estaba implementado.
* Mensaje de pytest: la prueba indicó que la funcionalidad no existía.
* Interpretación técnica: el fallo confirmó que el comportamiento esperado no estaba implementado, validando correctamente la fase RED.

**GREEN**

* Qué se implementó: se creó el método `registrar_producto` con la lógica mínima necesaria para almacenar el producto en memoria.
* Código mínimo aplicado: inserción del producto en una estructura interna (diccionario) y asignación de un ID autoincremental.
* Resultado de la prueba: la prueba pasó correctamente, validando atributos, persistencia e incremento de IDs.

**REFACTOR**

* Qué se mejoró: se reorganizó la lógica separando la creación del producto, la asignación de ID y el almacenamiento.
* Motivo técnico: mejorar la legibilidad, mantenimiento y escalabilidad del código.
* Verificación posterior: todas las pruebas continuaron en estado exitoso.

**Dificultades encontradas:** definir un mecanismo consistente de ID autoincremental sin afectar la integridad del inventario.
**Lecciones aprendidas:** en TDD, primero se valida el comportamiento esperado mediante pruebas antes de implementar la lógica.
**Próximos pasos:** agregar validaciones para datos inválidos (nombre vacío, cantidad negativa, precio incorrecto).
**Evidencia:** commits del test, implementación y ejecución exitosa de pytest.

---

### Micro-funcionalidad: Consultar la información de un producto

**Objetivo:** Verificar que el sistema retorne la información del producto cuando el ID existe y `None` cuando no existe.

**RED**

* Qué se esperaba: validar el comportamiento del método `consultar_producto` para IDs válidos e inválidos.
* Qué falló: la prueba falló porque el método no existía inicialmente.
* Mensaje de pytest: error indicando ausencia del método.
* Interpretación técnica: evidenció la necesidad de implementar la funcionalidad de consulta.

**GREEN**

* Qué se implementó: se creó el método `consultar_producto` utilizando acceso directo al diccionario interno.
* Código mínimo aplicado: `self._productos.get(producto_id)`.
* Resultado de la prueba: el método retornó correctamente el objeto o `None` según el caso.

**REFACTOR**

* Qué se mejoró: se documentó el método y se definió claramente su comportamiento ante datos inexistentes.
* Motivo técnico: mejorar claridad y mantenibilidad del código.
* Verificación posterior: todas las pruebas permanecieron en estado verde.

**Dificultades encontradas:** asegurar el manejo correcto de IDs inexistentes sin generar errores.
**Lecciones aprendidas:** el uso de `.get()` permite manejar casos borde de forma simple y eficiente.
**Próximos pasos:** evaluar validación de tipo para el identificador.
**Evidencia:** pruebas automatizadas y ejecución exitosa.

---

### Micro-funcionalidad: Actualizar la cantidad disponible de un producto

**Objetivo:** Verificar que el sistema permita modificar la cantidad de un producto existente manteniendo la integridad de los demás atributos.

**RED**

* Qué se esperaba: validar que el método `actualizar_cantidad` modifique correctamente el stock.
* Qué falló: la prueba falló porque el método no existía o no cumplía con las validaciones esperadas.
* Mensaje de pytest: fallo por ausencia de implementación o error en aserciones.
* Interpretación técnica: evidenció la necesidad de implementar una operación específica de actualización.

**GREEN**

* Qué se implementó: se añadió la lógica para ubicar el producto por ID y actualizar únicamente su cantidad.
* Código mínimo aplicado: búsqueda en la estructura interna y modificación del atributo cantidad.
* Resultado de la prueba: la actualización fue exitosa y consistente.

**REFACTOR**

* Qué se mejoró: se incorporaron validaciones para evitar cantidades negativas y manejar productos inexistentes mediante excepciones.
* Motivo técnico: fortalecer la robustez y evitar estados inválidos.
* Verificación posterior: todas las pruebas pasaron correctamente.

**Dificultades encontradas:** manejo de errores cuando el producto no existe o la cantidad es inválida.
**Lecciones aprendidas:** antes de modificar datos, es fundamental validar existencia y reglas de negocio.
**Próximos pasos:** centralizar validaciones en métodos reutilizables.
**Evidencia:** ejecución de pruebas con casos positivos y negativos.

---

### Micro-funcionalidad: Listar los productos registrados

**Objetivo:** Confirmar que el sistema devuelva todos los productos almacenados en el inventario.

**RED**

* Qué se esperaba: verificar que el método `listar_productos` existiera y retornara una colección de productos.
* Qué falló: la prueba falló porque el método no estaba implementado.
* Mensaje de pytest: error indicando ausencia del método.
* Interpretación técnica: el sistema no contaba con una vista global del inventario.

**GREEN**

* Qué se implementó: se creó el método `listar_productos` para retornar los productos almacenados en memoria.
* Código mínimo aplicado: retorno de la colección interna de productos.
* Resultado de la prueba: se validó correctamente el contenido y cantidad de elementos.

**REFACTOR**

* Qué se mejoró: se revisó la estructura de retorno para mantener consistencia con otras operaciones.
* Motivo técnico: facilitar la reutilización del método y mejorar diseño.
* Verificación posterior: no se afectaron funcionalidades existentes.

**Dificultades encontradas:** decidir si retornar copia o referencia de la colección.
**Lecciones aprendidas:** la fase REFACTOR permite mejorar diseño sin alterar el comportamiento validado.
**Próximos pasos:** evaluar inmutabilidad de la colección retornada.
**Evidencia:** pruebas automatizadas y resultados exitosos.

---

## Resumen de la Bitácora

Se aplicó el ciclo TDD de manera incremental para implementar las funcionalidades del sistema de inventario. En la fase RED se diseñaron pruebas que fallaron inicialmente, evidenciando la ausencia de funcionalidad. En la fase GREEN se desarrolló el código mínimo necesario para cumplir los requisitos. En la fase REFACTOR se mejoró la estructura del código sin afectar el comportamiento validado, manteniendo todas las pruebas en estado exitoso.

---

## Aprendizajes Clave

* TDD permite detectar errores antes de implementar funcionalidades.
* El código mínimo en fase GREEN debe ser simple y funcional.
* La refactorización mejora la calidad sin afectar el comportamiento validado.
* El uso de diccionarios optimiza el acceso por ID.
* Los casos borde deben definirse desde las pruebas.
* La indentación en Python es crítica para la estructura del código.
* Las pruebas automatizadas permiten detectar errores tempranos.
* Validar datos de entrada previene fallos en ejecución.
* La configuración de `.gitignore` mantiene el repositorio limpio.
* El ciclo RED–GREEN–REFACTOR fortalece la disciplina de desarrollo.