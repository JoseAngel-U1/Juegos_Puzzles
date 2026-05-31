# Puzzle 3x3 (Python)

Juego tipo Puzzle 3x3 desarrollado en Python utilizando PySide6.

El objetivo consiste en reorganizar las piezas numeradas hasta colocarlas en el orden correcto dejando el espacio vacío en la última posición.

Al completar el puzzle, el sistema muestra una imagen especial utilizada posteriormente como marcador para una aplicación de realidad aumentada desarrollada en Unity + Vuforia.

## Características

* Interfaz gráfica con PySide6.
* Mezcla aleatoria del tablero.
* Verificación de configuraciones resolubles.
* Movimiento por adyacencia.
* Detección automática de victoria.
* Visualización de imagen de recompensa.

## Tecnologías utilizadas

* Python 3
* PySide6
* Qt Framework

## Estructura

```text
py/
├── Puzzle15.py
├── Arbol.jpg
├── Puzzle 15.ico
└── README.md
```

## Funcionamiento

1. El tablero se mezcla aleatoriamente.
2. El jugador mueve las piezas.
3. El sistema valida movimientos permitidos.
4. Al resolver el puzzle:

   * aparece un mensaje de victoria;
   * se muestra la imagen `Arbol.jpg`.

Esta imagen puede ser utilizada por la aplicación móvil de realidad aumentada incluida en este proyecto.

## Instalación

Instalar dependencias:

```bash
pip install PySide6
```

Ejecutar:

```bash
python Puzzle15.py
```

## Relación con Realidad Aumentada

Este juego forma parte de una experiencia complementaria.

La imagen `Arbol.jpg` funciona como marcador visual (Image Target) para una aplicación móvil desarrollada en Unity + Vuforia capaz de mostrar un árbol 3D en realidad aumentada.
