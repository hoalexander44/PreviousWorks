#This is a monty gameshow simulator, seeing if it is really better to switch after the first door is revealed
import random
import sys

#The seed inputter that also has an input checker
the_seed = input("Enter Random Seed:\n")
try:
    the_seed = int(the_seed)
except ValueError:
    print("Seed is not a number!")
    sys.exit()
random.seed(the_seed)

print("Welcome to Monty Hall Analysis")
print("Enter 'exit' to quit.")
#The list that acts as the deck of doors that will be shuffled through each test
doors = ['C', 'G', 'G']
#The function that checks if the user input is an integer and will repeadetly ask for a new input if it is not an integer. Function will also exit the program when user types in "Exit"
def input_corrector(question):
    while True:
        try:
            x = input(question)
            if x =="exit":
                print("Thank you for using this program.")
                sys.exit()
                break
            else:
                x= int(x)
                return x
        except ValueError:
            question="Please enter a number:\n"

#This function simulates the game show
def simulator():
    #These are the initial variables for the function that will later decide how many tests are run and help keep track of the results of each test
    test_runs = input_corrector("How many tests should we run?\n")
    stay=0
    switch=0
    total=0
    #This loops shuffles the doors, prints the information for each test, and calculates and prints the results for each set of tests
    for i in range (1,test_runs+1):
        #These two lines determine the order of the doors and which door the player selects
        random.shuffle(doors)
        player_select = random.randint(0,2)
        #This if statement determines if the game information is printed or not, particularly when the number of tests is less than or equal to 10
        if test_runs<=10:
            print("Game",i)
            print("Doors:",doors)
            print("Player Selects Door",player_select+1)
        #This if statement decides what monty will pick and what the player should do after the player selects a door with a goat, also adds to the total, switch, and stay data
        if doors[player_select] == "G":
            for j in range(0,3):
                if j != player_select and doors[j] =="G":
                    monty_select = j
                    break
            if test_runs <=10:
                print("Monty Selects Door",monty_select+1)
                print("Player should switch to win.")
            total = total + 1
            switch = switch + 1
        #else statement that decides what monty will pick and what the plaer should do after the player selects a door with a car, also adds to the total, switch, and stay data
        else:
            for j in range(0,3):
                if j != player_select and doors[j] =="G":
                    monty_select = j
                    break
            if test_runs <=10:
                print("Monty Selects Door",monty_select+1)
                print("Player should stay to win.")
            total = total + 1
            stay = stay + 1
    #The output that displays the percentage of stay wins and switch wins
    print ("Stay Won",(stay/total)*100,"% of the time.")
    print ("Swich Won",(switch/total)*100,"% of the time.")
    #loops the simulator 
    simulator()
#runs the simulator
simulator()