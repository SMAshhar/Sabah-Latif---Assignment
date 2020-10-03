##############################################################################################################################
## The defined excersise is not that of python. Therefore, several things asked are not available in python. For example the##
## "friend" function required in Excersise number 3. Or taking in a variable name from user. THere are everal alternates to ##
## that, but I have tried to be as much close to following the script as possible.                                          ##
## Several names of functions/class/methods can be same, used in all excersises. Change them as you will                    ##
##############################################################################################################################

##############################################################################################################################
#################### Excersise No. 1 ##############################

class Player():                     # Class definition
    def __init__(self, name, average, team):
        self.name = name
        self.average = average
        self.team = team
    def change(self):               # Class change method
        self.name = input("Enter new name : ")
        self.average = input("Enter new average : ")
        self.team = input("Enter new Team name : ")
    def display(self):              # Class display method
        print(f"The famous player {self.name}, carrying an average of {self.average}, was part of {self.team}.")

def inputSpecifications():         # Function definition asking for input for class constructor
    global a
    a = input("Enter name of the player : ")
    global b
    b = input("Enter average of the player : ")
    global c
    c = input("Enter team name of the player : ")

inputSpecifications()              # Calling function for input

davidAndrew = Player(a, b, c)      # Constructor definition

davidAndrew.change()               # Calling change method to change the attributes

davidAndrew.display()              # Calling display method to display the statement with the designated attributes

##############################################################################################################################
#################### Excersise No. 2 ##############################

class BankAccount():               # Class Definition
    def __init__(self, name, accNo, typeAcc, balance):
        self.name = name
        self.accNo = accNo
        self.typeAcc = typeAcc
        self.balance = balance
    def deposit(self):              # Defining deposit method
        self.balance += float(input("Enter amount deposited : "))
        print(f"New balance is : {self.balance}")
    def withdraw(self, amount):     # Defining withdraw method
        if amount <= self.balance:
            self.balance -= amount
            print(f"Remaining Amount : {self.balance}")
        else:
            print("You don't have enough balance !")
    def display(self):              # Defining display method $ Has the same name as defined in Ex.1 change it as you will $
        print(f"{self.name} : {self.balance}")

##############################################################################################################################
#################### Question Excersise. 3 ##############################

class DM():                         # Class definition for Matric
    def __init__(self, valueInMetric):
        self.valueInMetric = valueInMetric
        self.inMeters = self.valueInMetric
        self.inCentiMeters = self.valueInMetric * 100

class DB():                         # Class definition for British
    def __init__(self, valueInBritish):
        self.valueInBritish = valueInBritish
        self.inFeet = self.valueInBritish
        self.inInches = self.valueInBritish * 12

                                    # Function definition for adding the two objects and presenting the sum value in Feet
def addFeet(dmCentiValue, dbInchesValue):
    sum = dmCentiValue * 2.54 + dbInchesValue 
    feet = sum//12
    inches = sum % 12
    return int(feet), int(inches)
                                    # Function definition for adding the two objects and presenting the sum value in Meter
def addMeter(dmCentiValue, dbInchesValue):
    sum = dmCentiValue + dbInchesValue * 0.393701
    meters = sum // 100
    cm = sum % 100
    return int(meters), int(cm)
                                    # An example
x = DM(10)
y = DB(25)
                                    
print(f"(Feet, Inches) : {addFeet(x.inCentiMeters, y.inInches)}")
    
    

##############################################################################################################################
#################### Excersise No. 4 ##############################

b = {}                          # Our Static data in form of dictionary

class Run():                    # Class Definition
    def __init__(self, name, distance):
        self.name = name
        self.distance = distance
        global b                # Adding each new object to our global dictionary. 
        b[self.name] = self.distance
    def input(self):            # Function to change a name 
        self.name = input("Enter the runner's name : ")
        self.distance = input("Enter the runner's distance : ")
    def show(self):
        print(f"{self.name} : {self.distance}")

a = 0                           
c = ""

def highScore():                # Function to display the highest scorer at anytime
    global a
    global c
    for k, v in b.items():
        if v > a:
            a = v
            c = k
    print(f"The highest scorer is {c} with a score of {a}.")
                                # Some examples of objects made
Usain_Bolt = Run("Usain Bolt", 200)
Karnazes = Run("Karnazes", 56000)

##############################################################################################################################
#################### Excersise No. 5 ##############################

class Car():                    # Class definition
    def __init__(self, name, direction):
        self.name = name
        self.direction = direction
        self.position = 0    

    def turnRight(self):        # Method of turning right
        if self.direction == "N":
            self.direction = "E"
        elif self.direction == "E":
            self.direction = "S"
        elif self.direction == "S":
            self.direction = "W"
        elif self.direction == "W":
            self.direction = "N"
                                # Method for overriding the direction
    def dirOverload(self, newDirection):
        self.direction = newDirection
                                # Method for adding distance in the position of the car
    def move(self, distance):
        self.position += distance

