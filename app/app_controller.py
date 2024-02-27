'''app_controller.py: Controller module responsible for managing the flow of the application.'''

from app.app_menu import AppMenu

class AppController:
    '''Controller class responsible for managing the flow of the application.'''

    def __init__(self):
        '''Initialize the AppController.'''
        # Create an instance of the menu
        self.menu = AppMenu()

    def start(self):
        '''Start the application.'''
        # Show the menu to the user
        self.menu.show_menu()
