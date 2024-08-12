class Person:

    def __init__(self, name, weight, gender, height, age, salary):

        self.name = name
        self.weight = weight
        self.gender = gender
        self.height = height
        self.age = age
        self.salary = salary




    def display_info(self):
        print(f'name: {self.name}')
        print(f'weight: {self.weight}')
        print(f'gender: {self.gender}')
        print(f'height: {self.height}')
        print(f'age: {self.age}')
        print(f'salary: {self.salary}')
    
    def have_birthday(self):
        self.age  += 1
        print(f'birthday: {self.age}')

    def dis_salary(self):
        print(f'new salary: {self.salary}')

person1 = Person('kewald',68,'M',6,18,1000)

person1.display_info()

person1.have_birthday()

person1.dis_salary()