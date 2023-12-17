from PyQt5.QtCore import Qt
from count import count
import sys
from PyQt5.QtWidgets import QApplication , QMainWindow , QFileDialog , QPushButton , QLabel , QTextEdit, QWidget 
from PyQt5.QtGui import QDragEnterEvent, QDragMoveEvent, QDropEvent, QPixmap , QIcon
from PyQt5.uic import loadUi

class MainWindow(QMainWindow):
    def __init__(self) :
        super().__init__()
        loadUi('design.ui',self)
        self.setWindowIcon(QIcon('./images/countIcon.png'))
        self.browseBtn:QPushButton
        self.browseBtn.clicked.connect(self.browse_files)
        self.countBtn:QPushButton
        self.countBtn.clicked.connect(self.count_action)

    def count_action(self):
        self.oNameText:QTextEdit
        self.numObjectsLabel:QLabel
        obj_name=self.oNameText.toPlainText()
        if obj_name == '':
            return
        if self.image_path == None:
            self.numObjectsLabel.setText("please choose an image!")
        else:
            result=count(obj_name,self.image_path)
            self.numObjectsLabel.setText(result[0])

    def browse_files(self):
        fname=QFileDialog.getOpenFileName(self,'Select Image','.\images','Images (*.png *.xmp *.jpg *.jpeg *.svg)')
        if(fname[0]==''):
            return
        self.imgLabel:QLabel
        self.set_image(fname[0])

        
        
    def dragEnterEvent(self, event: QDragEnterEvent | None) :
        if event.mimeData().hasImage:
            event.accept()
        else:
            event.ignore()

    def dragMoveEvent(self, event: QDragMoveEvent | None) :
        if event.mimeData().hasImage:
            event.accept()
        else:
            event.ignore()
    
    def dropEvent(self, event: QDropEvent | None) :
        if event.mimeData().hasImage:
            event.setDropAction(Qt.CopyAction)
            file_path=event.mimeData().urls()[0].toLocalFile()
            self.set_image(file_path)
            event.accept()
        else:
            event.ignore()

    def set_image(self,file_path):
        self.image_path=file_path
        pixmap = QPixmap(file_path)
        scaled_pixmap = pixmap.scaled(
                self.imgLabel.size(), Qt.KeepAspectRatio, Qt.SmoothTransformation)
        self.imgLabel.setPixmap(scaled_pixmap)

        

app=QApplication([])
mainWindow=MainWindow()
mainWindow.setWindowTitle('Object Counter')
mainWindow.show()
app.exec_()

