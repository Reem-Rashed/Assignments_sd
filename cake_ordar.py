# program to order a cake based on the number of people and optional details
def cake_order():  # Function to handle cake ordering
    print("Order Summary:")

    user_count = int(
        input("Enter the number of people: ")
    )  # Input for number of people
    if user_count <= 5:  # if the number of people is less than or equal to 5
        size = "small"
    elif user_count <= 10:  # if the number of people is less than or equal to 10
        size = "medium"
    else:  # if the number of people is greater than 10
        size = "large"

    print(f"Cake size: {size}")  # Display the cake size

    wants_details = input("Do you want to add cake details? (yes/no): ").strip().lower()
    # Initialize details dictionary
    details = {}  # Dictionary to hold additional details

    if wants_details == "yes":  # if the user wants to add details
        while True:  # Loop to collect details
            key = input("Enter detail type (e.g., flavor, decoration): ")
            value = input(f"Enter value for {key}: ")
            details[key] = value

            more = input("Add another detail? (yes/no): ").strip().lower()
            # Ask if the user wants to add more details
            if more != "yes":
                break

    print("\nFinal Order:")  # Display the final order summary
    print(f"Number of people: {user_count}")  # Display the number of people
    print(f"Cake size: {size}")  # Display the cake size
    if details:  # If there are details, display them
        print("Details:")
        for key, value in details.items():
            print(f"- {key.capitalize()}: {value}")
    else:
        print("No additional details provided.")
    dilivery_ = input("Do you want to add delivery information? (yes/no): ").strip().lower()
    if dilivery_ == "yes":  # If the user wants to add delivery information
        delivery_info = input("Enter delivery information: ")
        print(f"Delivery Information: {delivery_info}")
    else:
        print("No delivery information provided.")
    drincks_ = input("Do you want to add drinks? (yes/no): ").strip().lower()
    if drincks_ == "yes":  # If the user wants to add drinks
        drinks = input("Enter drinks: ")
        print(f"Drinks: {drinks}")
    else:
        print("No drinks added.")
    captain_reward = input("Do you want to add a captain reward? (yes/no): ").strip().lower()
    if captain_reward == "yes":  # If the user wants to add a captain reward
        
        print(f"Captain Reward: {user_count * 10} points")  # Example calculation for captain reward
    


cake_order()  # Call the function to execute the cake ordering process