import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QMessageBox, QFileDialog
from PySide6.QtGui import QPixmap
from PySide6.QtPdf import QPdfDocument
from view.MainWindow_ui import Ui_MainWindow
from helpers import absolute_path
from model.doctor import Doctor
from model.patient import Patient
from pdfmanager import PDF
from datetime import date

class MainWindow(QMainWindow, Ui_MainWindow):
    doctor_logo = ""
    def __init__(self):
        super().__init__()
        self.setFixedSize(self.size())
        self.setupUi(self)
        self.current_date = str(date.today())
        self.default_image = absolute_path("images/your_logo.png")
        self.prepare_gui()

    def prepare_gui(self):
         self.logo.setPixmap(QPixmap(self.default_image).scaled(100, 100))
         self.date_label.setText(self.current_date)
         self.pdf_viewer.setMinimumWidth(250)
         self.gender_combo.addItems(["Male", "Female"])
         self.set_signals()

    def set_signals(self):
           self.logo.image_loaded.connect(self.load_image)
           self.generate_button.clicked.connect(self.generate_prescription)

    def load_image(self, image_path: str):
         if image_path:
              self.doctor_logo = image_path
              self.logo.setPixmap(QPixmap(absolute_path(image_path)).scaled(100, 100))


    def generate_prescription(self):
         doctor_name = self.doctor_name_line.text().title()
         doctor_speciality = self.specialist_line.text().title()
         doctor_address = self.address_line.text().title()
         doctor_logo = self.doctor_logo if self.doctor_logo else self.default_image
         patient_name = self.patients_name_line.text().title()
         patient_age = self.age_line.text()
         patient_gender = self.gender_combo.currentText()
         if (doctor_name == "" or doctor_speciality == "" or doctor_address == "" or patient_name == "" 
         or patient_age == ""):
              QMessageBox.warning(self, "Warning", "The fields can't be empty.")
         else:
              if patient_age.isdigit():
                   if int(patient_age) >= 0 and int(patient_age) <= 100:
                        doctor = Doctor(doctor_name, doctor_speciality, doctor_address, doctor_logo) 
                        patient = Patient(patient_name, patient_age, patient_gender)
                        pdf = PDF(doctor, patient, self.current_date)
                        pdf.save_pdf(doc:=QFileDialog.getSaveFileName(self, "Save file", "", "PDF files(*.pdf)")[0])
                        self.open_prescription(doc=doc)
                   else: 
                        QMessageBox.warning(self, "Warning", "The patient's age has to be a positive number.")
              else:
                   QMessageBox.warning(self, "Warning", "The given age is not a number.")

    def open_prescription(self, doc:str):
         pdf_document = QPdfDocument(self)
         self.pdf_viewer.setDocument(pdf_document)
         pdf_document.load(doc)
         self.clean_fields()

    def clean_fields(self):
         self.doctor_name_line.setText("")
         self.specialist_line.setText("")
         self.address_line.setText("")
         self.patients_name_line.setText("")
         self.age_line.setText("")
         
                        
              


def main():
    app = QApplication(sys.argv)
    main_window = MainWindow()
    main_window.show()
    sys.exit(app.exec())


if __name__ == '__main__':
    main()