from fpdf import FPDF 


NEW_X = "LMARGIN"
NEW_Y = "NEXT"


class PDF(FPDF):
    def __init__(self, doctor: object, patient: object, date: str):
        super().__init__(format=(220, 170))
        self.__doctor = doctor
        self.__patient = patient
        self.__date = date

    def set_doctor_info(self):
        self.image(self.__doctor.get_logo(), 10, 10, 25, 25)
        self.set_font("Times", size=21)
        self.cell(95)
        self.cell(100, 25, f"Dr. {self.__doctor.get_name()}", align="C", new_x=NEW_X, new_y=NEW_Y)
        self.cell(0, 10, f"Specialist in: {self.__doctor.get_speciality()}", new_x=NEW_X, new_y=NEW_Y)
        self.cell(0, 10, f"Address: {self.__doctor.get_address()}", new_x=NEW_X, new_y=NEW_Y)

    def set_patient_info(self):
        self.set_font("Times", size=16)
        self.cell(0, 27, "Patient's name: ", new_x=NEW_X)
        self.cell(40)
        self.cell(20, 26, self.__patient.get_name(), new_x=NEW_X)
        self.cell(120)
        self.cell(20, 26, "Age: ", new_x=NEW_X)
        self.cell(136)
        self.cell(20, 26, self.__patient.get_age(), new_x=NEW_X)
        self.cell(150)
        self.cell(20, 26, "Gender:", new_x=NEW_X)
        self.cell(175)
        self.cell(20, 26, self.__patient.get_gender(), new_x=NEW_X)

    def set_extra_info(self):
          self.set_y(140)
          self.cell(20, 10, self.__date)
          self.cell(95)
          self.cell(20, 10, "Signature: ")

    def draw_separator_lines(self):
        self.set_line_width(0.5)
        self.set_draw_color(r=0, g=0, b=0)
        self.line(50, 70, 125, 70)
        self.line(145, 70, 155, 70) 
        self.line(180, 70, 205, 70) 
        self.line(155, 147, 200, 147)

    def save_pdf(self, path: str):
        self.add_page()
        self.set_doctor_info()
        self.set_patient_info()
        self.draw_separator_lines()
        self.set_extra_info()
        self.output(path)
