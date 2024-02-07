#### Must run this script with `sudo` ####

import sys
from pathlib import Path
from led_matrix import grid, left_turn_signal_on, left_turn_signal_off, right_turn_signal_on, right_turn_signal_off, third_brake_light_on, third_brake_light_off, rear_parking_lights_on, rear_parking_lights_off

from PySide6.QtCore import QObject, Slot
from PySide6.QtGui import QGuiApplication
from PySide6.QtQml import QQmlApplicationEngine



class ControlPanel(QObject):
	def __init__(self):
		super().__init__()


# --- Left Turn Signal button ------ #
	@Slot()
	def leftSignalOn(self):
		left_turn_signal_on(grid)
	
	@Slot()
	def leftSignalOff(self):
		left_turn_signal_off(grid)


# --- Right Turn Signal button ----- #
	@Slot()
	def rightSignalOn(self):
		right_turn_signal_on(grid)
	
	@Slot()
	def rightSignalOff(self):
		right_turn_signal_off(grid)


# --- Third Brake Light button ---------- #
	@Slot()
	def thirdBrakeLightOn(self):
		third_brake_light_on(grid)
	
	@Slot()
	def thirdBrakeLightOff(self):
		third_brake_light_off(grid)


# --- Rear Parking Lights button -------- #
	@Slot()
	def rearParkingLightsOn(self):
		rear_parking_lights_on(grid)
	
	@Slot()
	def rearParkingLightsOff(self):
		rear_parking_lights_off(grid)



if __name__ == "__main__":
	app = QGuiApplication(sys.argv)
	engine = QQmlApplicationEngine()

	controlPanel = ControlPanel()
	engine.rootContext().setContextProperty("controlPanel", controlPanel)

	qml_file = Path(__file__).parent / "main.qml"
	engine.load("main.qml")

	if not engine.rootObjects():
		sys.exit(-1)

	sys.exit(app.exec())
