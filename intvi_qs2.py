'''#simple
num=int(input('enter number:'))
if num>0:
    print('number positive:',num)
if num<0:
    print('number negative:',num)
if num==0:
    print('number zero:',num)

#miltiplication of numbers
master=int(input('enter master number:'))
for i in range(1,11):
    multiply=i*master
    print(i,'*',master,'=',multiply)
    print(f"{master} × {i} = {multiply}")
#random number generation & guessing the random number
import random
attempt=0
random_num=random.randint(1,100)
guess=None
while guess!=random_num:
    print(f"random_num is {random_num}")
    guess=int(input('enter number:'))
    attempt=attempt+1
    if guess > random_num:
        print('too high')
    elif guess < random_num:
        print('too low')
    elif guess == random_num:
        print(f"correct finding within {attempt} attempts")
#even odd numbers & append in a list

val={1,3,55,67,22,45}
evennum=[]
oddnum=[]
for i in val:
    if i%2==0:
        evennum.append(i)
    elif i%2==1:
        oddnum.append(i)
print(evennum)
print(oddnum)
print(len(evennum),len(oddnum))

#validate the input
inp=None
count=0
sumofnum=0
while True:
    inp=input('enter number:')
    if inp=='Done':
        break
    try:
        val=int(inp)
        sumofnum=sumofnum+val
        count=count+1
    except:
        print('invalid input')
        continue
print(sumofnum,count)


#password validation

def password_check(password):
    if len(password) < 8:
        print('password is too short')
        return False
    if not any(char.isupper() for char in password):
        print('password doesnt have char value in uppercase')
        return False
    print('password is ok')
    return True
max_attempt=3
current_attempt=0

while max_attempt >  current_attempt:
    password = input('enter password:')
    if password_check(password):
        print('correct password',password)
        break
    else:
        print('incorrect password')
        current_attempt=current_attempt+1
        print(current_attempt,'current attempt')
        continue

if current_attempt == max_attempt:
    print('max attempt reached')'''

student=input('enter student name:')
scores=[]

while True:
    score_indi_str=input('Enter score of student:')

    try:
        score_indi=int(score_indi_str)
        if score_indi > 0 & score_indi < 100:
            print('valid score')
            scores.append(score_indi)
        elif score_indi == -1 or score_indi < 0 or score_indi > 100:
            print('enter score between 0 and 100')
    except:
        print('invalid score - enter valid score')
        break
print(f"student name is {student},got scores {scores} & his average is {sum(scores)/len(scores)}")

