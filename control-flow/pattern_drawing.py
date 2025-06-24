# pattern_drawing.py

# Prompt user for pattern size
size = int(input("Enter the size of the pattern: "))

# Initialize row counter
row = 0

# Use while loop to iterate through each row
while row < size:
    # Use for loop to print asterisks on the same line
    for col in range(size):
        print("*", end="")
    # Move to the next line after a row is complete
    print()
    row += 1
