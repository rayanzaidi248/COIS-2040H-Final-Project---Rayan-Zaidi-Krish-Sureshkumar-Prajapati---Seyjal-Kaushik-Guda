#Final Project Assignment
#Restaurant Reservation System
#Group Members: Rayan Zaidi & Krish Sureshkumar Prajapati & Seyjal Kaushik Guda

#Importing certain plugins for file access and reading files

import json
import os

#Part 1 of ReservationSystem

class ValidationError(Exception):
    pass

class ReservationSystem:

    #Specifies the file where we are going to be saving our user information in (users.json)
    def __init__(self):
        self.file_name = "users.json"
        self.users = self.load_users()
        self.current_user = None

    #This function is used for already saved users in the ReservationSystem. It's job is to read the file containing the user's input of their email, name, password and date of birth
    def load_users(self):
        if os.path.exists(self.file_name):
            with open(self.file_name, "r") as file:
                return json.load(file)
        else:
            #Otherwise return an empty list if the file doesn't exist or does not have any content in it yet.
            return[]
        
    #This function writes down information that is being inputted by the user when registering in the system and save it in the file we just created (users.json file)
    def save_users(self):
        with open(self.file_name, "w") as file:
            json.dump(self.users, file, indent=4)
    
    #This function serves as the user interface for the main menu
    #Displays the options the user has when using the ReservationSystem
    
    def mainMenu(self):
        print("\n========== Restaurant Reservation System ==========")
        print("1. Register/Signup")
        print("2. Login")
        print("3. Exit")
        print("================================================")
        
    def ReservationMenu(self):
        ReservationMenuSwitch = True
        while ReservationMenuSwitch == True:
            
            print("\n======== Reservation Menu =========")
            print("1. View Reservation")
            print("2. Make Reservation")
            print("3. Modify Reservation")
            print("4. Cancel Reservation")
            print("5. Logout")

            ReservationChoice = input("Enter your choice: ")
            if ReservationChoice == "1":
                print ("You have selected to view your reservation")
                self.viewReservations(self.current_user)
                
            elif ReservationChoice == "2":
                print("You have selected to make a reservation")
                self.makeReservation(self.current_user)
                
            elif ReservationChoice == "3":
                print("You have selected to modify your reservation")
                self.modifyReservation(self.current_user)

            elif ReservationChoice == "4":
                print("You have selected to cancel a reservation")

            elif ReservationChoice == "5":
                print("Logging you out...")
                self.mainMenu()
                ReservationMenuSwitch = False
                
            else:
                print("The choice you have selected is not valid. Try Again")
                
    #Part 4-8 of ReservationSystem
    #making a resevartion function
    def makeReservation(self, user):
        print("\nMake a Reservation selected")
        num_days = input("Number of days: ")
        from_date = input("From date (YYYY-MM-DD): ")
        to_date = input("To date (YYYY-MM-DD): ")
        num_persons = input("Number of persons: ")
        num_rooms = input("Number of rooms: ")
        if num_days == "" or from_date == "" or to_date == "" or num_persons == "" or num_rooms == "":
            print("Please fill in all the fields.")
        else:
            # Create the reservation dictionary
            reservation = {
                "num_days": num_days,
                "from_date": from_date,
                "to_date": to_date,
                "num_persons": num_persons,
                "num_rooms": num_rooms
            }
            
            # Add 'reservations' key if it doesn't exist
            if 'reservations' not in user:
                user['reservations'] = []
            
            # Append the new reservation
            user['reservations'].append(reservation)
            
            # Save back to users.json
            self.save_users()
            
            print("Reservation details saved!")
            
            onSwitch = True
            while onSwitch == True:
                print("\nPlease confirm your reservation details:")
                print(f"Number of days: {num_days}")
                print(f"From date: {from_date}")
                print(f"To date: {to_date}")
                print(f"Number of persons: {num_persons}")
                print(f"Number of rooms: {num_rooms}")
                confirmation = input("Confirm reservation? (y/n): ")
                if confirmation.lower() == "yes" or confirmation.lower() == "y":
                    print("Reservation confirmed!")
                    onSwitch = False
                elif confirmation.lower() == "no" or confirmation.lower() == "n":
                    self.makeReservation(user)
                    onSwitch = False
                else:
                    print("Invalid input. Please enter 'yes' or 'no'.")

    def viewReservations(self, user):
        if 'reservations' not in user or not user['reservations']:
            print("No reservations found.")
        else:
            print("Your reservations:")
            for i, res in enumerate(user['reservations'], 1):
                print(f"{i}. Days: {res['num_days']}, From: {res['from_date']}, To: {res['to_date']}, Persons: {res['num_persons']}, Rooms: {res['num_rooms']}")
    
    def modifyReservation(self, user):
        print("\nModify Reservation selected")
        print("Your reservations:")
        for i, res in enumerate(user['reservations'], 1):
            print(f"{i}. Days: {res['num_days']}, From: {res['from_date']}, To: {res['to_date']}, Persons: {res['num_persons']}, Rooms: {res['num_rooms']}")
        reservation_choice = input("Enter the number of the reservation you want to modify: ")
        if reservation_choice.isdigit() and 1 <= int(reservation_choice) <= len(user['reservations']):
            reservation_index = int(reservation_choice) - 1
            reservation = user['reservations'][reservation_index]
            print("Enter new details (leave blank to keep current value):")
            num_days = input(f"Number of days ({reservation['num_days']}): ") or reservation['num_days']
            from_date = input(f"From date ({reservation['from_date']}): ") or reservation['from_date']
            to_date = input(f"To date ({reservation['to_date']}): ") or reservation['to_date']
            num_persons = input(f"Number of persons ({reservation['num_persons']}): ") or reservation['num_persons']
            num_rooms = input(f"Number of rooms ({reservation['num_rooms']}): ") or reservation['num_rooms']
            
            # Update the reservation
            user['reservations'][reservation_index] = {
                "num_days": num_days,
                "from_date": from_date,
                "to_date": to_date,
                "num_persons": num_persons,
                "num_rooms": num_rooms
            }
            
            # Save back to users.json
            self.save_users()
            
            print("Reservation modified successfully!")
        self.ReservationMenu()
    
    def cancelReservation(self, user):
        print("\nCancel Reservation selected")
        print("Your reservations:")
        for i, res in enumerate(user['reservations'], 1):
            print(f"{i}. Days: {res['num_days']}, From: {res['from_date']}, To: {res['to_date']}, Persons: {res['num_persons']}, Rooms: {res['num_rooms']}")
        reservation_choice = input("Enter the number of the reservation you want to cancel: ")
        if reservation_choice.isdigit() and 1 <= int(reservation_choice) <= len(user['reservations']):
            reservation_index = int(reservation_choice) - 1
            del user['reservations'][reservation_index]
            
            # Save back to users.json
            self.save_users()
            
            print("Reservation cancelled successfully!")
        self.ReservationMenu()

    #This function is used to check if the email is a valid email that is inputted by the user
    def email_validation(self, email):
        if email.strip() == "":
            raise ValidationError("Email can't be blank")
        elif "@" not in email or "." not in email:
            raise ValidationError("This is not a valid email format")
        
        else:
            return email

    #For this function we are checking if the user has only inputted alphabetical letters for their name. Because realistically their name would not have a number or for example an exclamation mark in it.
    def name_validation(self, name):
        #Returns the name without spaces
        #isalpha() is a function that is used to make sure that the string only contains alphabetical letters (can't have alphabetical letters in your name)
        if not name.replace(" ", "").isalpha():
            raise ValidationError("Name can only have letters")
        else:
            return name

        #This is for every other verification (password,
    def blank_verification(self, userinput):
        if userinput.strip() == "":
            raise ValidationError("You must have an input here")
        else:
            return userinput

    #This function is used for prompting the user about their registration details (email, name, password etc.)
        # And ensuring that the functions for validation that we made earlier are being used there
    def userInput(self, prompt, validation_function=None):
        while True:
            try:
                value = input(prompt)

                #If there is a validation function eing used it will go through that validation_function (email & name validation) and make sure it follows the requirements
                if validation_function:
                    return validation_function(value)

                #If it doesn't have a validation function associated with it, then we just continue as normal
                else:
                    return value
                
            #if we do run into an error in this process, we will then raise a ValidationError depending on where the user messed up in inputs.
            except ValidationError as e:
                print(e)
            
                
    #This function is used for registering the user
    def register_user(self):
        print("Registration in Progress:")

        #Using the userInput function we will ask the user for their email and pass the respected validation functions that we made to make sure the user isn't breaking any rules
        #Some are empty because there isn't any need for a validation function for them.
        email = self.userInput("Email: ", self.email_validation)
        first_name = self.userInput("First Name: ", self.name_validation)
        last_name = self.userInput("Last Name: ", self.name_validation)
        password = self.userInput("Password: ", self.blank_verification)
        date_of_birth = self.userInput("Date Of Birth: ", self.blank_verification)

        #This loop checks if the user has already registered in the system by going through the file and checking if the new user being made shares the same email as another user.
        for user in self.users:
            if user["email"] == email:
                print("Email has already been registered.")
                #this return just breaks the loop once it finds the exact same email that is in the system.
                return
        #This puts the user inputted data into the file and saves it
        new_user = User(email, first_name, last_name, password, date_of_birth)
        self.users.append(new_user.user_data())
        self.save_users()
        print("Your Registration Has Been Successful")

    #This function is used for logging the user into the ReservationSystem   
    def login_user(self):

        #login_userswitch is used to make a while loop to determine if the user want's to still try to login into the ReservationSystem or not
        login_userswitch = True

        
        while login_userswitch == True:

            #We set this variable as false because it is going to determine whether or not if we do or do not find the email and password in our system
            #If we don't we will prompt the user another set of options
            userVerified = False

            #We take the email and password from user as inputs and compare them to see if they match what is in our file
    
            emailinput = input("Enter your Email: ")
            passwordinput = input("Enter your Password: ")

            #We go through the users that is in our file by reading them one by one: self.users = load_users() to find a match
            for user in self.users:
                if user["email"] == emailinput and user["password"] == passwordinput:
                        print("You are now logged into our ReservationSystem")
                        self.current_user = user
                        self.ReservationMenu()
                        userVerified = True
                        return

            #if the user does not exist or mistakenly spelt their email or password it will keep this variable as false and run these if statements   
            if userVerified == False:

                #This will give a set of options what the user can do now if they messed up their login information or if they don't have an account
                print("The password and/or username is incorrect\n")
                print("What do you want to do now?")
                print("1. Try Logging in Again")
                print("2. Register for An Account")
                print("3. Exit")

                #We will take this input as a number and do things accordingly
                next_choice = input("Enter your choice: ")

                #If they want to login again we just start from the beginning of the loop by using continue and it will again prompt the user to put in their login information
            
                if next_choice == "1":
                    continue
                #If they don't have an account they type in 2 and they trigger the register_user() function to register the user into the system and save it into our file
                elif next_choice == "2":
                    login_userswitch = False
                    self.register_user()
                    
                #if they don't want to login again or want to register for an account they will go back to the mainMenu() where they can exit the program from there            
                elif next_choice == "3":
                    login_userswitch = False
                    self.mainMenu()

                #Otherwise if they type anything other than these 3 options it will read it as an invalid option and tell them to try again (heading back to the top of this while loop)        
                else:
                    print("Invalid Choice Try Again")

    #This function focuses on grabbing user inputs for either signing up or logging into the ReservationSystem
    # The user can log out by pressing 3, any other input other than 1, 2 or 3 is not accepted in this program
    def runMainMenu(self):
        onSwitch = True
        while onSwitch == True:
            self.mainMenu()
            choiceSelect = input("Enter your choice: ")

            if choiceSelect == "1":
                print("\nRegister/Signup selected")
                self.register_user()
            elif choiceSelect == "2":
                print("\nLogin selected")
                self.login_user()
            elif choiceSelect == "3":
                print("\n Thank you for using our Reservation System")
                onSwitch = False
            else:
                print("The choice you have selected is invalid. Try Again.")
    
#Part 2 Building the User (Changes are made in the ReservationSystem class)
class User:
    #When there is a user in the ReservationSystem, the user must have these properties in order to be a user in the system
    def __init__(self, email, first_name, last_name, password, date_of_birth):
        self.email = email
        self.first_name = first_name
        self.last_name = last_name
        self.password = password
        self.date_of_birth = date_of_birth

    #This function is used to save the user data using a dictonary type format. Example: "email" is a keyword for the user's email
    #This will then be saved in a json file where all of the user's information will easily be displayed for us to read.
    def user_data(self):
        return {
            "email": self.email,
            "first_name": self.first_name,
            "last_name": self.last_name,
            "password": self.password,
            "date_of_birth": self.date_of_birth
            }
    
    

system = ReservationSystem()
system.runMainMenu()

