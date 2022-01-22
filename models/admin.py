from models.user import User


class Admin(User):
    def __init__(self, f_name, l_name, email, password, con_password, phone, is_staff=0, is_superuser=0,
                 is_admin_user=1):
        super().__init__(f_name, l_name, email, password, con_password, phone)
        self.is_staff = is_staff
        self.is_superuser = is_superuser
        self.is_admin_user = is_admin_user
