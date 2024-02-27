'''main.py: Main module of the application.'''

from app.app_controller import AppController

if __name__ == "__main__":
    # Initialize the application controller
    controller = AppController()
    
    # Start the application
    controller.start()
