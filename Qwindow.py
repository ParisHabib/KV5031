from PySide6.QtWidgets import QApplication, QListView, QMainWindow, QWidget, QVBoxLayout, QListWidget, QMessageBox
from licensee import Licensee

#Main Application Widget
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("RHU") #Setting window title
        self.resize(400, 300) #Setting window size

        self.list_widget = QListWidget() #Create QListView

        #Layout setup
        layout = QVBoxLayout() #Create vertical layout
        layout.addWidget(self.list_widget) #Add the QListView to the layout
        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

        self.licensees = [
            Licensee("Test 1"),
            Licensee("Test 2"),
            Licensee("Test 3")
        ]

        for lic in self.licensees: #puts data into UI list
            self.list_widget.addItem(lic.get_name())
        self.list_widget.itemClicked.connect(self.on_item_clicked)
    
    def on_item_clicked(self, item) -> None:
        QMessageBox.information(self, "Selected", item.text())