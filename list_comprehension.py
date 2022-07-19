"""
>>>>>list comprehension
syntax1 : [append_item for loop]
syntax2 : [append_item for loop if (condition)]
syntax3 : [append_item if (condition) else -i ------ for loop]

user_number = int(input("enter a number"))

def square(any_num):
    square_list = []
    for i in range(1,any_num+1):
        square_list.append(i**2)
    return square_list

ok = square(user_number)
print (ok)

# same thing as up in small way. 
def same_square(n):
    return[i**2 for i in range(1,n+1)]
print(same_square(10))

"""
given_list = ["abc","def","ghi"]

def first_letter(any_letter):
    first_letter_from_list = []
    for i in any_letter:
        first_letter_from_list.append(i[0])
    return first_letter_from_list

ok = first_letter(given_list)
print (ok)
    
def first_letterr(n):
    return[i[0] for i in given_list]
print (first_letter(given_list))

"""# homwework
def reverse(no):
    return[i[-1::-1] for i in given_list]
print (reverse(given_list))"""

#even from list comprehension
def filter_even(num):
    return[i for i in range(num+1) if (i%2==0)]
print (filter_even(10))

def oddeven(num):
    return[i*2 if (i%2==0) else (-i) for i in range(num+1)]
print (oddeven(10))   

# nested loop
example = [[1,2,3],[1,2,3],[1,2,3]]

def nested_loop(num):
    return[ [m for m in range(1,num+1)] for k in range(1,num+1)]
print (nested_loop(3))



def reverse(no):
    return[i[-1::-1] for i in given_list]
print (reverse(given_list))