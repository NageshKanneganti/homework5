'''app_menu.py: Menu module responsible for handling the application menu.'''

class AppMenu:
    '''Class responsible for handling the application menu.'''

    def show_menu(self):
        '''Display the menu options to the user and handle user input.'''
        # Display initial greeting message
        print("Hello World! Type 'exit' to quit application.")

        while True:
            # Get user input
            user_input = input(">>> ")

            # Check if user wants to exit
            if user_input.lower() == 'exit':
                print("Exiting...")
                break
            else:
                # Display message for unknown command
                print("Unknown command. Type 'exit' to quit application.")
