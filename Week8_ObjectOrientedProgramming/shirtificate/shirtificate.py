from fpdf import FPDF, Align

class PDF(FPDF):
    def header(self):
        self.set_font('helvetica', 'B', 36)
        self.cell(0, 20, 'CS50 Shirtificate', 0, align=Align.C, new_x="LMARGIN", new_y="NEXT")

def main():
    name = input("Name: ")
    pdf = PDF()
    pdf.add_page( format='A4' )
    pdf.image('shirtificate.png', x=10, y=50, w=pdf.w - 20)
    pdf.set_font('helvetica', '', 24)
    pdf.set_text_color(255, 255, 255)
    pdf.cell(0, 160, f'{name} took CS50', 0, align= Align.C)
    pdf.output('shirtificate.pdf')  
    
if __name__ == "__main__":
    main()

    