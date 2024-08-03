# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'MainWindow.ui'
##
## Created by: Qt User Interface Compiler version 6.7.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtPdfWidgets import QPdfView
from PySide6.QtWidgets import (QApplication, QComboBox, QFormLayout, QHBoxLayout,
    QLabel, QLineEdit, QMainWindow, QPushButton,
    QSizePolicy, QSpacerItem, QVBoxLayout, QWidget)

from customlabel import CustomLabel

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(407, 408)
        MainWindow.setStyleSheet(u"QMainWindow{\n"
"  background-color: #1F2544;\n"
"}\n"
"\n"
"QLineEdit{\n"
"  background-color: #EEEDEB; \n"
"  color: #000000;\n"
"  padding: 2px; \n"
"  border:none; \n"
"  border-radius: 5px;\n"
"  width: 200px\n"
"}\n"
"\n"
"QPushButton{\n"
"   background-color: #474F7A;\n"
"   border: none; \n"
"   border-radius: 10px;\n"
"   padding: 5px; \n"
"   color: #FFD0EC;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"  background-color: #343a59\n"
"}\n"
"\n"
"QComboBox::editable:!on { border: 4px black; border-style: dotted;}")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.pdf_viewer = QPdfView(self.centralwidget)
        self.pdf_viewer.setObjectName(u"pdf_viewer")

        self.horizontalLayout.addWidget(self.pdf_viewer)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.logo = CustomLabel(self.centralwidget)
        self.logo.setObjectName(u"logo")
        self.logo.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout.addWidget(self.logo)

        self.formLayout = QFormLayout()
        self.formLayout.setObjectName(u"formLayout")
        self.doctors_name_label = QLabel(self.centralwidget)
        self.doctors_name_label.setObjectName(u"doctors_name_label")
        font = QFont()
        font.setFamilies([u"Academy Engraved LET"])
        font.setPointSize(24)
        self.doctors_name_label.setFont(font)

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.doctors_name_label)

        self.doctor_name_line = QLineEdit(self.centralwidget)
        self.doctor_name_line.setObjectName(u"doctor_name_line")

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.doctor_name_line)

        self.specialist_label = QLabel(self.centralwidget)
        self.specialist_label.setObjectName(u"specialist_label")
        self.specialist_label.setFont(font)

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.specialist_label)

        self.specialist_line = QLineEdit(self.centralwidget)
        self.specialist_line.setObjectName(u"specialist_line")

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.specialist_line)

        self.address_label = QLabel(self.centralwidget)
        self.address_label.setObjectName(u"address_label")
        self.address_label.setFont(font)

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.address_label)

        self.address_line = QLineEdit(self.centralwidget)
        self.address_line.setObjectName(u"address_line")

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.address_line)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.formLayout.setItem(3, QFormLayout.LabelRole, self.verticalSpacer)


        self.verticalLayout.addLayout(self.formLayout)


        self.verticalLayout_2.addLayout(self.verticalLayout)

        self.formLayout_4 = QFormLayout()
        self.formLayout_4.setObjectName(u"formLayout_4")
        self.patients_name_label = QLabel(self.centralwidget)
        self.patients_name_label.setObjectName(u"patients_name_label")
        self.patients_name_label.setFont(font)

        self.formLayout_4.setWidget(0, QFormLayout.LabelRole, self.patients_name_label)

        self.patients_name_line = QLineEdit(self.centralwidget)
        self.patients_name_line.setObjectName(u"patients_name_line")

        self.formLayout_4.setWidget(0, QFormLayout.FieldRole, self.patients_name_line)

        self.age_label = QLabel(self.centralwidget)
        self.age_label.setObjectName(u"age_label")
        self.age_label.setFont(font)

        self.formLayout_4.setWidget(1, QFormLayout.LabelRole, self.age_label)

        self.age_line = QLineEdit(self.centralwidget)
        self.age_line.setObjectName(u"age_line")

        self.formLayout_4.setWidget(1, QFormLayout.FieldRole, self.age_line)

        self.gender_combo = QComboBox(self.centralwidget)
        self.gender_combo.setObjectName(u"gender_combo")
        font1 = QFont()
        font1.setFamilies([u"Academy Engraved LET"])
        font1.setPointSize(16)
        self.gender_combo.setFont(font1)

        self.formLayout_4.setWidget(2, QFormLayout.SpanningRole, self.gender_combo)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.formLayout_4.setItem(3, QFormLayout.LabelRole, self.verticalSpacer_2)

        self.date_label = QLabel(self.centralwidget)
        self.date_label.setObjectName(u"date_label")
        font2 = QFont()
        font2.setFamilies([u"Academy Engraved LET"])
        font2.setPointSize(18)
        self.date_label.setFont(font2)
        self.date_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.formLayout_4.setWidget(4, QFormLayout.SpanningRole, self.date_label)


        self.verticalLayout_2.addLayout(self.formLayout_4)

        self.generate_button = QPushButton(self.centralwidget)
        self.generate_button.setObjectName(u"generate_button")
        self.generate_button.setFont(font2)

        self.verticalLayout_2.addWidget(self.generate_button)


        self.horizontalLayout.addLayout(self.verticalLayout_2)

        self.horizontalLayout.setStretch(0, 70)
        self.horizontalLayout.setStretch(1, 30)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Prescription Generator", None))
        self.logo.setText("")
        self.doctors_name_label.setText(QCoreApplication.translate("MainWindow", u"Doctor's name", None))
        self.specialist_label.setText(QCoreApplication.translate("MainWindow", u"Specialist In", None))
        self.address_label.setText(QCoreApplication.translate("MainWindow", u"Address", None))
        self.patients_name_label.setText(QCoreApplication.translate("MainWindow", u"Patient's name", None))
        self.age_label.setText(QCoreApplication.translate("MainWindow", u"Age", None))
        self.gender_combo.setCurrentText("")
        self.date_label.setText("")
        self.generate_button.setText(QCoreApplication.translate("MainWindow", u"Generate", None))
    # retranslateUi

