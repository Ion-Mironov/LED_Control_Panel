from PySide6.QtGui import QGuiApplication
from PySide6.QtQml import QQmlApplicationEngine
import sys


if __name__ == "__main__":
	app = QGuiApplication(sys.argv)
	engine = QQmlApplicationEngine()
	engine.load('Main.qml')

	if not engine.rootObjects():
		sys.exit(-1)

sys.exit(app.exec())
