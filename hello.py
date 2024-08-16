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

