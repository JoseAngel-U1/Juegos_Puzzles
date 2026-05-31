import os, sys, random
from PySide6.QtWidgets import QApplication, QWidget, QPushButton, QGridLayout, QMessageBox, QVBoxLayout, QLabel, QHBoxLayout, QComboBox
from PySide6.QtCore import Qt, QTimer
from PySide6.QtGui import QIcon

def cls():
    os.system('cls' if os.name == 'nt' else 'clear')

cls()

buttons = []
dificultad = "Fácil/Media"  #? valor por defecto

#* Combinaciones ganadoras
combinaciones = [
    [0, 1, 2], [3, 4, 5], [6, 7, 8],  #? Filas
    [0, 3, 6], [1, 4, 7], [2, 5, 8],  #? Columnas
    [0, 4, 8], [2, 4, 6]              #? Diagonales
]

#* Verifica si alguien ganó o empate
def verificar_ganador():
    for c in combinaciones:
        if buttons[c[0]].text() != "" and buttons[c[0]].text() == buttons[c[1]].text() == buttons[c[2]].text():
            return buttons[c[0]].text()
    
    if all(btn.text() != "" for btn in buttons):
        return "Empate"
    
    return None

#* Jugada del jugador
def marcar(idx):
    if buttons[idx].text() == "":
        buttons[idx].setText("X")

        ganador = verificar_ganador()
        if ganador:
            mostrar_resultado(ganador)
            return
        
        #** Desactivar tablero
        for btn in buttons:
            btn.setEnabled(False)

        QTimer.singleShot(150, turno_maquina)

#* Turno de la máquina - IA BÁSICA (Dificultad Fácil/Media)
def turno_maquina_basica():
    casillas_libres = [i for i, btn in enumerate(buttons) if btn.text() == ""]
    
    #** Buscar ganar
    for i in casillas_libres:
        buttons[i].setText("O")
        if verificar_ganador() == "O":
            mostrar_resultado("O")
            return
        buttons[i].setText("")  #? Deshacer simulación

    #** Bloquear jugador si va a ganar
    for i in casillas_libres:
        buttons[i].setText("X")
        if verificar_ganador() == "X":
            buttons[i].setText("")      #? quitar simulación
            buttons[i].setText("O")     #? bloquear de verdad

            ganador = verificar_ganador()
            if ganador:
                mostrar_resultado(ganador)
            return
        
        buttons[i].setText("")

    #** Elegir centro si está libre
    if buttons[4].text() == "":
        buttons[4].setText("O")
        ganador = verificar_ganador()
        if ganador:
            mostrar_resultado(ganador)
        return

    #** Elegir esquinas si hay
    esquinas = [i for i in [0, 2, 6, 8] if buttons[i].text() == ""]
    if esquinas:
        eleccion = random.choice(esquinas)
        buttons[eleccion].setText("O")
        ganador = verificar_ganador()
        if ganador:
            mostrar_resultado(ganador)
        return

    #** Si no, jugada aleatoria
    if casillas_libres:
        eleccion = random.choice(casillas_libres)
        buttons[eleccion].setText("O")
        ganador = verificar_ganador()
        if ganador:
            mostrar_resultado(ganador)

#* Turno de la máquina - IA MINIMAX (Dificultad Imposible)
def turno_maquina_minimax():
    mejor_score = -float("inf")
    mejor_jugada = None

    for i, btn in enumerate(buttons):
        if btn.text() == "":
            btn.setText("O")
            score = minimax(False)
            btn.setText("")
            if score > mejor_score:
                mejor_score = score
                mejor_jugada = i

    if mejor_jugada is not None:
        buttons[mejor_jugada].setText("O")
        ganador = verificar_ganador()
        if ganador:
            mostrar_resultado(ganador)

#* Algoritmo Minimax
def minimax(es_turno_maquina):
    ganador = verificar_ganador()
    if ganador == "O":
        return 1
    elif ganador == "X":
        return -1
    elif ganador == "Empate":
        return 0

    if es_turno_maquina:
        mejor_score = -float("inf")
        for i, btn in enumerate(buttons):
            if btn.text() == "":
                btn.setText("O")
                score = minimax(False)
                btn.setText("")
                mejor_score = max(score, mejor_score)
        return mejor_score
    else:
        peor_score = float("inf")
        for i, btn in enumerate(buttons):
            if btn.text() == "":
                btn.setText("X")
                score = minimax(True)
                btn.setText("")
                peor_score = min(score, peor_score)
        return peor_score

#* Selecciona el turno según dificultad
def turno_maquina():
    if dificultad == "Fácil/Media":
        turno_maquina_basica()
    else:
        turno_maquina_minimax()
    
    #** Reactivar tablero
    for btn in buttons:
        if btn.text() == "":
            btn.setEnabled(True)

#* Mostrar resultado (ganador o empate)
def mostrar_resultado(ganador):
    if ganador == "Empate":
        QMessageBox.information(window, "Empate", "¡El juego terminó en empate!")
    else:
        QMessageBox.information(window, "Ganador", f"¡{ganador} ha ganado!")
    limpiar()

#* Limpiar el tablero
def limpiar():
    for btn in buttons:
        btn.setText("")
        btn.setEnabled(True)
        btn.setStyleSheet("""
            QPushButton {
                font-size: 20px;
                font-weight: bold;
                background-color: #3498DB;
                color: white;
            }

            QPushButton:disabled {
                background-color: #3498DB;
                color: white;
            }
        """)

#* Cambiar dificultad
def cambiar_dificultad(valor):
    global dificultad
    dificultad = valor
    limpiar()

#* === Interfaz ===
app = QApplication(sys.argv)
window = QWidget()
window.setWindowTitle("Gato - Jose Angel")
window.setStyleSheet("background-color: #2C3E50;")

main_layout = QVBoxLayout()

title = QLabel("Gato - 1 Jugador")
title.setAlignment(Qt.AlignCenter)
title.setStyleSheet("font-size: 24px; font-weight: bold; color: #ECF0F1;")
main_layout.addWidget(title)

#* Selector de dificultad
selector_layout = QHBoxLayout() 

label_dif = QLabel("Dificultad:")
label_dif.setStyleSheet("color: #ECF0F1; font-weight: bold;")

combo_dificultad = QComboBox()
combo_dificultad.addItems(["Fácil/Media", "Imposible"])
combo_dificultad.setStyleSheet("background-color: #34495E; color: #ECF0F1; padding: 5px;")
combo_dificultad.currentTextChanged.connect(cambiar_dificultad)

#** Centrado
selector_layout.addStretch()
selector_layout.addWidget(label_dif)
selector_layout.addWidget(combo_dificultad)
selector_layout.addStretch()

main_layout.addLayout(selector_layout)

grid = QGridLayout()
for i in range(9):
    btn = QPushButton()
    btn.setFixedSize(100, 100)
    btn.setStyleSheet("""
        QPushButton {
            font-size: 20px;
            font-weight: bold;
            background-color: #3498DB;
            color: white;
        }

        QPushButton:disabled {
            background-color: #3498DB;
            color: white;
        }
    """)
    btn.clicked.connect(lambda checked, idx=i: marcar(idx))
    grid.addWidget(btn, i // 3, i % 3)
    buttons.append(btn)

main_layout.addLayout(grid)

#* Botón Limpiar
bottom = QHBoxLayout()
btn_reset = QPushButton("Limpiar")
btn_reset.setFixedSize(100, 40)
btn_reset.setStyleSheet("background-color: #E67E22; font-weight: bold;")
btn_reset.clicked.connect(limpiar)
bottom.addWidget(btn_reset, alignment=Qt.AlignCenter)
main_layout.addLayout(bottom)

window.setLayout(main_layout)
window.show()
sys.exit(app.exec())
