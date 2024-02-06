import QtQuick
import QtQuick.Controls
import QtQuick.Layouts


ApplicationWindow {
	width: 1920
	height: 1080
	visibility: Window.Maximized

	Image {
		source: "images/background.svg"
		anchors.fill: parent
	}

	GridLayout {
		columns: 3
		columnSpacing: 15
		rows: 2
		rowSpacing: 15
		anchors.margins: 15
		anchors.fill: parent


		// Bool properties to hold each button's state
		property bool leftSignalState: false
		property bool rightSignalState: false
		property bool brakeLightsState: false
		property bool parkingLightsState: false


		/* ----- Left Turn Signal -------------------------------------------------------------- */
		// Function to toggle the LED animation on and off
		function toggleLeftSignal() {

			// Stop all other animations
    		controlPanel.rightSignalOff();
			controlPanel.brakeLightsOff();
			controlPanel.parkingLightsOff();

			leftSignalState ? controlPanel.leftSignalOn() : controlPanel.leftSignalOff();
			leftSignalState = !leftSignalState;
		}


		/* ----- Brake Lights ------------------------------------------------------------------ */
		function toggleBrakeLights() {
			controlPanel.leftSignalOff();
			controlPanel.rightSignalOff();;
			controlPanel.parkingLightsOff();

			brakeLightsState ? controlPanel.brakeLightsOn() : controlPanel.brakeLightsOff();
			brakeLightsState = !brakeLightsState;
		}


		/* ----- Right Turn Signal ------------------------------------------------------------- */
		function toggleRightSignal() {
			controlPanel.leftSignalOff();
			controlPanel.brakeLightsOff();
			controlPanel.parkingLightsOff();

			rightSignalState ? controlPanel.rightSignalOn() : controlPanel.rightSignalOff();
			rightSignalState = !rightSignalState;
		}


		/* ----- Parking Lights ---------------------------------------------------------------- */
		function toggleParkingLights() {
			controlPanel.leftSignalOff();
			controlPanel.rightSignalOff();;
			controlPanel.brakeLightsOff();

			parkingLightsState ? controlPanel.parkingLightsOn() : controlPanel.parkingLightsOff();
			parkingLightsState = !parkingLightsState;
		}



		// Buttons

		/* ----- Left Turn Signal -------------------------------------------------------------- */
		Image {
			id: leftSignal
			source: "images/left_" + (leftSignalState ? "on" : "off") + ".svg"
			Layout.fillWidth: true
			Layout.fillHeight: true
			fillMode: Image.PreserveAspectFit

			MouseArea {
				anchors.fill: parent

				onClicked: {
					toggleLeftSignal();
				}
			}
		}


		/* ----- Brake Lights ------------------------------------------------------------------ */
		Image {
			id: brakeLights
			source: "images/brake_" + (brakeLightsState ? "on" : "off") + ".svg"
			Layout.fillWidth: true
			Layout.fillHeight: true
			fillMode: Image.PreserveAspectFit

			MouseArea {
				anchors.fill: parent
				onClicked: {
					toggleBrakeLights();
				}
			}
		}


		/* ----- Right Turn Signal ------------------------------------------------------------- */
		Image {
			id: rightSignal
			source: "images/right_" + (rightSignalState ? "on" : "off") + ".svg"
			Layout.fillWidth: true
			Layout.fillHeight: true
			fillMode: Image.PreserveAspectFit

			MouseArea {
				anchors.fill: parent
				onClicked: {
					toggleRightSignal();
				}
			}
		}


		/* ----- Extra ------------------------------------------------------------------------- */
		Image {
			id: extra1
			source: "images/extra.svg"
			Layout.fillWidth: true
			Layout.fillHeight: true
			fillMode: Image.PreserveAspectFit
		}


		/* ----- Parking Lights ---------------------------------------------------------------- */
		Image {
			id: parkingLights
			source: "images/right_" + (parkingLightsState ? "on" : "off") + ".svg"
			Layout.fillWidth: true
			Layout.fillHeight: true
			fillMode: Image.PreserveAspectFit

			MouseArea {
				anchors.fill: parent
				onClicked: {
					toggleParkingLights();
				}
			}
		}


		/* ----- Extra ------------------------------------------------------------------------- */
		Image {
			id: extra2
			source: "images/extra.svg"
			Layout.fillWidth: true
			Layout.fillHeight: true
			fillMode: Image.PreserveAspectFit
		}
	}
}
