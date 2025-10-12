"""
CP1404/CP5632 Practical
Data file -> lists program
"""

FILENAME = "subject_data.txt"


def main():
    subject_data = load_data(FILENAME)
    print(subject_data)
    print_subject_details(FILENAME)


def load_data(filename=FILENAME):
    """Read data from file formatted like: subject,lecturer,number of students."""
    input_file = open(filename)
    data = []
    for line in input_file:
        print(line)  # See what a line looks like
        print(repr(line))  # See what a line really looks like
        line = line.strip()  # Remove the \n
        parts = line.split(',')  # Separate the data into its parts
        print(parts)  # See what the parts look like (notice the integer is a string)
        parts[2] = int(parts[2])  # Make the number an integer (ignore PyCharm's warning)
        print(parts)  # See if that worked
        data.append(parts)
        print("----------")
    input_file.close()
    return data


def print_subject_details(filename=FILENAME):
    """Prints subject details."""
    input_file = open(filename)
    for line in input_file:
        line = line.strip()
        parts = line.split(',')
        print(f"{parts[0]} is taught by {parts[1]} and has {parts[2]} students")
main()