# Abdelrahman Khaled 

from datetime import datetime
from .fileoperations import projects, save_projects
from tabulate import tabulate


def view_project():
    if not projects:
        print("No projects available")
        return

    table = []
    for project in projects:
        table.append([
            project["title"],
            project["description"],
            project["target"],
            project["creator"]
        ])

    headers = ["Title", "Description", "Target", "Creator"]
    print(tabulate(table, headers, tablefmt="grid"))







def search_projects_by_date():
    date_to_search = input("Enter date to search (YYYY-MM-DD): ")
    try:
        search_date = datetime.strptime(date_to_search, "%Y-%m-%d")
    except ValueError:
        print("Invalid date format")
        return

    filtered_projects = [
        p for p in projects 
        if 'start_date' in p and 'end_date' in p and 
        datetime.strptime(p["start_date"], "%Y-%m-%d") <= search_date <= datetime.strptime(p["end_date"], "%Y-%m-%d")
    ]

    if not filtered_projects:
        print("No projects found for the given date")
        return

    table = []
    for project in filtered_projects:
        table.append([
            project["title"],
            project["description"],
            project["target"],
            project["creator"]
        ])

    headers = ["Title", "Description", "Target", "Creator"]
    print(tabulate(table, headers, tablefmt="grid"))




def delete_project(user_email):
    title_to_delete = input("Enter the title of the project to delete: ")
    project_to_delete = next((p for p in projects if p["title"] == title_to_delete and p["creator"] == user_email), None)
    
    if not project_to_delete:
        print("Project not found or you do not have permission to delete this project.")
        return

    projects.remove(project_to_delete)
    save_projects(projects)
    print("Project deleted successfully!")




def update_project(user_email):
    title_to_update = input("Enter the title of the project to update: ")
    project_to_update = next((p for p in projects if p["title"] == title_to_update and p["creator"] == user_email), None)
    
    if not project_to_update:
        print("Project not found or you do not have permission to update this project.")
        return

    print("Enter new details for the project (leave blank to keep current value):")
    new_title = input(f"Title [{project_to_update['title']}]: ") or project_to_update['title']
    new_description = input(f"Description [{project_to_update['description']}]: ") or project_to_update['description']
    new_target = input(f"Target [{project_to_update['target']}]: ") or project_to_update['target']
    new_start_date = input(f"Start Date [{project_to_update['start_date']}]: ") or project_to_update['start_date']
    new_end_date = input(f"End Date [{project_to_update['end_date']}]: ") or project_to_update['end_date']

    project_to_update.update({
        "title": new_title,
        "description": new_description,
        "target": new_target,
        "start_date": new_start_date,
        "end_date": new_end_date
    })

    save_projects(projects)
    print("Project updated successfully!")
    print("Project updated brooo!!!!!")