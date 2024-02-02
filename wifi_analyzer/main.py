import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QLabel, QListWidget
from wifi_scanner import scan_networks


class WiFiAnalyzerGUI(QMainWindow):
    def __init__(self):
        super().__init__()
        self.layout = None
        self.networkListWidget = None
        self.centralWidget = None
        self.setWindowTitle("WiFi Analyzer")
        self.setGeometry(100, 100, 600, 400)  # x, y, width, height
        self.initUI()

    def initUI(self):
        self.centralWidget = QWidget()
        self.setCentralWidget(self.centralWidget)
        self.layout = QVBoxLayout()
        self.networkListWidget = QListWidget()

        self.scanNetworks()

        self.layout.addWidget(QLabel("Detected Networks:"))
        self.layout.addWidget(self.networkListWidget)
        self.centralWidget.setLayout(self.layout)

    def scanNetworks(self):
        interface = "wlan0"  # Change to your interface
        networks = scan_networks(interface)
        for network in networks:
            self.networkListWidget.addItem(network)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWindow = WiFiAnalyzerGUI()
    mainWindow.show()
    sys.exit(app.exec_())
