#The program knows if the user's password is correct or incorrect.
print("Welcome to our system! ") # Welcome message for the user
Correct_password="reem1234"#The correct password

print("You're password 8 codes") # the system tells the user (You're password 8 codes).

User_password=input("Please enter your password:") # Ask  the user enters the password.

if User_password==Correct_password: #check if the user enter password.
  print("Welcome!") # If the password correct password display (Welcome! ).

if User_password!=Correct_password: 
  print("Did you forget your password?")  # If the password incorrect display (Did you forget your pasword?).


print("Thank you for using our system!")  # Final message for the user.

#End the program