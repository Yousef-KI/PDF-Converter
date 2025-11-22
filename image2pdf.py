import img2pdf

def convert_image(input_path, output_path):
    with open(output_path, "wb") as f:
        f.write(img2pdf.convert(input_path))
