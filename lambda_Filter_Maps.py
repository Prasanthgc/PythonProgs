#Best thing in labda is - it can be invoke immediatly i.e in same line
def even_num(x):
    for n in range(2,x):
        if x%n==0:
            return True
        else:
            return False
Y=filter(even_num,range(15))
print(list(Y))
#is simplified version of function in single line
x=lambda a:a+10
y=x(2)
print(y)
#Nested Lambda function
x=lambda a,b:a+b(a)
print(x(10,lambda a:a*a))
#Map_filter
list_num=[2,4,6,8]
print(list(map(lambda a:a*2,list_num)))
print(list(filter(lambda a:a*1==2,list_num)))

def lam_fun(x):
   d= lambda a:a+x
   return d
ab=lam_fun(5)
print(ab(4))


#normalFunction
def norm_func(x):
    y=x+10
    return y
cr=norm_func(10)
print("normal Output",cr)
#lambdafunction: writes function in simplest way : lambda <variables/arguments = <exporession>
x=lambda a:a+10
print("lambda_output" ,x(10))

#can be invokked like below as well
(lambda x,y:x+y) (5,2)