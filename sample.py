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

