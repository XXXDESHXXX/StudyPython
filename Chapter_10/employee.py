class Employee:
    def __init__(self, name, identifier, department, post):
        self.__name = name
        self.__identifier = identifier
        self.__department = department
        self.__post = post

    def get_name(self):
        return self.__name

    def get_identifier(self):
        return self.__identifier

    def get_department(self):
        return self.__department

    def get_post(self):
        return self.__post

    def set_name(self, name):
        self.__name = name

    def set_identifier(self, identifier):
        self.__identifier = identifier

    def set_department(self, department):
        self.__department = department

    def set_post(self, post):
        self.__post = post

    def __str__(self):
        return f'{self.__name}, {self.__post}, {self.__department}, {self.__identifier}'
