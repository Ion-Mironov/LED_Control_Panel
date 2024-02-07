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

	property bool leftSignalState: false
	property bool rightSignalState: false
	property bool thirdBrakeLightState: false
	property bool rearParkingLightsState: false


	/* ----- Left Turn Signal ---------------------------------------------------------------------------- */
	function toggleLeftSignal() {
		controlPanel.rightSignalOff();
		controlPanel.thirdBrakeLightOff();
		controlPanel.rearParkingLightsOff();

		leftSignalState ? controlPanel.leftSignalOff() : controlPanel.leftSignalOn();
		leftSignalState = !leftSignalState;
	}


	/* ----- Third Brake Light --------------------------------------------------------------------------- */
	function toggleThirdBrakeLight() {
		controlPanel.leftSignalOff();
		controlPanel.rightSignalOff();
		controlPanel.rearParkingLightsOff();

		thirdBrakeLightState ? controlPanel.thirdBrakeLightOff() : controlPanel.thirdBrakeLightOn();
		thirdBrakeLightState = !thirdBrakeLightState;
	}


	/* ----- Right Turn Signal --------------------------------------------------------------------------- */
	function toggleRightSignal() {
		controlPanel.leftSignalOff();
		controlPanel.thirdBrakeLightOff();
		controlPanel.rearParkingLightsOff();

		rightSignalState ? controlPanel.rightSignalOff() : controlPanel.rightSignalOn();
		rightSignalState = !rightSignalState;
	}


	/* ----- Rear Parking Lights ------------------------------------------------------------------------- */
	function toggleRearParkingLights() {
		controlPanel.leftSignalOff();
		controlPanel.rightSignalOff();
		controlPanel.thirdBrakeLightOff();

		rearParkingLightsState ? controlPanel.rearParkingLightsOff() : controlPanel.rearParkingLightsOn();
		rearParkingLightsState = !rearParkingLightsState;
	}


	// ===== Grid layout of buttons ====================================================================== //
	GridLayout {
		columns: 3
		columnSpacing: 15
		rows: 2
		rowSpacing: 15
		anchors.margins: 15
		anchors.fill: parent


		/* ----- Left Turn Signal ------------------------------------------------------------------------ */
		Image {
			id: leftSignal
			Layout.column: 0
			Layout.row: 0
			Layout.fillWidth: true
			Layout.fillHeight: true
			source: "images/left_" + (leftSignalState ? "on" : "off") + ".svg"
			fillMode: Image.PreserveAspectFit

			MouseArea {
				anchors.fill: parent

				onClicked: {
					toggleLeftSignal();
				}
			}
		}


		/* ----- Brake Lights ---------------------------------------------------------------------------- */
		Image {
			id: thirdbrakeLight
			Layout.column: 1
			Layout.row: 0
			Layout.fillWidth: true
			Layout.fillHeight: true
			source: "images/brake_" + (thirdBrakeLightState ? "on" : "off") + ".svg"
			fillMode: Image.PreserveAspectFit

			MouseArea {
				anchors.fill: parent
				onClicked: {
					toggleThirdBrakeLight();
				}
			}
		}


		/* ----- Right Turn Signal ----------------------------------------------------------------------- */
		Image {
			id: rightSignal
			Layout.column: 2
			Layout.row: 0
			Layout.fillWidth: true
			Layout.fillHeight: true
			source: "images/right_" + (rightSignalState ? "on" : "off") + ".svg"
			fillMode: Image.PreserveAspectFit

			MouseArea {
				anchors.fill: parent
				onClicked: {
					toggleRightSignal();
				}
			}
		}


		/* ----- Extra 1 --------------------------------------------------------------------------------- */
		Image {
			id: extra1
			Layout.column: 0
			Layout.row: 1
			Layout.fillWidth: true
			Layout.fillHeight: true
			source: "images/extra.svg"
			fillMode: Image.PreserveAspectFit
		}


		/* ----- Parking Lights -------------------------------------------------------------------------- */
		Image {
			id: rearParkingLights
			Layout.column: 1
			Layout.row: 1
			Layout.fillWidth: true
			Layout.fillHeight: true
			source: "images/parking_" + (rearParkingLightsState ? "on" : "off") + ".svg"
			fillMode: Image.PreserveAspectFit

			MouseArea {
				anchors.fill: parent
				onClicked: {
					toggleRearParkingLights();
				}
			}
		}


		/* ----- Extra 2 --------------------------------------------------------------------------------- */
		Image {
			id: extra2
			Layout.column: 2
			Layout.row: 1
			Layout.fillWidth: true
			Layout.fillHeight: true
			source: "images/extra.svg"
			fillMode: Image.PreserveAspectFit
		}
	}
}
