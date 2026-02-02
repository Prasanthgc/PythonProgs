#List : [<hetro values>] - Changeble/ordered/allow dups
#Tuple: (<hetro values>) - Non Changeble (but change to list & converted to tuple)/ordered/allow dups
#Dictionary : {<key:value pairs>} - Changeble/unordered/does not allow dups

#List is changeble / allows duplicate / ordered
new_lst=['a','b',1,2,3,'apple'] #list = array but can be mix of dataypes + changeble during runtime
print(new_lst)
print(new_lst[2:4])
print(new_lst.insert(2,"abc")) #inserts at defined posision
print(new_lst.append('append')) #apped any at last inside array
new_lst[2:1]=["new"] #add any to the list 
#print(new_lst.count(0))
print(new_lst)

#Tuple - Unchangeble / allows duplicate / ordered (Same as List but diff is (C - bracket)
tuple1=("car",'cycle',1,2,3,1.0)
print(tuple1)
print(type(tuple1))
tuple_list=list(tuple1) #change to list type & insert the values since tuple is unchangeble
tuple_list.insert(1,"new")
tuple_list.append("last")
tuple_list[2:0]="abc","CARD"
tuple1=tuple(tuple_list) #change back to tuple type
print(tuple1)

#Dictionaries - Changeble/Un ordered (Since key value pair)/No duplicates
#Dec2025 - how to merge two lists (of equal values) to dictionary
listval=[1,2,3,4,5]
list=['pra','san','th','ums','kut']
dict1= dict(zip(list,listval))
#or use for loop
for i,e in zip(list,listval):
dictio={
    "name":"prasanth",
    "dob":15031992,
    "loc":"salem",
    "twowheelar":"yamaha",
    "loc":"madurai" #eventhpough duplicates , it wont fail , instead will display last value of the key
}
print(type(dictio))
print(dictio)
print(dictio.get('dob')) #to get the value for the key inside dictionary
print(dictio["name"]) #another way for getting value for key inside dictionary
dictio["twowheelar"]="scooter" #update dictionary
dictio.update({"name":"updated_prsnth"}) #update using function update
print(dictio)
dictio.pop("loc") #hides the key & pair while display
print(dictio)
print(dictio.keys()) #display list of keys inside the dictionary
print(dictio.values()) #display list of values inside the dictionary