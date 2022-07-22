import sys
from threading import main_thread

from additional_string import process_code

from PySide6.QtCore import Slot
from PyQt5.QtWidgets import *
from PySide6.QtGui import *
import os

def create_app():
    app = QApplication(sys.argv)
    windo = QWidget()
    windo.setWindowTitle('Torah Code Finder')

    main_layout = QGridLayout()

    # This block sets up the two buttons for clear and running


    # This button adds a label for the rules
    rules = QLabel("Please select your text to apply codes to on the left.\n\
Then input your skip codes below. Seperate each number by a comma (i.e 1,3,5).\n\
The section below will output your processed skip code.")

    sequence_loc = QLineEdit('Insert Code Here')

    processed = QTextEdit()

    # This is the functionality of the Test Code button
    @Slot()
    def use_process_code():

        code = process_code(sequence_loc.text(), get_text())
        processed.setText(code)


    # This is the functionality of the Clear button
    @Slot() 
    def clear_fields():
        sequence_loc.clear()
        sequence_loc.setText('Insert Code Here')
        processed.clear()

    # This is for the radio button to obtain the text to apply the code to
    def get_text():
        if chumash.isChecked():
            return os.path.join('processed_text', 'Chumash', 'All.txt')
        elif genesis.isChecked():
            return os.path.join('processed_text', 'Chumash', 'Genesis.txt')
        elif exodus.isChecked():
            return os.path.join('processed_text', 'Chumash', 'Exodus.txt')
        elif leviticus.isChecked():
            return os.path.join('processed_text', 'Chumash', 'Leviticus.txt')
        elif numbers.isChecked():
            return os.path.join('processed_text', 'Chumash', 'Numbers.txt')
        elif deuteronomy.isChecked():
            return os.path.join('processed_text', 'Chumash', 'Deuteronomy.txt')
        elif esther.isChecked():
            return os.path.join('processed_text', 'Megillah', 'Esther.txt')
        elif shir.isChecked():
            return os.path.join('processed_text', 'Megillah', 'Shir_Hashirim.txt')



    button_layout = QGridLayout()
    run = QPushButton('Test Code')
    run.clicked.connect(use_process_code)
    clear = QPushButton('Clear')
    clear.clicked.connect(clear_fields)
    button_layout.addWidget(run, 0, 0)
    button_layout.addWidget(clear, 1, 0)

    radio_layout = QGridLayout()
    chumash = QRadioButton('חומש')
    chumash.setChecked(True)
    genesis = QRadioButton('בראשית')
    exodus = QRadioButton('שמות')
    leviticus = QRadioButton('ויקרא')
    numbers = QRadioButton('במדבר')
    deuteronomy = QRadioButton('דברים')
    esther = QRadioButton('אסתר')
    shir = QRadioButton('שיר השירים')
    radio_layout.addWidget(chumash, 0, 0)
    radio_layout.addWidget(genesis, 1, 0)
    radio_layout.addWidget(exodus, 2, 0)
    radio_layout.addWidget(leviticus, 3, 0)
    radio_layout.addWidget(numbers, 0, 1)
    radio_layout.addWidget(deuteronomy, 1, 1)
    radio_layout.addWidget(esther, 2, 1)
    radio_layout.addWidget(shir, 3, 1)

    main_layout.addLayout(radio_layout, 0, 1)
    main_layout.addWidget(rules, 0, 0)
    main_layout.addLayout(button_layout, 1, 1)
    main_layout.addWidget(sequence_loc, 1, 0)
    main_layout.addWidget(processed, 2, 0,)

    windo.setLayout(main_layout)
    windo.show()
    app.exec()
