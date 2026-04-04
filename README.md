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

## 📝 5. Bitácora Reflexiva
* **Mayor dificultad:** Configurar las *fixtures* de Pytest para que el inventario se reiniciara entre cada prueba, evitando que el estado de un test afectara al siguiente.
* **Lección aprendida:** El uso de TDD nos obligó a pensar en los "casos borde" (como intentar actualizar un producto que no existe) antes de escribir la primera línea de lógica, lo que resultó en un código más limpio y menos propenso a errores desde el inicio.

Gestión de Archivos: Se configuró el .gitignore para evitar subir carpetas temporales de Python como __pycache__ o el entorno virtual .venv.

Aprendizaje: El desarrollo basado en pruebas permitió detectar errores de importación y lógica de manera temprana, facilitando la integración de los módulos de inventario, suma y resta.