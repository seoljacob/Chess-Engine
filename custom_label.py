from PyQt5.QtWidgets import QLabel
from PyQt5.QtCore import Qt

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
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setMouseTracking(True)  # Enable mouse tracking for the label
        self.dragging = False  # Flag to track whether the label is being dragged

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.setCursor(Qt.ClosedHandCursor)
            self.dragging = True  # Set the dragging flag to True
            self.drag_start_pos = event.pos()  # Record the start position of the drag

    def mouseMoveEvent(self, event):
        if self.dragging:
            # Calculate the distance moved from the start position
            delta = event.pos() - self.drag_start_pos
            # Update the position of the label by the distance moved
            self.move(self.x() + delta.x(), self.y() + delta.y())

    def mouseReleaseEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.dragging = False  # Set the dragging flag to False

            x = round_to_100(self.x())
            y = round_to_100(self.y())
            print(x, y)
            self.move(x, y)
            
        
