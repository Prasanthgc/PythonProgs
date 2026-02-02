list_data=[1,2,3]

def add_list(acs):
    res = 0
    for i in acs:
        res+=i
    return res
def multi(op_add,snd_inp):
    result=op_add*snd_inp
    return result
print(multi(add_list(list_data),3))

#Step over : Calculates/Executes the break point and move to next
#Step into: Moves to detailing of the system function in break point or if its user defined allows user to select which function to move into
#Step into code: Moves control inside the code only , but if there are nested functions , control moves first to the child function
#Step out : Kind of undo of the step into . moves out of the control of function
#Evaluate Expression: in a particular block if you want  to make any calculations on the expression , you can use evaluate
