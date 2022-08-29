from PySide6.QtCore import Slot
from PyQt5.QtWidgets import *
from ..parsing.data_collection import find_words
from .parts import create_converter


def create_words() -> QGridLayout:
    words = QGridLayout()

    blurb = QLabel("Below are a few fields. First input the location of the word"
                   " you are searching for, then the number of additional words."
                   " So the first field would have 57 for the 57th word, and the"
                   " second field you put the amount of following letters you want."
                   " So if you put 57 and 3, you will get the 57th, 58th, 59th and"
                   " 60th words.")
    blurb.setWordWrap(True)

    word_loc = QLineEdit("Insert word location here")
    add_words = QLineEdit("Insert number of additional words here")
    input_space = QGridLayout()
    input_space.addWidget(word_loc, 0, 0)
    input_space.addWidget(add_words, 0, 1)

    words_found = QTextEdit()

    converter = create_converter('words')

    @Slot()
    def use_input() -> None:
        if sel_chum.isChecked():
            curr_text = chumash.currentText()
        else:
            curr_text = katubim.currentText()

        try:
             loc = int(word_loc.text())
        except ValueError:
            words_found.setText('Location number must be greater then or equal to 1')
        else:
            code = find_words(converter[curr_text], loc, int(add_words.text()))
            words_found.setText(code)

    @Slot()
    def reset() -> None:
        word_loc.setText("Insert word location here")
        add_words.setText("Insert number of additional words here")
        words_found.clear()

    chumash = QComboBox()
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
    run.clicked.connect(use_input)

    clear = QPushButton('Reset')
    clear.clicked.connect(reset)

    button_layout = QGridLayout()
    button_layout.addWidget(run, 0, 0)
    button_layout.addWidget(clear, 1, 0)

    words.addWidget(blurb, 0, 0)
    words.addLayout(selection, 0, 1)
    words.addLayout(input_space, 1, 0, 1, 2)
    words.addLayout(button_layout, 2, 1)
    words.addWidget(words_found, 2, 0)

    return words
