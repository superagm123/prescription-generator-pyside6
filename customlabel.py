from PySide6.QtWidgets import QLabel, QFileDialog
from PySide6.QtCore import Signal, Slot
from PySide6.QtGui import QMouseEvent


class CustomLabel(QLabel):
    image_loaded = Signal(str)
    def __init__(self, parent: None):
        super().__init__(parent)
        self.setToolTip("Double click to load your logo")
        
    @Slot()
    def mouseDoubleClickEvent(self, event: QMouseEvent) -> None:
        image_path = QFileDialog.getOpenFileName(self, "Open an image", "", "(All Images) *.jpg *png")[0]
        self.image_loaded.emit(image_path)