""" 6 modes in file handling
r - Read
w- Write
a - Append
r+ - Read and then write
w+ - Write and then read (Use seek(0) to move reader to start of file)
a+ - append and then read (use seek(0))
Usage of with , you need not use file.close option explicitly
with open(<file>,'mode') as <var>: """
#for reading 10th/n line of a file without opening it
import linecache
line = linecache.getline('/Users/pcinthamani/Desktop/Partner Team Management/Python_learning/employee_data_100.csv', 10)
print(line,end=" ")

#block 1 : for desotn open the file it jus has the content of list as file name , so need
   # explicit read()
count=0
filelist=['/Users/pcinthamani/Desktop/Partner Team Management/Python_learning/Details_Learning.txt','/Users/pcinthamani/Desktop/Partner Team Management/Python_learning/employee_data_100.csv']
#fname=input("Enter the filename: ")
for i in filelist:
    fh = open(i,'r')
    print(fh.read(), end=" ")
    count = count + 1
print(count)

#block 2: here file itself opened and given to for loop , which takes the first line of file ,
#    so no read() needed
count = 0
with open('/Users/pcinthamani/Desktop/Partner Team Management/Python_learning/Details_Learning.txt', 'r') as file_write:
    for i in file_write:
        #if i.startswith('I'):
            print(i,end=" ")
            count = count + 1
print(count)

count = 0
with open('/Users/pcinthamani/Desktop/Partner Team Management/Python_learning/Details_Learning.txt', 'r') as file_write:
    for i in file_write:
        if i.startswith('I'):
            print(i,end=" ")
            count = count + 1
print(count)
#use enumerate for the row number against the result
count = 0
with open('/Users/pcinthamani/Desktop/Partner Team Management/Python_learning/employee_data_100.csv', 'r') as file_write:
    for line_num, i in enumerate(file_write, 1):
        if not 'Arjun Singh' in i:
            print(f"{line_num}: {i}", end="")
            count = count + 1
print(f"\nTotal: {count}")

#use enumerate for the row number against the result
count = 0
with open('/Users/pcinthamani/Desktop/Partner Team Management/Python_learning/employee_data_100.csv', 'r') as file_write:
    for line_num, i in enumerate(file_write, 1):
        if not 'Arjun Singh' in i:
            print(f"{line_num}: {i}", end="")
            count = count + 1
print(f"\nTotal: {count}")

file_assign=open('C:/Users/pcinthamani/Desktop/Partner Team Management/Python_learning/Works/Python_sample.txt','r')
#Opens file in read mode
print(file_assign.read()) #Full read
print(file_assign.readline()) #Full read
print(file_assign.readline()) #add readline to read as much as lines you want - we cant put readline(<linenum>)

file_append=open('C:/Users/pcinthamani/Desktop/Partner Team Management/Python_learning/Works/Python_sample.txt','a')
#append mode : Above doesnt creates file if mentioned file not available in path , if exists it will append at last line
file_append.write("new line as append")
file_append=open('C:/Users/pcinthamani/Desktop/Partner Team Management/Python_learning/Works/Python_sample.txt','r')
print(file_append.read())
file_write=open('C:/Users/pcinthamani/Desktop/Partner Team Management/Python_learning/Works/Python_write.txt','w')
#with open('C:/Users/pcinthamani/Desktop/Partner Team Management/Python_learning/Works/Python_write.txt','w') as file_write:
#Write mode : Above creates file if mentioned file not available in path , if exists it will clear content and write new
file_write.write("writing content to a file")
file_write.close() #if we use with open(<file>,'w') as <variable> , we need not use explicit close
file_write=open('C:/Users/pcinthamani/Desktop/Partner Team Management/Python_learning/Works/Python_write.txt','r')
print(file_write.read())
file_write.close()
#to remove a file import OS & remove it
import os
if os.path.isfile('C:/Users/pcinthamani/Desktop/Partner Team Management/Python_learning/Works/Python_write.txt'):
    os.remove('C:/Users/pcinthamani/Desktop/Partner Team Management/Python_learning/Works/Python_write.txt')
else:
    print("file not there")
#os.system('dir')
#os.system('ls') #used for executing shell scripts in python
#Read and append with a+
file_app_read=open('C:/Users/pcinthamani/Desktop/Partner Team Management/Python_learning/Works/python_append_read.txt','a+')
file_app_read.write('read & append Test')
file_app_read.seek(0) #Move the pointer to starting point of the file
print(file_app_read.read())