import pytest

from model.project import Project
from data.add_project import testdata

@pytest.mark.parametrize("project", testdata, ids=[repr(x) for x in testdata])
def test_add_project(app, project):
    old_project = app.db.get_project_list()
    app.project.add_project(project)
    new_project = app.db.get_project_list()
    assert len(old_project) + 1 == len(new_project)
    old_project.append(project)
    assert sorted(old_project, key=Project.id_or_max) == sorted(new_project, key=Project.id_or_max)