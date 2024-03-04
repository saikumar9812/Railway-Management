# Function to handle option 5
def User.AvailableTrains():
    source = input("Enter Source Station: ")
    destination = input("Enter Destination Station: ")
    date = input("Enter Date (YYYY-MM-DD): ")

    # Check for available trains between source and destination on given date
    available_trains = User.CheckAvailableTrains(source, destination, date)

    if available_trains:
        print("Available Trains:")
        for train in available_trains:
            print(train)
    else:
        print("No trains available for the given route and date.")

# Update the main loop to handle option 5
elif ans == "5":
    User.AvailableTrains()
