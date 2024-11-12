from Citizen import Citizen
from Student import Student

print(Citizen.citizen_counter)

pilietis = Citizen("Jonas", "Jablauskas", 114)
print(Citizen.citizen_counter)

pilietis2 = Citizen("Vytis", "Nemuninskas", 106)
print(Citizen.citizen_counter)


print(pilietis.Name)

pilietis.intro()
pilietis2.intro()

Citizen.class_intro()

Citizen.intro(pilietis)


Citizen.class_count()

studentas = Student("Naglis", "Mockevičius", 34, "Gyvenimo mokykla")

print(studentas)

Citizen.class_count()

studentas.intro()