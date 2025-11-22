import img2pdf
from pathlib import Path

def img_to_pdf(input_path, output_path):

    if not Path(input_path).is_file():
        print(f" the file does not exists here! {input_path}")
        return

    with open(output_path, "wb") as file:
        file.write(img2pdf.convert(input_path))
    print(f" succefully converted:✅ {output_path}")

img_to_pdf("example.png", "image.pdf")