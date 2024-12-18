class UserInfo:
    def putData(self):
        self.name=input("Enter Your Name: ")
        self.id=int(input("Enter Your ID: "))
        self.salary=float(input("Enter Your Salary: "))
    def display(self):
        print("Username: ",self.name)
        print("Use ID: ",self.id)
        print("User Salary: ",self.salary)

obj=UserInfo()
obj.putData()
obj.display()
