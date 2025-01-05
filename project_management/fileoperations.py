import json
from datetime import datetime




def read_projects():

    try:
        projectobject = open("projects.json", "r")
        projects_list = json.load(projectobject)
        projectobject.close()

        # for project in projects_list:
        #     project["title"] = project["title"]
        #     project["start_date"] = datetime.strptime(project["start_date"], "%Y-%m-%d")
        #     project["end_date"] = datetime.strptime(project["end_date"], "%Y-%m-%d")
        #     project["target"] = float(project["target"])

    except FileNotFoundError:
        print("The file projects.json was not found.")
        projects_list = []
    except json.JSONDecodeError:
        print("Error decoding JSON from the file.")
        projects_list = []
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        projects_list = []

    return projects_list
projects = read_projects()




def save_projects(projects_list):
    try:
        projectobject = open("projects.json", "w")

        # for project in project:
        #     project["title"] = project["title"]
        #     project["start_date"] = project["start_date"].strftime("%Y-%m-%d")
        #     project["end_date"] = project["end_date"].strftime("%Y-%m-%d")
        #     project["target"] = float(project["target"])

        json.dump(projects_list, projectobject, indent=4)
        projectobject.close()
        print("Projects saved successfully!")
        return True
        
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return False
        

def add_project():
    old_projects = read_projects() # read old projects
    print(old_projects)
    old_projects.append("new project") # add new project
    save_projects(old_projects) # save all projects
    print("Save Projects")
    return old_projects # return all projects

















# def generate_project_id():
    
#     try:
#         projectobject = open("projects.json", "r")
#         id = projectobject.read()
#         id = int(id)
#         id += 1
#         projectobject.close()
#         projectobject = open("projects.json", "w")
#         projectobject.write(str(id))
#         projectobject.close()
#     except Exception as e:
#         print(f"An unexpected error occurred: {e}")
#         return 1
        
#     else:
#         return id
