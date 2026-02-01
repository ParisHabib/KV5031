from PySide6.QtWidgets import QInputDialog, QApplication, QListView, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QListWidget, QMessageBox, QLineEdit, QPushButton
from licensee import Licensee

#Main Application Widget
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("RHU") #Setting window title
        self.resize(400, 300) #Setting window size

        self.list_widget = QListWidget() #Create QListView
        #self.name_input = QLineEdit()
        self.add_button = QPushButton("Add")
        self.delete_button = QPushButton("Delete")

        self.add_button.clicked.connect(self.add_licensee)
        self.list_widget.itemClicked.connect(self.on_item_clicked)
        self.delete_button.clicked.connect(self.delete_licensee)

        input_layout = QHBoxLayout()
        #input_layout.addWidget(self.name_input)
        input_layout.addWidget(self.add_button)
        input_layout.addWidget(self.delete_button)

        #Layout setup
        layout = QVBoxLayout() #Create vertical layout
        layout.addLayout(input_layout)
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

    def add_licensee(self):
        value, ok = QInputDialog.getText(
            self,
            "Add Licensee",
            "Enter name"
        )
        if ok and value != "":
            self.licensees.append(Licensee(value))
            self.list_widget.addItems([value])

    def delete_licensee(self):
        hitItems = self.list_widget.selectedItems()
        if hitItems is not None and len(hitItems) > 0:
            row = self.list_widget.row(hitItems[0])
            self.list_widget.takeItem(row)
            self.licensees.pop(row)
        else:
            QMessageBox.information(
                self,
                "Delete",
                "Select licensee"
            )

    
    def on_item_clicked(self, item) -> None:
        QMessageBox.information(self, "Selected", item.text())