class employee_record:
    def __init__(self, name, experience):
        self.name = name
        self.experience = experience

    def display(self):
        if self.experience >=2:
            print(self.name + ' has ' + str(self.experience) + ' years of experience.')

employee1 = employee_record("John Doe", 2)
employee2 = employee_record("Abhraham Lincoln", 1.5)

employee1.display()
employee2.display()
