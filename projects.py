from google.cloud import resource_manager
import csv

PROD_FOLDER_ID = "913243806677"


def list_projects():
    client = resource_manager.Client()
    filter_param = {"parent.id": PROD_FOLDER_ID}
    projects = client.list_projects(filter_param)
    project_list = []
    for project in projects:
        project_list.append({
            "project_id": project.project_id,
            "name": project.name,
        })
    return project_list


def dict_to_csv(data, file_name):
    with open(file_name, 'w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=data[0].keys())
        writer.writeheader()
        for row in data:
            writer.writerow(row)


project_list = list_projects()
file_name = 'output/data.csv'
dict_to_csv(project_list, file_name)
print(project_list)
