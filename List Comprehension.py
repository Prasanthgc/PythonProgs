#list comprehension - adding a block of code in single list

#Convention/Usual
name_list=["Prasanth","Umayal","Saran","Pradee"]
Selected_list=[]
for x in name_list:
    if "P" in x:
        Selected_list.append(x)
print(Selected_list)

#List_Comprehension - rewrite the above block into list
list_comp=[x for x in name_list if "P" in x]
print(list_comp)
list_comp2=[x for x in name_list if "Pra" not in x]
print(list_comp2)
list_comp3=[x if x > 3 else 4 for x in range(20) ]
print(list_comp3)
list_comp4=[x if x!="Umayal" else "Thangam" for x in name_list ] #if applying any <else block> put <if block> first b4 <for block>
print(list_comp4)