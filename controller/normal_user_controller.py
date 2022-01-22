class NormalUserController:
    def __init__(self, Helpers):
        self.helper = Helpers()

    def register(self, user, file):
        new_user = {}

        data = self.helper.loaddata(file)

        new_user['first_name'] = user.f_name
        new_user['last_name'] = user.l_name
        new_user['email'] = user.email
        new_user['password'] = user.password
        new_user['phone'] = user.phone

        try:
            if user.is_staff is not None:
                new_user['is_staff'] = user.is_staff
        except:
            pass

        try:
            if user.is_superuser is not None:
                new_user['is_superuser'] = user.is_superuser
        except:
            pass

        try:
            if user.is_admin_user is not None:
                new_user['is_admin_user'] = user.is_admin_user
        except:
            pass

        data.append(new_user)

        self.helper.saveData(file, data)
        print("Added")

    def login(self, email, password, file):
        data = self.helper.loaddata(file)
        for user in data:
            if user['email'] == email and user['password'] == password:
                return user
        return "Can't login"

    def create_project(self, project):
        new_project = {}

        data = self.helper.loaddata("db/project.json")

        new_project['title'] = project.title
        new_project['details'] = project.details
        new_project['total_target'] = project.total_target
        new_project['start_time'] = project.start_time
        new_project['end_time'] = project.end_time
        new_project['author'] = project.author

        data.append(new_project)

        self.helper.saveData("db/project.json", data)
        print("Added")

    def delete_project(self, project_title):
        data = self.helper.loaddata("db/project.json")
        for index, project in enumerate(data):
            if project['title'] == project_title:
                data.pop(index)
                self.helper.saveData("db/project.json", data)
                print(f"{project_title} Deleted")
                break
        else:
            print(f"{project_title} Doesn't exists")

    def view_all_projects(self):
        return self.helper.loaddata("db/project.json")

    def search_by_date(self, start_time, author):
        projects = self.helper.loaddata("db/project.json")

        for project in projects:
            if project['start_time'] == start_time and project['author'] == author:
                self.helper.printProjectData(project)
                break
        else:
            print("This Project Doesn't Exists")
