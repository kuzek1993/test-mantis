import pymysql.cursors
from model.project import Project



class DbFixture:
    def __init__(self, app):
        self.app = app


    connection = pymysql.connect(host="127.0.0.1", database="bugtracker", user="root", password="")

    def get_project_list(self):
        list = []
        cursor = self.connection.cursor()
        try:
            cursor.execute("select id, name from mantis_project_table")
            for row in cursor:
                [id, name] = row
                list.append(Project(id=str(id), name=name))

        finally:
            cursor.close()
        return list

    def destroy(self):
        self.connection.close()