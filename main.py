print("Welcome to data analysis bot, this project is to help me get a better understanding data base files in python.")

launch_options = ["store data", "advanced commands"]
options = ["integer", "sentence", "password"]

while True:
    action_to_take = input(f"Would you like to {launch_options[0]} or see {launch_options[1]}? ")

    if action_to_take.lower() == launch_options[0]:
        print("You have selected Store Data, please enter 'back' to go back to the previous selection")

        while True:
            # Prompt user for the type of information to store
            info_type = input(f"What type of info would you like to store? {options}. Type 'exit' to quit. ")

            # Check if the user wants to exit
            if info_type.lower() == "exit":
                print("Exiting data analysis bot.")
                break
            elif info_type.lower() == "back":
                break

            # Check if the input is a valid option
            if info_type.lower() not in options:
                print("This is not a valid option type.")
                continue

            # Prompt user for the information to store
            info_to_store = input("Enter the information you'd like to store: ")

            # Open a file for appending (creates a new file if it doesn't exist)
            with open("data.txt", "a") as f:
                # Check if the file already has information, if so, write to a new line
                if f.tell() != 0:
                    f.write("\n")
                # Write the stored information to the file
                f.write(f"{info_type}: {info_to_store}")

            # Print out a message to confirm that the information was successfully stored
            print("Information stored in file.")

    elif action_to_take.lower() == launch_options[1]:
        print(""""*feature not currently in use*" You have selected Advanced Commands, please enter 'back' to go back to the previous selection""")

        # Add advanced commands here

    else:
        print("Invalid option. Please try again.")