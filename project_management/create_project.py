from datetime import datetime

projects = []

def create_project(usaer_email):
    print("Create Project")
    title = input("Enter project title: ")
    description = input("Enter project description: ")
    target = int(input("Enter project target: "))

    try:
        target = float(target)
    except ValueError:
        print("Invalid target amount")
        return
    
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
        "start_date": start_date,
        "end_date": end_date,
        "creator": user_email,
    }


    projects.append(project)
    
    print("Project created successfully!")