from PySide6.QtWidgets import QToolBar, QStatusBar, QMenuBar, QTextEdit, QInputDialog, QApplication, QListView, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QListWidget, QMessageBox, QLineEdit, QPushButton
from PySide6.QtGui import QAction
from licensee import Licensee

#Main Application Widget
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("RHU") #Setting window title
        self.resize(400, 300) #Setting window size

        self.setStatusBar(QStatusBar(self)) #create status bar
        self.statusBar().showMessage("Ready")
        menubar = self.menuBar() #create menus bar and add a file menu and licensee menu
        file_menu = menubar.addMenu("File")
        licensees_menu = menubar.addMenu("Licensees")
        menubar.setNativeMenuBar(False) #found this on a forum because im on mac and menubar was appearing at the top and was confusing me

        add_action = QAction("Add", self) #add actions to file menu
        add_action.triggered.connect(self.add_licensee)
        licensees_menu.addAction(add_action)

        delete_action = QAction("Delete", self)
        delete_action.triggered.connect(self.delete_licensee)
        licensees_menu.addAction(delete_action)

        exit_action = QAction("Exit", self)
        exit_action.triggered.connect(self.close)
        file_menu.addAction(exit_action)

        self.list_widget = QListWidget() #Create QListView
        #self.name_input = QLineEdit()
        self.add_button = QPushButton("Add")
        self.delete_button = QPushButton("Delete")

        self.add_button.clicked.connect(self.add_licensee)
        self.list_widget.itemDoubleClicked.connect(self.on_item_double_clicked)
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
            Licensee("Test 1", "001"),
            Licensee("Test 2", "002"),
            Licensee("Test 3", "003")
        ]

        for lic in self.licensees: #puts data into UI list
            self.list_widget.addItem(lic.get_name())

    def add_licensee(self):
        name, ok = QInputDialog.getText(
            self,
            "Add Licensee",
            "Enter name"
        )
        if ok and name != "":
            personal_id, ok2 = QInputDialog.getText(
                self,
                "Add Licensee",
                "Enter ID"
            )
            if ok2 and personal_id != "":
                licensee_select = Licensee(name, personal_id)
                reply = QMessageBox.question(
                    self,
                    "Sex Offender",
                    "Is he/she a sex offender?",
                    QMessageBox.StandardButton.Yes |
                    QMessageBox.StandardButton.No
                )
                if reply == QMessageBox.StandardButton.Yes:
                    licensee_select.set_sex_offender(True)
                else:
                    licensee_select.set_sex_offender(False)
                self.licensees.append(licensee_select)
                self.list_widget.addItem(licensee_select.get_name())
                
        

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

    
    def on_item_double_clicked(self, item) -> None:
        row = self.list_widget.row(item)
        licensee_select = self.licensees[row]
        QMessageBox.information(self, "Selected", 
                                f"Name: {licensee_select.get_name()} \nID: {licensee_select.get_id()} \nSex Offender: {licensee_select.get_sex_offender()}")
