import zlib

class User:
    def __init__(self,name,mobileNumber,email,username,password):
        self.name = name
        self.mobileNumber = mobileNumber
        self.email = email
        self.username = username
        self.password = self.__encrypt(password)

    def __encrypt(self,password):
        return zlib.compress(str(password).encode(),1)

    def validate(self,Pswd):
        pswd = zlib.decompress(self.password)
        if pswd == Pswd:
            return 'Valid'
        else:
            return 'InValid'



user_list = []
testcase = int(input("testcase:"))
for i in range(testcase):
    user = User(input(),int(input()),input(),input(),input())
    user_list.append(user)

queries = int(input("querries:"))
for i in range(queries):
    uname = input()
    pwd = input()
    for user in user_list:
        if user.username == uname:
            print(user.validate(pwd))
            break






