# import sys
# from PyQt5.QtCore import Qt, QBasicTimer, QTime, QDate, QDateTime, QCoreApplication
# from PyQt5.QtWidgets import QApplication, QWidget, QGridLayout, QMenu, QCheckBox, QLabel, QPushButton, QToolTip, \
#     QHBoxLayout, QVBoxLayout, QRadioButton, QLineEdit, QComboBox, QProgressBar, QSlider, QDial, QSplitter, QGroupBox, \
#         QSpinBox, QDoubleSpinBox, QTabWidget, QTimeEdit, QDateTimeEdit, QDateEdit, QCalendarWidget, QTextEdit, QTextBrowser, \
#         QTableWidget, QInputDialog, QMessageBox, QFontDialog, QColorDialog, QFrame, QFileDialog
# from PyQt5.QtGui import QIcon, QPixmap, QFont, QColor
# import urllib.request
# import json
# import requests
# from pathlib import Path

# class video_tab4(QWidget):
#     def __init__(self):
#         super().__init__()
#         layout = QVBoxLayout()
#         layout.addWidget(QLabel('This is Tab 4'))
#         self.setLayout(layout)

        
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QTextEdit

class video_tab4(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setAcceptDrops(True)  # 드래그 앤 드롭 활성화

        self.layout = QVBoxLayout()
        self.label = QLabel('Drag and drop files here', self)
        self.text_edit = QTextEdit(self)
        self.text_edit.setReadOnly(True)

        self.layout.addWidget(self.label)
        self.layout.addWidget(self.text_edit)
        self.setLayout(self.layout)

        self.setWindowTitle('File Drag and Drop Example')
        self.setGeometry(300, 300, 400, 300)

    def dragEnterEvent(self, event):
        if event.mimeData().hasUrls():
            event.acceptProposedAction()

    def dropEvent(self, event):
        files = [url.toLocalFile() for url in event.mimeData().urls()]
        for file in files:
            self.text_edit.append(file)  # 파일 경로를 텍스트 에디트에 추가

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = DragDropWidget()
    window.show()
    sys.exit(app.exec_())
