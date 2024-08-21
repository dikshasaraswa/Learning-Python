print("hello world")
name="diksha"
age=23
price=25.99
print(age)
# data type in python are = int,float,string, boolean(T and F should be captial), none
# python is case sensitive and in dbms SQL is not case sensitive and python is implicit typed language, implicit typed language are those in which data type is not defined in front of the variable  * and the second type is explicit typed language(c++,java) in which datatype is defined like (int a=5;)
#tokens- punctuators,

#expression execution
# string and numeric can operate with * 
a,b=2,3
txt="@"
print(2*txt*3)
#string and string can operate with +
c,d='2',3
txtt="@"
print((c+txtt)*3)

# interger division(//) with float and int will give int displayed as float
# floor gives closest integer,which is lesser than equal to float value, result of (A//B) is same as floor(A/B)
# remainder(%) is negative when denominator is negative 

#1.string input
name=input("Enter your name: ")
print("Hello",name)
#2.integer input
age=int(input("Enter your age: "))
#3.float input
price=float(input("Enter the price: "))

#precedence -> not>and>or 
# inside if for next line 4 spaces is required 
#clever if / terary operator ---->  <var>=(false_val,true_val)[<condition>]
#type conversion 
a=5
b=3.5
print(a+b) #automatically get converted to float

#Type CAsting 
a,b=1,int("2")
#c=int(b)
sum=a+c
print(sum)

#\n->nxt line , \t->tab

# slicing 
# str[starting_idx : ending_idx ] ending idx is not included
#str[:4] is same as str[0:4], str[1:] is same as str[1: len(str)]

#string functions 
str.endswith("er.")#returns true if string ends with substr
str.capitalize() #capital 1st character
str.replace(old,new) #replaces all occurences of old with new
str.find(word) #returns 1st idx of the word
str.count(word) #returns count of word

#lists and tuples 
# in list we can store element of different type together , in python strings are  immutable but list are mutable
# immutable : can be accessed using index number but can not be updated ; mutable : can be accessed using index number + update
#list slicing same as string slicing
#1. list.append(4) , list.sort() , list.sort(reverse=True),list.reverse(), list.index(idx,el) 3:43:11

#Tuples : a built-in data type  that lets us create immutable sequences of values 
#tup.index(): returns idx of the first occurrence of element

#dictionary in python
#stores values in key:value pairs , they are unordered ,mutable(changeable) & dont allow duplicate keys
#4:24:34

dict = {
    "name" :"Diksha",
    "age" : 20,
    "subjects" :["c","java","c++"],
    "topic" : ("list","tuple","set"),
    "address": {
        "street": "123 Main St",
        "city": "New York"
    }
}

#Set in python : set is the collection of unordered items ,each element in the set is unique & immutable.
# in set we can add string, numerics, tuple but not list(bcoz list are mutable)
collection ={1,2,3,"hello","hi"}
print(collection)
print(type(collection))
print(len(collection)) #total no. of diff. values
coll = set() #empty set coll={} this is a empty dictionary 
coll.add(1)
coll.add(2)
coll.remove(1)

#loops 
#break : used to terminate the loop when encountered
#continue: terminates execution in the current iteration & contiues execution of the loop with the next iteration 
#pass is a null statement that does nothing .it is used as a placeholder for future work.(5:56:49)

# functions in Python : Block of statements that perform a task , functions reduces redancy in code 
def cal_sum(a,b):
    return a+b
sum = cal_sum(4,5) # function call
print(sum)

# both lines to be printed in a single line 
print("hello", end ="") #sep=" "
print("world") #end ="\n"

def cal_prod(a=1,b=1):#default values , (a=1,b) is not valid ,(a,b=1) is valid , default value are given from last
    print(a*b)
    return a*b
cal_prod()

#recursion : when a function calls itself repeatedly
def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n-1)
print(factorial(5))

def show(n):
    if(n==0):
        return 
    print(n)
    show(n-1)
    print("end")
    