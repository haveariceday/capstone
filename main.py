# Escape Room Text Adventure Game
import random

# Define player attributes
player = {
    "name": "",
    "oxygen_level": 100,
    "inventory": ["air tank"],
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
    "go": "go to",  #unnecessary
    "take": "take",
    "use": "use"
}


# Function to display the player's current status
def display_status():
    print("Player: " + player["name"])
    print("Oxygen Level: " + str(player["oxygen_level"]))
    print("Inventory: " + str(player["inventory"]))
    print("Current location: " + str(player["current_room"]))


# Function to handle player input and perform actions
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
def take_item(current_room, item):
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
    elif item == "air tank":
        print("You must unlock this air tank by solving a riddle, if you are successful, your oxygen will increase by "
              "5, if you are unsuccessful, your oxygen will decrease by 2")
        choice = input("Do you wish to solve the riddle?")
        if choice == "yes":
            air_tank_riddle()
        else:
            pass
    else:
        print("You cannot use the " + item + " here.")


def air_tank_riddle():
    riddles = {
        "Riddle 1": {
            "riddle": "A treasure sought by pirates bold,\nBuried deep in sand and gold.\n'X' marks the spot, a map to guide,\nWhere is this chest of wealth and pride?",
            "answer": "Treasure chest"
        },
        "Riddle 2": {
            "riddle": "Upon the waves, a ship I steer,\nA skull and bones flag, a sight of fear.\nMy crew and I sail, seeking the loot,\nWhat am I, the terror of the route?",
            "answer": "Pirate ship"
        },
        "Riddle 3": {
            "riddle": "With a peg leg and eye patch, I roam,\nSearching for treasures and tales to be known.\nIn tales of the sea, I'm a legend renowned,\nWho am I, with a parrot and a hound?",
            "answer": "Pirate captain"
        },
        "Riddle 4": {
            "riddle": "An island hideout, a pirate's reprieve,\nCaves and coves where secrets weave.\nWhispers of gold and maps are shared,\nWhat place is this, where pirate legends dared?",
            "answer": "Secret island"
        },
        "Riddle 5": {
            "riddle": "Through storms and calms, my compass true,\nGuiding to riches, the old and the new.\nI point to fortune, adventure untold,\nWhat instrument am I, made of metal and bold?",
            "answer": "Compass"
        }
    }

    # Select a random riddle
    random_riddle_name = random.choice(list(riddles.keys()))
    selected_riddle = riddles[random_riddle_name]

    # Display the riddle and get player's answer
    print(selected_riddle["riddle"])
    user_answer = input("Your answer: ")

    # Check if the answer is correct
    if user_answer.lower() == selected_riddle["answer"].lower():
        print("Correct! Your oxygen level increases by 5.")
        player["oxygen_level"] += 5
    else:
        print("Incorrect. Your oxygen level decreases by 2.")
        player["oxygen_level"] -= 2


def scramble_word(current_room):
    room_word_associations = {
        "lodging": "Beds",
        "theatre": "Stage",
        "nightclub": "Dance",
        "casino": "Gamble",
        "buffet": "Food",
        "crews break room": "Rest",
        "steering room": "Helm",
        "kitchen": "Cook",
        "backstage": "Props",
        "engine room": "Machinery"
    }

    if current_room in room_word_associations:
        original_word = room_word_associations[current_room].replace(" ", "").upper()
        scrambled_word = list(original_word)
        random.shuffle(scrambled_word)
        scrambled = ''.join(scrambled_word)

        print(f"Unscramble the following word associated with the {current_room}:")
        print(scrambled)

        player_guess = input("Your guess: ")

        if player_guess.upper() == original_word:
            print(f"Correct! You unscrambled the word for the {current_room}.")
            return True
        else:
            print("Incorrect. Try again.")
            return False
    else:
        print(f"There's no word association available for the {current_room}.")
        return False


def choose_random_word():
    word_list = ["chest", "skull", "sword", "storm"]
    return random.choice(word_list)


def get_guess():
    while True:
        guess = input("Enter your 5-letter word guess: ").lower()
        if len(guess) == 5 and guess.isalpha():
            return guess
        else:
            print("Please enter a valid 5-letter word.")


def evaluate_guess(hidden_word, guess):
    if guess == hidden_word:
        player["oxygen_level"] += 10
        return "You guessed the word! Congratulations! You earned 10 oxygen level"

    feedback = []
    for i in range(5):
        if guess[i] == hidden_word[i]:
            feedback.append(guess[i])
        elif guess[i] in hidden_word:
            feedback.append("O")
        else:
            feedback.append(".")

    return " ".join(feedback)


def wordle():
    hidden_word = choose_random_word()
    attempts = 6

    print("Welcome to Wordle! You have 6 attempts to guess two letters to complete a word.")
    print("If you get within the limit, the oxygen will increase by 10, your oxygen will decrease by 2 every time you have a wrong guess."
          "In this game O means that the letter exists in the letter but not in order. The dot . means the letter does not exist in the word."
          "If the letter you guessed is in the right place, then the letter shows up on the correct position.")
    for attempt in range(1, attempts + 1):
        print(f"Attempt {attempt}:")
        guess = get_guess()
        result = evaluate_guess(hidden_word, guess)
        print(result)

        if result == "You guessed the word! Congratulations! You earned 10 oxygen level":
            break
        else:
            player["oxygen_level"] -= 2
            print("Your guess is wrong. Your oxygen decreased by 2.")

    if result != "You guessed the word! Congratulations! You earned 10 oxygen level":
        print(f"Sorry, you're out of attempts. The word was '{hidden_word}'.")

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
    print("Current location: " + player["current_room"])
    print("     __________________________________________")
    print("   _/|      _______                           |")
    print(" _/  |  2   +  3  |   4   |   5    |          |")
    print("/  1 |______+_++__|__++___|__++____|          |")
    print("\_   +      |     |       |        |    10    |")
    print("  \_ +  6   +  7  +   8   |   9    |          |")
    print("    \|______+_____+_______|________|__________|")
    print(
        "1. steering room, 2. buffet, 3. kitchen, 4.theatre, 5. casino, 6.engine room, 7.crew break room, 8. back stage, 9.nightclub, 10. lodging")

def check_oxygen_level():
    if player['oxygen_level'] <= 0:
        print("Your oxygen level has dropped to 0 or below. You can't breathe anymore.")
        print("Game Over.")
        # You can add further actions here, like asking the player if they want to restart or exit.
        # For simplicity, this function just ends the game.
        exit()  # This exits the game. You can replace it with other actions as needed.

# Main game loop
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
        if command == "help":
            display_help()
        else:
            check_oxygen_level()
            game_running = handle_input(command)
            wordle()
            check_oxygen_level()


# Start the game
play_game()
