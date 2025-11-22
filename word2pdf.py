from docx2pdf import convert
from pathlib import Path

def docx_to_pdf(input_path, output_path):

    if not Path(input_path).is_file():
        print(f" the file does not exists here! {input_path}")
        return


    convert(input_path, output_path)
    print(f" succefully converted:✅ {output_path}")


docx_to_pdf("sample.docx", "docx.pdf")
