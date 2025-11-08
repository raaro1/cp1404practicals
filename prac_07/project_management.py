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
    print("Loaded {} projects from {}".format(len(project_data), FILENAME))
    print(MENU)
    choice = input(">>> ").upper()
    while choice != "Q":
        if choice == "L":
            new_data = post_load_data()
            if new_data is not None:
                project_data = new_data
        elif choice == "S":
            save_data(project_data)
        elif choice == "D":
            display_projects(project_data)
        elif choice == "F":
            pass
        elif choice == "A":
            pass
        elif choice == "U":
            pass
        else:
            print("Invalid Input")

        print(MENU)
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

def save_data(projects):
    """Save project data from a file selected by the user"""
    chosen_file = input("Enter a file name: ")
    while chosen_file == "":
        print("No file selected")
        chosen_file = input("Enter a file name: ")
    with open(chosen_file, "w", encoding="utf-8") as out_file:
        for project in projects:
            out_file.write(str(project + "\n"))

def display_projects(projects):
    """Display projects in two groups: Unfinished and Finished"""
    completed_projects = []
    incomplete_projects = []
    for project in projects:
        if project.completion_percentage == 100:
            completed_projects.append(project)
        else:
            incomplete_projects.append(project)
    print("Completed projects:")
    for project in completed_projects:
        print(project)
        print(f"   {project.name}, start: {project.start_date}, priority {project.priority}, estimate: ${project.cost_estimate:.2f}, {project.completion_percentage}%")
    print("\nIncomplete projects:")
    for project in incomplete_projects:
        print(f"   {project.name}, start: {project.start_date}, priority {project.priority}, estimate: ${project.cost_estimate:.2f}, {project.completion_percentage}%")


main()