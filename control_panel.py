#### Must run this script with `sudo` ####

import sys
from pathlib import Path
from led_matrix import main
from multiprocessing import Process, Event
from PySide6.QtCore import QObject, Signal, Slot
from PySide6.QtGui import QGuiApplication
from PySide6.QtQml import QQmlApplicationEngine



class ControlPanel(QObject):
	processStarted = Signal(str)

	def __init__(self):
		super().__init__()
		self.stop_event = Event()
		self.current_process = None


	@Slot(str)
	def runAnimation(self, animation_name):
		if self.current_process and self.current_process.is_alive():
			self.stop_event.set()
			self.current_process.join()

		self.stop_event.clear()
		self.current_process = Process(target = main, args = (animation_name, self.stop_event))
		self.current_process.start()
		self.processStarted.emit(animation_name)


if __name__ == "__main__":
	controlPanel = ControlPanel()
	qml_file = Path(__file__).parent / "Main.qml"
	app = QGuiApplication(sys.argv)

	engine = QQmlApplicationEngine()
	engine.rootContext().setContextProperty("controlPanel", controlPanel)
	engine.load("Main.qml")
	engine.quit.connect(app.quit)

	if not engine.rootObjects():
		sys.exit(-1)

	sys.exit(app.exec())
