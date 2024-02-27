'''Test for app_meny.py'''
from app.app_menu import AppMenu

def test_app_start_exit_command(capfd, monkeypatch):
    '''Test that the REPL exits correctly on 'exit' command.'''
    # Create an instance of AppMenu
    menu = AppMenu()

    # Simulate user entering 'exit'
    monkeypatch.setattr('builtins.input', lambda _: 'exit')

    # Call show_menu() on the instance of AppMenu
    menu.show_menu()

    out, _ = capfd.readouterr()

    # Check that the initial greeting is printed and the REPL exits gracefully
    assert "Hello World! Type 'exit' to quit application." in out
    assert "Exiting..." in out

def test_app_start_unknown_command(capfd, monkeypatch):
    '''Test how the REPL handles an unknown command before exiting.'''
    # Create an instance of AppMenu
    menu = AppMenu()

    # Simulate user entering an unknown command followed by 'exit'
    inputs = iter(['unknown_command', 'exit'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))

    # Call show_menu() on the instance of AppMenu
    menu.show_menu()

    out, _ = capfd.readouterr()

    # Check that the REPL responds to an unknown command and then exits after 'exit' command
    assert "Hello World! Type 'exit' to quit application." in out
    assert "Unknown command. Type 'exit' to quit application." in out
    assert "Exiting..." in out
