"""
Estimate: 2 Hours
Actual:
"""

from project import Project
# import datetime


FILENAME = "projects.txt"
MENU = """
- (L)oad projects  
- (S)ave projects  
- (D)isplay projects  
- (F)ilter projects by date
- (A)dd new project  
- (U)pdate project
- (Q)uit
"""

def main():
    project_data = load_data(FILENAME)
    project_count = len(project_data)
    print("Loaded {} projects from {}".format(project_count, FILENAME))
    print(MENU)
    choice = input(">>> ").upper()
    while choice != "Q":
        if choice == "L":
            new_data = post_load_data()
            if new_data is not None:
                project_data = new_data

        elif choice == "S":
            pass
        elif choice == "D":
            pass
        elif choice == "F":
            pass
        elif choice == "A":
            pass
        elif choice == "U":
            pass
        else:
            print("Invalid Input")
            choice = input(">>> ").upper()


def load_data(filename):
    """Loads project data from file"""
    projects = []
    with open(filename, "r", encoding="utf-8") as in_file:
        in_file.readline()
        for line in in_file:
            parts = line.strip().split('\t')
            name = parts[0]
            start_date = parts[1]
            priority = parts[2]
            cost_estimate = parts[3]
            completion = parts[4]
            project_attributes = Project(name, start_date, int(priority), float(cost_estimate), int(completion))
            projects.append(project_attributes)
        return projects

def post_load_data():
    """Post-load project data from a file selected by the user"""
    chosen_file = input("Enter a file name: ")
    if chosen_file == "":
        print("No file selected")
        return None

    try:
        projects = load_data(chosen_file)
        print("Loaded {} projects from {}".format(len(projects), chosen_file))
        return projects
    except FileNotFoundError:
        print("File not found")
        return None
main()