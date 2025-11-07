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
    print(MENU)
    for project in project_data:
        print(project)

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


main()