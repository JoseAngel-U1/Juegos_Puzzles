import os, sys, random
from PySide6.QtWidgets import QApplication, QWidget, QPushButton, QGridLayout, QMessageBox, QVBoxLayout, QLabel, QHBoxLayout
from PySide6.QtCore import Qt
from PySide6.QtGui import QPixmap, QIcon

def Cls():
    os.system("cls")

Cls()
#! Estado del tablero
board = list(range(1, 9)) + [None]
empty_index = 8
buttons = []

def is_solvable(board):
    inversion_count = 0
    nums = [n for n in board if n is not None]
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] > nums[j]:   
                inversion_count += 1
    return inversion_count % 2 == 0

def shuffle_board():
    global board, empty_index
    while True:
        random.shuffle(board)
        if is_solvable(board):
            break
    empty_index = board.index(None)

def check_win():
    return board == list(range(1, 9)) + [None]

def update_ui():
    for i, val in enumerate(board):
        btn = buttons[i]
        if val is not None:
            btn.setText(str(val))
            btn.setEnabled(True)
            btn.setStyleSheet("background-color: #3498DB; font-size: 20px; color: white;")
        else:
            btn.setText("")
            btn.setEnabled(False)
            btn.setStyleSheet("background-color: #34495E;")

def move_piece(index):
    global empty_index
    row1, col1 = divmod(index, 3)
    row2, col2 = divmod(empty_index, 3)

    if (abs(row1 - row2) == 1 and col1 == col2) or (abs(col1 - col2) == 1 and row1 == row2):
        board[empty_index], board[index] = board[index], board[empty_index]
        empty_index = index
        update_ui()

        if check_win():
            QMessageBox.information(window, "¡Ganaste!", "¡Felicidades, has completado el puzzle!")
            show_win_image()  #* Muestra la imagen al ganar "Arbol"

def restart():
    shuffle_board()
    update_ui()

def show_win_image():
    msg = QMessageBox(window)
    msg.setWindowTitle("¡Ganaste!")
    msg.setIcon(QMessageBox.Information)

    ruta = os.path.join(os.path.dirname(__file__), "Arbol.jpg")

    pixmap = QPixmap(ruta)

    if pixmap.isNull():
        print("No se pudo cargar:", ruta)
        msg.setText("Ganaste, pero no se encontró la imagen.")
    else:
        pixmap = pixmap.scaled(
            200, 200,
            Qt.KeepAspectRatio,
            Qt.SmoothTransformation
        )

        img_label = QLabel()
        img_label.setPixmap(pixmap)
        msg.layout().addWidget(img_label, 1, 1)
        msg.setText("¡Felicidades, has completado el puzzle!")

    msg.exec()

#! === Interfaz ===
app = QApplication(sys.argv)
window = QWidget() #? Crear ventana
window.setWindowTitle("Puzzle 3x3 - Jose Angel") #? Titulo de la ventana
window.setWindowIcon(QIcon("Puzzle 15.ico")) #? Icono de las ventanas
window.setStyleSheet("background-color: #2C3E50;") #? Fondo de la ventana

#TODO: deseño principal:
main_layout = QVBoxLayout()

title = QLabel("Puzzle 3x3")
title.setAlignment(Qt.AlignCenter)
title.setStyleSheet("font-size: 24px; font-weight: bold; color: #ECF0F1;")
main_layout.addWidget(title)

grid = QGridLayout()
for i in range(9):
    btn = QPushButton()
    btn.setFixedSize(100, 100)
    btn.setStyleSheet("font-size: 20px; font-weight: bold; background-color: #3498DB;")
    btn.clicked.connect(lambda checked, idx=i: move_piece(idx))
    grid.addWidget(btn, i // 3, i % 3)
    buttons.append(btn)

main_layout.addLayout(grid)

#* Botón mezclar
bottom = QHBoxLayout()
btn_reset = QPushButton("Mezclar")
btn_reset.setFixedSize(100, 40)
btn_reset.setStyleSheet("background-color: #E67E22; font-weight: bold;")
btn_reset.clicked.connect(restart)
bottom.addWidget(btn_reset, alignment=Qt.AlignCenter)
main_layout.addLayout(bottom)

window.setLayout(main_layout)

shuffle_board()
update_ui()

window.show()
sys.exit(app.exec())
