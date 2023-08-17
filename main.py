# Escape Room Text Adventure Game

# Define player attributes
player = {
    "name": "",
    "health": 100,
    "inventory": [],
    "current_room": "lobby"
}

# Define game rooms and their descriptions
rooms = {
    # "lodging": {
    #     "description": "",
    #     "exits": [casino,theatre,buffet],
    #     "items": [""]
    # },
    # "theatre": {
    #     "description": "",
    #     "exits": [buffet, casino,backstage,lodging],
    #     "items": [""]
    # },
    # "nightclub": {
    #     "description": "",
    #     "exits": [casino],
    #     "items": [""]
    # },
    # "casino": {
    #     "description": "",
    #     "exits": [nightclub,theatre,lodging,buffet],
    #     "items": [""]
    # },
    # "buffet": {
    #     "description": "",
    #     "exits": [nightclub,theatre,lodging,kitchen],
    #     "items": [""]
    # },
    # "crews break room": {
    #     "description": "",
    #     "exits": [kitchen, engine room,backstage],
    #     "items": [""]
    # },
    # "steering room": {
    #     "description": "",
    #     "exits": [engine room],
    #     "items": [""]
    # },
    # "kitchen": {
    #     "description": "",
    #     "exits": [buffet, crew break room],
    #     "items": [""]
    # },
    # "backstage": {
    #     "description": "",
    #     "exits": [theatre, crew break room],
    #     "items": [""]
    # },
    # "engine room": {
    #     "description": "",
    #     "exits": [steering room, crew break room],
    #     "items": [""]
    # }

    "lobby": {
        "description": "You are in the lobby of an old mansion.",
        "exits": ["kitchen", "living room", "hallway"],
        "items": ["key"]
    },
    "kitchen": {
        "description": "You are in a dusty kitchen with old appliances.",
        "exits": ["lobby"],
        "items": ["knife"]
    },
    "living room": {
        "description": "You are in a grand living room with antique furniture.",
        "exits": ["lobby", "dining room"],
        "items": ["book"]
    },
    "hallway": {
        "description": "You are in a dimly lit hallway with many doors.",
        "exits": ["lobby", "bedroom"],
        "items": []
    },
    "dining room": {
        "description": "You are in an elegant dining room with a large table.",
        "exits": ["living room"],
        "items": []
    },
    "bedroom": {
        "description": "You are in a creepy bedroom with a creaky bed.",
        "exits": ["hallway"],
        "items": ["flashlight"]
    }
}

# Define game actions
actions = {
    "look": "look around",
    "go": "go to",
    "take": "take",
    "use": "use"
}


# Function to display the player's current status
def display_status():
    print("Player: " + player["name"])
    print("Health: " + str(player["health"]))
    print("Inventory: " + str(player["inventory"]))
    print("Current location: " + str(player["current_room"]))


# Function to handle player input and perform actions
def handle_input(command):
    if command == "quit":
        print("Game over. Thanks for playing!")
        return False

    if command.startswith(actions['go']):
        destination = command.split(actions["go"])[1].strip()
        move_to_room(player["current_room"],destination)
    elif command.startswith(actions["look"]):
        look_around(player["current_room"])
    elif command.startswith(actions["take"]):
        item = command.split(actions["take"])[1].strip()
        take_item(player["current_room"],item)
    elif command.startswith(actions["use"]):
        item = command.split(actions["use"])[1].strip()
        use_item(player["current_room"],item)
    else:
        print("Unknown command.")
    return True


# Function to move the player to a new room
def move_to_room(current_room, destination):
    if destination in rooms[current_room]["exits"]:
        print("Moving to " + destination + "...")
        current_room = str(destination)
        player["current_room"] = str(destination)
        print(rooms[current_room]["description"])
    else:
        print("You cannot go to " + destination + ".")


# Function to look around the current room
def look_around(current_room):
    print(rooms[current_room]["description"])


# Function to take an item and add it to the player's inventory
def take_item(current_room,item):
    if item in rooms[current_room]["items"]:
        player["inventory"].append(item)
        rooms[current_room]["items"].remove(item)
        print("You have taken the " + item + ".")
    else:
        print("There is no " + item + " here.")


# Function to use an item and perform a specific action
def use_item(current_room, item):
    if item == "key" and current_room == "bedroom":
        print("You have unlocked a hidden compartment!")
        # Additional game logic for unlocking the secret
    elif item == "flashlight" and current_room == "kitchen":
        print("You have found a hidden clue!")
        # Additional game logic for revealing the clue
    else:
        print("You cannot use the " + item + " here.")

def display_help():
    print("--- COMMAND OPTIONS---")
    print("1. go to [location name]")
    print("2. look")
    print("3. inspect [item name]")
    print("4. take [item name]")
    print("5. use [item name]")
    print("6. quit")
    print("")
    print("--- MAP ---")
    print("     __________________________________________")
    print("   _/|      _______                           |")
    print(" _/  |  2   +  3  |   4   |   5    |          |")
    print("/  1 |______+_++__|__++___|__++____|          |")
    print("\_   +      |     |       |        |    10    |")
    print("  \_ +  6   +  7  +   8   |   9    |          |")
    print("    \|______+_____+_______|________|__________|")
    print("1. steering room, 2. buffet, 3. kitchen, 4.theatre, 5. casino, 6.engine room, 7.crew break room, 8. back stage, 9.nightclub, 10. lodging")

# Main game loop
def play_game():
    print("Welcome to the Escape Room Text Adventure Game!")
    player["name"] = input("Enter your name: ")
    print("Hello, " + player["name"] + "! Let's begin. Type 'help' for details about the game")
    #current_room = player["current_room"]
    display_status()

    game_running = True
    while game_running:
        command = input("Enter a command: ")
        print("command print: ", command)
        if command == "help":
            display_help()
        else:
            game_running = handle_input(command)


# Start the game
play_game()
