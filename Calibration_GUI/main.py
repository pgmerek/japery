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

        # Start adding widgets to our layout!
        # Unit choice
        layout.addWidget(QRadioButton('Metric Units'))
        layout.addWidget(QRadioButton('Imperial Units'))
        # Axle width
        axle = QLineEdit()
        axle.setPlaceholderText('Axle Width')
        layout.addWidget(axle)
        # Wheel radius
        wheel_rad = QLineEdit()
        wheel_rad.setPlaceholderText('Wheel Radius')
        layout.addWidget(wheel_rad)
        # Height, axle-to-top
        height = QLineEdit()
        height.setPlaceholderText('Height (Axle-to-top)')
        layout.addWidget(height)
        # Mass of entire robot
        mass = QLineEdit()
        mass.setPlaceholderText('Mass (entire robot, assembled)')
        layout.addWidget(mass)
        # Wheel Mass
        wheel_mass = QLineEdit()
        wheel_mass.setPlaceholderText('Wheel Mass (each)')
        layout.addWidget(wheel_mass)
        # Load Mass
        load_mass = QLineEdit()
        load_mass.setPlaceholderText('Mass of Load (only)')
        layout.addWidget(load_mass)
        # Body Mass (no load, no wheels)
        body_mass = QLineEdit()
        body_mass.setPlaceholderText('Body Mass (no load, no wheels)')
        layout.addWidget(body_mass)
        # Confirm and Cancel buttons
        layout.addWidget(QPushButton('Confirm'))
        layout.addWidget(QPushButton('Cancel'))
        layout.addWidget(QSlider())
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

# class ConfirmButton(Qbutton):
# # This button should interpret all of the numbers and verify that all fields were filled in
# # If all fields not filled in, then the process cancels
# # If all fields are filled in with acceptable data types, pass the numbers and the
# # choice of units along to a JSON file in the form of a dict
#     def keyPRessEvent(self, e):
#     # when you click "Confirm"
#         super(ConfirmButton, self).keyPressEvent(e)

app = QApplication(sys.argv) #every app must have at least one instance of this
window = MainWindow() # this is our container!

# Always end with calls to show() and to exec_()
window.show() # make the window appear
app.exec_() # tells the program to run until the user closes it
# end program
