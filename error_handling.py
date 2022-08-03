# ERROR HANDLING


#1 SYNTAX ERROR

from itertools import tee


def fun():
    print ("done")

name = "kritika"
print (name)


#2 indentation error   #use tab

def fun():
    print ("sth")

#3) name error >> not defined prevousily

#print (ok)    "ok is not defined"  #name error it is

ok = 0
print (ok)

#4) type error
#print (1 + "a")



#5)index error
list = [1,2,3]
#print (list[5])  #error as 5 ma kei chaina tyaaaaaa

#6) value error
#s=B
m="9"
#print (int(s))  #as int kept here and s is string

#7) attribute error
list=["a","b"]
list.append("c")  #if we keep anything else like pop and tya chaina bhane error attribute error

#8) key errror
dic = {"name":"apple"}
print (dic["name"])  #here it is name if i keep age and age chaina mathi so error


#>>>>>>> Raise error

class ChalNikalError(TypeError):
    pass

def add(a,b):
    if (type(a)==int and type(b)==int):
        return a+b
    raise ChalNikalError("not int datatype")

print (add(2,3))
#print (add("2","3"))   #raise error for this




def divide(a,b):
    try:
        print (a/b)
    except ZeroDivisionError as zero_error_mssg:
        print(zero_error_mssg)
        raise ZeroDivisionError ("dont divide by 0")
    except TypeError as te:
        print(te)
        raise TypeError("input int only")
    except:
        return("unexpected error")

#print(divide(1,0))  #shows error of zero division
print(divide(4,2))
print(divide(4,1))