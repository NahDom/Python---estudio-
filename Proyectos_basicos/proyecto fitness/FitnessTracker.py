# Pyqt -- Proyecto de aplicacion de ejercicio

# Imports

from PyQt6.QtCore import Qt, QDate
from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QBoxLayout,  QMessageBox, QTableWidget, QTableWidgetItem, QCheckBox, QDateEdit, QLineEdit,QHBoxLayout, QVBoxLayout,QHeaderView, QButtonGroup,QStyle
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
        self.events()

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
        
        self.sub_row1 = QHBoxLayout()
        self.sub_row2 = QHBoxLayout()
        self.sub_row3 = QHBoxLayout()
        self.sub_row4 = QHBoxLayout()

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

        self.aplicar_css()
        self.load_table()
    
     # Load tables

    # eventos de la interfaz
    def events(self):
        # realizo conexiones a los objetos boton para los eventos de la bd
        self.agregar.clicked.connect(self.add_workout)
        self.borrar.clicked.connect(self.delete)
        self.boton_enviar.clicked.connect(self.calculate)
        self.limpiar.clicked.connect(self.reset)
    
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
    def add_workout(self):
        # añado los objetos a la base de datos por medio de enlazamiento, es decir consultas de tipo DML a la BD con los datos del usuario, como la fecha, las calorias consumidas, la distancia recorrida y la descripcion del ejercicio
        Fecha = self.date_box.date().toString("dd-MM-yyyy")
        Calorias = self.kal_box.text()
        Distancia = self.distant_box.text()
        Descripcion = self.descripcion.text()

        # instancia de agregado de datos a la BD
        query = QSqlQuery("""
                          INSERT INTO fitness(Fecha, Calorias, Distancia, Descripcion)
                          VALUES(?,?,?,?)
                          """)
        # realizo una insercion de los datos dentro de la bd, es decir debo de adherir los datos para que el usuario en el checkbox confirme que son esos mismos
        query.addBindValue(Fecha)
        query.addBindValue(Calorias)
        query.addBindValue(Distancia)
        query.addBindValue(Descripcion)
        query.exec()

        # ahora quiero que por cada ejecucion esto se pueda limpiar para el usuario, asi puede ingresar mas de un ejercicio realizado
        self.date_box.setDate(QDate.currentDate())
        self.kal_box.clear()
        self.distant_box.clear()
        self.descripcion.clear()

        self.load_table()
 
    # delete tables
    def delete(self):
        selected_row = self.table.currentRow()
        #fila actual que selecciona el usuario
        if selected_row == -1:
            #el usuario todavia no selecciona nada
            QMessageBox.warning(self,"Error", "Por favor, debes seleccionar una fila para que sea borrada")
        
        fit_ID = int(self.table.item(selected_row,0).text()) 
        # como es un valor entero debo asegurar que sea el que el usuario selecciono
        confirm = QMessageBox.question(self, "¿Estás seguro?", "Borra este ejercicio", QMessageBox.StandardButton.Yes |QMessageBox.StandardButton.No)
        # los enums y referencialidades a botones de eventos cambiaron de pyqt5 a pyqt6 para que?
        # SAVE GOD!

        # si no es el que selecciono el usuario debo de retornar a la aplicacion
        if confirm == QMessageBox.StandardButton.No:
            return
        
        query = QSqlQuery()
        query.prepare("DELETE FROM fitness WHERE fit_ID = ?")
        #esto es asi porque es para el enlace que se da en la carga de los datos, nosotros aqui ahcemos ams referencia al enlace de SQLite de python para referenciar al elemento de la BD
        query.addBindValue(fit_ID)
        query.exec()

        self.load_table()
 
    #calcular calorias
    def calculate(self):

        distance = []
        calories = []
        # los introduzco en una lista para calcular la distancia media
        # realizo la consulta para obtener las calorias y distancia desde la BD
        query = QSqlQuery("SELECT Distancia, Calorias FROM fitness ORDER BY calorias ASC")
        # voy a recorrer la bd por medio los datos presentes
        while query.next():
            # vienen de la lista de valores ordinales
            dist_val = query.value(0)
            cal_val = query.value(1)
            distance.append(dist_val)
            calories.append(cal_val)

    
        try: 
            min_calorie = min(calories)
            max_calorie = max(calories)
            # lo envio a una lista para que pueda usarse como variable para la grafica de dispersion en mathplot
            calorias_normalizadas = [(calorie - min_calorie)/(max_calorie - min_calorie) for calorie in calories]

            # dibujo de la grafica
            plt.style.use("Solarize_Light2")
            ax = self.figure.subplots()
            ax.scatter(distance, calories, c = calorias_normalizadas, cmap= "plasma", label = "Meta de Calorias")
            ax.set_title("Distancia vs. Calorías", color='darkgray')
            ax.set_xlabel("Distancia", color='darkgray')
            ax.set_ylabel("Calorías", color='#B0B0B0')
            ax.tick_params(colors='#B0B0B0')
            cbar = ax.figure.colorbar(ax.collections[0], label="Calorías Normalizadas")
            cbar.ax.yaxis.label.set_color("#B0B0B0")
            cbar.ax.tick_params(color='#B0B0B0', labelcolor='#B0B0B0')
            self.canvas.draw()

        except Exception as e:
            QMessageBox.critical(self, "ERROR", f"Ocurrió un error: {str(e)}")


     # estilos
   
    # aplico estilos de CSS
    def aplicar_css(self):
        self.setStyleSheet("""
            QWidget {
                background-color: #0f1c2e;  /* azul marino oscuro */
                color: #e0e6ed;             /* texto claro */
                font-family: 'Segoe UI', sans-serif;
                font-size: 14px;
            }

            QLabel {
                color: #e0e6ed;
            }

            QLineEdit, QDateEdit, QTableWidget {
                background-color: #1e2d3f;
                border: 1px solid #3a4a5f;
                border-radius: 5px;
                padding: 5px;
                color: #ffffff;
            }

            QPushButton {
                background-color: #2874A6;
                color: white;
                border-radius: 6px;
                padding: 6px;
                font-weight: bold;
            }

            QPushButton:hover {
                background-color: #1F618D;
            }

            QPushButton:pressed {
                background-color: #154360;
            }

            QHeaderView::section {
                background-color: #1e2d3f;
                color: white;
                padding: 4px;
                border: 1px solid #3a4a5f;
            }

            QTableWidget {
                gridline-color: #3a4a5f;
                selection-background-color: #154360;
                selection-color: white;
            }

            QMessageBox {
                background-color: #1e2d3f;
            }
            """)
        ##########
        # REVISAR QUE PASO AQUI CON EL MODO OSCURO
        ##########
    # Modo oscuro

    # resetear
    def reset(self):
        self.date_box.setDate(QDate.currentDate())
        self.kal_box.clear()
        self.distant_box.clear()
        self.descripcion.clear()
        self.figure.clear()
        self.canvas.draw()
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