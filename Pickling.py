import pickle
#For loading/dumping data into a file and reuse it later point - like pickle
Dict_load={1:'sd',2:'fg'}
pick_file=open('C:/Users/pcinthamani/Desktop/Partner Team Management/Python_learning/Works/Python_sample_1.txt','wb')
pickle.dump(Dict_load,pick_file)
pick_file.close()
pick_file_op=open('C:/Users/pcinthamani/Desktop/Partner Team Management/Python_learning/Works/Python_sample_1.txt',"rb")
read_pickle=pickle.load(pick_file_op)
print(read_pickle)
#to read entire file content use read or pickle
pick_file_o=open('C:/Users/pcinthamani/Desktop/Partner Team Management/Python_learning/Works/python_append_read.txt',"r")
content = pick_file_o.read()
print(content)