from fpdf import FPDF

class PDF(FPDF):
    def __init__(self):
        super().__init__()
        self.set_auto_page_break(auto=True, margin=15)
        self.add_page()
        self.set_font('Arial', 'B', size=12)

def text_to_pdf(input_path, output_path):
    pdf = PDF()

    with open(input_path, 'r', encoding='utf-8') as file:
        for line in file:
            pdf.cell(200, 10, txt=line.strip(), ln=True)

    pdf.output(output_path)

text_to_pdf("example.txt", "text.pdf")