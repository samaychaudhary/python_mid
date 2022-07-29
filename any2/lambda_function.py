"""
>>> anonymous function

def add(a,b):
    return a+b
SYNTAX:
lambda param1,param2 : returning_values

actually, we dont assign lambda function into variable
we use it with built in function.. builtin, map, reduce, filter(later we study)"""


def add(num1,num2):
    return num1+num2

print (add(2,5))

lambda p1,p2,p3 : p1+p2+p3
sum_num = lambda p1,p2,p3 : p1+p2+p3
print (sum_num(1,2,3))
print (sum_num)

lambda p1: p1%2==0 
even = lambda p1: p1%2==0 
print (even(12))



