class Bank:
    BankName="ICICI"
    ROI=14
    MBranch="Bangalore"

    def __init__(self,Name,age,phoneNo,email,Bal=0):
     self.Name=Name
     self.age=age
     self.email=email
     self.phoneNo=phoneNo
     self.Bal=Bal


    def withdraw(self,amt=0):
        if amt==0:
            amt=self.get_amount()
        if amt>self.Bal:
            self.failure()
            print("insufficent funds")
        return
        self.Bal=self.sub(self.Bal,amt)
        self.success()

    def display(self):
            print(self.Name,self.age,self.phoneNo,self.email,self.Bal)

    def modify(self,Name="",age=0,phoneNo=0,email=""):
            if Name!="":
                self.Name=Name
            if age!=0:
                self.age=age
            if phoneNo!=0:
                self.phoneNo
            if email!="":
             self.email=email
             self.success

    @classmethod
    def change_Bname(cls,new=""):
            if new=="":
                cls.BankName=new
            cls.success()

    @classmethod
    def modify_ROI(cls, new=0):
            if new == 0:
                cls.get_ROI()
                cls.ROI=new

            cls.success()

    @staticmethod
    def get_ROI():
            new=float(input("enter the ROI"))
            return new

    @staticmethod
    def sub(a,b):
            return a-b
    @staticmethod
    def failure():
            print("transaction failure")
    @staticmethod
    def get_amount():
            amount=int(input("enter the amount"))
            return amount

    @staticmethod
    def success():
            print("Transation Success")


class Bank2(Bank):
    def __init__(self,Name,age,phoneNo,email,Aadhar,PanNo,Bal=0):
      super(Bank2.self).__init__(Name,age,phoneNo,email,Aadhar,PanNo,Bal)

      self.Pan=PanNo
      self.Aadhar=Aadhar

    def add_Aadhar(self,PanNo,Aadhar):
        self.Aadhar=Aadhar
        self.Pan=PanNo



# Anusha=Bank("anusha",27,1234566,"anu@gamush.com",10000)
# Bank.modify_ROI()
# Anusha.display()
# Anusha.withdraw()
# Bank.display(Anusha)
# Bank.withdraw(Anusha,1000)
Anvi=Bank2("anvika",3,12345,"anvi@gmal.com",100001,123456,3455555)




