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


		// ======================================================================================================= //
		Image {
			id: leftSignal
			source: 'images/left_' + leftSignal.buttonState + '.svg'
			Layout.fillWidth: true
			Layout.fillHeight: true
			fillMode: Image.PreserveAspectFit

			property string buttonState: "off"

			states: [
				State { name: 'off' },
				State { name: 'on' }
			]

			MouseArea {
				anchors.fill: parent

				onClicked: {
					rightSignal.buttonState = 'off';					// These additional handlers will set the other buttons to Off when this button is pressed
					brakeLights.buttonState = 'off';
					parkingLights.buttonState = 'off';

					leftSignal.buttonState = (leftSignal.buttonState === 'on') ? 'off' : 'on';
				}
			}
		}


		// ======================================================================================================= //
		Image {
			id: brakeLights
			source: 'images/brake_' + brakeLights.buttonState + '.svg'
			Layout.fillWidth: true
			Layout.fillHeight: true
			fillMode: Image.PreserveAspectFit

			property string buttonState: "off"

			states: [
				State { name: 'off' },
				State { name: 'on' }
			]

			MouseArea {
				anchors.fill: parent
				onClicked: {
					leftSignal.buttonState = 'off';
					rightSignal.buttonState = 'off';
					parkingLights.buttonState = 'off';

					brakeLights.buttonState = (brakeLights.buttonState === 'on') ? 'off' : 'on';
				}
			}
		}


		// ======================================================================================================= //
		Image {
			id: rightSignal
			source: 'images/right_' + rightSignal.buttonState + '.svg'
			Layout.fillWidth: true
			Layout.fillHeight: true
			fillMode: Image.PreserveAspectFit

			property string buttonState: "off"

			states: [
				State { name: 'off' },
				State { name: 'on' }
			]

			MouseArea {
				anchors.fill: parent
				onClicked: {
					leftSignal.buttonState = 'off';
					brakeLights.buttonState = 'off';
					parkingLights.buttonState = 'off';

					rightSignal.buttonState = (rightSignal.buttonState === 'on') ? 'off' : 'on';
				}
			}
		}


		// ======================================================================================================= //
		Image {
			id: extra1
			source: "images/extra.svg"
			Layout.fillWidth: true
			Layout.fillHeight: true
			fillMode: Image.PreserveAspectFit
		}


		// ======================================================================================================= //
		Image {
			id: parkingLights
			source: 'images/parking_' + parkingLights.buttonState + '.svg'
			Layout.fillWidth: true
			Layout.fillHeight: true
			fillMode: Image.PreserveAspectFit

			property string buttonState: "off"

			states: [
				State { name: 'off' },
				State { name: 'on' }
			]

			MouseArea {
				anchors.fill: parent
				onClicked: {
					leftSignal.buttonState = 'off';
					brakeLights.buttonState = 'off';
					rightSignal.buttonState = 'off';

					parkingLights.buttonState = (parkingLights.buttonState === 'on') ? 'off' : 'on';
				}
			}
		}


		// ======================================================================================================= //
		Image {
			id: extra2
			source: "images/extra.svg"
			Layout.fillWidth: true
			Layout.fillHeight: true
			fillMode: Image.PreserveAspectFit
		}
	}
}
