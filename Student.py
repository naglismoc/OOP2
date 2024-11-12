from Citizen import Citizen


class Student(Citizen):
    def __init__(self, name="", surname="", age=0, university=""):
        super().__init__( name, surname, age)
        self.University = university

    @property
    def university(self):
        return self._university

    @university.setter
    def university(self, value):
        self._university = value

    def __str__(self):
        return f"Student(Name: {self.Name}, Surname: {self.Surname}, Age: {self.Age}, University: {self.University})"