#dec2025

def firstFUnct(x,y):
    print('adding in second function ',x+y)
    print('& finishing 2nd function')

def secondFUnct(a,b):
    addition=a+b
    subtraction=a-b
    print('calling 2nd function')
    firstFUnct(addition,subtraction)
    print('completing first function')
    return subtraction #for return test

def thirdFUnct(a,b):
    add=a+b
    return add

secondFUnct(20,10)
print('finishing the sample nested function')
print('return test',thirdFUnct(2,3),secondFUnct(20,10))

def computepay(h, r):
    if h<=40:
        return h*r
    elif h>40:
        return (40*r+((h-40)*(1.5*r)))

hrs = input("Enter Hours:")
rate=input("rate:")
h=float(hrs)
r=float(rate)
p = computepay(h, r)
print("Pay", p)

'''
def samplefunct(x,y):
    #x=21
    #y=22
    print(x+y)

samplefunct(21,22)
#samplefunct(44,33)

def arg_func(in_func):
    z=in_func
    print(z)

arg_func(samplefunct(2,3)) #pass function as argument of another function

#list - same as array in other techs but cant store mixed datatypes but in python we can store mixed dtypes
list_sample=['ABC',30,30.1]
for x in list_sample:
    print(x)

#SAmple of function as arguments :
def func1(x,y):
    c=x+y
    print(c)

def func2(inval,func1): #You can give different name
    funvar=inval+2
    print(funvar)
    func1(funvar,1)

func2(2,func1) #makesure call with actual function name'''