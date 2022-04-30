class Bank:
    def system(self):
        print("This is parent class")
        x=input("Enter the id of bank employee:")
        if x=="e123" :
            print("Valid user")
        else:
            print("Invalid user")
class Branch (Bank):
    def accounts(self):
        print("This is a child class")
        y=input("Enter the account number:")
        print("Account number is:",y)
obparent=Bank()        #Object of parent class
obparent.system()     #CASE 1: method of parent class by object of parent class
obchild=Branch()      #Object of child class
obchild.accounts()    #CASE 2: method of child class by object of child class
obchild.system()      #CSE 3:method of parent class by object of child class




