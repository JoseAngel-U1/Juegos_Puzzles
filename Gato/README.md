# 🎮 Juego del Gato - IA Difícil

Un juego clásico del Gato (Tic-Tac-Toe) desarrollado con Python y PySide6, donde puedes jugar contra una inteligencia artificial con estrategias avanzadas.

## 📋 Características

- ✅ **Interfaz Gráfica Moderna**: Interfaz intuitiva y atractiva con colores personalizados
- 🤖 **IA Inteligente**: Algoritmo con múltiples estrategias:
  - Busca ganar en el siguiente movimiento
  - Bloquea los intentos de victoria del jugador
  - Prioriza el centro del tablero
  - Toma esquinas estratégicas
  - Realiza movimientos aleatorios como último recurso
  - **2 niveles de dificultad**:
    - Fácil/Media → IA basada en estrategias inteligentes
    - Imposible → IA usando algoritmo Minimax
- 🎯 **Jugabilidad Fluida**: Interfaz responsiva y sin lag
- 🔄 **Función de Reinicio**: Botón para limpiar el tablero y jugar nuevamente
- 🎚️ **Selector de Dificultad**: Cambia entre niveles de IA sin cerrar el juego
- 📦 **Multiplataforma**: Compatible con Windows, macOS y Linux

## 🎮 Cómo Jugar

1. **Ejecuta el programa**
2. Antes de empezar, usa el menú desplegable **Dificultad** para elegir:
   - `Fácil/Media`
   - `Imposible`
3. **Eres la "X"** y haces el primer movimiento
4. **La IA es la "O"** y responde a tus movimientos
5. **Presiona "Limpiar"** para reiniciar el tablero

## 🎚️ Selector de dificultad

El juego incluye un control de dificultad en la parte superior de la ventana.

- **Fácil/Media**
  - Usa una IA estratégica basada en reglas.
  - Busca ganar, bloquea tus ataques, toma el centro y elige esquinas.
  - Usa un movimiento aleatorio como último recurso.
  - Ideal para partidas más relajadas.

- **Imposible**
  - Usa el algoritmo **Minimax**.
  - Evalúa todas las jugadas posibles y elige la mejor opción.
  - Juega sin errores y fuerza empate si el jugador no comete fallas.

> Cambiar la dificultad reinicia automáticamente el tablero para comenzar una nueva partida con el nivel seleccionado.

## 🛠️ Requisitos

- Python 3.8 o superior
- PySide6

## 📦 Instalación

### 1. Clonar el repositorio

```bash
git clone https://github.com/JoseAngel-U1/Juegos_Puzzles.git
cd Juegos_Puzzles
```

### 2. Instalar dependencias

```bash
pip install PySide6
```

### 3. Ejecutar el juego

```bash
python JuegoGato.py
```

## 🎯 Estrategia del Juego

La aplicación ofrece dos modos de IA:

- **Fácil/Media**: IA basada en prioridades. Se enfoca en ganar y bloquear con reglas simples.
- **Imposible**: IA con algoritmo Minimax que busca la mejor jugada en cada turno.

### IA Estratégica (Fácil/Media)

1. **Intenta ganar**: Si la IA puede completar una línea, lo hace.
2. **Bloquea al jugador**: Si el jugador puede ganar en el siguiente movimiento, bloquea.
3. **Toma el centro**: Busca la casilla central siempre que esté libre.
4. **Toma una esquina**: Prefiere las esquinas antes que los lados.
5. **Movimiento aleatorio**: Si ninguna de las anteriores aplica, elige una casilla disponible al azar.

### IA Minimax (Imposible)

- Evalúa todas las jugadas posibles en el tablero.
- Calcula el resultado óptimo para cada movimiento.
- Juega perfectamente y no comete errores.
- Si el jugador juega sin fallos, la partida termina en empate.

## 👨‍💻 Autor

**Jose Angel**

## 📄 Licencia

Este proyecto es de código abierto y está disponible bajo la licencia MIT.

## 🚀 Posibles Mejoras Futuras

- [ ] Modo multijugador (Jugador vs Jugador)
- [ ] Más niveles de dificultad (por ejemplo, Normal y Difícil separados)
- [ ] Estadísticas de juegos ganados/perdidos
- [ ] Temas visuales personalizables
- [ ] Sonidos y efectos visuales

## 📧 Contacto

Si tienes sugerencias o encuentras bugs, siéntete libre de abrir un issue o hacer un pull request.

---

**¿Crees que puedes ganarle a la IA? 🤔 ¡Inténtalo!**
