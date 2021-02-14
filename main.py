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
    first_name = ''
    last_name = ''
    email = ''
    pay = 0


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
# On python, the constructor is a special method called __init__ and you should always define a first parameter
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
