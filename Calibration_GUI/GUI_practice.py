from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

import sys

# Subclass QMainWindow to customise your application's main window
class MainWindow(QMainWindow):
    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        self.setWindowTitle("My Awesome App")
        label = QLabel("THIS IS AWESOME!!!")
        # The `Qt` namespace has a lot of attributes to customise
        # widgets. See: http://doc.qt.io/qt-5/qt.html
        label.setAlignment(Qt.AlignCenter)
        # Set the central widget of the Window. Widget will expand to take up all the space
        # in the window by default.
        self.setCentralWidget(label)

# TEST CODE
        layout = QVBoxLayout()

        # define validator for number inputs
        dbl_valid = QDoubleValidator(0.0000, 99999.9999, 4)
        # wheel radius line edit box
        self.wheel_rad = QLineEdit()
        self.wheel_rad.setPlaceholderText('Wheel Radius')
        self.wheel_rad.setValidator(dbl_valid)
        layout.addWidget(self.wheel_rad)


        confirm_button = QPushButton('Confirm')
        confirm_button.pressed.connect(self.ConfirmButton)

        layout.addWidget(confirm_button)
        layout.addWidget(QPushButton('Cancel'))

        widget = QWidget()
        widget.setLayout(layout)  # this executes the layout we defined earlier
        # Create widget, set location and size of window that appears
        self.setCentralWidget(widget)
#        self.setGeometry(40, 80, 500, 380) # offset, offset, size, size
# END TEST CODE

        # Toolbar stuff - add a toolbar. Call it my_toolbar.
        my_toolbar = QToolBar("My freaking toolbar")
        my_toolbar.setIconSize(QSize(16,16))
        self.addToolBar(my_toolbar)
        '''Define a button by name, add it to the toolbar, label it.
        We have to pass in an object to be the parent of the QAction. Since we are doing this
        inside of a class, we can pass 'self' for the class itself.'''
        button_action = QAction(QIcon("./GUI_icons/16/073.png"), "Your button", self)
        # Once we have a status bar, the status tip will be visible. Define it here.
        button_action.setStatusTip("This is your button")
        # tell it that, when the toolbar button is clicked, connect this custom function
        # 'triggered' is builtin, as is 'connect.'
        button_action.triggered.connect(self.onMyToolBarButtonClick)
        my_toolbar.addAction(button_action)

        # Add a status bar. Ours is pretty canned. We can create and define it all at once.
        self.setStatusBar(QStatusBar(self))

    def ConfirmButton(self, widget_name):
        print("I'm a button!")
        print(self.wheel_rad.text())


    def onMyToolBarButtonClick(self,s):
        # all this does is print "click" and the state of the button. Since the button
        # doesn't toggle, it always prints 'false' (meaning it has returned to its
        # unpressed state)
        print("click", s)

app = QApplication(sys.argv)
window = MainWindow()

window.show()
app.exec_()