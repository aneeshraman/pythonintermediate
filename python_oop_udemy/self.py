class Employee:
    def employeeDetails(self):
        self.name = "Mathew"
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
