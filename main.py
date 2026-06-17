import os
from svglib.svglib import svg2rlg
from reportlab.graphics import renderPDF


INPUT_DIRECTORY = "input"
OUTPUT_DIRECTORY = "output"


def get_all_files_in_directory(directory):
    all_files = []
    for root, _, files in os.walk(directory):
        for file in files:
            all_files.append(os.path.join(root, file))
    return all_files


def remove_all_non_svg_files(files):
    return [file for file in files if file.lower().endswith(".svg")]


def convert_svg_to_pdf(svg_file, output_directory=OUTPUT_DIRECTORY):
    drawing = svg2rlg(svg_file)
    output_file_name = os.path.basename(svg_file).replace(".svg", ".pdf")
    output_file = os.path.join(output_directory, output_file_name)
    renderPDF.drawToFile(drawing, output_file)


def main():
    if os.path.exists(OUTPUT_DIRECTORY):
        print(f"Directory '{OUTPUT_DIRECTORY}' already exists.")
        print("Exiting the program. Without processing any files.")
        return

    all_files = get_all_files_in_directory(INPUT_DIRECTORY)
    svg_files = remove_all_non_svg_files(all_files)

    if not svg_files:
        print(f"No SVG files found in the '{INPUT_DIRECTORY}' directory.")
        print("Exiting the program. Without processing any files.")
        return

    os.makedirs(OUTPUT_DIRECTORY, exist_ok=True)
    for svg_file in svg_files:
        convert_svg_to_pdf(svg_file, OUTPUT_DIRECTORY)
    print("All SVG files have been processed and converted to PDF format.")
    print(f"Converted files are saved in the '{OUTPUT_DIRECTORY}' directory.")


if __name__ == "__main__":
    main()
