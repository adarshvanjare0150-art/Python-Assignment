# File Processor Program
# Count lines, extract first two lines, and display output content

# Sample text (simulates the input file)
text = """Python Programming
File Handling Assignment
This is the third line.
This is the fourth line."""

# Read text and count lines
lines = text.splitlines()
print("Total number of lines:", len(lines))

# Extract first two lines
first_two = lines[:2]

print("\nFirst two lines:")
for line in first_two:
    print(line)

# Prepare output file content
output_text = "\n".join(first_two)

print("\nOutput file content:")
print(output_text)

print("\nProgram executed successfully.")
