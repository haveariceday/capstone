def handle_input(command):
    if command == "quit":
        print("Game over. Thanks for playing!")
        return False

    if command.startswith(actions['go']):
        destination = command.split(actions["go"])[1].strip()
        move_to_room(player["current_room"], destination)
    elif command.startswith(actions["look"]):
        look_around(player["current_room"])
    elif command.startswith(actions["take"]):
        item = command.split(actions["take"])[1].strip()
        take_item(player["current_room"], item)
    elif command.startswith(actions["use"]):
        item = command.split(actions["use"])[1].strip()
        use_item(player["current_room"], item)
    else:
        print("Unknown command.")
    return True

def play_game():
    print("Welcome to the Escape Room Text Adventure Game!")
    player["name"] = input("Enter your name: ")
    print("Hello, " + player["name"] + "! Let's begin. Type 'help' for details about the game")
    # current_room = player["current_room"]
    display_status()

    game_running = True
    while game_running:
        command = input("Enter a command: ")
        print("command print: ", command)
        else:
            game_running = handle_input(command)


# Start the game
play_game()