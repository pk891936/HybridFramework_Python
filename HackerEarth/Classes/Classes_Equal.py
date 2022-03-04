class User:
    def __init__(self,name,username,password,mobileNumber):
        self.name = name
        self.username = username
        self.password = password
        self.mobileNumber= mobileNumber
    def __eq__(self, other):
        if self.mobileNumber == other.mobileNumber:
            return 'Equal'
        else:
            return 'Not Equal'


testcase = int(input())
for i in range(testcase):
    user1 = User(input(),input(),input(),int(input()))
    user2 = User(input(),input(),input(),int(input()))
    print(user1 == user2)





