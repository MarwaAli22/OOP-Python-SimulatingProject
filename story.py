from PythonProject.iti.myfunction.email_validator import email_validation

class Person :
    def __init__(self,name,money:int):
        self.name = name
        if not isinstance(money,(int,float)) or money <0:
            print("Error:Money must be a positive number")
            self.money=0
        else:
            self.money = money
        self.mood = None
        self.healthRate = 0

    def sleep(self,hours:int):
        if hours == 7:
            self.mood ="happy"
        elif hours < 7:
            self.mood ="tired"
        else:
            self.mood ="lazy"
        print(f'{self.name} mood is {self.mood}')
        return self.mood

    def eat(self,meals:int):
        health = {1:50, 2:75, 3:100}
        if meals in health:
            self.healthRate =health[meals]
            print(f"{self.name} eat {meals} meals\nHealth rate is: {self.healthRate}%")
            return self.healthRate
        else:
            print("Error: number of meals should be 1 or 2 or 3")
            return None

    def buy(self, item_count:int):
        cost = item_count *10
        if self.money >= cost:
            self.money -=cost
            print(f"{self.name} bought {item_count} items\nmoney balance: {self.money}$ ")
            return self.money
        else:
            print(f"no enough money to buy this item\nmoney balance: {self.money}$")
            return self.money

class  Employee(Person):
    def __init__(self,name,money,id,car,email,salary,distanceToWork,targetHour):
        super().__init__(name,money)
        self.id = id
        self.car =car
        try:
            if email_validation(email):
                self.email = email
        except Exception as error:
            print(f"not valid email: {error}")
            self.email =None
        if not isinstance(salary,(int, float)) or salary <=0:
            print("Salary must be a positive number")
            self.salary=0
        else:
            self.salary = salary

        if not isinstance(distanceToWork,(int,float)) or distanceToWork<=0:
            print("Distance to work must be a positive number")
            self.distanceToWork =0
        else:
            self.distanceToWork = distanceToWork

        self.targetHour = targetHour

    def work(self,hours:int):
        if hours ==8:
            self.mood ="happy"
        elif hours >8:
            self.mood ="tired"
        else:
            self.mood ="lazy"
        print(f'{self.name} worked for {hours} hours and feeling {self.mood}.')

    def drive(self):
        distance = self.distanceToWork
        if self.car is None:
            print(f"No car assigned to {self.name}, Can't drive ")
            return
        if distance ==0:
            print("no distance to drive")
            return
        print(f'{self.name} is driving for {distance}Km...')
        return self.car.run(distance,self.car.velocity)

    def refuel(self,gasAmount:int =100):
        if self.car is None:
            print(f"no car assigned to {self.name} , can't refuel")
            return
        if gasAmount < 0 or gasAmount > 100:
            print("pleas enter a gas amount between 0 and 100 l]")
            return
        self.car.fuelRate =min(self.car.fuelRate+gasAmount,100)
        print(f'car refueled with {gasAmount} l\nthe total fuelRate: {self.car.fuelRate}%')
        return self.car.fuelRate

    def send_mail(self,body,to):
        if self.email is not None:
            print(f'sending email...\nfrom:{self.email} \nto: {to}\n({body})')
        else:
            print(f"can't send email, {self.name} have unvalidated email ")

class Office:
    employees_num =0

    def __init__(self,name):
        self.name = name
        self.employees = {}

    def hire(self,emp_name,id,car,email,salary,distanceToWork,targetHour):
        if id not in self.employees:
            new_emp = Employee(name=emp_name,money=0,id=id,car=car,email=email,salary=salary,distanceToWork=distanceToWork,targetHour=targetHour)
            self.employees[id]= new_emp
            print(f"new employee hired with id {id} ")
            Office.employees_num+=1
        else:
            print(f"{id} is already taken")

    def get_all_employees(self):
        return  [{"id": emp.id ,"name":emp.name} for emp in self.employees.values()]

    def get_employee(self,id):
        if id in self.employees:
            emp = self.employees[id]
            return {"id": emp.id ,"name":emp.name}
        else:
            print(f"no employee with id {id}")

    def fire(self,id):
        if id in self.employees:
            del self.employees[id]
            print(f"employee with id {id} fired")
            Office.employees_num-=1
        else:
            print(f"no employee with id {id}")

    @staticmethod
    def calculate_lateness(targetHour,moveHuor,distance,velocity):
        time = distance/velocity
        if moveHuor+time > targetHour:
            lateness = (moveHuor+time) - targetHour
            print(f"employee is late by{round(lateness,2)} hours")
            return lateness
        else:
            print("employee is not late")
            return 0

    def check_lateness(self,id,moveHour):
        if id in self.employees:
            emp = self.employees[id]

            if emp.car is None:
                print(f"can't check lateness, no car assigned to {emp.name}")
                return
            if emp.distanceToWork == 0 :
                print(f"can't check lateness, no distance")
            lateness =self.calculate_lateness(targetHour=emp.targetHour,moveHuor=moveHour,distance=emp.distanceToWork,velocity=emp.car.velocity)
            if lateness ==0:
                self.reward(id=id,amount=10)
            else:
                self.deduct(id=id,amount=10)
        else:
            print(f"employee with id {id} not founded")
    def deduct(self,id,amount):
        if id in self.employees:
            emp = self.employees[id]
            if emp.money>= amount:
                emp.money -= amount
                return emp.money
            else:
                print(f"{emp.name} money balance not enough to deduct{amount}")
                return
        else:
            print("employee not founded")

    def reward(self,id,amount):
        if id in self.employees:
            emp = self.employees[id]
            emp.money+=amount
            return  emp.money
        else:
            print("employee not founded")

    @classmethod
    def change_emps_num(cls,num):
        if num <0:
            print("Error: Number of employees cannot be negative")
            return
        else:
            cls.employees_num=num
            print(f"total employees number: {cls.employees_num}employees")

class Car:
    def __init__(self,name,fuelRate,velocity):
        self.name = name
        self.fuelRate =max(0,min(fuelRate,100))
        self.velocity =max(0,min(velocity,200))
        self.distance=0

    def run(self,distance,velocity):
        self.velocity = velocity
        self.distance = distance

        if self.fuelRate <= 0:
            print("fuel is empty! can't run the car")
            return self.stop()

        print(f'car{self.name} is running at {velocity} Km/h')
        while self.fuelRate > 0 and self.distance > 0:
            self.fuelRate-=0.10*self.fuelRate
            self.distance-=10
            if self.distance <= 0:
                print(f'arrived the destination')
                self.distance=0
                break

        if self.fuelRate==0:
            print("fuel is empty!")
            self.stop()

        return self.fuelRate,self.distance

    def stop(self):
        self.velocity=0
        print(f"car {self.name} has stopped, remaining distance: {self.distance}Km")
        return self.fuelRate
