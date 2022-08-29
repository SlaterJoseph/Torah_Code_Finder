from PySide6.QtCore import Slot
from PyQt5.QtWidgets import *
from ..parsing.data_collection import process_nums
from .parts import create_converter


def create_letter() -> QGridLayout:
    letters = QGridLayout()

    blurb = QLabel("Please select your text to apply codes to on the left."
                   " Then input your skip codes below. Separate each number with commas (i.e. 1, 3, 5)"
                   " The section below will output your processed skip code.")
    blurb.setWordWrap(True)

    sequence_loc = QLineEdit('Insert Code Here')
    processed = QTextEdit()

    converter = create_converter('letter')

    @Slot()
    def use_code() -> None:
        if sel_chum.isChecked():
            curr_text = chumash.currentText()
        else:
            curr_text = katubim.currentText()

        print(curr_text)
        print(converter[curr_text])
        code = process_nums(sequence_loc.text(), converter[curr_text])
        processed.setText(code)

    @Slot()
    def reset() -> None:
        sequence_loc.setText('Insert Code Here')
        processed.clear()

    chumash = QComboBox()
    chumash.addItem('חומש')
    chumash.addItem('בראשית')
    chumash.addItem('שמות')
    chumash.addItem('ויקרא')
    chumash.addItem('במדבר')
    chumash.addItem('דברים')
    sel_chum = QRadioButton('חומש')
    sel_chum.setChecked(True)

    katubim = QComboBox()
    katubim.addItem('אסתר')
    katubim.addItem('שיר השירים')
    sel_kat = QRadioButton('כתובים')

    selection = QGridLayout()
    radio_layout = QGridLayout()
    radio_layout.addWidget(sel_chum, 0, 0)
    radio_layout.addWidget(sel_kat, 1, 0)
    selection.addLayout(radio_layout, 0, 0, 0, 1)
    selection.addWidget(chumash, 0, 1)
    selection.addWidget(katubim, 1, 1)

    run = QPushButton('Run')
    run.clicked.connect(use_code)

    clear = QPushButton('Reset')
    clear.clicked.connect(reset)

    button_layout = QGridLayout()
    button_layout.addWidget(run, 0, 0)
    button_layout.addWidget(clear, 1, 0)

    letters.addWidget(blurb, 0, 0)
    letters.addLayout(selection, 0, 1)
    letters.addWidget(sequence_loc, 1, 0)
    letters.addLayout(button_layout, 1, 1)
    letters.addWidget(processed, 2, 0, 1, 0)

    return letters
