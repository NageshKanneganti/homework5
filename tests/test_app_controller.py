'''Test for app_controller.py'''
import pytest
from app.app_controller import AppController

@pytest.fixture
def app_controller():
    '''Fixture function to create an instance of AppController for testing.'''
    return AppController()

def test_app_controller_start_exit_command(capfd, monkeypatch, app_controller):
    '''Test that the application exits correctly on 'exit' command.'''
    # Simulate user entering 'exit'
    monkeypatch.setattr('builtins.input', lambda _: 'exit')

    # Call start() method of AppController
    app_controller.start()

    out, _ = capfd.readouterr()

    # Check that the initial greeting is printed and the application exits gracefully
    assert "Hello World! Type 'exit' to quit application." in out
    assert "Exiting..." in out

def test_app_controller_start_unknown_command(capfd, monkeypatch, app_controller):
    '''Test how the application handles an unknown command before exiting.'''
    # Simulate user entering an unknown command followed by 'exit'
    inputs = iter(['unknown_command', 'exit'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))

    # Call start() method of AppController
    app_controller.start()

    out, _ = capfd.readouterr()

    # Check that the application responds to an unknown command and then exits after 'exit' command
    assert "Hello World! Type 'exit' to quit application." in out
    assert "Unknown command. Type 'exit' to quit application." in out
    assert "Exiting..." in out
