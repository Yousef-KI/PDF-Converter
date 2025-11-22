from fpdf import FPDF

def convert_txt(input_path, output_path):
    class PDF(FPDF):
        def __init__(self):
            super().__init__()
            self.set_auto_page_break(auto=True, margin=15)
            self.add_page()
            self.set_font("Arial", size=12)

    pdf = PDF()
    with open(input_path, 'r', encoding='utf-8') as file:
        for line in file:
            pdf.cell(200, 10, txt=line.strip(), ln=True)
    pdf.output(output_path)
