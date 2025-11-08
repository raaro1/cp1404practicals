"""
Estimate: 2 Hours
Actual:
"""

from project import Project
from datetime import datetime


FILENAME = "projects.txt"
MENU = """- (L)oad projects  
- (S)ave projects  
- (D)isplay projects  
- (F)ilter projects by date
- (A)dd new project  
- (U)pdate project
- (Q)uit"""

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
            filter_by_date(project_data)
        elif choice == "A":
            new_project = add_project()
            project_data.append(new_project)
        elif choice == "U":
            update_project(project_data)
        else:
            print("Invalid Input")

        print(MENU)
        choice = input(">>> ").upper()

    save_projects(project_data)

def load_data(filename):
    """Loads project data from file"""
    projects = []
    with open(filename, "r", encoding="utf-8") as in_file:
        in_file.readline()
        for line in in_file:
            parts = line.strip().split('\t')
            name = parts[0]
            date = parts[1]
            start_date = datetime.strptime(date, "%d/%m/%Y")
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

    print("\nIncomplete projects:")
    incomplete_projects.sort()
    for project in incomplete_projects:
        print(f"  {project}")

    print("Completed projects:")
    completed_projects.sort()
    for project in completed_projects:
        print(f"  {project}")

def filter_by_date(projects):
    filer_date = input("Show projects that start after date (dd/mm/yy): ")
    while filer_date == "":
        print("No date selected")
        filer_date = input("Show projects that start after date (dd/mm/yy): ")

    try:
        filter_converted = datetime.strptime(filer_date, "%d/%m/%Y")
    except ValueError:
        print("Invalid date format. Please use dd/mm/yy")
        return

    projects.sort()
    for project in projects:
        if  project.start_date >= filter_converted:
            print(project)

def update_project(project):
    projects = project
    for index, project in enumerate(projects):
        print(index, project)
    project_choice = int(input("Select project index: "))

    while project_choice < 0 or project_choice > len(projects):
        print("Invalid choice")
        project_choice = int(input("Select project index: "))

    print(projects[project_choice])

    try:
        new_percentage = int(input("New Percentage: "))
    except ValueError:
        return

    if new_percentage < 0 or new_percentage > 100:
        return

    projects[project_choice].completion_percentage = new_percentage

    try:
        new_priority = int(input("New Priority: "))
    except ValueError:
        return

    if new_priority < 0 or new_priority > len(projects):
        return

    projects[project_choice].priority = new_priority

def add_project():
    """Adds a project to the projects list"""
    print("Let's add a new project")
    name = input("Name: ")
    start_date_str = input("Start date (dd/mm/yy): ")
    priority = int(input("Priority: "))
    cost_estimate = float(input("Cost estimate: "))
    completion = int(input("Percent completion: "))

    start_date = datetime.strptime(start_date_str, "%d/%m/%Y")

    new_project = Project(name, start_date, priority, cost_estimate, completion)

    return new_project

def save_projects(projects):
    """Save project data from a file selected by the user"""
    save_choice = input(f"Would you like to save to {FILENAME}?: ").lower()
    if save_choice in ("y", "yes"):
        with open(FILENAME, "w", encoding="utf-8") as out_file:
            for project in projects:
                out_file.write(str(project + "\n"))

    print("Thank you for using custom-built project management software.")
main()