# what is file handling?
'''handling a certain file which is not python'''
'''ex:pdf,json file,xcel,..'''

'''to handle a file in python we require an in-built function.
These in-built functions are also called as open function'''

'''While you are handling the file we will have 4modes: r,a,w,x
r-read mode
a-append mode
w-write mode
x-execute mode'''

# x-mode:
'''it is used to create a new file.'''
# f=open('trail.txt','x')

# w-mode---->over write mode
'''f=open('trail.txt','w')
f.write("Applying write mode to my file,"
        "if i write one more time my content can be overwritten")
f.close()'''

# r-->read mode-->to read the content in file
# by default when u use the open()function it is in read mmode.
'''f=open('trail.txt','r')
print(f.read())
f.close()'''

# write mode:-
'''f=open('trail.txt','w')
f.write("i am over writing my content in the file"
        "so the previous content can be over written ")
f.close()'''

# a mode:-append mode:
'''f=open('trail.txt','a')
f.write(" I am adding extra content at the end of the existing content.")
f.close()'''

# read the file
'''f=open('trail.txt')
print(f.read())
f.close()'''

# iterators:divides a data into small size of chains
'''instead of for loop,if loop u can use iterators'''




# GENERATORS in python:
'''is a function which returns an iterator that produce a sequence of values when iterated over.'''

#when we have to use this generators?
'''wehn u want to produce large sequence of values but we dont want to store all of them in the memory at once'''

#to create a generator use a keyword "def"
# #and instead of "return" use the "yield"

'''def my_generator(n):
    value=0
    #loop until the counter is less than n
    while value<n:
        yield value
        value += 1
#iterate over your generator to generate sequence of values
for value in my_generator(9):
        print(value)'''

"""NOTE: when u r using integer directly into for loop. it throws an error use it with range function"""
"""when you are using generators then instead of return use 'yield'
it supports int object in for loop"""

# Pickling:
'''conversion of 2D data format to 1D data and store it and in same conversion 1D data into 2D is known as pickling. '''
'''pickle converts the 2 dimensional line data into 1 dimensional points data'''
'''The process of converting at any type of object in python 
ex:list,tuple,set,arrays into bytes is known as pickling'''
"""when it comes to python thse pickling conversion is known as 'serialisation','deserialisation'"""
"""serialisation:-converting 2D to 1D
Desearialisation:- converting 1D into 2D"""
#1D-SERIAL DATA(points)
#2D-Data frames(lines)
#3D-Panels

#what are bytes?
'''0's and 1's are known as bytes'''

# c,cpp are low-level languages
# python,jave are high-level languages.

'''to do the pickling we need to use package called 'pickle' '''
import pickle
# open a pickle.txt
pickle_file=open("pickle2.txt","wb")#wb-work and bytes
# use pickle.dump command to dump the file
# pickle.dump(collection_name,pickle_file(where you want to store))

#in the above step you dump the data in to serialisation

#if you want to read or visualize the real data then
'''my_dict={'1':"a","2":"b"}
pickle.dump(my_dict,pickle_file)
#open the file
pickle_file=open("pickle2.txt","rb")
#load the data that you have stored
new_dict=pickle.load(pickle_file)
print(new_dict)'''

"""steps:-"""
# step1: import the pickle library
# step2: creating a pickle file in "work and byte(wb)"mode by default
# step3: use "pickle.dump" to convert the data
# step 4:if you want to read the actual data by using--->open("pickle filename","rb")
# step5: after that load the data into new_file
# step6: print the file


# pip:
"""it is a package manager for python package or module"""  # packages are nothing but libraries

# what is package?
"""package is basically something that contains all the files you needed."""
"""so packages contain all the files that you need for certain modules"""
"whenever you want to install extra libraries then we need to use 'pip' package"
# what is a module?
"""modules are code libraries which you can include in your project"""

# NumPy
# Pandas
# matplotlib and seaborne
# pendulum
# python image processing
# movie py
# Tkinter
# pyqt
# py32
# pytest

# how to install these packages?
"""py -m pip install "package_name" when you use CMD"""
"""!pip install "package_name"--> colab notebook and jupyter notebook"""
# what is global package and local package?
"""global package:-packages which u install in cmd
local package:-packages which u install in any ide"""

'''import camelcase
x=camelcase.CamelCase()
a="hi there! this is the message to check whether each word of the letters are capitalized"
print(x.hump(a))'''

# how to uninstall package from cmd?
"""py -m uninstall 'package_name'"""
# how to check the installed packages on your system?
""" use command 'py -m pip list' in cmd"""
# how to upgrade the pip?
"""use command 'py-m pip install --upgrade pip' in cmd"""
# how to check the version of pip?
"""use command 'py -m pip --version' in cmd"""

# json:
"""java script object notation"""
"""it is basically a syntax that is used for storing and exchanging
of data"""
"""used for data transmission in web applications"""
# it does not have indexes

"""{"first_name":"bindhu",
    "last_name":"reddy"
    "address:"{street:2,xyz colony,
               "city":hyd}"""
# json have dictionaries inside a key-value pairs i.e  a clumsy data


# to create a json file we need to import a json
'''import json
# what is parse?
"""it is a method where one string of data is converting into another form of data"""
person={'name':'bindhu',
        'language':['eng','french']}
print(type(person))
# converting this into json format--->use dumps
person_dict = json.dumps(person)
print(person_dict)
print(type(person_dict))
# here dict file is converted into json file using dumps()'''


# let's open json file by using "with open"
import json
loc="C:\\Users\\bindhu reddy\\Downloads\\example_1.json"
with open(loc) as f:  # here we are giving file location as a reference to f
        data = json.load(f)  # json.load() used to convert the loaded file into dictionary
print(data)
print(type(data))


# data structures:
# linked list
# hash maps
# trees
# arrays
