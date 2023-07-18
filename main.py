# Escape Room Text Adventure Game

# Define player attributes
player = {
    "name": "",
    "health": 100,
    "inventory": []
}

# Define game rooms and their descriptions
rooms = {

    # "lobby": {
    #     "description": "You are in the lobby of an old mansion.",
    #     "exits": ["kitchen", "living room", "hallway"],
    #     "items": ["key"]
    # },
    # "kitchen": {
    #     "description": "You are in a dusty kitchen with old appliances.",
    #     "exits": ["lobby"],
    #     "items": ["knife"]
    # },
    # "living room": {
    #     "description": "You are in a grand living room with antique furniture.",
    #     "exits": ["lobby", "dining room"],
    #     "items": ["book"]
    # },
    # "hallway": {
    #     "description": "You are in a dimly lit hallway with many doors.",
    #     "exits": ["lobby", "bedroom"],
    #     "items": []
    # },
    # "dining room": {
    #     "description": "You are in an elegant dining room with a large table.",
    #     "exits": ["living room"],
    #     "items": []
    # },
    # "bedroom": {
    #     "description": "You are in a creepy bedroom with a creaky bed.",
    #     "exits": ["hallway"],
    #     "items": ["flashlight"]
    # }
}

# Define game actions
actions = {
    "look": "look around",
    "go": "go to",
    "take": "take item",
    "use": "use item"
}


# Function to display the player's current status
def display_status():
    print("Player: " + player["name"])
    print("Health: " + str(player["health"]))
    print("Inventory: " + str(player["inventory"]))


# Function to handle player input and perform actions
def handle_input(command):
    if command == "quit":
        print("Game over. Thanks for playing!")
        return False

    if command.startswith(actions["go"]):
        destination = command.split(actions["go"])[1].strip()
        move_to_room(destination)
    elif command.startswith(actions["look"]):
        look_around()
    elif command.startswith(actions["take"]):
        item = command.split(actions["take"])[1].strip()
        take_item(item)
    elif command.startswith(actions["use"]):
        item = command.split(actions["use"])[1].strip()
        use_item(item)
    else:
        print("Unknown command.")

    return True


# Function to move the player to a new room
def move_to_room(destination):
    if destination in rooms[current_room]["exits"]:
        current_room = destination
        print("Moving to " + destination + "...")
        print(rooms[current_room]["description"])
    else:
        print("You cannot go to " + destination + ".")


# Function to look around the current room
def look_around():
    print(rooms[current_room]["description"])


# Function to take an item and add it to the player's inventory
def take_item(item):
    if item in rooms[current_room]["items"]:
        player["inventory"].append(item)
        rooms[current_room]["items"].remove(item)
        print("You have taken the " + item + ".")
    else:
        print("There is no " + item + " here.")


# Function to use an item and perform a specific action
def use_item(item):
    if item == "key" and current_room == "bedroom":
        print("You have unlocked a hidden compartment!")
        # Additional game logic for unlocking the secret
    elif item == "flashlight" and current_room == "kitchen":
        print("You have found a hidden clue!")
        # Additional game logic for revealing the clue
    else:
        print("You cannot use the " + item + " here.")


# Main game loop
def play_game():
    print("Welcome to the Escape Room Text Adventure Game!")
    player["name"] = input("Enter your name: ")
    print("Hello, " + player["name"] + "! Let's begin.")
    current_room = "lobby"
    display_status()

    game_running = True
    while game_running:
        command = input("Enter a command: ")
        game_running = handle_input(command)


# Start the game
play_game()