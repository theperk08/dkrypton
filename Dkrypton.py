#!/usr/bin/env python3

import sys

from dkrypton.view import DkryptonUi
from dkrypton.controller import DkryptonCtrl
from dkrypton.model import Models

from PyQt6.QtWidgets import QApplication

__version__ = "1.2"
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


    
