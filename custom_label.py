from PyQt5.QtWidgets import QLabel
from PyQt5.QtCore import Qt, pyqtSignal

"""
370 rounds to 400
430 rounds to 400
"""
def round_to_100(number):
    rounded_number = number / 100 #3.7 || 4.3
    rounded_number = round(rounded_number) #4.0 || 4.0
    rounded_number *= 100 # 400 || 400
    if rounded_number < 0:
        return 0
    if rounded_number > 700:
        return 700
    return rounded_number

class ChessPieceLabel(QLabel):
    mouse_press = pyqtSignal(int, int)
    mouse_release = pyqtSignal(int, int) # set up event listener for mouse release event

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setMouseTracking(True)
        self.dragging = False

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.setCursor(Qt.ClosedHandCursor)
            self.dragging = True
            self.drag_start_pos = event.pos()
            self.mouse_press.emit(self.x(), self.y())

    def mouseMoveEvent(self, event):
        if self.dragging:
            delta = event.pos() - self.drag_start_pos
            self.move(self.x() + delta.x(), self.y() + delta.y())

    def mouseReleaseEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.dragging = False
            x = round_to_100(self.x())
            y = round_to_100(self.y())
            self.move(x, y)
            self.mouse_release.emit(x, y) # send x, y on mouse release
           
        
