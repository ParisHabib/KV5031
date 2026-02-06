from PySide6.QtWidgets import QToolBar, QStatusBar, QMenuBar, QTextEdit, QInputDialog, QApplication, QListView, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QListWidget, QMessageBox, QLineEdit, QPushButton
from PySide6.QtGui import QAction
from licensee import Licensee, Officer, Rehabilitation_Housing_Unit

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
        RHU_menu = menubar.addMenu("RHU")
        menubar.setNativeMenuBar(False) #found this on a forum because im on mac and menubar was appearing at the top and was confusing me

        add_action = QAction("Add", self) #add actions to file menu
        add_action.triggered.connect(self.add_licensee)
        licensees_menu.addAction(add_action)

        delete_action = QAction("Delete", self)
        delete_action.triggered.connect(self.delete_licensee)
        licensees_menu.addAction(delete_action)

        add_RHU_action = QAction("Add RHU", self)
        add_RHU_action.triggered.connect(self.add_RHU)
        RHU_menu.addAction(add_RHU_action)

        delete_RHU_action = QAction("Delete RHU", self)
        delete_RHU_action.triggered.connect(self.delete_RHU)
        RHU_menu.addAction(delete_RHU_action)

        exit_action = QAction("Exit", self)
        exit_action.triggered.connect(self.close)
        file_menu.addAction(exit_action)

        self.list_widget = QListWidget() #Create QListView
        self.RHU_list_widget = QListWidget()
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
        layout.addWidget(self.RHU_list_widget)
        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

        self.licensees = [
            Licensee("Test 1", "no notes", "no address", "male", "1st January", "1st february", "Strangeways", "001"),
            Licensee("Test 2", "anger issues", "12 Albert Place", "female", "2nd January", "2nd February", "Strangeways", "002"),
            Licensee("Test 3", "no notes", "37 Northumberland Street", "male", "3rd January", "3rd February", "Forest Bank", "003")
        ]

        for lic in self.licensees: #puts data into UI list
            self.list_widget.addItem(lic.get_name())

        self.RHU = [
            Rehabilitation_Housing_Unit("Unit 1", "no notes", "12 test street"),
            Rehabilitation_Housing_Unit("Unit 2", "no males", "13 test street"),
            Rehabilitation_Housing_Unit("Unit 3", "no notes", "14 test street")
        ]

        for unit in self.RHU:
            self.RHU_list_widget.addItem(unit.get_RHU_name())

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
                notes, ok3 = QInputDialog.getText(
                    self,
                    "Add Licensee",
                    "Enter notes"
                )
                if ok3:
                    home_address, ok4 = QInputDialog.getText(
                        self, 
                        "Add Licensee",
                        "Enter home address"
                    )
                    if ok4:
                        prisoner_gender, ok5 = QInputDialog.getText(
                            self,
                            "Add Licensee",
                            "Enter gender"
                        )
                        if ok5:
                            release_date, ok6 = QInputDialog.getText(
                                self,
                                "Add Licensee",
                                "Enter release date"
                            )
                            if ok6:
                                end_of_license, ok7 = QInputDialog.getText(
                                    self,
                                    "Add Licensee",
                                    "Enter end of license date"
                                )
                                if ok7:
                                    current_prison, ok8 = QInputDialog.getText(
                                        self,
                                        "Add Licensee",
                                        "Enter current prison"
                                    )
                                    if ok8:
                                        licensee_select = Licensee(
                                            name,
                                            notes,
                                            home_address,
                                            prisoner_gender,
                                            release_date,
                                            end_of_license,
                                            current_prison,
                                            personal_id
                                        )
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
                                        
                                        reply2 = QMessageBox.question(
                                            self,
                                            "Drug Search",
                                            "Does he/she require a drug search?",
                                            QMessageBox.StandardButton.Yes |
                                            QMessageBox.StandardButton.No
                                        )
                                        if reply2 == QMessageBox.StandardButton.Yes:
                                            licensee_select.set_needed_drug_search(True)
                                        else:
                                            licensee_select.set_needed_drug_search(False)
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

    def add_RHU(self):
        name, ok = QInputDialog.getText(self, 
                                        "Add RHU", 
                                        "Enter RHU name")
        if ok and name != "":
            notes, ok2 = QInputDialog.getText(self,
                                              "Add RHU",
                                              "Enter notes")
            if ok2:
                address, ok3 = QInputDialog.getText(self,
                                                    "Add RHU",
                                                    "Enter address")
                if ok3 and address != "":
                    unit = Rehabilitation_Housing_Unit(name,
                                                       notes,
                                                       address)
                    reply = QMessageBox.question(
                        self,
                        "Safe Distance from School",
                        "Is this unit within 5 miles of a school?",
                        QMessageBox.StandardButton.Yes |
                        QMessageBox.StandardButton.No
                    )
                    if reply == QMessageBox.StandardButton.Yes:
                        unit.set_within_school_distance(True)
                    else:
                        unit.set_within_school_distance(False)
                    self.RHU.append(unit)
                    self.RHU_list_widget.addItem(unit.get_RHU_name())

    def delete_RHU(self):
        hitItems = self.RHU_list_widget.selectedItems()
        if hitItems is not None and len(hitItems) > 0:
            row = self.RHU_list_widget.row(hitItems[0])
            self.RHU_list_widget.takeItem(row)
            self.RHU.pop(row)
        else:
            QMessageBox.information(self, "Delete RHU", "Select RHU")

    
    def on_item_double_clicked(self, item) -> None:
        row = self.list_widget.row(item)
        licensee_select = self.licensees[row]
        QMessageBox.information(self, "Selected", 
                                f"Name: {licensee_select.get_name()} \nID: {licensee_select.get_id()}, \nNotes: {licensee_select.get_notes()}, \nAddress: {licensee_select.get_home_address()} \nGender: {licensee_select.get_prisoner_gender()}, \nRelease: {licensee_select.get_release_date()}, \nEnd of License: {licensee_select.get_end_of_license()}, \nPrison: {licensee_select.get_current_prison()},  \nSex Offender: {licensee_select.get_sex_offender()} \nDrug Search Needed: {licensee_select.get_needed_drug_search()}")
