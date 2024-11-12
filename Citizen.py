class Citizen():
    citizen_counter = 0
    def __init__(self, name="", surname="", age=0):
        self.Name = name
        self.Surname = surname
        self.Age = age
        Citizen.citizen_counter += 1

    @property
    def name(self):
        return self._name

    @property
    def surname(self):
        return self._surname

    @property
    def age(self):
        return self._age

    # Setters
    @name.setter
    def name(self, value):
        self._name = value

    @surname.setter
    def surname(self, value):
        self._surname = value

    @age.setter
    def age(self, value):
        self._age = value

    def intro(self):
        print(f'sveiki, as esu {self.Name} {self.Surname}. Man yra {self.Age} metu.')

    @staticmethod
    def class_intro():
        print("si klase yra skirta kurti pielieciu objektams")

    @staticmethod
    def class_count():
        '''
        Args:
            param1 (type): Description of the first parameter.
            param2 (type): Description of the second parameter.
            kazkas apie metoda
        :return: nieko
        '''
        print(f"Mes jau turime {Citizen.citizen_counter} pilieciu!")