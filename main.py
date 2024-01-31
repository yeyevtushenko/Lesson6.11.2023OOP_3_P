class User:
    def __init__(self, name, age, email):
        self.__name = name
        self.__age = age
        self.__email = email

    def get_name(self):
        return self.__name

    def get_age(self):
        return self.__age

    def get_email(self):
        return self.__email

    def set_name(self, new_name):
        self.__name = new_name

    def set_age(self, new_age):
        self.__age = new_age

    def set_email(self, new_email):
        self.__email = new_email



user1 = User("John Doe", 18, "john@doe123gmail.com")


print("Ім'я:", user1.get_name())
print("Вік:", user1.get_age())
print("Email:", user1.get_email())


user1.set_name("John Doe")
user1.set_age(19)
user1.set_email("john@doe123gmail.com")


print("\nІм'я (після змін):", user1.get_name())
print("Вік (після змін):", user1.get_age())
print("Email (після змін):", user1.get_email())