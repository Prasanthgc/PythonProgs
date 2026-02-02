class prasanth_home:
    #__init__ is initilatization method & its initializes the attributes of the objects to class
    #self - it mentions the objects belongs to class & via which the methods can access the attributes of the objects
    def __init__(self,Member,age):  #these are arguments that takes values
        self.Member=Member #any variables can be created at left and assignments by above arguments
        self.detail=Member+' '+str(age)
    def create_initial(self,second): #all the methods in class shuld have first arg as SELF (Which is instance of class)
        #we can access self attributes from above block easily
        mem_initial=self.Member[0]
        return mem_initial+' '+second
    @staticmethod #How to use normal function instead of Method + self concept of clasee
    def normal_func(a,b):
        return a*b
    @classmethod #classs method if not needed to use Instance metnod/initialize method
    def class_methd(cls,input):
        multi=int(input)
        return cls(multi)

person_1=prasanth_home('prasanth',32)
person_2=prasanth_home('saranyaa',26)
person_3=prasanth_home('umayal',2)
print(person_1.create_initial('New')) #how to call new method created
print(person_1.Member)
print(person_1.detail)
print(person_3.Member)
print(person_3.detail)
print(prasanth_home.normal_func(2,3))
#class_mothod=prasanth_home.class_methd('2')
#print(class_mothod.multi)