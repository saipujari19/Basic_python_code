#saiprasad pujari
#Once you have completed the Employee class,
#program that creates three Employee objects to hold the following data:
class Person:
    """Represents a person with a name and phone number."""

    def __init__(self, name, phone, age, gender):
        self.name = name
        self.phone = phone
        self.age = age
        self.gender = gender
class Employee(Person):
    """Extends Person with age, gender, ID number, department, and job title."""
    def __init__(self, name, phone, age, gender, id_number, department, job_title):
        super().__init__(name, phone, age, gender)
        self.id_number = id_number
        self.department = department
        self.job_title = job_title
    def display(self):
        """Prints the employee's details."""
        print(f"Name: {self.name}")
        print(f"Phone: {self.phone}")
        print(f"Age: {self.age}")
        print(f"Gender: {self.gender}")
        print(f"ID Number: {self.id_number}")
        print(f"Department: {self.department}")
        print(f"Job Title: {self.job_title}")
        print("\n")
def main():
    # Creating and displaying three Employee objects
    employees = [
        Employee("Susan Meyers","212-555-1212",35,"male",47899,"Accounting","Vice President"),
        Employee("Mark Jones","212-555-2468",18,"female",39119,"IT","Programmer"),
        Employee("Joy Rogers","212-555-9753",25,"male",81774,"Operations","Engineer")
    ]

    for employee in employees:
        employee.display()

if __name__ == "__main__":
    main()


