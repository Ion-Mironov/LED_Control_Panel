import QtQuick
import QtQuick.Controls
import QtQuick.Layouts


ApplicationWindow {
	title: "LED Control Panel"
	visibility: Window.Maximized
	width: 1920
	height: 1080

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


		// ============================================================================================================== //
		Image {
			id: leftSignal
			source: 'images/left_' + leftSignal.buttonState + '.svg'
			property string buttonState: "off"
			Layout.fillWidth: true
			Layout.fillHeight: true
			fillMode: Image.PreserveAspectFit

			states: [
				State { name: 'off' },
				State { name: 'on' }
			]

			MouseArea {
				anchors.fill: parent
				onClicked: leftSignal.buttonState = (leftSignal.buttonState === 'on') ? 'off' : 'on';
			}
		}


		// ========================================================================================== //
		Image {
			id: brakeLights
			source: 'images/brake_' + brakeLights.buttonState + '.svg'
			property string buttonState: "off"
			Layout.fillWidth: true
			Layout.fillHeight: true
			fillMode: Image.PreserveAspectFit

			states: [
				State { name: 'off' },
				State { name: 'on' }
			]

			MouseArea {
				anchors.fill: parent
				onClicked: brakeLights.buttonState = (brakeLights.buttonState === 'on') ? 'off' : 'on';
			}
		}


		// ========================================================================================== //
		Image {
			id: rightSignal
			source: 'images/right_' + rightSignal.buttonState + '.svg'
			property string buttonState: "off"
			Layout.fillWidth: true
			Layout.fillHeight: true
			fillMode: Image.PreserveAspectFit

			states: [
				State { name: 'off' },
				State { name: 'on' }
			]

			MouseArea {
				anchors.fill: parent
				onClicked: rightSignal.buttonState = (rightSignal.buttonState === 'on') ? 'off' : 'on';
			}
		}


		// ========================================================================================== //
		Image {
			id: extra1
			source: "images/extra.svg"
			Layout.fillWidth: true
			Layout.fillHeight: true
			fillMode: Image.PreserveAspectFit
		}


		// ========================================================================================== //
		Image {
			id: parkingLights
			source: 'images/parking_' + parkingLights.buttonState + '.svg'
			property string buttonState: "off"
			Layout.fillWidth: true
			Layout.fillHeight: true
			fillMode: Image.PreserveAspectFit

			states: [
				State { name: 'off' },
				State { name: 'on' }
			]

			MouseArea {
				anchors.fill: parent
				onClicked: parkingLights.buttonState = (parkingLights.buttonState === 'on') ? 'off' : 'on';
			}
		}


		// ========================================================================================== //
		Image {
			id: extra2
			source: "images/extra.svg"
			Layout.fillWidth: true
			Layout.fillHeight: true
			fillMode: Image.PreserveAspectFit
		}
	}
}
