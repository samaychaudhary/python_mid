def decorator_function(any_function):
    def wrapper_function(*args,**kwargs):
        print('This is extra function')
        return any_function(*args,**kwargs)
    return wrapper_function

def decorator_function2(any_function):
    def wrapper_function(*args,**kwargs):
        print("this is extra function")
        return any_function(*args,**kwargs)
    return wrapper_function

#extra line>>>'this is extra function'

def fun1():
    print ("function1")

#extra line>> this is extra function

@decorator_function     #using whole decorator function here.  
def func2(any_value):
    print (f"function with {any_value}")

func2(5)


@decorator_function2
#this function adds two and returns one. 
def add_two_num(num1,num2):
    return num1+num2
add_two_num(3,5)      #doesnt print like this
print (add_two_num(3,5))    #prints..



#importing module





from functools import wraps
def decorator_function3(any_function):
    @wraps(any_function)             #for seeing doc of any_function which is add
    def wrapper_function(*args,**kwargs):
        '''this is wrapper function'''
        print ("this is extra function")
        return any_function(*args,**kwargs)
    return wrapper_function

@decorator_function3
def add(a,b):
    '''this is add function'''
    return a+b

add(2,3)
print (add(2,4))
print (add.__name__)
print (add.__doc__)   #print the doc string of wrapper function (problem)


from functools import wraps
def show_function(any_function):
    @wraps(any_function)              
    def wrapper_function(*args,**kwargs):
        '''this is wrapper function'''
        print (f"you are calling {any_function.__name__} function ")
        return any_function(*args, **kwargs)
    return wrapper_function

@show_function
def add(a,b):
    '''this is add function'''
    return a+b
print (add(3,2))
print(add.__doc__)





#finding time difference
import time as t
t1=t.time()
print (t1)
for i in range(100,10000,100):
    print (i)
t2 = t.time()
total_required_time=t2-t1
print (f"total_required_time is {total_required_time}")




#time difference to run the program
def show_time(any_function):
	def wrapper_function(*args,**kwargs):
		''' this is wrapper function '''
		print(f"Executing func {any_function.__name__}")
		t1= t.time()
		returned_value=any_function(*args,**kwargs)
		t2= t.time()
		total_time = t2-t1
		print(f"This func took {total_time} time")
		return returned_value
	return wrapper_function

@show_time
def sq_finder(n):
	return [i**2 for i in range(1,n+1)]

sq_finder(500)

    
# decorator practice

#@only_int_allowed

def only_int_allowed(any_function):
    @wraps(any_function)
    def wrapper_function(*args,**kwargs):
        stored_data_type = []
        for arg in args:
            stored_data_type.append(type(arg)==int)    #stores true or false in stored_data_type .. true if it is int else false
        if all(stored_data_type):
            return any_function(*args,**kwargs)
        else:
            print("only int is allowed")
    return(wrapper_function)

@only_int_allowed
def add_func(*args):
    total = 0
    for i in args:
        total += i
    return total
print (add_func(1,2,3,4,[5,6,7]))






#same as above in one line
def only_int_allowed(any_function):
    @wraps(any_function)
    def wrapper_function(*args,**kwargs):
        if all([type(arg)==int for arg in args]):
            return any_function(*args,**kwargs)
        else:
            print ("only int allowed")
    return (wrapper_function)

@only_int_allowed
def add_func(*args):
    total = 0
    for i in args:
        total += i
    return total
print (add_func(1,2,3,4,[5,6,7]))




# decorator practice 4

def which_data_allow(data_type):   #now the same program is inside this function. so we can write data types.
    def only_int_allowed(any_function):
        @wraps(any_function)
        def wrapper_function(*args,**kwargs):
            if all([type(arg)==data_type for arg in args]):
                return any_function(*args,**kwargs)
            else:
             print ("only int allowed")
        return (wrapper_function)
    return only_int_allowed

@which_data_allow(int)   #now we can check int wala.....
def string_join(*args):
    joined_string = ""
    for i in args:
        joined_string += i
    return joined_string

print(string_join("kritika","deo"))


