from datetime import datetime
from .fileoperations import save_projects, projects

def create_project(user_email):
    title = input("Enter project title: ")
    description = input("Enter project description: ")
    target = float(input("Enter project target: "))
    start_date = input("Enter project start date (YYYY-MM-DD): ")
    end_date = input("Enter project end date (YYYY-MM-DD): ")

    try:
        start_date = datetime.strptime(start_date, "%Y-%m-%d")
        end_date = datetime.strptime(end_date, "%Y-%m-%d")
        if end_date <= start_date:
            print("End date must be after start date")
            return
    except ValueError:
        print("Invalid date format")
        return
    
    project = {
        "title": title,
        "description": description,
        "target": target,
        "start_date": start_date.strftime("%Y-%m-%d"),
        "end_date": end_date.strftime("%Y-%m-%d"),
        "creator": user_email,
    }

    projects.append(project)
    save_projects(projects)

    print("Project created successfully!")