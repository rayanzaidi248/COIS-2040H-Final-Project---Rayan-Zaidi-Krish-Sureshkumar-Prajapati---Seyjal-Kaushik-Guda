#Final Project Assignment
#Restaurant Reservation System
#Group Members: Rayan Zaidi & Krish Sureshkumar Prajapati & Seyjal

#Importing certain plugins for file access and reading files

import json
import os
import re

#Part 1 of ReservationSystem

class ValidationError(Exception):
    pass

class ReservationSystem:

    #Specifies the file where we are going to be saving our user information in (users.json)
    def __init__(self):
        self.file_name = "users.json"
        self.users = self.load_users()

    #This function is used for already saved users in the ReservationSystem. It's job is to read the file containing the user's input of their email, name, password and date of birth
    def load_users(self):
        if os.path.exists(self.file_name):
            with open(self.file_name, "r") as file:
                return json.load(file)
        else:
            #Otherwise return an empty list if the file doesn't exist or does not have any content in it yet.
            return[]
        
    #This function's job is to write down information that is being inputted by the user when registering in the system and save it in the file we just created (users.json file)
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

    #This function is used to check if the email is a valid email that is inputted by the user
    def email_validation(self, email):
        #We use a Regex pattern to determine if the email is a valid email
        #Regex is used in python to manipulate complex text patterns which in this case an email is a complex text pattern with an @ sign and
        #a dot symbolizing either it is .com, .ca etc.
        emailPattern = r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$"

        #if the email doesn't have the general email pattern, then it has an invalid email format.
        if not re.match(emailPattern, email):
            raise ValidationError("Invalid Email Format")
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
        password = self.userInput("Password: ")
        date_of_birth = self.userInput("Date Of Birth: ")

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

        
            
            

    #This function focuses on grabbing user inputs for either signing up or logging into the ReservationSystem
    # The user can log out by pressing 3, any other input other than 1, 2 or 3 is not accepted in this program
    def run(self):
        onSwitch = True
        while onSwitch == True:
            self.mainMenu()
            choiceSelect = input("Enter your choice: ")

            if choiceSelect == "1":
                print("\nRegister/Signup selected")
                self.register_user()
            elif choiceSelect == "2":
                print("\nLogin selected")
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
system.run()
#Group Members: Rayan Zaidi, Krish Sureshkumar Prajapati & Seyjal Kaushik Guda
