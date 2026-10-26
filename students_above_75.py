import csv
from io import StringIO

data = """Name,Marks
Rahul,85
Priya,92
Amit,68
Sneha,78
"""

file = StringIO(data)
reader = csv.DictReader(file)

print("Students who scored above 75:")

for row in reader:
    if int(row["Marks"]) > 75:
        print(row["Name"], row["Marks"])
