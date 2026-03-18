# import random

# class MMDT:
#   def __init__(self):
#     self.userinfo = []

#   def addRequest(self, name):
#     self.userinfo.append(name)
  
#   def processRequest(self):
#     if self.isEmpty():
#       print("There is no pending requests now.")
#       return False
#     name = self.userinfo.pop(0)
#     print(f"{name} request has been processed.")
#     return True

#   def generateLogin(self, name):
#     num = random.randint(000, 999)
#     username = name + str(num)
#     return username

#   def isEmpty(self):
#     return len(self.userinfo) == 0

#   def size(self):
#     return len(self.userinfo)

# ## Testing
# system = MMDT()

# system.addRequest("MMDT")
# system.addRequest("Zaw")

# print("Size of Queue:", system.size())       
# print("Queue is Empty??", system.isEmpty())  

# system.processRequest()            
         
# print("Size:", system.size())      

import random
from collections import deque

class MMDT:
    def __init__(self):
        self.userinfo = deque()          

    def addRequest(self, name):
        self.userinfo.append(name)       

    def processRequest(self):
        if self.isEmpty():
            print("There is no pending requests now.")
            return False
        name = self.userinfo.popleft()   
        username = self.generateLogin(name)
        print(f"{name} request has been processed.")
        print(f"Login credentials: {username}")
        return True

    def generateLogin(self, name):
        num = random.randint(0, 999)
        username = name + f"{num:03d}"   
        return username

    def isEmpty(self):
        return len(self.userinfo) == 0

    def size(self):
        return len(self.userinfo)

# Testing
system = MMDT()

system.addRequest("MMDT")
system.addRequest("Zaw")

print("Size of Queue:", system.size())
print("Queue is Empty?:", system.isEmpty())

system.processRequest()
system.processRequest()
system.processRequest()    

print("Size:", system.size())
print("Queue is Empty?:", system.isEmpty())