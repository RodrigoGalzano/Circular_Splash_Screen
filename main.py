import sys
from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *

from ui_main import Ui_MainWindow
from ui_splash_screen import Ui_SplashScreen
from widgets import CircularProgress

# GOLBALS
counter = 0

class SplashScreen(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_SplashScreen()
        self.ui.setupUi(self)

        # Remove Title Bar
        self.setWindowFlag(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)

        # Import Circular Progress
        self.progress = CircularProgress()
        self.progress.width = 270
        self.progress.height = 270
        self.progress.value = 0
        self.progress.setFixedSize(self.progress.width, self.progress.height)
        self.progress.move(15, 15)
        self.progress.font_size = 40
        self.progress.add_shadow(True)
        self.progress.bg_color = QColor(68, 71, 90, 140)
        self.progress.setParent(self.ui.centralwidget)
        self.progress.show()


        self.shadow = QGraphicsDropShadowEffect(self)
        self.shadow.setBlurRadius(15)
        self.shadow.setXOffset(0)
        self.shadow.setYOffset(0)
        self.shadow.setColor(QColor(0, 0, 0, 80))
        self.setGraphicsEffect(self.shadow)  

        self.timer = QTimer() 
        self.timer.timeout.connect(self.update)  
        self.timer.start(25)   

        self.show()

    def update(self):
        global counter   

        # SET VALUE TO PORGRESS BAR
        self.progress.set_value(counter)

        if counter >= 100:
            self.timer.stop()  

            self.main = MainWindow()  
            self.main.show() 

            self.close()

        # Increase Counter
        counter += 1

class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)


if __name__ == "__main__":
        app = QApplication(sys.argv)
        window = SplashScreen()
        sys.exit(app.exec())

