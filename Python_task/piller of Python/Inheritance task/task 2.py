class Person:
    def __init__(self):
        self.name="Rahul"
        self.age=41
    def display_info(self):
        print("\nName:",self.name)
        print("Age:",self.age)


class Doctor(Person):
    def __init__(self):
        Person.__init__(self)
        self.specialization="Neurologist"
    def diagnose(self):
        Person.display_info(self)
        print("Specilization:",self.specialization)
        print("A neurologist specializes in diagnosing and treating disorders \nof the nervous system, including the brain, spinal cord, and nerves.")

class Patient(Person):
    def __init__(self):
        Person.__init__(self)
        self.disease="Parkinson's Desease"
    def treatment(self):
        Person.display_info(self)
        print("Disease:",self.disease)
        print("Parkinson's disease is treated with medicines like Levodopa and\n Carbidopa that help control movement-related symptoms.")

d=Doctor()
p=Patient()
d.diagnose()
p.treatment()

