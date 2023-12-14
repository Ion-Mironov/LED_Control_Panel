import QtQuick 2.15
import QtQuick.Window 2.15


Window {
	id: mainWindow
	title: "Instrument Panel"
	visibility: Window.Maximized
	width: 1920
	height: 1080


	// Background
	Image {
		id: background
		source: "assets/background.svg"
		anchors.fill: parent
	}

	// Left Button (ON)
	Image {
		id: left_on
		source: "assets/left_on.svg"
		width: 500
		height: 500
		x: 70
		y: 20
	}

	// Extra Button
	Image {
		id: extra
		source: "assets/extra.svg"
		width: 500
		height: 500
		x: 70
		y: 560
	}
}
