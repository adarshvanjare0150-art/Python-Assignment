"""
CSV TO JSON CONVERTER (in-memory version — no file writing required)
"""

import csv
import json
import io


def read_csv_from_string(csv_text):
    """Returns a list of dictionaries, one per CSV row, from CSV text."""
    reader = csv.DictReader(io.StringIO(csv_text))
    return list(reader)


def convert_csv_to_json(csv_text):
    """Converts CSV text into a JSON-formatted string."""
    data = read_csv_from_string(csv_text)
    return json.dumps(data, indent=4)


if __name__ == "__main__":

    sample_csv = (
        "id,name,department,marks\n"
        "1,Aditi Sharma,Computer Science,88\n"
        "2,Rahul Verma,Mechanical,76\n"
        "3,Sneha Iyer,Electronics,92\n"
    )

    print("Contents of sample CSV:")
    print(sample_csv)

    json_output = convert_csv_to_json(sample_csv)

    print("Converted CSV to JSON:")
    print(json_output)
