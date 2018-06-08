#This is a rcket simulator that allows a user to attempt to land on various interstellar masses
import sys
#Setting all the global variables that will be used for each iteration of the game
name = "Moon"
gravity = -1.622
current_fuel = 150
level = 1
velocity = 0
altitude = 50
fuel_use = 0
seconds = 0
#These are lists , dictating the information for each specific level
name_list = ["Moon","Earth","Pluto","Neptune","Uranus","Saturn","Jupiter","Mars","Venus","Mercury","Sun"]
gravity_list=[-1.622,-9.81,-0.42,-14.07,-10.67,-11.08,-25.95,-3.77,-8.87,-3.59,-274.13]
fuel_list = [150,5000,1000,1000,1000,1000,1000,1000,1000,1000,50000]
level_dictionary = {
    "Moon":1,
    "Earth":2,
    "Pluto":3,
    "Neptune":4,
    "Uranus":5,
    "Saturn":6,
    "Jupiter":7,
    "Mars":8,
    "Venus":9,
    "Mercury":10,
    "Sun":11}
#This function acts as an input checker when asking the player for fuel, also gives back a variable represnting the used fuel in a second
def ask_fuel(current_fuel):
    stopper = False
    while stopper == False:
        try:
            fuel_use = int(input("Enter units of fuel to use:\n"))
            if fuel_use%1 == 0 and fuel_use >=0 and fuel_use <=current_fuel:
                return fuel_use
                stopper = True
            else:
                print("please enter a valid number")
        except ValueError:
            print("please enter a valid number")
#This function initializes a level, ends the level depending on whether or not the player wants to keep playing, and loops to interate between levels
def play_level(name,gravity,fuel):
    #This variable works to stop the input correcter loop when the player is asked "Do you want to play level #"
    stopper2=False
    #This variable works to stop the loop that runs each level
    stop_level=False
    #These variables gives each level the same starting velocity, altitude, level, and seconds
    velocity =0
    altitude = 50
    level = level_dictionary[name]
    seconds = 0
    #This is the start of input correcter loop as well as where the player is asked to keep playing or exit
    print("Do you want to play level",level,"? (yes/no)")
    while stopper2==False:
        resume = input()
        if resume.lower() == "no":
            print("You made it past",level-1,"levels.")
            print("Thanks for Playing.")
            sys.exit()
            stopper2=True
        elif resume.lower()=="yes":
            print("Entering Level",level)
            stopper2=True
        else:
            print("Please enter a valid answer")
    #prints out the initial stats for the level
    print("Landing on the",name)
    print("Gravity is",gravity,"m/s^2")
    print("Initial Altitude:",altitude,"meters")
    print("Initial Velocity:",velocity,"m/s")
    print("Burning a unit of fuel causes 0.10m/s slowdown.")
    print("Initial Fuel Level:",fuel,"units")
    print(" ")
    print("GO")
    #The level loop that repeadetly asks the player for fuel usage and calculates the current status of the simulation
    while stop_level ==False:
        fuel_use= ask_fuel(fuel)
        fuel = fuel- fuel_use
        velocity = velocity + gravity + (0.1*fuel_use)
        altitude = altitude + velocity
        if altitude <=0:
            altitude = 0
            stop_level = True
        seconds = seconds +1
        print("After %d seconds Altitude is %.2f meters, velocity is %.2f m/s" % (seconds, altitude,velocity))
        print("Remaining Fuel:",fuel,"units.")
    #Decides whether the player has succsfully landed the simulation
    if (velocity < -2) or (velocity >2):
        print("Crashed!")
    else:
        print("Landed Successfully.")
        level +=1
    #Gives the next level the correct variables
    if level <=11:
        name = name_list[level-1]
        gravity=gravity_list[level-1]
        fuel = fuel_list[level-1]
        play_level(name,gravity,fuel)

#starts the game
print("Welcome to Lunar Lander Game.")
play_level("Moon",-1.622,150)


