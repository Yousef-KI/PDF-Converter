import argparse
from pathlib import Path
import sys

from txt2pdf import convert_txt
from image2pdf import convert_image
from word2pdf import convert_docx

def main():
    parser = argparse.ArgumentParser(description="Convert files to PDF")

    parser.add_argument("type", choices=["txt", "img", "docx"], help="Type of the input file")
    parser.add_argument("input", help="Path to the input file")
    parser.add_argument("output", help="Path to the output PDF file")

    args = parser.parse_args()

    if not Path(args.input).is_file():
        print(f"❌ File not found: {args.input}")
        sys.exit(1)

    if args.type == "txt":
        convert_txt(args.input, args.output)
    elif args.type == "img":
        convert_image(args.input, args.output)
    elif args.type == "docx":
        convert_docx(args.input, args.output)
    else:
        print("❌ Unknown file type")

if __name__ == "__main__":
    main()
