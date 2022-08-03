
# """>>>>>>>>>>>>Enumerate functions
# >>>>> we use it with for loop to track the position of our item in iterable or loop"""

#0)track the position without enumerate function:

list_of_names = ["kritika", "aryama","rushav","samay"]

position = 0
for i in list_of_names:
    print(f"the name {i} is in {position} position")
    position +=1
print (position)


#this in short 
#USING ENUMERATE

for loc,name in enumerate(list_of_names):       #enumerate gives location and name of the list/tuples
    print (f"the name {name} is in {loc} position")


#exercise 1 >>>
# a list containing many strings name and find the position of one target string from the list. (dynamic)"""


"""list_of_names = ["kritika", "aryama","rushav","samay"]
def find_name(name_list,target_name):
    for position,name in enumerate(name_list):
        if name == target_name:
            print (position)
        

ok = find_name(list_of_names, "samay")
print (ok) 
"""


"""
>>>>>>>>MAP function

it is iterators. so we can use loop in map object but only one time

task1: return the list of square num from the list with >> normal way, list comprehension, def function with lambda ani normal"""


num_list = [1,2,3,4]   #iterables list  by default iterable


def square(a):
    return a**2 
# oko = square(num_list)
# print (oko)

#iterator - >> loop chaulana milne        esma milcha last ma OR cha and FOR ma ni so chalcha 
#iterable >>>> loop chalauna na milne


k_ho = map(square,num_list)    #iterator

for i in k_ho:
    print (f"k_ho>>>>{i}")


 #using lambda                                                 # map for like combining everything...iterating...no need to make a function..or call it or anything
k_ho = list(map(lambda a:a**2, num_list))        #lambda we use to denote any anonymous whole function. 
print (k_ho)




#why do we use map and lambda?


"""
>>>>>>>>>>>> ITERATOR VS ITERABLE
-----------------------------------------------------
 for i in square:
    print (i)


#how loops work in this iterator?"""

"""num_list = [1,2,3,4]      #iterables
#iter() >>>>> iterator ma convert garne

iterator_converted = iter(num_list)      #converting to iterator
print(next(iterator_converted))
print(next(iterator_converted))
print(next(iterator_converted))
print(next(iterator_converted))"""

# this is how iterator works.. next will goo on till we break it using break function.


"""
>>>>>>>>>>FILTER FUNCTIONS
------------------------------
IT IS ITERATORS:
"""

# TASK 1 : return the list of even numbers from the list with >> normal way, list comprehension,

#normal way
num_list = [1,2,3,4,5,6,7,8]
def even(a):
    list_even = []
    for i in a:
        if i%2==0:
            list_even.append(i)
    return list_even
ok = even(num_list)
print (ok)

#using comprehension
def even_numbers(a):
    return[i for i in a if i%2==0]
print (even_numbers(num_list))

# using map and lambda
evenn = print (list(map(lambda a:a%2==0, num_list)))
evenn = print (tuple(map(lambda a:a%2==0, num_list)))
evenn = print (set(map(lambda a:a%2==0, num_list)))





def filter_even2(list):
    return [i for i in list if i%2==0]
ok = filter_even2(num_list)
print (ok)


def even_func(i):
    return i%2==0
even_list = tuple(filter(even_func,num_list))
print (even_list)

#one line
even_list2 = list(filter(lambda a: a%2==0, num_list))
print (even_list2)


#map and filter is same,
#we use map for boolean output
#we use filter for actual output


char_list = ["a","b","c"]
num_list = [1,2,3,4,5,6,7,8]

print (list(zip(char_list,num_list)))
print (dict(zip(char_list,num_list)))

small_char_list = ["a","b","c"]
num_list = [1,2,3,4,5,6,7,8]
big_char_list = ["A","B","C","D"]

print (list(zip(small_char_list,num_list,big_char_list)))
#print (dict(zip(small_char_list,num_list,big_char_list)))      # error 
# BECAUSE DICTIONARY CAN ONLY BE PRINTED WHEN ONLY TWO ARE GIVEN. ESMA THREE CHA SO NO DICTIONARY.

# ZIP LE DUITA LAI ADD GARERA ORDERLY DINCHA


l = list(zip(small_char_list,big_char_list))
print (l)

# for un-zip
l1, l2 = zip(*l)    #unzip * is unpacking
print (l1)
print (l2)

"""
1) ask a num with user: filter odd or even store in list>>>zip it>>> and add max value into new list from pairs"""

user_number =int(input("enter a number"))
def oddeven(a):
    odd_list = []
    even_list = []
    for i in range(0,a+1):
        if i%2==0:
            even_list.append(i)
        else:
            odd_list.append(i)
    return odd_list,even_list
ok1,ok2 = oddeven(user_number)       #two list so here should also be two.

ziplist = list(zip(ok2,ok1))
print (ziplist)

ok2,ok1 = zip(*ziplist)
print (ok1)


#same mathi wala
user_number =int(input("enter a number"))
def oddeven(a):
    odd_list = []
    even_list = []
    for i in range(0,a+1):
        if i%2==0:
            even_list.append(i)
        else:
            odd_list.append(i)
    return [max(pair) for pair in zip(odd_list,even_list)]
print(oddeven(user_number))


#2) define a fun which take many list: (lambda function) such as [1,2,3] [4,5,6] [7,8,9] and return avg of (1+4+7/3)

l1 = [1,2,3]
l2 = [4,5,6]
l3 = [7,8,9]

def average(*args):
    zipped = list(zip(l1,l2,l3))
 #   for i in zipped:






#>>>>>>>>>>>>> Any and ALL function

# all>> true if all the items are true
#any> 

num_list1 = [2,3,6,8,10]
num_list2 = [1,3,5,7,9]

even_list = [True, True, True , True]

#print(all(even_list))         #output true because all are true there

def check_even(list):
    even_list = []
    for i in list:
        even_list.append(i%2==0)
    return even_list

print (any(check_even(num_list1)))
print (all(check_even(num_list1)))

print (all([num%2==0 for num in num_list1]))


#if all true then in function all it is true...if using any, whatever is there and even single is true returns as true.


#practice of all and any

def sum(*args):
    if all([(type(arg) == int or type(arg) == float) for arg in args]):
        total = 0
        for num in args:
            total+=num
        return total
    else:
        return"input a float or a integer value"
print(sum(1,2,3,4))





    