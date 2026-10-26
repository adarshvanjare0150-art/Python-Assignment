"""
FILE PROCESSOR PROGRAM
Count lines, extract the first two lines, and write them to a new file.
"""

def process_file(input_filename, output_filename):
    try:
        with open(input_filename, "r", encoding="utf-8") as file:
            lines = file.readlines()

        print("Total number of lines:", len(lines))

        first_two_lines = lines[:2]

        with open(output_filename, "w", encoding="utf-8") as output_file:
            output_file.writelines(first_two_lines)

        print("First two lines:")
        for line in first_two_lines:
            print(line, end="")

        print(f"\nExtracted lines written to '{output_filename}' successfully.")

    except FileNotFoundError:
        print(f"Error: Input file '{input_filename}' was not found.")
    except OSError as error:
        print("File error:", error)


if __name__ == "__main__":
    input_filename = input("Enter input text filename (e.g., input.txt): ").strip()
    output_filename = input("Enter output filename (e.g., output.txt): ").strip()

    process_file(input_filename, output_filename)
