from model.project import Project
import random

def test_delete_project(app):
    if len(app.soap.get_project_list()) == 0:
        app.project.add_project(Project(name="для удаления"))
    old_project = app.soap.get_project_list()
    project = random.choice(old_project)
    app.project.delete_project_by_id(project.id)
    new_project = app.soap.get_project_list()
    assert len(old_project) - 1 == len(new_project)
    old_project.remove(project)
    assert sorted(old_project, key=Project.id_or_max) == sorted(new_project, key=Project.id_or_max)