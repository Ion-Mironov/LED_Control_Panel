#### Must run this script with `sudo` ####

import sys
import threading
from pathlib import Path
from led_matrix import grid, stop_animation, left_turn_signal, front_parking_lights, right_turn_signal, sequential_brake_lights, third_brake_light, rear_parking_lights
from PySide6.QtCore import QObject, Slot, Signal
from PySide6.QtGui import QGuiApplication
from PySide6.QtQml import QQmlApplicationEngine


class ControlPanel(QObject):
	animationStateChanged = Signal(int, bool)								# Signal to communicate animation state changes

	def __init__(self):
		super().__init__()
		self.current_animation_id = None									# Track the current animation by ID
		self.animation_thread = None


	def start_animation(self, animation_function, animation_id):

		# Check if the same button was pressed again to stop the current animation
		if self.current_animation_id == animation_id:
			self.stop_animation()
			self.animationStateChanged.emit(animation_id, False)
			self.current_animation_id = None
			return

		# Stop any currently running animation before starting a new one
		if self.animation_thread is not None:
			self.stop_animation()

			# Emit signal to update the state of the previously active button to "off"
			if self.current_animation_id is not None:
				self.animationStateChanged.emit(self.current_animation_id, False)

		# Start the new animation
		self.current_animation_id = animation_id
		self.animation_thread = threading.Thread(target = animation_function, args = (grid,))
		self.animation_thread.start()

		self.animationStateChanged.emit(animation_id, True)					# Emit signal to update the state of the new button to "on"


	def stop_animation(self):
		stop_animation()
		if self.animation_thread is not None:
			self.animation_thread.join()
			self.animation_thread = None


	@Slot(int)
	def handleButtonPress(self, buttonId):
		if buttonId == 1:
			self.start_animation(left_turn_signal, 1)
		elif buttonId == 2:
			self.start_animation(front_parking_lights, 2)
		elif buttonId == 3:
			self.start_animation(right_turn_signal, 3)
		elif buttonId == 4:
			self.start_animation(sequential_brake_lights, 4)
		elif buttonId == 5:
			self.start_animation(rear_parking_lights, 5)
		elif buttonId == 6:
			self.start_animation(third_brake_light, 6)


	@Slot(int, result=bool)
	def isAnimationOn(self, animationId):
		return self.current_animation_id == animationId


if __name__ == "__main__":
	app = QGuiApplication(sys.argv)
	engine = QQmlApplicationEngine()

	controlPanel = ControlPanel()
	engine.rootContext().setContextProperty("controlPanel", controlPanel)

	qml_file = Path(__file__).resolve().parent / "main.qml"
	engine.load(qml_file)

	if not engine.rootObjects():
		sys.exit(-1)

	sys.exit(app.exec())
