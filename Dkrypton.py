#!/usr/bin/env python3

import sys

from dkrypton.view8 import DkryptonUi
from dkrypton.controller8 import DkryptonCtrl
from dkrypton.model8 import Models

from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QApplication

__version__ = "1.1"
__author__ = "Manuel Musy"

def main():
    """
    Départ du programme principal
    """
    
    dkrypt = QApplication(sys.argv)
    view = DkryptonUi()   # Appel du GUI
    view.show()         # Affichage du GUI
    model = Models          # Creation instance du model
    DkryptonCtrl(model=model, view=view)  # Creation instance du controller
    sys.exit(dkrypt.exec())    # Execution de l'application en boucle
    
if __name__ == "__main__":
    main()


    
