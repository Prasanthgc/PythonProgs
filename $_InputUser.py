x=input('press the lift floor')
#y=int(x)+23
print('go to the mentioned flow',x)

#scenario
score = input("Enter Score: ")
sc=float(score)
if sc >=0.9:
    print('A')
elif sc>=0.8:
    print('B')
elif sc>=0.7:
    print('C')
elif sc>=0.6:
    print('D')
elif sc<0.6:
    print('F')
elif sc>1.0:
    print('outofrange')
#string values
f='mystring'
secval=f[2]
capture=[]
for i in f:
    capture.append(i)
    print(i)
print(secval,capture)