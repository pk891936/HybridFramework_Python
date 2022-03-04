class User:
    def __init__(self,name,age,gender):
        self.name = name
        self.age = age
        self.gender = gender
    def __str__(self):
        return ("{}\n{}\n{}".format(self.name,self.age,self.gender))

class Contact:
    def __init__(self,phoneNo,emailId,address,User):
        self.phoneNo = phoneNo
        self.emailId = emailId
        self.address = address
        self.User = User
    def __str__(self):
        return ("{}\n{}\n{}\n{}".format(self.User,self.phoneNo,self.emailId,self.address))


user = User(input(),int(input()),input())
contact = Contact(int(input()),input(),input(),user)
print(contact)