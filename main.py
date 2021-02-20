########################################################################################################################

# #1 Classes and Instances

# Empty class: without constructor, attributes and methods
# The pass keyword is used to specify that the class is empty

class Employee:
    pass


# Instantiating Employee class
employee_one = Employee()
employee_two = Employee()

print(employee_one)
print(employee_two)
print('')

# On python, you can create attributes at runtime
employee_one.first_name = 'Leonardo'
employee_one.last_name = 'Sibela'
employee_one.email = 'Leonardo.Sibela@company.com'
employee_one.pay = 5000

print("employee_one first name: " + employee_one.first_name)
print("employee_one last name: " + employee_one.last_name)
print("employee_one email: " + employee_one.email)
print("employee_one pay: " + employee_one.pay.__str__())
print('')


# A better option would be to define the attributes in your class
# On Python, there is nothing like { } to define the scopes. The indentation itself does that.
# There is not something as ; to represent the end of a instruction.
class Employee:
    def __init__(self):
        self.first_name = ''
        self.last_name = ''
        self.email = ''
        self.pay = 0


employee_three = Employee()

employee_three.first_name = 'Marta'
employee_three.last_name = 'May'
employee_three.email = 'Marta.May@company.com'
employee_three.pay = 6000

print("employee_three first name: " + employee_three.first_name)
print("employee_three last name: " + employee_three.last_name)
print("employee_three email: " + employee_three.email)
print("employee_three pay: " + employee_three.pay.__str__())
print('')


# Another option would be to define the attributes in your class' constructor
# On python, the constructor is a magic method called __init__ and you should always define a first parameter
# that will be the object itself. This is true for any method you create in a class. On languages such as Kotlin
# or Java you do not need to specify this parameter but you can use it by calling the keyword this.
# Although the name does not matter, it's a convention to call this parameter self.
class Employee:
    def __init__(self, first_name, last_name, pay):
        self.first_name = first_name
        self.last_name = last_name
        self.pay = pay
        self.email = first_name + "." + last_name + "@yourcompany.com"


# You don't pass the first parameter self
employee_four = Employee('Billy', 'Joel', 50000)

print("employee_four first name: " + employee_four.first_name)
print("employee_four last name: " + employee_four.last_name)
print("employee_four email: " + employee_four.email)
print("employee_four pay: " + employee_four.pay.__str__())
print('')


# The keyword to create a function in Python is def, which is short for “define” (define a function).
# Just like any method within a class, we must specify the first parameter as being self.
class Employee:
    def __init__(self, first_name, last_name, pay):
        self.first_name = first_name
        self.last_name = last_name
        self.pay = pay
        self.email = first_name + "." + last_name + "@yourcompany.com"

    # On Python, you do not need to specify the type your function returns
    def full_name(self):
        return '{} {}'.format(self.first_name, self.last_name)


employee_five = Employee('Bill', 'Gates', 100000)
print("employee_five full_name(): " + employee_five.full_name())


########################################################################################################################

# #2 Class Variables

# Python has a concept that you can either alter a parameter for a single object or you can alter it for all instances
# Let's create a parameter called raise and alter it for all instances and them for a single object

class Employee:
    default_raise_amount = 1.04

    def __init__(self, first_name, last_name, pay):
        self.first_name = first_name
        self.last_name = last_name
        self.pay = pay
        self.email = first_name + "." + last_name + "@yourcompany.com"
        self.employee_raise_amount = 1.04

    # On Python, you do not need to specify the type your function returns
    def full_name(self):
        return '{} {}'.format(self.first_name, self.last_name)

    def apply_default_raise(self):
        self.pay = int(self.pay * self.default_raise_amount)

    def apply_raise(self):
        self.pay = int(self.pay * self.employee_raise_amount)


employee_six = Employee('Luiz', 'Amaral', 10000)
employee_seven = Employee('Sofia', 'Faria', 10000)

# Applying the default raise amount
employee_seven.apply_raise()
employee_six.apply_raise()
print("employee_six after a default (1.04) raise_amount: " + str(employee_six.pay))
print("employee_six after a default (1.04) raise_amount: " + str(employee_six.pay))

employee_six.pay = 10000
employee_seven.pay = 10000

# Changing the class attribute (for all instances)
Employee.default_raise_amount = 1.05
employee_six.apply_default_raise()
employee_seven.apply_default_raise()
print("employee_six after a raise amount changed to (1.05) raise_amount: " + str(employee_six.pay))
print("employee_seven after a raise amount changed to (1.05) raise_amount: " + str(employee_seven.pay))

employee_six.pay = 10000
employee_seven.pay = 10000

# Changing the instance attribute (for the that instance only)
employee_six.employee_raise_amount = 1.06
employee_six.apply_raise()
employee_seven.apply_raise()
print("employee_six after a raise amount changed to (1.06) raise_amount: " + str(employee_six.pay))
print("employee_seven without changing it's raise amount (1,04): " + str(employee_seven.pay))


########################################################################################################################

# #3 Classmethods and Staticmethods

# Staticmethods
# It's basic a method that should output the same value for every instance.
# To do so, you must use a decorator called staticmethod (it's analogous to annotation in Java).

class Employee:
    default_raise_amount = 1.04

    def __init__(self, first_name, last_name, pay):
        self.first_name = first_name
        self.last_name = last_name
        self.pay = pay
        self.email = first_name + "." + last_name + "@yourcompany.com"
        self.employee_raise_amount = 1.04

    # On Python, you do not need to specify the type your function returns
    def full_name(self):
        return '{} {}'.format(self.first_name, self.last_name)

    def apply_default_raise(self):
        self.pay = int(self.pay * self.default_raise_amount)

    def apply_raise(self):
        self.pay = int(self.pay * self.employee_raise_amount)

    @staticmethod
    def is_work_day(date): return date.weekday == 5 or date.weekday == 6


employee_eight = Employee('Marco', 'Polo', 1000)
employee_nine = Employee('Freddie', 'Mercury', 10000)

import datetime

some_saturday = datetime.date(2021, 2, 13)
print('employee_eight calling static method is_work_day(): ' + str(employee_eight.is_work_day(some_saturday)))
print('employee_nine calling static method is_work_day(): ' + str(employee_nine.is_work_day(some_saturday)))


# Classmethods
# You can think of a class method as a static method that needs to be aware of it's own class.
# This is a concept better understand with a example.
#
# Let's say that in your system it's common to create a Employee instance from a string of data separated by hyphens.
# You can create a method that split those values into variables and return a new instance like so:
# return Employee(first_name, last_name, pay). However, you are explicit writing the name of the class.
# That is not interesting because once you change the class name, you must also change this line of code.
# Also, you cannot do something like return self(first_name, last_name, pay).
# Whoever, a static method allow you to receive automatically a class as parameter (without the need to pass it and
# by convention called cls) and with that variable you can create and return a new instance of the class;

class Employee:
    default_raise_amount = 1.04

    def __init__(self, first_name, last_name, pay):
        self.first_name = first_name
        self.last_name = last_name
        self.pay = pay
        self.email = first_name + "." + last_name + "@yourcompany.com"
        self.employee_raise_amount = 1.04

    # On Python, you do not need to specify the type your function returns
    def full_name(self):
        return '{} {}'.format(self.first_name, self.last_name)

    def apply_default_raise(self):
        self.pay = int(self.pay * self.default_raise_amount)

    def apply_raise(self):
        self.pay = int(self.pay * self.employee_raise_amount)

    @staticmethod
    def is_work_day(date): return date.weekday == 5 or date.weekday == 6

    @classmethod
    def from_string(cls, employee_string):
        first_name, last_name, pay = employee_string.split('-')
        return cls(first_name, last_name, pay)


employee_ten = Employee.from_string('Kelvin-Klein-900000')
print(employee_ten.__dict__)


# classmethods are commonly used to create additional constructor

########################################################################################################################

# #3 Inheritance - Creating Subclasses

# On the OOP world, it's common to create a class that has some functionalities and data that is also presented on
# another class. Let's say for example that we realize that some Employees are managers and some are developers
# and both will have specific methods and parameters, but they should also be able to have all the existing methosa
# and parameters present in the employee class. To avoid creating those to classes and duplicating those data on the
# more specific classes (manager and developer), we can use inheritance and reuse them like this:


class Employee:
    default_raise_amount = 1.04

    def __init__(self, first_name, last_name, pay):
        self.first_name = first_name
        self.last_name = last_name
        self.pay = pay
        self.email = first_name + "." + last_name + "@yourcompany.com"
        self.employee_raise_amount = 1.04

    # On Python, you do not need to specify the type your function returns
    def full_name(self):
        return '{} {}'.format(self.first_name, self.last_name)

    def apply_default_raise(self):
        self.pay = int(self.pay * self.default_raise_amount)

    def apply_raise(self):
        self.pay = int(self.pay * self.employee_raise_amount)

    @staticmethod
    def is_work_day(date): return date.weekday == 5 or date.weekday == 6

    @classmethod
    def from_string(cls, employee_string):
        first_name, last_name, pay = employee_string.split('-')
        return cls(first_name, last_name, pay)


# This is the way to specify that the Developer class is a subclass of Employee in Python
class Developer(Employee):
    default_raise_amount = 1.10  # Overriding the default_raise_amount value

    # Creating the default constructor with one more parameter and calling the super constructor (from Employeee class)
    def __init__(self, first_name, last_name, pay, programing_language):
        super().__init__(first_name, last_name, pay)
        self.programing_language = programing_language


developer = Developer('John', 'Doe', 10000, 'Python')
developer.apply_default_raise()

print('developer pay after a 10% default raise amount: ' + str(developer.pay))


class Manager(Employee):

    def __init__(self, first_name, last_name, pay, employees=None):
        super().__init__(first_name, last_name, pay)
        if employees is None:
            self.employees = []
        else:
            self.employees = employees

    def add_employee(self, employee):
        if employee not in self.employees:
            self.employees.append(employee)

    def remove_employee(self, employee):
        if employee in self.employees:
            self.employees.remove(employee)

    def print_employees(self):
        for employee in self.employees:
            print('--> ', employee.full_name())


manager = Manager('Sue', 'Smith', 9000, [developer])
manager.add_employee(employee_ten)
manager.print_employees()

manager.remove_employee(developer)
manager.print_employees()

# Python has two useful functions: isinstance() and issubclass()

# Let us know that manager is instance of Manager
print('Is manager instance of Manager? ' + str(isinstance(manager, Manager)))

# Let us know that developer is not instance of Manager
print('Is developer instance of Manager? ' + str(isinstance(developer, Manager)))

# Let us know that Developer class is subclass of Employee
print('Is Developer subclass of Employee? ' + str(issubclass(Developer, Employee)))

# Let us know that Developer class is not subclass of Manager
print('Is Developer subclass of Employee? ' + str(issubclass(Developer, Manager)))

########################################################################################################################

# #4 Special (Magic/Dunder) Methods

# On Python there are some special methods called Magic Methods (some also say Dunder for Double Underscore)
# Those special methods allows to emulate some built in behavior within Python and it's also how we implement
# operator overloading. When your hear someone saying dunder init, they mean init surrounded by double underscore

# Let's see how the + operator works with two Integers and two Strings:

# The behavior when we add two Integers together, they add the two values together
print(1 + 2)

# The behavior when we add two Strings together, they concatenate the two values
print('a' + 'b')

# Depending on the object, the addition has different behaviour


# When we print out an employee, it just shows us the class and the memory position this object is in
print(employee_one)


# One of the things we can do with those magic methods is to change this behavior


class Employee:
    default_raise_amount = 1.04

    def __init__(self, first_name, last_name, pay):
        self.first_name = first_name
        self.last_name = last_name
        self.pay = pay
        self.email = first_name + "." + last_name + "@yourcompany.com"
        self.employee_raise_amount = 1.04

    # On Python, you do not need to specify the type your function returns
    def full_name(self):
        return '{} {}'.format(self.first_name, self.last_name)

    def apply_default_raise(self):
        self.pay = int(self.pay * self.default_raise_amount)

    def apply_raise(self):
        self.pay = int(self.pay * self.employee_raise_amount)

    @staticmethod
    def is_work_day(date): return date.weekday == 5 or date.weekday == 6

    @classmethod
    def from_string(cls, employee_string):
        first_name, last_name, pay = employee_string.split('-')
        return cls(first_name, last_name, pay)

    # Used to find the “official” string representation of an object
    def __repr__(self):
        return "Employee('{}', '{}', '{}')".format(self.first_name, self.last_name, self.pay)

    # used to find the “informal”(readable) string representation of an object
    def __str__(self):
        return "'{}' - '{}')".format(self.full_name(), self.email)

    # The return value of str() depends on two these two methods:
    # __str__ being the default choice and __repr__ as a fallback


employee_eleven = Employee('Mark', 'Schafer', 50000)
print(employee_eleven)


# When you add two integers together, what is actually being called is the __add__ method from the int class
print(1 + 2)
print(int.__add__(1, 2))


# When you "add" two strings together, what is actually being called is the __add__ method from the int class
print('a' + 'b')
print(str.__add__('a', 'b'))


class Employee:
    default_raise_amount = 1.04

    def __init__(self, first_name, last_name, pay):
        self.first_name = first_name
        self.last_name = last_name
        self.pay = pay
        self.email = first_name + "." + last_name + "@yourcompany.com"
        self.employee_raise_amount = 1.04

    # On Python, you do not need to specify the type your function returns
    def full_name(self):
        return '{} {}'.format(self.first_name, self.last_name)

    def apply_default_raise(self):
        self.pay = int(self.pay * self.default_raise_amount)

    def apply_raise(self):
        self.pay = int(self.pay * self.employee_raise_amount)

    @staticmethod
    def is_work_day(date): return date.weekday == 5 or date.weekday == 6

    @classmethod
    def from_string(cls, employee_string):
        first_name, last_name, pay = employee_string.split('-')
        return cls(first_name, last_name, pay)

    def __repr__(self):
        return "Employee('{}', '{}', '{}')".format(self.first_name, self.last_name, self.pay)

    def __str__(self):
        return "'{}' - '{}')".format(self.full_name(), self.email)

    # We are overriding the behavior of the add function for the Employee class
    def __add__(self, other):
        return self.pay + other.pay


employee_twelve = Employee('Sarah', 'Connor', 100000)
employee_thirteen = Employee('Felix', 'Kjellberg', 1000000)

# The + sign is now adding the two salaries together
print(employee_twelve + employee_thirteen)

# You can find more special arithmetics methods at
# https://docs.python.org/3/reference/datamodel.html#emulating-numeric-types


# Another example we will work with is the len method, that display the length of something

print('The lenght of the characters strings is ' + str(len('Characters')))
two_size_array = ['First', 'Second']
print('The lenght of the two_size_array is ' + str(len(two_size_array)))


# Now let's override the len method of employee to return the number of characters in the employee full name

class Employee:
    default_raise_amount = 1.04

    def __init__(self, first_name, last_name, pay):
        self.first_name = first_name
        self.last_name = last_name
        self.pay = pay
        self.email = first_name + "." + last_name + "@yourcompany.com"
        self.employee_raise_amount = 1.04

    # On Python, you do not need to specify the type your function returns
    def full_name(self):
        return '{} {}'.format(self.first_name, self.last_name)

    def apply_default_raise(self):
        self.pay = int(self.pay * self.default_raise_amount)

    def apply_raise(self):
        self.pay = int(self.pay * self.employee_raise_amount)

    @staticmethod
    def is_work_day(date): return date.weekday == 5 or date.weekday == 6

    @classmethod
    def from_string(cls, employee_string):
        first_name, last_name, pay = employee_string.split('-')
        return cls(first_name, last_name, pay)

    def __repr__(self):
        return "Employee('{}', '{}', '{}')".format(self.first_name, self.last_name, self.pay)

    def __str__(self):
        return "'{}' - '{}')".format(self.full_name(), self.email)

    def __add__(self, other):
        return self.pay + other.pay

    def __len__(self):
        return len(self.full_name())


employee_fourteen = Employee('Nick', 'Fury', 7000)
print("The number of characters on \"Nick Fury\" (including the spece) is " + str(len(employee_fourteen)))
