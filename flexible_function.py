"""
>>>> flexible function

*operator or *args or *kwargs"""

#*arg"""              #unlimited values can be provided. 

# args takes values in tuples
"""def sum(a,b):
    return a +b 
print(sum(3,4))

def another_sum(*args):       #*kritika is args, which means unlimited arguements can be taken. not like before that we need to specify how many we need to take.
    print (args)
    print (type(args))
print (another_sum(2,3,4))  """  #unlimited values provided


"""def calculator(*args):
    sum=0
    for i in args:
        sum+=i
    return sum 
print(calculator(2,4,2))"""



"""def calculator(num1,*args):     #first paramter then only args
    sum=0 +num1
    for i in args:
        sum+=i
    return sum 
print(calculator())




a = int(input("enter numbers")).split(',')
def calculator(num1,*args):
    for i in num1:"""
        
# list = [3,4,5,6]
# print (sum(*list))

"""# the power will be given by user. 
power_number = int(input('enter a number'))
list_num = [3,4,5,6]

def cube(power_num,*args):
    cube_list = []
    for i in args:
        cube_list.append(i**power_num)   #list ma append garnu parcha 
    return cube_list
print (cube(power_number,*list_num))     # *denotes unpacking of everyone


# the power will be given by user.
power_number = int(input('enter a number'))
list_num = [3,4,5,6]
def to_power(num,*args):
    if args:
        return [i**num for i in args]
    else:
        return "you did not pass args"
print (to_power(power_number,*list_num))"""
        

# unsupported operand type bhaneko string lai multiply garna lageko bhane




"""
**KWARGS
double star denotes kwargs
0) intro
>>>about the problem and solution of function for *kwargs(convensions)
"""
# kwargs takes values in dictionary

#kwargs keeps everything in dictionary

from pickle import FALSE
from re import U


def sum_all_num(**kwargs):     #kwargs = key word args
    print (type(kwargs))
    print (kwargs)
print (sum_all_num(first_name = "aryama", last_name = "sharma"))       # key = value


def details(**kwargs):
    print (kwargs)
    for key,value in kwargs.items(): # esle dictionary ma rakhcha so .items le ekai choti key ra value nikalna milcha
        print (f"{key}:{value}")

print (details(first_name = "kritika", last_name = "deo"))



def add(**kwargs):
    sum = 0
    for value in kwargs.values():       #for dict use . hufieg
        sum = sum+value
    return sum

dict = {"a":1, "b":2, "c":3}
print (add(**dict))


#3) function with all type of parameter (PADK)  = (parameter, arguement, default argument, kwargs)

def user_info (name, *args, address = "unknown" , **kwargs):
    print (name)
    print (args)
    print (address)
    print (kwargs)
    
user_info ("maharshi",1,2,4,address = "ktm", p=12, q=13)




list_of_names = ["kritika","aryama","rushav","samay"]
is_reverse = False

def upper_case (namelist,**kwargs):
    ''' to reverse you must give {is_reverse = False} .../..........'''   #doc string
    if kwargs.get("is_reverse"):            #gives values 
        return [name[-1::-1].title() for name in namelist]
    else:
        return [name.title() for name in namelist]
    
print (upper_case(list_of_names,is_reverse = True))
print(upper_case.__doc__)

# print(len.__doc__)
# print(max.__doc__)
# print(sorted.__doc__)
# print(range.__doc__)

# doc le mssg dincha for every function. and hamle afno function ko lagi euta mssg deko.

