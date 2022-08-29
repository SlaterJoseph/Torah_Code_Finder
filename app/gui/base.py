import sys

from PyQt5.QtCore import Qt
from PySide6.QtCore import Slot
from PyQt5.QtWidgets import *
from .letters import create_letter
from .words import create_words


def create_app():
    app = QApplication(sys.argv)
    windo = QWidget()
    windo.setMinimumSize(600, 400)
    windo.setWindowTitle('Torah Code Finder')
    main_layout = QGridLayout()
    start = QFrame()

    letters = QFrame()
    letters.setLayout(create_letter())
    main_layout.addWidget(letters, 0, 0)
    letters.hide()

    words = QFrame()
    words.setLayout(create_words())
    main_layout.addWidget(words, 0, 0)
    words.hide()

    front_page = QGridLayout()
    start.setLayout(front_page)
    blurb = QLabel('Please select which option you want to work with')
    blurb.setAlignment(Qt.AlignCenter)

    @Slot()
    def select_letters() -> None:
        start.hide()
        letters.show()

    @Slot()
    def select_words() -> None:
        start.hide()
        words.show()

    letter_code = QPushButton('Code Finder')
    letter_code.clicked.connect(select_letters)
    word_finder = QPushButton('Word Locator')
    word_finder.clicked.connect(select_words)

    front_page.addWidget(blurb, 0, 0, 1, 0)
    front_page.addWidget(letter_code, 2, 0)
    front_page.addWidget(word_finder, 2, 2)

    main_layout.addWidget(start, 0, 0)
    windo.setLayout(main_layout)
    windo.show()
    app.exec()







