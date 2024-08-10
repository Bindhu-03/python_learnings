# classes and objects:
# why we are creating the classes and objects?


# how to create a class?
'''To create a class use a keyword called "class"'''
'''class customer:
    pass
# object creation
c1=customer()
print(c1)
'''
# what is __main__?
'''it is nothing but from which file the class is coming from'''
'''nthg but a file where the cls is coming from'''

# Attributes:
"""the attributes can be 2 types:
1.class attribute: come from class and these attributes are accessible by every object.(common 
/shared attributes)
2.object attribute: these object attributes are unique attributes that can be applicable to particular object."""

#create a class
'''class customer:
    # create class attributes-->creating variables inside the class
    Bank_name="HFC BANK"
    Branch="Mumbai"
    State="Maharastra"
    IFSC_code="HFC000023"

# create an object
c1=customer()
c2=customer()
# how can an object access the class attributes
print(c1.Bank_name)
print(c2.IFSC_code)
'''
# create methods for class customer
# what is methods?
'''methods can be created inside the class.'''
'''methods are nothing but creating functions inside the class.'''

class customer:
    # create class attributes-->creating variables inside the class
    Bank_name="HFC BANK"
    Branch="Mumbai"
    State="Maharastra"
    IFSC_code="HFC000023"
    '''before crating the object attributes we need to initiate object attributes inside the class.'''
    def __init__(self,name,age,initial_amount,acc_no):
        #what is __init__?
        '''when u create an object by default it runs with __init__method--->initialising method'''
        self.name=name
        self.age=age
        self.initial_amount=initial_amount
        self.acc_no=acc_no
    # creating methods
    def welcome(self):
        print(f"Hello {self.name},Welcome to {self.Bank_name},{self.Branch}")
    def check_balance(self):
        print(f"Your current balance is {self.initial_amount}")

    def deposit(self,amount):
        self.initial_amount +=amount #-->initial_amount=initial_amount+amount
        print(f'Your transaction is completed.'
              f'{amount} has been credited to your bank account {self.acc_no}.'
              f'The updated balance is {self.initial_amount}')
    def withdraw(self,amount):
        if amount<=self.initial_amount:
            self.initial_amount -= amount
            print(f'Your transaction is completed.'
                f'{amount} has been debited from your bank account {self.acc_no}'
                f'The updated balnce is {self.initial_amount}')
        else:
            print("Insufficient balance")
            self.check_balance()
# create an object
c1=customer("Python",28,10000,9876543210)
c2=customer("Jaanu",22,32000,1234567890)
# how can we access particular methods
c1.welcome()
c1.check_balance()
c1.deposit(10000)
c1.withdraw(25000)

c2.withdraw(5000)
'''if you want to use a method, you have to mention the object name first
and then mention the method.'''
# how can an object access the class attributes
print(c1.Bank_name)
#print(c2.IFSC_code)

# how can an object access object attributes?
print(c1.initial_amount)
# what is self?
'''it is an extra parameter in a method definition'''
# class.method(object)
'''self act as a pointer or reference to access the object'''
'''when we are creating a function we need to call arguments,but when u are creating method
u should not call any arguments,so we use self()'''

# STEP1----> Create a class-->"customer-->in a bank project
# STEP2--->Create an object by using variables
'''ex: c1=customer()'''
# STEP3--->Creating class attributes inside the class-->these are common/shared attributes
# STEP4--->How to access the class attributes by particular object
'''print(c1.Bank_Name)'''
# STEP5--->Created the methods inside the class which are nothing but functions inside class
'''ex:welcome(),check_balance(),deposit(),withdraw()'''
# STEP6--->how to access particular method by particular object
'''ex:c1.welcome(),c1.deposit()'''


# class
# object
# methods
# inheritance
'''The child object can acquire all the properties and behaviour of parent object'''
# polymorphism
'''One task can be performed in many ways'''
# data abstraction
'''data abstraction and encapsulation both are like synonyms.'''
'''used to hide the internal details and show only the functionalities'''
# encapsulation
'''restricting the use of unnecessary data in the methods'''
