# Program name: OURAI_DANIEL_Test_Ride_Lafayette_M08-fp
# Author: Daniel J Ourai
# Date: 5/10/2022
# Summary: This app will allow a user (rider) to schedule a test ride, compare
#           motorcycle prices, and specs as well as include a FAQ list
# Variables:
#   Rider: The rider's name (str)
#   Bike: Make, model and year of the motorcycle the rider intends to ride (str)
#   rideDate: Intended date for rider's test ride (str)
#   age: age of the rider (int)
#   faq: function used to display the FAQ list
#   Info: Class for documented rider info for later use in program

mcycle1 = ("Kawasaki Vulcan 650")

print("Here is our current list of test ride options: ")
print("2018 Kawasaki Vulcan 650 (67hp) $6,699")
print("2016 Suzuki SV650 (75hp) $4,175")
print("2020 Kawasaki Ninja H2 (310hp) $55,000")
print("2015 Yamaha FJR (107.5hp) $15,899")

    # Define classes
class Info():

    def __init__(self, rider, rideDate):
        self.rider = rider
        self.rideDate = rideDate

    def getRider(self, rider):
        return self.rider

    def getRideDate(self, rideDate):
        return self.rider

    def setRider(self, rider):
        self.rider = Rider

    def setRideDate(self, rideDate):
        self.rideDate = rideDate

def main():

    # Get user input
    Rider = input("Enter your First and Last name:")
    if Rider == "":
        print("ERROR... No entry detected.")
        Rider = input("Enter your First and Last name:")
    rideDate = str(input("Enter your intended test ride date. (MM/DD/YYYY): "))
    if rideDate == "":
        print("ERROR... No entry detected.")
        rideDate = str(input("Enter your intended test ride date. (MM/DD/YYYY): "))
    age = input("Enter your age:")
    if age == "":
        print("ERROR... No entry detected.")      
    if age == "100":
        print("ERROR...If you were that old, you would'nt be on a bike!: ")
        age = input("Enter your age:")
    if age == "200":
        print("ERROR...Now you are just messing around! How old are you?")
        age = input("Enter your age:")
    Bike = input("Enter the name of the motorcycle you would like to ride: ")
    if Bike == "2018 Kawasaki Vulcan 650":
        print("Your test ride has been scheduled!")
        print("Stop by our location on the specified date with your license and gear!")
    if Bike == "2016 Suzuki SV650":
        print("Your test ride has been scheduled!")
        print("Stop by our location on the specified date with your license and gear!")
    if Bike == "2020 Kawasaki Ninja H2":
        print("Your test ride has been scheduled!")
        print("Stop by our location on the specified date with your license and gear!")
    if Bike == "2015 Yamaha FJR":
        print("Your test ride has been scheduled!")
        print("Stop by our location on the specified date with your license and gear!")

    # Create an instance of the Info class
    myInfoRecord =(Rider)

    # Display information

    faq = input("To view our FAQ list, enter Yes. To skip this, enter Stop:")
    if faq == "Yes":
        import OURAI_DANIEL_Test_ride_Lafayette_M08_fp_FAQ
    else:
         print("See you soon!")
    print(" Thank you" + " " + Rider + "!" + " We hope to get you on the" + " " + Bike + " " + "soon!")
main()
    





