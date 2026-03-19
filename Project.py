#Final Project Assignment
#Restaurant Reservation System
#Group Members: Rayan Zaidi & Krish Sureshkumar Prajapati

#Part 1 of ReservationSystem
class ReservationSystem:
    def mainMenu(self):
        print("\n========== Restaurant Reservation System ==========")
        print("1. Register/Signup")
        print("2. Login")
        print("3. Exit")
        print("=============================================")

    def run(self):
        onSwitch = True
        while onSwitch == True:
            self.mainMenu()
            choiceSelect = input("Enter your choice: ")

            if choiceSelect == "1":
                print("\nRegister/Signup selected")
            elif choiceSelect == "2":
                print("\nLogin selected")
            elif choiceSelect == "3":
                print("\n Thank you for using our Reservation System")
                onSwitch = False
                
            else:
                print("The choice you have selected is invalid. Try Again.")


system = ReservationSystem()
system.run()
