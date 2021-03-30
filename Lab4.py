#Adalysa Rosales
#Lab 4
#3/30/2021

class Employee:
    def __init__(self, employee_name, employee_number):
        self.__employee_name=employee_name
        self.__employee_number=employee_number

    def set_employee_name(self, employee_name):     #setters
        self.__employee_name=employee_name

    def set_employee_number(self, employee_number):
        self.__employee_number=employee_number

    def get_employee_name(self):     #getters
        return self.__employee_name

    def get_employee_number(self):
        return self.__employee_number

class ProductionWorker(Employee):
    def __init__(self, employee_name, employee_number, shift_number, hourly_rate):
        Employee.__init__(self, employee_name, employee_number)
        self.__shift_number=shift_number
        self.__hourly_rate=hourly_rate

    def set_shift_number(self, shift_number):       #setters
        self.__shift_number=shift_number

    def set_hourly_rate(self, hourly_rate):
        self.__hourly_rate

    def get_shift_number(self):     #getters
        return self.__shift_number

    def get_hourly_rate(self):
        return self.__hourly_rate

def main():
    print('Enter Employee Data... ')
    employee_name=input('Enter employee name: ')
    employee_number=input('Enter employee number: ')
    shift_number=input('Enter shift number: ')
    hourly_rate=input('Enter hourly rate: ')

    employee=ProductionWorker(employee_name, employee_number, shift_number, hourly_rate)

    print('Employee Information: ')
    print('Name: ', employee.get_employee_name())
    print('Number: ', employee.get_employee_number())
    print('Shift Number: ', employee.get_shift_number())
    print('Hourly Rate:', employee.get_hourly_rate())
main()