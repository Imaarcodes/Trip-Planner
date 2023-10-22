#Septemeber 6, 2023
#Imaar Chauthani
#Trip planner

def intro_data():
    #intro_data takes basic user input
    #global makes all variables valid outside of this function
    global firstname
    global lastname
    global destination

    #Name and Destination input
    print("Hello! Welcome to The Best Trip Planner Program!")
    firstname =input("Can you please give me your first name?")
    lastname = input("Can you please give me your last name?")
    print("Hi "+firstname+ " "+lastname + ". It is a pleasure to meet you!")
    destination = input("Where would you like to go?")
    print("That sounds like a great idea! I love " + destination + "!")

def number_inputs():
    global traveldays
    global inttraveldays
    global budget
    global fltbudget
    global currencysymbol
    global fltconversion

    #traveldays, budget,currency symbol input and conversion all in integers or floats
    traveldays = input("How many days will you be spending in " + destination +"? Be sure to only input a number.")
    try:
        inttraveldays = int(traveldays)
    except:
        print('Travel days needs to be a positive integer. Read instructions and try again.')
        number_inputs()
    budget = input("What is your total budget in USD? Input must only be a number.")
    try:
        fltbudget= float(budget)
    except:
        print("Total budget needs to be a number only.")
        number_inputs()
    currencysymbol = input("What is your currency symbol for your destination?")
    conversion = input("What is the conversion rate from USD to " +currencysymbol+ "?")
    try:
        fltconversion = float(conversion)
    except:
        print("The conversion rate can only be a decimal number. Retry.")
        number_inputs()

def Converters():

        #Time conversions
    hourstravelled = int(traveldays) * 24
    print("hourstravelled:" ,hourstravelled)
    minutestravelled = int(hourstravelled) * 60
    print("minutes travelled:" ,minutestravelled)
    secondstravelled = int(minutestravelled) * 60
    print("seconds travelled" ,secondstravelled)

    #budget conversion
    print("Your total budget for the trip is" ,budget)
    dailybudget = (fltbudget) / (inttraveldays)
    roundeddailybudget = round(dailybudget,2)
    print("Your daily budget is:" ,roundeddailybudget)

    destinationAmount = fltbudget * fltconversion
    print("You will need " , destinationAmount , currencysymbol + ".")

def Time_difference():
    timeDiff = input("What is the time difference between CST and " + destination+ "? If behind input a negative number.")
    try:
        fltTimeDiff = float(timeDiff)
        if (fltTimeDiff < 24 and fltTimeDiff > -24):
            midnightInDestination = (fltTimeDiff + 24) % 24
            print("When it is Midnight in CST it will be " + str(midnightInDestination) + " in " + destination + ".")
            noonInDestination = (fltTimeDiff + 12) % 24
            print("When it is Noon in CST it will be " + str(noonInDestination) + " in " + destination + ".")
        else:
            print("Enter value between 24 and -24")
            Time_difference()
    except:
        print("Input must only be a negative or positive number.")
        Time_difference()

def Country_area():
    destinationArea = input("What is the area of " + destination + " in square kilometers?")
    try:
        fltKmArea = float(destinationArea)
        fltMilesArea = fltKmArea/2.5899
    except:
        print("Input can only be numbers.")
        Country_area()
    print("The area of " + destination + " in square miles is ",fltMilesArea,".")

intro_data()
number_inputs()
Converters()
Time_difference()
Country_area()

print("I hope you enjoy your time in " + destination + "!")
