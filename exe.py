#Defin a function  call card_number
def card_number():

    card_number=1 # Start from card number 1

    # Loop through numbers up to 10
    while card_number <=10:

        if card_number %2==0:# Check if the card number is even
            print(f"Card #{card_number}: Paid collection!")  # Even numbers are paid

        else:
            print(f"Card #{card_number}: Free collection")  # Odd numbers are free

        card_number += 1  # Increment the card number to move to the next one
        
card_number() #End difin function.