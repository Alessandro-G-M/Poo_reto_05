# Poo_reto_05

## Descripción del Reto

Este repositorio contiene una solución modularizada para trabajar con figuras geométricas en Python. La solución utiliza **paquetes y módulos** para organizar el código de manera eficiente, y se implementa de dos formas:

1. **Paquete con módulos individuales**: Cada clase tiene su propio archivo dentro del paquete, y las clases heredan de la clase base `Shape`.
2. **Paquete único con un módulo (`Shape.py`)**: Todas las clases se encuentran en un único archivo dentro del paquete.

## Estructura del Paquete

El proyecto incluye dos configuraciones de paquetes, según la solución implementada:

### Solución 1: Módulos individuales
```
Reto_05/
├── 1/
│   ├── Package/
│   │   ├── __pycache__/        # Archivos de caché de Python
│   │   ├── Rectangle.py        # Clase Rectangle
│   │   ├── Shape.py            # Clase base Shape
│   │   ├── Triangle.py         # Clase Triangle
│   │   └── __init__.py         # Archivo para definir el paquete
│   └── main.py                 # Programa principal
```

### Solución 2: Módulo único
```
Reto_05/
├── 2/
│   ├── Package/
│   │   ├── __pycache__/        # Archivos de caché de Python
│   │   ├── Shape.py            # Todas las clases en un único archivo
│   │   └── __init__.py         # Archivo para definir el paquete
│   └── main.py                 # Programa principal
```

