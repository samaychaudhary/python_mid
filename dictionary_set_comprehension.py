"""
# dictionary
syntax1 : {append_item for loop}
syntax2 : {i: ("even" if i%2==0 else "odd") for loop)
0) intro>>> create dictionary in one line."""

# odd even without comprehension
user_number = int(input("enter a number"))
def oddeven(any_number):
    odd_even_numbers = {}
    for i in range(0,any_number+1):
        if i%2==0:
            odd_even_numbers[i]="even" 
        else:
            odd_even_numbers[i]="odd"
    return odd_even_numbers
ok = oddeven(user_number)
print (ok)

#square without comprehension
num = int(input("enter a number"))
def square(number):
    square_number = {}
    for i in range(0,num+1):
        square_number[i] = i**2
    return square_number
anything = square(num)
print (anything)



# using dictionary comprehension
num = int(input("enter a number"))
def oddeven(any_number):
    return {i:"even" if i%2==0 else "odd" for i in range(0,num+1)}
ok = oddeven(num)
print (ok)

#eg : "samay"

user_name = input("enter a name")
def count_char (any_name):
    characters = {}
    for i in user_name:
        if i in any_name:
            characters[i] = any_name.lower().count(i)
    return characters
ok = count_char(user_name)
print (ok)

#using dictionary comprehension
user_name = input("enter a name")
def count_char (any_name):
    return{i:any_name.lower().count(i) for i in user_name}
ok = count_char(user_name)
print (ok)

# set comprehension
user_number = int(input("enter a number"))
def square_number(any_num):
    return{i**2 for i in range(0,user_number+1)}
ok = square_number(user_number)
print (ok)

# in tuples
number = int(input("enter a number"))
def square(any_num):
    return{(i,i**2) for (i) in range(0,number+1)}
ok = square(number)
print (ok)

a,b = input("enter 5 names: ").split(',')
name_list = [a,b]

def first_letter(name):
    letter = {}
    for i in name:
        letter = i[0]
    return letter
        
    
ok = first_letter(name_list)
print (ok)

