from datetime import datetime
from project_management import projects




def view_project():
    print("View Projects")

    if not projects:
        print("No projects available")
        return
    
    for project in projects:
        print(f"Title: {project['title']}, Description: {project['description']}, Target: {project['target']}, Start Date: {project['start_date']}, End Date: {project['end_date']}, Creator: {project['creator']}")




def search_projects_by_date():
    search_date = input("Enter date to search (YYYY-MM-DD): ")
    try:
        search_date = datetime.strptime(search_date, "%Y-%m-%d")
        filtered_projects = [p for p in projects if p["start_date"] <= search_date <= p["end_date"]]
        if not filtered_projects:
            print("No projects found for this date!")
        for project in filtered_projects:
            print(f"Title: {project['title']}, Owner: {project['owner']}, Target: {project['target']} EGP")
    except ValueError:
        print("Invalid date format!")