import QtQuick
import QtQuick.Controls
import QtQuick.Layouts


ApplicationWindow {
	title: "LED Control Panel"
	visibility: Window.Maximized
	width: 1920
	height: 1080

	Image {
		source: "assets/background.svg"
		anchors.fill: parent
	}

	GridLayout {
		columns: 3
		rows: 2
		rowSpacing: 15
		columnSpacing: 15
		anchors.fill: parent
		anchors.margins: 15

		Image {
			source: "assets/left_on.svg"
			Layout.fillHeight: true
			Layout.fillWidth: true
			fillMode: Image.PreserveAspectFit
		}

		Image {
			source: "assets/brake_on.svg"
			Layout.fillWidth: true
			Layout.fillHeight: true
			fillMode: Image.PreserveAspectFit
		}

		Image {
			source: "assets/right_on.svg"
			Layout.fillWidth: true
			Layout.fillHeight: true
			fillMode: Image.PreserveAspectFit
		}

		Image {
			source: "assets/extra.svg"
			Layout.fillWidth: true
			Layout.fillHeight: true
			fillMode: Image.PreserveAspectFit
		}

		Image {
			source: "assets/parking_on.svg"
			Layout.fillWidth: true
			Layout.fillHeight: true
			fillMode: Image.PreserveAspectFit
		}

		Image {
			source: "assets/extra.svg"
			Layout.fillWidth: true
			Layout.fillHeight: true
			fillMode: Image.PreserveAspectFit
		}
	}
}
