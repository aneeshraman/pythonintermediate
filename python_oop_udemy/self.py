class Employee:
    def __init__(self):
        self.name = "Mathew"

    def employeeDetails(self):
        print("Name = ", self.name)
        age = 30
        print("Age = ", age)

    def printEmployeeDetails(self):
        print("Printing in another method")
        print("Name: ", self.name)
        print("Age: ", age)


employee = Employee()
employee.employeeDetails()
# Employee.employeeDetails(employee)
employee.printEmployeeDetails()
