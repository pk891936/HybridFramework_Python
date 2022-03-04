class Event:
    def __init__(self,name,dob):
        self.__name = name
        self.__dob = dob

    def checkDate(self):
        #12/12/2009
        list = self.__dob.split("/")
        #if int(list[1])==2 or int(list[1])==4 or int(list[1])==6 or int(list[1])==8 or int(list[1])==10 or int(list[1])==12:
        if int(list[i])%2 ==0 and int(list[i])<=12:
            return 'Yes'
        else:
            return 'No'


testcase = int(input())
for i in range(testcase):
    event = Event(input(),input())
    print(event.checkDate())





