from controller.super_admin_controller import SuperAdminController
from controller.normal_user_controller import NormalUserController
from controller.admin_controller import AdminController
from helpers.helpers import Helpers
from models import user, project, admin
from models.project import Project
from models.admin import Admin
from models.user import User

super_admin_controller = SuperAdminController(Helpers)
normal_user_controller = NormalUserController(Helpers)
admin_controller = AdminController(Helpers)
helper = Helpers()

# admin = Admin("Adham", "Atef", "adham.atef45@gmail.com", "123456789", "000", "01098815199", 1)
# user = User("Adhwam", "Atewf", "adhwam.2atef45@gmail.com", "1234556", "000", "01098885199")
# project = Project("pro3", "pro3", 28000, "2022-2-30", "2023-5-25", "atf@gmail.com")

# super_admin_controller.create_admin(admin)
# super_admin_controller.deactivate_admin("aa@gmail.com")
# super_admin_controller.activate_admin("a@gmail.com")
# super_admin_controller.delete_admin("a@gmail.com")
# super_admin_controller.create_user(user)
# super_admin_controller.delete_user("a@gmail.com")
# super_admin_controller.register(admin,"db/admin.json")
# print(super_admin_controller.login("adham.atef45@gmail.com", "123456789", "db/admin.json"))

admin_controller.create_user(user)
# admin_controller.delete_user("adham.atef45@gmail.com")
# admin_controller.register(admin, "db/admin.json")
# admin_controller.search_by_date("2022-2-30", "atf@gmail.com")
# print(admin_controller.login("adham.atef45@gmail.com", "123456789", "db/admin.json"))

# normal_user_controller.create_project(project)
# normal_user_controller.delete_project("pro2")
# normal_user_controller.register(user,"db/user.json")
# data = normal_user_controller.view_all_projects()
# print(data)
# print(normal_user_controller.login("a@gmail.com","123","db/user.json"))
# normal_user_controller.search_by_date("2020-2-30","at@gmail.com")

# print(helper.isemail_exsist(user.email, "db/user.json"))
