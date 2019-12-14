class Company:
    CompanyName="LT"
    Location="Bangalore"
    Hike_Rate=10

    def __init__(self,Name, age,id,sal):
        self.Name=Name
        self.id=id
        self.sal=sal
        self.age=age

    def display_employedetails(self):
        print(self.Name,self.age,self.id,self.sal)


    def modify_details(self,Name="",age=0,id=0,sal=0 ):
        if Name!="":
            self.Name=Name
        if id!=0:
            self.id=id
        if age!=0:
            self.age=age
        if sal!=0:
            self.sal=sal

    @classmethod
    def modify_hike(cls,new=0):
        if new==0:
            cls.Hike=new
            return new

    @staticmethod
    def get_hike():
        new = float(input("enter the new hike"))
        return new


    @staticmethod
    def success():
     print("Employee details has been updated successfully")

    @staticmethod
    def failure():
        print("Employee details modification has been failed")


ob=Company("anusha",20,1121,10000)
Company.display_employedetails(ob)







