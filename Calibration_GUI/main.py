'''This is the GUI for the Self-Balancing Robot Settings Page.
This code is intended to collect measurements and Weight of the parts of a two-wheeled
inverted pendulum robot. The user can select Imperial or Metric unit types, and then the
data is collected and output to a JSON file.
Amanda Voegtlin, 2019
Portland State University'''

from PyQt5.QtWidgets import * # QApplication, QWidget, QLineEdit, QLabel, QCheckBox, QRadioButton, QPushButton, QVBoxLayout
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import json
import sys

class Weight_Menu(QComboBox): # Making this a class allows it to be duplicated
    def __init__(self, parent=None):
        QComboBox.__init__(self, parent=parent)
        self.addItem("grams")
        self.addItem("kilograms")
        self.addItem("lbs")
        self.addItem("ounces")

class Size_Menu(QComboBox): # Making this a class allows it to be duplicated
    def __init__(self, parent=None):
        QComboBox.__init__(self, parent=parent)
        self.addItem("inches")
        self.addItem("centimeters")

# This subclass will set our main window up
class MainWindow(QMainWindow):

    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs) # set up our object

        self.setWindowTitle("Robot Configuration")

        main_vertical_layout = QVBoxLayout()  # This is where we put all our widgets, which will go in the window
        main_vertical_layout.setSpacing(1) # makes it look nice
        inside_left_vert_layout = QVBoxLayout()
        inside_middle_vert_layout = QVBoxLayout()
        inside_right_vert_layout = QVBoxLayout()
        horizontal_layout = QHBoxLayout()
        horizontal_layout.setSpacing(10)
        
        # define validator for number inputs
        dbl_valid = QDoubleValidator(0.0000, 99999.9999, 4)

        # Axle width
        self.axle = QLineEdit()
        self.axle.setPlaceholderText('Axle Width')
        self.axle.setValidator(dbl_valid)
        inside_middle_vert_layout.addWidget(self.axle)
        axle_label = QLabel('Axle Width')
        inside_left_vert_layout.addWidget(axle_label)
        self.axle_dropdown = Size_Menu()
        inside_right_vert_layout.addWidget(self.axle_dropdown)

        # Wheel radius
        self.wheel_rad = QLineEdit()
        self.wheel_rad.setPlaceholderText('Wheel Radius')
        self.wheel_rad.setValidator(dbl_valid)
        inside_middle_vert_layout.addWidget(self.wheel_rad)
        wheel_rad_label = QLabel('Wheel Radius')
        inside_left_vert_layout.addWidget(wheel_rad_label)
        self.wheel_rad_dropdown = Size_Menu()
        inside_right_vert_layout.addWidget(self.wheel_rad_dropdown)

        # Height, axle-to-top
        self.height = QLineEdit()
        self.height.setPlaceholderText('Height (Axle-to-top)')
        self.height.setValidator(dbl_valid)
        inside_middle_vert_layout.addWidget(self.height)
        height_label = QLabel('Height (Axle-to-top)')
        inside_left_vert_layout.addWidget(height_label)
        self.height_dropdown = Size_Menu()
        inside_right_vert_layout.addWidget(self.height_dropdown)

        # Weight of entire robot
        self.weight = QLineEdit()
        self.weight.setPlaceholderText('Weight (entire robot, assembled)')
        self.weight.setValidator(dbl_valid)
        inside_middle_vert_layout.addWidget(self.weight)
        weight_label = QLabel('Weight (entire robot, assembled)')
        inside_left_vert_layout.addWidget(weight_label)
        self.weight_dropdown = Weight_Menu()
        inside_right_vert_layout.addWidget(self.weight_dropdown)

        # Wheel Weight
        self.wheel_weight = QLineEdit()
        self.wheel_weight.setPlaceholderText('Wheel Weight (each)')
        self.wheel_weight.setValidator(dbl_valid)
        inside_middle_vert_layout.addWidget(self.wheel_weight)
        wheel_weight_label = QLabel('Wheel Weight (each)')
        inside_left_vert_layout.addWidget(wheel_weight_label)
        self.wheel_weight_dropdown = Weight_Menu()
        inside_right_vert_layout.addWidget(self.wheel_weight_dropdown)

        # Load Weight
        self.load_weight = QLineEdit()
        self.load_weight.setPlaceholderText('Weight of Load (only)')
        self.load_weight.setValidator(dbl_valid)
        inside_middle_vert_layout.addWidget(self.load_weight)
        load_weight_label = QLabel('Weight of Load (only)')
        inside_left_vert_layout.addWidget(load_weight_label)
        self.load_weight_dropdown = Weight_Menu()
        inside_right_vert_layout.addWidget(self.load_weight_dropdown)

        # Body Weight (no load, no wheels)
        body_weight_label = QLabel('Body Weight (no load, no wheels)')
        inside_left_vert_layout.addWidget(body_weight_label)
        self.body_weight = QLineEdit()
        self.body_weight.setPlaceholderText('Body Weight (no load, no wheels)')
        self.body_weight.setValidator(dbl_valid)
        inside_middle_vert_layout.addWidget(self.body_weight)
        self.body_weight_dropdown = Weight_Menu()
        inside_right_vert_layout.addWidget(self.body_weight_dropdown)

        # now add those to the main layout here
        horizontal_layout.addLayout(inside_left_vert_layout) # add the left box contents
        horizontal_layout.addLayout(inside_middle_vert_layout) # add the middle box contents
        horizontal_layout.addLayout(inside_right_vert_layout) # add the box with the dropdowns
        main_vertical_layout.addLayout(horizontal_layout)
        # Confirm Button
        confirm_button = QPushButton('Confirm')
        confirm_button.pressed.connect(self.ConfirmButtonFunc)
        main_vertical_layout.addWidget(confirm_button)
        # Cancel Button
        cancel_button = QPushButton('Cancel')
        cancel_button.pressed.connect(self.CancelButtonFunc)
        main_vertical_layout.addWidget(cancel_button)

        # Initialize all of the above as a single Widget
        widget = QWidget()


        widget.setLayout(main_vertical_layout)  # make the vertical layout the primary container
        # Create widget, set location and size of window that appears
        self.setCentralWidget(widget)
        self.setGeometry(40, 80, 600, 380) # offset, offset, width size, height size

    def ConfirmButtonFunc(self):
        print("Saved data to output.json")
        print("Axle width: " + self.axle.text() + " " + self.axle_dropdown.currentText())
        print("Wheel radius: " + self.wheel_rad.text() + " " + self.wheel_rad_dropdown.currentText())
        print("Height: " + self.height.text() + " " + self.height_dropdown.currentText())
        print("Weight of entire robot: " + self.weight.text() + " " + self.weight_dropdown.currentText())
        print("Wheel Weight (each); " + self.wheel_weight.text() + " " + self.wheel_weight_dropdown.currentText())
        print("Load Weight: " + self.load_weight.text() + " " + self.load_weight_dropdown.currentText())
        print("Body Weight: " + self.body_weight.text() + " " + self.body_weight_dropdown.currentText())

        # DATA QUALITY CHECK CODE GOES HERE. Are all values filled in? Units? 

        axle = self.convert_length(self.axle, self.axle_dropdown)
        wheel_rad = self.convert_length(self.wheel_rad, self.wheel_rad_dropdown)
        height = self.convert_length(self.height, self.height_dropdown)
        weight = self.convert_mass(self.weight, self.weight_dropdown)
        wheel_weight = self.convert_mass(self.wheel_weight, self.wheel_weight_dropdown)
        load_weight = self.convert_mass(self.load_weight, self.load_weight_dropdown)
        body_weight = self.convert_mass(self.body_weight, self.body_weight_dropdown)
        
        raw_dict = {'axle width': axle.magnitude, 'wheel radius': wheel_rad.magnitude, 
            'height': height.magnitude, 'Robot Weight': weight.magnitude, 
            'Wheel Weight': wheel_weight.magnitude, 'Load Weight': load_weight.magnitude, 
            'Body Weight': body_weight.magnitude}
        print(raw_dict)
        file = open('output.json', 'w+') #creates output.json if it doesn't exist, opens and truncates if it does 
        json.dump(raw_dict, file)
        
    def convert_length(self, object, dropdown):
        if dropdown.currentText() == "inches":
            converted_value = float(object.text()) * self.ureg.inch
        if dropdown.currentText() == "centimeters":
            converted_value = float(object.text()) * self.ureg.cm
        converted_value.ito_base_units()
        return converted_value

    def convert_mass(self, object, dropdown):
        if dropdown.currentText() == "grams":
            converted_value = float(object.text()) * self.ureg.gram
        if dropdown.currentText() == "kilograms":
            converted_value = float(object.text()) * self.ureg.kg        
        if dropdown.currentText() == "lbs":
            converted_value = float(object.text()) * self.ureg.pound        
        if dropdown.currentText() == "ounces":
            converted_value = float(object.text()) * self.ureg.ounce
        converted_value.ito_base_units()
        return converted_value

    def CancelButtonFunc(self):
        print("You're CANCELED")
        print("(Also I'm closing the program)")
        window.close()


app = QApplication(sys.argv) #every app must have at least one instance of this
window = MainWindow() # this is our container!

# Always end with calls to show() and to exec_()
window.show() # make the window appear
app.exec_() # tells the program to run until the user closes it
# end program
