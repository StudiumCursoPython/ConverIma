""" 
Curso Python empresa de 'Lenguaje de Programación Python'

Autor: José Antonio Calvo López

Fecha: Noviembre 2023

"""

from PyQt5 import QtCore, QtGui, QtWidgets
import os,sys

def resource_path(relative_path):
        """ Obtener el camino absoluto al recurso,
        funciona para el desarrollo y para el ejecutable único 
        """
        try:
            # PyInstaller crea un directorio temporal y almacena el path en _MEIPASS
            base_path = sys._MEIPASS
        except Exception:
            base_path = os.path.abspath(".")

        return os.path.join(base_path, relative_path)

class Ui_LoginDialog(object):
    

    def setupUi(self, LoginDialog):
        LoginDialog.setObjectName("LoginDialog")
        LoginDialog.resize(300, 220)

        icono_ruta = resource_path("Studium.png")
        icono = QtGui.QIcon(icono_ruta)
        LoginDialog.setWindowIcon(icono)

        # Configurar imagen de fondo
        fondo_ruta = resource_path("ImgCurso.png")
        self.background_pixmap = QtGui.QPixmap(fondo_ruta)
        self.background_label = QtWidgets.QLabel(LoginDialog)
        self.background_label.setGeometry(QtCore.QRect(0, 0, 300, 220))

        # Aplicar efecto de opacidad
        opacity_effect = QtWidgets.QGraphicsOpacityEffect()
        opacity_effect.setOpacity(0.5)  # Ajusta este valor según sea necesario
        self.background_label.setGraphicsEffect(opacity_effect)

        self.background_label.setPixmap(self.background_pixmap)
        self.background_label.setScaledContents(True)

        self.username_label = QtWidgets.QLabel(LoginDialog)
        self.username_label.setGeometry(QtCore.QRect(50, 50, 100, 30))
        font = QtGui.QFont()
        font.setFamily("ELEGANT TYPEWRITER")
        font.setPointSize(12)
        font.setItalic(False)
        self.username_label.setFont(font)
        self.username_label.setObjectName("username_label")

        self.username_input = QtWidgets.QLineEdit(LoginDialog)
        self.username_input.setGeometry(QtCore.QRect(150, 50, 100, 30))
        self.username_input.setObjectName("username_input")

        self.password_label = QtWidgets.QLabel(LoginDialog)
        self.password_label.setGeometry(QtCore.QRect(50, 100, 100, 30))
        font.setFamily("ELEGANT TYPEWRITER")
        font.setPointSize(12)
        font.setItalic(False)
        self.password_label.setFont(font)
        self.password_label.setObjectName("password_label")

        self.password_input = QtWidgets.QLineEdit(LoginDialog)
        self.password_input.setGeometry(QtCore.QRect(150, 100, 100, 30))
        self.password_input.setEchoMode(QtWidgets.QLineEdit.Password)
        self.password_input.setObjectName("password_input")

        self.login_button = QtWidgets.QPushButton(LoginDialog)
        self.login_button.setGeometry(QtCore.QRect(100, 150, 100, 50))
        
        self.login_button.setObjectName("login_button")

        self.retranslateUi(LoginDialog)
        QtCore.QMetaObject.connectSlotsByName(LoginDialog)

    def retranslateUi(self, LoginDialog):
        _translate = QtCore.QCoreApplication.translate
        LoginDialog.setWindowTitle(_translate("LoginDialog", "Login"))
        self.username_label.setText(_translate("LoginDialog", "Usuario:"))
        self.password_label.setText(_translate("LoginDialog", "Contraseña:"))
        self.login_button.setText(_translate("LoginDialog", "Login"))


class LoginDialog(QtWidgets.QDialog, Ui_LoginDialog):
    def __init__(self, db, parent=None):
        super(LoginDialog, self).__init__(parent)
        self.setupUi(self)
        self.db = db
        self.login_button.clicked.connect(self.check_credentials)

    def check_credentials(self):
        username = self.username_input.text()
        password = self.password_input.text()

        cursor = self.db.cursor()
        cursor.execute("SELECT * FROM Claves WHERE nombre = %s AND clave = %s", (username, password))
        result = cursor.fetchone()

        if result is not None:
            self.accept()
        else:
            QtWidgets.QMessageBox.warning(self, "Login error", "Incorrect username or password.")





