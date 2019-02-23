'''This is the GUI for the Self-Balancing Robot Settings Page.
This code is intended to collect measurements and mass of the parts of a two-wheeled
inverted pendulum robot. The user can select Imperial or Metric unit types, and then the
data is collected and output to a JSON file.

Amanda Voegtlin, 2019
Portland State University'''

from PyQt5.QtWidgets import * # QApplication, QWidget, QLineEdit, QLabel, QCheckBox, QRadioButton, QPushButton, QVBoxLayout
        # QVBoxLayout stacks widgets vertically
from PyQt5.QtCore import *
from PyQt5.QtGui import *

import sys

# This subclass will set our main window up
class MainWindow(QMainWindow):

    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs) # set up our object

        self.setWindowTitle("Robot Configuration")

        label = QLabel("Some label")
        label.setAlignment(Qt.AlignCenter)
        layout = QVBoxLayout()  # This is where we put all our widgets, which will go in the window
        # define validator for number inputs
        dbl_valid = QDoubleValidator(0.0000, 99999.9999, 4)

        # Start adding widgets to our layout!
        # Unit choice
        layout.addWidget(QRadioButton('Metric Units'))
        layout.addWidget(QRadioButton('Imperial Units'))
        # Axle width
        self.axle = QLineEdit()
        self.axle.setPlaceholderText('Axle Width')
        self.axle.setValidator(dbl_valid)
        layout.addWidget(self.axle)
        # Wheel radius
        self.wheel_rad = QLineEdit()
        self.wheel_rad.setPlaceholderText('Wheel Radius')
        self.wheel_rad.setValidator(dbl_valid)
        layout.addWidget(self.wheel_rad)
        # Height, axle-to-top
        self.height = QLineEdit()
        self.height.setPlaceholderText('Height (Axle-to-top)')
        self.height.setValidator(dbl_valid)
        layout.addWidget(self.height)
        # Mass of entire robot
        self.mass = QLineEdit()
        self.mass.setPlaceholderText('Mass (entire robot, assembled)')
        self.mass.setValidator(dbl_valid)
        layout.addWidget(self.mass)
        # Wheel Mass
        self.wheel_mass = QLineEdit()
        self.wheel_mass.setPlaceholderText('Wheel Mass (each)')
        self.wheel_mass.setValidator(dbl_valid)
        layout.addWidget(self.wheel_mass)
        # Load Mass
        self.load_mass = QLineEdit()
        self.load_mass.setPlaceholderText('Mass of Load (only)')
        self.load_mass.setValidator(dbl_valid)
        layout.addWidget(self.load_mass)
        # Body Mass (no load, no wheels)
        self.body_mass = QLineEdit()
        self.body_mass.setPlaceholderText('Body Mass (no load, no wheels)')
        self.body_mass.setValidator(dbl_valid)
        layout.addWidget(self.body_mass)
        # Confirm Button
        confirm_button = QPushButton('Confirm')
        confirm_button.pressed.connect(self.ConfirmButtonFunc)
        layout.addWidget(confirm_button)
        # Cancel Button
        cancel_button = QPushButton('Cancel')
        cancel_button.pressed.connect(self.CancelButtonFunc)
        layout.addWidget(cancel_button)

        # layout.addWidget(QSlider())
        # Initialize all of the above as a single Widget
        widget = QWidget()
        widget.setLayout(layout)  # this executes the layout we defined earlier
        # Create widget, set location and size of window that appears
        self.setCentralWidget(widget)
        self.setGeometry(40, 80, 500, 380) # offset, offset, size, size

    # TO DO: implement button function
    # class CancelButton(Qbutton):
    #
    #     def keyPressEvent(self, e):
    #         # when you click 'Cancel'
    #         super(CancelButton, self).keyPressEvent(e)

    def ConfirmButtonFunc(self):
        print("I'm a button!")
        print("Axle width: " + self.axle.text())
        print("Wheel radius: " + self.wheel_rad.text())
        print("Height: " + self.height.text())
        print("Mass of entire robot: " + self.mass.text())
        print("Wheel Mass (each); " + self.wheel_mass.text())
        print("Load mass: " + self.load_mass.text())
        print("Body mass: " + self.body_mass.text())

    def CancelButtonFunc(self):
        print("You're CANCELED")

    def file_save(self):
        name = QtGui.QFileDialog.getSaveFileName(self, 'Save File')
        file = open(name,'w')
        text = self.textEdit.toPlainText()
        file.write(text)
        file.close()


app = QApplication(sys.argv) #every app must have at least one instance of this
window = MainWindow() # this is our container!

# Always end with calls to show() and to exec_()
window.show() # make the window appear
app.exec_() # tells the program to run until the user closes it
# end program
