print("hello world!")


my_var = "variable"

# no undefined
print(my_var)

my_var = 4
print(my_var)

MY_CONSTANT_VARIABLE = 10 
MY_CONSTANT_VARIABLE = 9 

#every piece of data in python is an object  
#this is the same as javascript

print(type(my_var))
#strictly backend
#serve on front end? need templates 

#booleans are the same as JS but you need capitalization 

#null is NONE in python, same as null  
my_var = None 

#python has normal math operations like JS + - * // % ** 

#no ternary operators  
# if yes left side if no right side in JS but in python has a different syntax

#takes conditional and puts it in the middle
#beverage = 'Beer' if age >=21 else 'Milk'

#how to convert values in python - what are the out of box functions? 

'''
quote 

'''
string = '''multi 
line
string
'''
#different is that beginnign of string is touching the quotes 
print(string)

#what is the lsit method? is it like split? 
#list('abcd')
#dot index  - 
# dot upper() dot lower()

#what's a built in fucntion? What is a method on the isntance of the calss that are wealing 

# everything in pyhton is an object  

#in JS what did control flow dictate? was it order of operations? 

#turhy or falseey? #what is falsy in python? is false none zero  empty range

# == no tripel equals in python 

#hello or 0 0 or hello 
#false and true is false -- hello and 0 is 0 

#control flow
#how does python use indnetaiton? how does it bypass squiggly brackets? how do you branch iwth if statement? 

floor = "sticky"
walls ="clean"
if floor =="sticky":
    print("clean the floor, its sticky")
    if walls =="sticky":
        print("clean the walls!")
        
color =input('Enter "green", "yellow", "red": ').lower()
print(f'The user entered {color}')


if color == "green": 
    print('go')
elif color == "yellow":
    print('slow')
elif color == "red":
    print('stop')
else:
    print ('uh-oh')