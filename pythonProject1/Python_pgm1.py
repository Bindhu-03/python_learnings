#functions
"""Create a sum() it can take 2 arguments to perform sum operation"""
"""def sum(a,b):
    print(a+b)
a=int(input("enter your num: 2"))
b=int(input("enter your num: "))
sum(a,b)"""

#Write a python function to sum all the numbers in a list
#sample list=[8,2,3,0,7]
#expected output:20


'''def sum(number):
    total = 0

    for i in number:
        total=total+i
    print(total)
number=[8,2,3,0,7]
sum(number)'''

#write a pgm to multiply elemnts in th list
'''def mul(number):
    total = 1

    for i in number:
        total=total*i
    print(total)
number=[8,2,3,7]
mul(number)'''


#write a function to print even numbers from given list
#sample input=[1,2,3,4,5,6,7,8,9]
#expected output:[2,4,6,8]

'''def even_num(lst):
    l=[]
    for i in lst:
        if i%2==0:
            l.append(i)
    print(l)
lst=[1,2,3,4,5,6,7,8,9]
even_num(lst)'''


#write a program function to covert a decimal num to binary num

'''def deci_to_bin(num):
    if num>1:
        deci_to_bin(num//2)
    print(num%2,end="")
deci_to_bin(21)
'''

#Return() keyword: it returns the output,
# whenever you are using return(), call the function using print function
'''def deci_to_bin(num):
    if num>1:
        deci_to_bin(num//2)
    return(num%2)
print(deci_to_bin(21))'''

'''sum=10
def f1(x):
    return x+sum
print(f1(5))'''

#return():-return is a special keyword that can be used inside a function or metho to send tha function result back to the caller.
#type("hello")
#len("hello")
#above two operations just return the value but will not display any output to the screen
'''def f1(x):
    print(x)
f1(10)

def f2(x):
    return x
print(f2(10))'''

"""what is the purpose of return()?"""
#when you return the value you can decide what you gonna do with the value

'''x=len(input("enter your string"))
print(x**2)
'''
'''def f1(x):
    print(x)    #-->10
print(f1(10)) '''  #-->outputs none
#why we are getting none?
'''whenever I use print(x) and the argument is given f1(10),then the 10 will gets to the f1(x) place and it 1st prints the 10'''
# '''once we call the arguments it returns back to the caller(parameter x).,m ,.and prints in the print(x) function and now it is empty in the function,hence it returns none'''

'''def f1(x):
    return(x)
print(f1(10))'''

'''sum=10
def fun_sum(x):
    return x+sum
print(fun_sum(100))'''

"""sum=10"""
'''def fun_sum(x):
    a=x+sum
print(fun_sum(100)) ''' #outputs none
#here the value is not returning back to the caller ,if  we use a return statement inside the function the it gives the output value


'''sum=10
def fun_sum(x):
    a= x+sum
    return a
print(fun_sum(100))'''
# here it gives the value as it return the vallue of a to the caller and the it prints the value of a


#Write a program to print sum of range of numbers.
# sample input:7
#expected output: 28

'''Num=int(input("Enter you num: "))
sum=0
for i in range(0,Num+1):
    sum=sum+i
print(sum)'''


'''
Num=int(input("Enter you num: "))
sum= sum(range(1,Num+1))
print(sum)'''


# LIST COMPREHENSION:-
'''It offers you a smaller line of code that you can create a new list from the existing list '''

# print the fruits with letter "A" in it and sore in in the new list

'''list_fruits=['kiwi','Apple','grapes','cherry','banana','anar']
new_list=[]
for i in list_fruits:
    if "A" in i:
        new_list.append(i)
print(new_list)
'''

'''list_fruits=['kiwi','Apple','grapes','cherry','banana','anar']
#new_list=[items(i) for items(i) in collection_name]
new_list=[x for x in list_fruits if "e" in x]
print(new_list)

new_list=[x for x in list_fruits if "B" in x]
print(new_list)
'''
# Print the new_list without "banana"
'''list_fruits=['kiwi','Apple','grapes','cherry','banana','anar']
new_list=[x for x in list_fruits if x != 'banana' and 'Apple']
print(new_list)
'''
# create list of numbers from 0 to 20?
'''nums=[]
for i in range (21):
  nums.append(i)
print(nums)'''

'''nums=[x for x in range(21)]
print(nums)'''

# from above if we want only even numbers
'''nums=[x for x in range(21) if x%2==0]
print(nums)'''

'''NOTE:So,list comprehension can offer shorter syntax and also it is time efficient.'''

# create a list  of numbers in range of 20
# expected output must be multiples of 2
'''nums=[x*2 for x in range(21)]
print(nums)'''

# LAMBDA FUNCTION:
'''It is an anonymous function'''
'''anonymous function means it does not have any name'''
'''when you have to create a function'''
# syntax of lambda function is:
'''lambda arguments:expression'''
'''so lambda function is an anonymous function,it can have many arguments and single expression'''

# what is an expression?
'''Expression is some kind of stmt/calculation/step using that values to give single value/output '''

# Lambda is an anonymous function,then how can you call it?
'''we generally use this funcation where it has some name.
we can create a variable to call this function'''
'''x=lambda a:a+10
# when you are calling the lambda function use the variable name
print(x(5))
'''
'''x=lambda a,b,c:a+10&b+10&c+10
print(x(a:5,b:6,c:7))  #it outputs nothing

x=lambda a,b,c:a+10 or b+10 or c+10
print(x(a:5,b:6,c:7))   ##it outputs nothing
'''
'''x=lambda a,b,c:a+b+c
print(x(5,6,7))  #prints 18'''

# when we can use lambda function?
'''create a function that can give square of every number'''
'''def square(x):
    return x**2
def cube(x):
    return x**3
def four(x):
    return x**4
def sqrt(x):
    return x**0.5
print (square(4))
print (cube(4))
print (four(4))
print (sqrt(4))'''

# here for every operation expression is same i.e (**),argument is also same
# here only values are changing i.e (2,3,4,0.5)
'''if we have single expression and multiple arguments the instead of creating function we can use lambda function'''

'''def power(n):
    return lambda a:a**n
square=power(2)
cube=power(3)
four=power(4)
sqrt=power(0.5)
print(square(4))
print(cube(4))
print(four(4))
print(sqrt(4))'''

# try lambda function to multiplication
'''def mul(n):
    return lambda a:a*n
two=mul(2)
three=mul(3)
four=mul(4)
print(two(5))
print(three(5))
print(four(5))'''

#here for every operation expression is same i.e (**),argument is also same
#here only values are changing(2,3,4,0.5)
#if we have single expression and multiple arguments instead of creating function,we can use lambda function.

#Global and Local variables:
'''global-declared outside the function'''
'''global variables are more powerful than local variables'''
'''global are permanent variables whereas local are temporary variables'''
'''x="amazing"
def f():
    return x
print(f())'''

#what is local variable?
'''local variables are created inside the function'''
'''Local variable is temporary and it only lasts inside the function'''
'''def f():
    x='fantastic'
    return x
print(f())
print(x)'''

# NOTE:Even if the variable names are same, the local variables never affect the global variables.

# Map() function:-
# what map() fuction does?
'''it uses a function on iterables(collections-lists,tuples,sets,arrays,dict)'''
'''map() will take a function and run it over the iterables'''
'''functions are the class objects i.e one function can act as an argument fir anotehr function'''
"""--->syntax: Map=(function_name,iterables)"""

# calculate length of certain fruits
'''a=['apple','banana','cherries','pineapple']
length=[]
for i in a:
    length.append(len(i))
print(length)'''

# do same above operation using list comprehension
'''a=['apple','banana','cherries','pineapple']
l=[len(i) for i in a]
print(l)'''

#using map() function
'''a=['apple','banana','cherries','pineapple']
length=map(len,a)
print(length)'''#---> if you want to diaplay the output by using map(),then we need to decide in which collection /iterables
# the output has to be,means if u want to display the output using map() then you need to mention the collection infront of map().
# ex:
'''a=['apple','banana','cherries','pineapple']
length=list(map(len,a))
print(length)'''

'''a=['apple','banana','cherries','pineapple']
def f1(x):
    return "hello "+x
print(f1(apples)) '''  #-->outputs hello apples

#if i wnt to apply this function on all the itemd on above list
'''l=list(map(f1,a))
print(l)
'''

#when we have to us map()?
'''if you are having multiple user input collections,then we can use map() function.'''

'''user=input()
print(user)
print(type(user))'''#--->it returns as a string

#if i want to seperate the values :
'''use split() function'''
'''user=input().split()
print(user)
print(type(user))'''

'''user=input().split()
print(user)
print(type(user))

# how to convert this string of elements into integers
numbers=[]
for x in user:
    numbers.append(int(x))
print(numbers)
print(type(numbers))'''

'''user=input().split()
number=tuple(map(int,user))
print(number)'''

'''number=tuple(map(int,input().split()))
print(number)'''

#NOTE:before executing a map(),we need to decide the collection in which we need the output.

#how can we print the following 10 20 30 40 50 as double of them thatto in tuple collection
'''lambda: you can have many arguments but a single expression'''

'''number=tuple(map(int,input().split()))
double=tuple(map(lambda a:a*2,number))
print(double)'''

'''double=tuple(map(lambda a:a*2,tuple(map(int,input().split()))))
print(double)'''

# map(int(input().split()))--->map storing entire thing/data,if we want to be in a readable object,then we needtoa dd collections i.e,tuple or list or set

#filter():
'''syntax: collection_name(filter(function,iterable))'''
'''filter() gives output of the collection'''
'''age=[18,48,31,24,16,56,35,45,12,14,18,20]
def adult(x):
    if x>=18:
        return x
f1=list(filter(adult,age))
print(f1)
print(adult(20))--->it outputs 20
print(adult(16))---->it outputs None as it is not satisfying condition'''

#write above program using lambda function
'''age=[18,48,31,24,16,56,35,45,12,14,18,20]
f1=list(filter(lambda a:a>=18,age))
print(f1)'''

#how can i get more expression when i am using conditional statements
'''using logical operators'''

#can we use logical operators in lambda?-->YES
'''age=[18,48,31,24,16,56,35,45,12,14,18,20]
f1=list(filter(lambda a:a>=20 and a<=30,age))
print(f1)'''

'''age=[18,48,31,24,16,56,35,45,12,14,18,20]
f1=list(filter(lambda a:18<=a<=30,age))
print(f1)'''

#List comprehension
#lambda
#map()
#filter()
#along with sending one function as argument to another function

'''filter() basically filters your original collection that returns True or False, 
any value that comes out to be True,the original value can be stored as a collection(list,tuple,set) of items'''

'''map() returns all the values whereas filter() returns only the values which are True.'''

'''age=[18,48,31,24,16,56,35,45,12,14,18,20]
def adult(x):
    if x>=18:
        return x
m1=list(map(adult,age))
print(m1)''' #--->prints the age value if condition is True else it prints None.

#Regular expressions:-
'''It is a built in package '''
'''which is also calles as "re".'''
'''A RegEx or regular expression is a sequence of characters that forms a search patter.'''

'''import re
txt='Hello World!'
#search whether World! is present or not
x=re.search("World!$",txt)
print(x)'''

#regular expression functions:
'''1.findall()-->returns a list containing all the matches
   2.search()--->returns a match object
   3.split()--->returns a list
   4.sub()--->used to replace one or many matches with the string'''
