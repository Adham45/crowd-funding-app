import json
import re
import datetime


class Helpers:
    def __init__(self):
        pass

    def loaddata(self, file):
        try:
            db = open(file, 'r')
            data_string = db.read()
            db.close()
            data = json.loads(data_string)
            return data
        except Exception:
            return []

    def saveData(self, file, data):
        try:
            db = open(file, 'w')
            db.write(json.dumps(data))
            db.close()
        except Exception:
            print(f"{file} Doesn't exists")

    def isString(self, item):
        if item and not item.isdigit():
            return True

        return False

    def isNumber(self, item):
        if item and item.isdigit():
            return True

        return False

    def isemail(self, email):
        email_regix = '^(\w|\.|\_|\-)+[@](\w|\_|\-|\.)+[.]\w{2,3}$'
        if email and re.match(email_regix, email):
            return True

        return False

    def ispassword(self, password, con_password):
        if password is None or con_password is None:
            return False
        if password != con_password:
            return False

        return True

    def isphone(self, phone):
        phone_regex = '^01[0125][0-9]{8}'
        if phone and re.match(phone_regex, phone):
            return True

        return False

    def isemail_exsist(self, email, file):
        data = self.loaddata(file)

        for item in data:
            if item['email'] == email:
                return "Email is Existing"

        return "Email Doesn't Exist"

    def isDate(self, date):
        try:
            if date and datetime.datetime.strptime(date, '%Y-%m-%d'):
                return True
            return False
        except ValueError:
            return False

    def istitle_exsist(self, title, file):
        data = self.loaddata(file)

        for item in data:
            if item['title'] == title:
                return True

        return False

    def printProjectData(self, project):
        print("----------------------------------")
        print(f"Title: {project['title']}")
        print(f"Details: {project['details']}")
        print(f"Total Target: {project['total_target']}")
        print(f"Start Time: {project['start_time']}")
        print(f"End Time: {project['end_time']}")
        print(f"Author: {project['author']}")
        print("----------------------------------")
