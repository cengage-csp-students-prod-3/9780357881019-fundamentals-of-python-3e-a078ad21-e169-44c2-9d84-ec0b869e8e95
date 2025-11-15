# numberlines.py
# Copies lines from input file to output file, numbering each line

def main():
    input_file = input("Enter the input file name: ")
    output_file = input("Enter the output file name: ")

    with open(input_file, "r", encoding="utf-8") as infile, \
         open(output_file, "w", encoding="utf-8") as outfile:

        line_number = 1
        for line in infile:
            # Sağdaya dayalı 4 sütun, ardından ">" ve satır içeriği
            numbered_line = f"{line_number:>4}> {line}"
            outfile.write(numbered_line)
            line_number += 1

    print("File copied with line numbers successfully!")

if __name__ == "__main__":
    main()
