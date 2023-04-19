#!/usr/bin/env python3

import sys

from dkrypton.view6 import DkryptonUi
from dkrypton.controller6 import DkryptonCtrl
#from dkrypton.model1 import evaluateExpression
from dkrypton.model6 import Models

from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QApplication



__version__ = "0.1"
__author__ = "Manuel Musy"

def main():
    """
    Départ du programme principal
    """
    dkrypt = QApplication(sys.argv)
    view = DkryptonUi()   # Render calculator GUI
    view.show()         # Display calculator GUI
    model = Models          # Create instance of model
    DkryptonCtrl(model=model, view=view)  # Create instance of controller
    sys.exit(dkrypt.exec())    # Execute application main loop
    
if __name__ == "__main__":
    main()

    

    
