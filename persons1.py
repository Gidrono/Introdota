class Person:
    def __init__(self, name, job, salary, gender="male"):
        self.name = name
        self.job = job
        if gender=="female":
            self.salary = salary*0.72
        else:
            self.salary = salary
        self.gender = gender
    def get_raise(self, n):
        self.salary+=n*self.salary
    def __str__(self):
        return f'{self.name} is a {self.gender} who works as a {self.job} and earns {self.salary}'
class Person:
    def __init__(self, name, job, salary, gender="male"):
        self.name = name
        self.job = job
        if gender=="female":
            self.salary = salary*0.72
        else:
            self.salary = salary
        self.gender = gender
    def get_raise(self, n):
        self.salary+=n*self.salary
    def __str__(self):
        return f'{self.name} is a {self.gender} who works as a {self.job} and earns {self.salary}'

class Manager(Person):
    def __init__(self, name, job, salary, gender="male"):
        Person.__init__(self, name, job, salary, gender="male")
    def get_raise(self, n, bonus=0.1):
        self.salary+=n*self.salary+bonus*self.salary
        #self.salary+=bonus*self.salary
donald = Manager('Donald Duck', 'sailor', 500, 'male')
donald.get_raise(0.1, 0.2)
print(donald.salary)