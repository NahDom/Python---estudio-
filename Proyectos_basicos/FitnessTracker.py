# Pyqt -- Proyecto de aplicacion de ejercicio

# Imports

from PyQt6.QtCore import Qt, QDate
from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QBoxLayout, QMessageBox, QTableWidget, QTableWidgetItem, QCheckBox, QDateEdit, QLineEdit,QHBoxLayout, QVBoxLayout,QHeaderView
from PyQt6.QtSql import QSqlDatabase, QSqlQuery

###
import matplotlib.pyplot as plt 
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
###
import numpy as np
from sys import exit

# Main class
class FitTrack(QWidget):
    def __init__(self):
        super().__init__()
        self.settings()
        self.initUI()
    # init UI

    #configuracion
    def settings(self):
        self.setWindowTitle("😊FitTracker👌")
        self.resize(800,600)

    # defino todas las clases de la interfaz de usuario
    def initUI(self):
        self.date_box = QDateEdit()
        self.date_box.setDate(QDate.currentDate())
        self.kal_box = QLineEdit()
        self.kal_box.setPlaceholderText("Numero de calorias quemadas")
        self.distant_box = QLineEdit()
        self.distant_box.setPlaceholderText(" Ingrese distancia recorrida")
        self.descripcion = QLineEdit()
        self.descripcion.setPlaceholderText("Ingrese una descripcion")

        self.boton_enviar = QPushButton("Enviar")
        self.agregar = QPushButton("Agregar")
        self.borrar = QPushButton("Borrar")
        self.limpiar = QPushButton("Limpiar")
        self.modo_oscuro = QPushButton("Modo Oscuro")

        self.table = QTableWidget()
        self.table.setColumnCount(5)
        self.table.setHorizontalHeaderLabels(["ID","Fecha","Calorias","Distancia","Descripcion"])
        self.table.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.Stretch)


        self.figure = plt.figure()
        self.canvas = FigureCanvas(self.figure)

        # diseño de layout
        self.master_layout = QHBoxLayout()
        self.columna1 = QVBoxLayout()
        self.columna2 = QVBoxLayout()
        
        self.sub_row1 = QVBoxLayout()
        self.sub_row2 = QVBoxLayout()
        self.sub_row3 = QVBoxLayout()
        self.sub_row4 = QVBoxLayout()

        self.sub_row1.addWidget(QLabel("Fecha: "))
        self.sub_row1.addWidget(self.date_box)
        self.sub_row2.addWidget(QLabel("Calorias "))
        self.sub_row2.addWidget(self.kal_box)
        self.sub_row3.addWidget(QLabel("Km "))
        self.sub_row3.addWidget(self.distant_box)
        self.sub_row4.addWidget(QLabel("Descripcion: "))
        self.sub_row4.addWidget(self.descripcion)

        self.columna1.addLayout(self.sub_row1)
        self.columna1.addLayout(self.sub_row2)
        self.columna1.addLayout(self.sub_row3)
        self.columna1.addLayout(self.sub_row4)
        self.columna1.addWidget(self.modo_oscuro)

        btn_row1 = QHBoxLayout()
        btn_row2 = QHBoxLayout()

        btn_row1.addWidget(self.agregar)
        btn_row1.addWidget(self.borrar)
        btn_row2.addWidget(self.boton_enviar)
        btn_row2.addWidget(self.limpiar)

        self.columna1.addLayout(btn_row1)
        self.columna1.addLayout(btn_row2)

        self.columna2.addWidget(self.canvas)
        self.columna2.addWidget(self.table)

        self.master_layout.addLayout(self.columna1, 30)
        self.master_layout.addLayout(self.columna2, 70)
        self.setLayout(self.master_layout)

        self.load_table()
    
     # Load tables

    # Load tables
    def load_table(self):
        self.table.setRowCount(0)
        query = QSqlQuery("SELECT * FROM fitness ORDER BY Fecha DESC")
        row = 0
        while query.next():
            fit_ID = query.value(0)
            Fecha = query.value(1)
            Calorias = query.value(2)
            Distancia = query.value(3)
            Descripcion = query.value(4)

            self.table.insertRow(row)
            self.table.setItem(row, 0, QTableWidgetItem(str(fit_ID)))
            self.table.setItem(row, 1, QTableWidgetItem(Fecha))
            self.table.setItem(row, 2, QTableWidgetItem(str(Calorias)))
            self.table.setItem(row, 3, QTableWidgetItem(str(Distancia)))
            self.table.setItem(row, 4, QTableWidgetItem(Descripcion))
            row += 1

    
    # add tables

    # delete tables

    #calcular calorias

    #clicks

    # Modo oscuro

    # resetear

# Inicializar la base de datos

if __name__ == "__main__":
    app = QApplication([])

    db = QSqlDatabase.addDatabase("QSQLITE")
    db.setDatabaseName("fitness.db")

    if not db.open():
        QMessageBox.critical(None, "ERROR","Cannot open the database")
        exit(2)

    query = QSqlQuery()
    query.exec("""
                CREATE TABLE IF NOT EXISTS fitness(
                fit_ID INTEGER PRIMARY KEY AUTOINCREMENT,
                Fecha TEXT,
                Calorias REAL,
                Distancia REAL,
                Descripcion TEXT
                )
                """)

    main = FitTrack()
    main.show()
    app.exec()