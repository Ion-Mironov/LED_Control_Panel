import QtQuick 2.15
import QtQuick.Controls
import QtQuick.Layouts
from control_panel import "*"

ApplicationWindow {
	title: "LED Control Panel"
	visible: true
	width: 400
	height: 300

	GridLayout {
		columns: 3
		anchors.fill: parent

		Button { text: "Left"; onClicked: controlPanel.runAnimation("Left") }
		Button { text: "Right"; onClicked: controlPanel.runAnimation("Right") }
		Button { text: "Brake"; onClicked: controlPanel.runAnimation("Brake") }
		Button { text: "Parking Lights"; onClicked: controlPanel.runAnimation("Parking Lights") }
		Button { text: "Extra 2"; onClicked: controlPanel.runAnimation("Extra 2") }
		Button { text: "Extra 3"; onClicked: controlPanel.runAnimation("Extra 3") }
	}

	Connections {
		target: controlPanel
		onProcessStarted: {
			console.log("Animation started: " + animationName)
		}
	}
}
