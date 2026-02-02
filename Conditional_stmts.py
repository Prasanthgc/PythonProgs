# new for DEc2025
x=10
if(x==1):
    print('x is equal to 1')
if(x==2):
    print('x is equal to 2')
print('thats all')

#try and except block - sample , for any sort of exceptions (Generic handling)

x='pap'
try:
    y=int(x)
except:
    y=-1
print(y)

x=5
while (x>1):
    x=x-1
    print('x inside lop',x)
print('x outside loop',x)

#break continue block
while True:
    x=input('>>>')
    if x=='quit':
        break
    elif x=='continue':
        print('continue')
        continue
print('out block')

#identify larget number + sum of values + count of values
basic=0
large=0
sum=0
f=[1,33,22,100,99,2,4]
for i in f:
    basic=basic+1
    sum=sum+i
    print(basic,i,sum)
#print(basic,sum,'largest')
    if i > large:
        large=i
        print(large,i)
print('total:',basic,'largest:',large,'sum:',sum)

#identify smallest number - tricky (use none value)
small=None
f=[422,323,222,100,929,112,412]
for i in f:
    if  small is None or i < small:
        small=i
        print(small,i)
print('samllest:',small)

################
pra = 34
while pra > 0:
    print("valid", pra)
    pra = pra - 1
print("lost")

x=200
y=2009
#If loop & else if
if x>y:
    print('x is big')
elif x==y:
    print('y is bigger')
else:
    print('mopodu')
#For loop & break & continue
arrayval=[1,2,3,4,5,6,7,8,9]
stringval="false"
for x in stringval: #arrayval:
    if x=='a': #x==4:
      # continue -- pause at 4 & continue rest
      #break - put break at the mentioned value
        break
    print(x)
for x in range(1,10): #range function - inbuild function
    if x==7:
        break
    print(x)