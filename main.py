# # Escape Room Text Adventure Game
# import random
#
# # Define player attributes
# player = {
#     "name": "",
#     "oxygen_level": 100,
#     "inventory": ["air tank"],
#     "current_room": "lobby"
# }
#
# # Define game rooms and their descriptions
# rooms = {
#     # "lodging": {
#     #     "description": "",
#     #     "exits": [casino,theatre,buffet],
#     #     "items": [""]
#     # },
#     # "theatre": {
#     #     "description": "",
#     #     "exits": [buffet, casino,backstage,lodging],
#     #     "items": [""]
#     # },
#     # "nightclub": {
#     #     "description": "",
#     #     "exits": [casino],
#     #     "items": [""]
#     # },
#     # "casino": {
#     #     "description": "",
#     #     "exits": [nightclub,theatre,lodging,buffet],
#     #     "items": [""]
#     # },
#     # "buffet": {
#     #     "description": "",
#     #     "exits": [nightclub,theatre,lodging,kitchen],
#     #     "items": [""]
#     # },
#     # "crews break room": {
#     #     "description": "",
#     #     "exits": [kitchen, engine room,backstage],
#     #     "items": [""]
#     # },
#     # "steering room": {
#     #     "description": "",
#     #     "exits": [engine room],
#     #     "items": [""]
#     # },
#     # "kitchen": {
#     #     "description": "",
#     #     "exits": [buffet, crew break room],
#     #     "items": [""]
#     # },
#     # "backstage": {
#     #     "description": "",
#     #     "exits": [theatre, crew break room],
#     #     "items": [""]
#     # },
#     # "engine room": {
#     #     "description": "",
#     #     "exits": [steering room, crew break room],
#     #     "items": [""]
#     # }
#
#     "lobby": {
#         "description": "You are in the lobby of an old mansion.",
#         "exits": ["kitchen", "living room", "hallway"],
#         "items": ["key"]
#     },
#     "kitchen": {
#         "description": "You are in a dusty kitchen with old appliances.",
#         "exits": ["lobby"],
#         "items": ["knife"]
#     },
#     "living room": {
#         "description": "You are in a grand living room with antique furniture.",
#         "exits": ["lobby", "dining room"],
#         "items": ["book"]
#     },
#     "hallway": {
#         "description": "You are in a dimly lit hallway with many doors.",
#         "exits": ["lobby", "bedroom"],
#         "items": []
#     },
#     "dining room": {
#         "description": "You are in an elegant dining room with a large table.",
#         "exits": ["living room"],
#         "items": []
#     },
#     "bedroom": {
#         "description": "You are in a creepy bedroom with a creaky bed.",
#         "exits": ["hallway"],
#         "items": ["flashlight"]
#     }
# }
#
# # Define game actions
# actions = {
#     "look": "look around",
#     "go": "go to",  #unnecessary
#     "take": "take",
#     "use": "use"
# }
#
#
# # Function to display the player's current status
# def display_status():
#     print("Player: " + player["name"])
#     print("Oxygen Level: " + str(player["oxygen_level"]))
#     print("Inventory: " + str(player["inventory"]))
#     print("Current location: " + str(player["current_room"]))
#
#
# # Function to handle player input and perform actions
# def handle_input(command):
#     if command == "quit":
#         print("Game over. Thanks for playing!")
#         return False
#
#     if command.startswith(actions['go']):
#         destination = command.split(actions["go"])[1].strip()
#         move_to_room(player["current_room"], destination)
#     elif command.startswith(actions["look"]):
#         look_around(player["current_room"])
#     elif command.startswith(actions["take"]):
#         item = command.split(actions["take"])[1].strip()
#         take_item(player["current_room"], item)
#     elif command.startswith(actions["use"]):
#         item = command.split(actions["use"])[1].strip()
#         use_item(player["current_room"], item)
#     else:
#         print("Unknown command.")
#     return True
#
#
# # Function to move the player to a new room
# def move_to_room(current_room, destination):
#     if destination in rooms[current_room]["exits"]:
#         print("Moving to " + destination + "...")
#         current_room = str(destination)
#         player["current_room"] = str(destination)
#         print(rooms[current_room]["description"])
#     else:
#         print("You cannot go to " + destination + ".")
#
#
# # Function to look around the current room
# def look_around(current_room):
#     print(rooms[current_room]["description"])
#
#
# # Function to take an item and add it to the player's inventory
# def take_item(current_room, item):
#     if item in rooms[current_room]["items"]:
#         player["inventory"].append(item)
#         rooms[current_room]["items"].remove(item)
#         print("You have taken the " + item + ".")
#     else:
#         print("There is no " + item + " here.")
#
#
# # Function to use an item and perform a specific action
# def use_item(current_room, item):
#     if item == "key" and current_room == "bedroom":
#         print("You have unlocked a hidden compartment!")
#         # Additional game logic for unlocking the secret
#     elif item == "flashlight" and current_room == "kitchen":
#         print("You have found a hidden clue!")
#         # Additional game logic for revealing the clue
#     elif item == "air tank":
#         print("You must unlock this air tank by solving a riddle, if you are successful, your oxygen will increase by "
#               "5, if you are unsuccessful, your oxygen will decrease by 2")
#         choice = input("Do you wish to solve the riddle?")
#         if choice == "yes":
#             air_tank_riddle()
#         else:
#             pass
#     else:
#         print("You cannot use the " + item + " here.")
#
#
# def air_tank_riddle():
#     riddles = {
#         "Riddle 1": {
#             "riddle": "A treasure sought by pirates bold,\nBuried deep in sand and gold.\n'X' marks the spot, a map to guide,\nWhere is this chest of wealth and pride?",
#             "answer": "Treasure chest"
#         },
#         "Riddle 2": {
#             "riddle": "Upon the waves, a ship I steer,\nA skull and bones flag, a sight of fear.\nMy crew and I sail, seeking the loot,\nWhat am I, the terror of the route?",
#             "answer": "Pirate ship"
#         },
#         "Riddle 3": {
#             "riddle": "With a peg leg and eye patch, I roam,\nSearching for treasures and tales to be known.\nIn tales of the sea, I'm a legend renowned,\nWho am I, with a parrot and a hound?",
#             "answer": "Pirate captain"
#         },
#         "Riddle 4": {
#             "riddle": "An island hideout, a pirate's reprieve,\nCaves and coves where secrets weave.\nWhispers of gold and maps are shared,\nWhat place is this, where pirate legends dared?",
#             "answer": "Secret island"
#         },
#         "Riddle 5": {
#             "riddle": "Through storms and calms, my compass true,\nGuiding to riches, the old and the new.\nI point to fortune, adventure untold,\nWhat instrument am I, made of metal and bold?",
#             "answer": "Compass"
#         }
#     }
#
#     # Select a random riddle
#     random_riddle_name = random.choice(list(riddles.keys()))
#     selected_riddle = riddles[random_riddle_name]
#
#     # Display the riddle and get player's answer
#     print(selected_riddle["riddle"])
#     user_answer = input("Your answer: ")
#
#     # Check if the answer is correct
#     if user_answer.lower() == selected_riddle["answer"].lower():
#         print("Correct! Your oxygen level increases by 5.")
#         player["oxygen_level"] += 5
#     else:
#         print("Incorrect. Your oxygen level decreases by 2.")
#         player["oxygen_level"] -= 2
#
#
# def scramble_word(current_room):
#     room_word_associations = {
#         "lodging": "Beds",
#         "theatre": "Stage",
#         "nightclub": "Dance",
#         "casino": "Gamble",
#         "buffet": "Food",
#         "crews break room": "Rest",
#         "steering room": "Helm",
#         "kitchen": "Cook",
#         "backstage": "Props",
#         "engine room": "Machinery"
#     }
#
#     if current_room in room_word_associations:
#         original_word = room_word_associations[current_room].replace(" ", "").upper()
#         scrambled_word = list(original_word)
#         random.shuffle(scrambled_word)
#         scrambled = ''.join(scrambled_word)
#
#         print(f"Unscramble the following word associated with the {current_room}:")
#         print(scrambled)
#
#         player_guess = input("Your guess: ")
#
#         if player_guess.upper() == original_word:
#             print(f"Correct! You unscrambled the word for the {current_room}.")
#             return True
#         else:
#             print("Incorrect. Try again.")
#             return False
#     else:
#         print(f"There's no word association available for the {current_room}.")
#         return False
#
#
# def choose_random_word():
#     word_list = ["chest", "skull", "sword", "storm"]
#     return random.choice(word_list)
#
#
# def get_guess():
#     while True:
#         guess = input("Enter your 5-letter word guess: ").lower()
#         if len(guess) == 5 and guess.isalpha():
#             return guess
#         else:
#             print("Please enter a valid 5-letter word.")
#
#
# def evaluate_guess(hidden_word, guess):
#     if guess == hidden_word:
#         return "You guessed the word! Congratulations!"
#
#     feedback = []
#     for i in range(5):
#         if guess[i] == hidden_word[i]:
#             feedback.append(guess[i])
#         elif guess[i] in hidden_word:
#             feedback.append("O")
#         else:
#             feedback.append(".")
#
#     return " ".join(feedback)
#
#
# def wordle():
#     hidden_word = choose_random_word()
#     attempts = 6
#
#     print("Welcome to Wordle! You have 6 attempts to guess two letters to complete a word.")
#
#     for attempt in range(1, attempts + 1):
#         print(f"Attempt {attempt}:")
#         guess = get_guess()
#         result = evaluate_guess(hidden_word, guess)
#         print(result)
#
#         if result == "You guessed the word! Congratulations!":
#             break
#
#     if result != "You guessed the word! Congratulations!":
#         print(f"Sorry, you're out of attempts. The word was '{hidden_word}'.")
#
# def display_help():
#     print("--- COMMAND OPTIONS---")
#     print("1. go to [location name]")
#     print("2. look")
#     print("3. inspect [item name]")
#     print("4. take [item name]")
#     print("5. use [item name]")
#     print("6. quit")
#     print("")
#     print("--- MAP ---")
#     print("Current location: " + player["current_room"])
#     print("     __________________________________________")
#     print("   _/|      _______                           |")
#     print(" _/  |  2   +  3  |   4   |   5    |          |")
#     print("/  1 |______+_++__|__++___|__++____|          |")
#     print("\_   +      |     |       |        |    10    |")
#     print("  \_ +  6   +  7  +   8   |   9    |          |")
#     print("    \|______+_____+_______|________|__________|")
#     print(
#         "1. steering room, 2. buffet, 3. kitchen, 4.theatre, 5. casino, 6.engine room, 7.crew break room, 8. back stage, 9.nightclub, 10. lodging")
#
# def check_oxygen_level():
#     if player['oxygen_level'] <= 0:
#         print("Your oxygen level has dropped to 0 or below. You can't breathe anymore.")
#         print("Game Over.")
#         # You can add further actions here, like asking the player if they want to restart or exit.
#         # For simplicity, this function just ends the game.
#         exit()  # This exits the game. You can replace it with other actions as needed.
#
# # Main game loop
# def play_game():
#     print("Welcome to the Escape Room Text Adventure Game!")
#     player["name"] = input("Enter your name: ")
#     print("Hello, " + player["name"] + "! Let's begin. Type 'help' for details about the game")
#     # current_room = player["current_room"]
#     display_status()
#
#     game_running = True
#     while game_running:
#         command = input("Enter a command: ")
#         print("command print: ", command)
#         if command == "help":
#             display_help()
#         else:
#             check_oxygen_level()
#             game_running = handle_input(command)
#             wordle()
#             check_oxygen_level()
#
#
# # Start the game
# play_game()

import json
import os
import random

def load_data(data_type):
    with open('gameSetup.json', 'r') as file:
        game_data = json.load(file)

    return game_data.get(data_type, {})


class Gameplay:
    def __init__(self):
        self.name = input("Enter your name: ")
        self.current_room = "room1"
        self.oxygen = 100
        self.inventory = []
        self.rooms_data = load_data('Rooms')
        self.objects_data = load_data('Objects')
        self.verbs_data = load_data('Verbs')
        self.features_data = load_data('Features')
        self.words_data = load_data('Words')
        self.riddles_data = load_data('Riddles')

    # def load_game_state(self, filename='saved_game.json'):
    #     if os.path.exists(filename):
    #         choice = input("Do you want to load a saved game? (yes/no): ").lower()
    #
    #         if choice == 'yes':
    #             with open(filename, 'r') as file:
    #                 game_state = json.load(file)
    #
    #             self.name = game_state.get('name', '')
    #             self.current_room = game_state.get('current_room', 'room1')
    #             self.oxygen = game_state.get('oxygen', 100)
    #             self.inventory = game_state.get('inventory', [])
    #             self.rooms_data = game_state.get('inventory', [])
    #             self.objects_data = game_state.get('inventory', [])
    #             self.verbs_data = game_state.get('inventory', [])
    #
    #             print(f"Welcome back, {self.name}!")
    #             return True
    #         else:
    #             print("Starting a new game.")
    #             return False
    #     else:
    #         return False


    def go(self, direction):
        # Make go able to be used without keyword go, if a direction or exit is
        # described
        #
        exits = list(self.rooms_data.get(self.current_room, {}).get('exits', {}).keys())

        if direction in exits:
            new_room = self.rooms_data.get(self.current_room, {}).get('exits', {}).get(direction)
            print(f"{self.name} is moving {direction} to {new_room}.")
            self.current_room = new_room
            entered_already = self.rooms_data.get(self.current_room, {}).get('entered_already')
            if entered_already == "False":
                self.look()
                self.rooms_data[self.current_room]['entered_already'] = True
            else:
                short_description = self.rooms_data.get(self.current_room, {}).get('short_description')
                print(short_description)
        else:
            print(f"There is no exit in the {direction} direction.")

    def look(self):
        room_description = self.rooms_data.get(self.current_room, {}).get('long_description', {})
        print(room_description)

    def look_at(self, item_name):
        if item_name in self.inventory:
            item_description = self.objects_data.get(item_name, {}).get('description')
            print(item_description)
        elif self.features_data.get(item_name, {}).get('room') == self.current_room:
            feature_description = self.features_data.get(item_name, {}).get('description')
            print(feature_description)
            # logic for playing games?
            game = self.features_data.get(item_name, {}).get('game')
            required_items = self.features_data.get(item_name, {}).get('required_item')
            if game:
                for item in required_items:
                    if item not in self.inventory:
                        self.parse_user_input(True)
                answer = input(f"play {game}(yes/no)?")
                if answer == 'yes':
                    self.play(game)

    def drop(self, item_name):
        if item_name in self.inventory:
            item = self.objects_data.get(item_name, {})
            item['room'] = self.current_room
            self.inventory.remove(item_name)
            print(f"{self.name} dropped the {item_name} in the {self.current_room}.")
        else:
            print(f"{self.name}, you don't have {item_name} in your inventory.")

    def take(self, item_name):
        if item_name in self.objects_data:
            item = self.objects_data[item_name]
            if item.get('room') == self.current_room:
                if item_name not in self.inventory:
                    self.inventory.append(item_name)
                    print(f"{self.name} took the {item_name}.")
                    item['room'] = None
                else:
                    print(f"{self.name}, you already have the {item_name} in your inventory.")
            else:
                print(f"{self.name}, there is no {item_name} in the current room.")
        else:
            print(f"{self.name}, there is no {item_name} in the game.")

    def eat(self, item_name):
        if item_name in self.inventory:
            self.inventory.remove(item_name)
            print(f"{self.name} ate the {item_name}. It disappears from your inventory.")
        else:
            print(f"{self.name}, you don't have {item_name} in your inventory.")

    def display_inventory(self):
        print(f"{self.name}'s Inventory: {', '.join(self.inventory)}")

    def save_game(self, filename='saved_game.json'):
        game_state = {
            'name': self.name,
            'current_room': self.current_room,
            'oxygen': self.oxygen,
            'inventory': self.inventory
        }

        with open(filename, 'w') as file:
            json.dump(game_state, file)

        print(f"Game state saved to {filename}.")

    def quit_game(self):
        print("Exiting the game. Goodbye!")
        exit()

    def display_help(self):
        valid_commands = load_data('Verbs').get('valid_commands', [])
        print("Available commands (verbs):", ', '.join(valid_commands))

    def play(self, game):
        def choose_random_word():
            word_list = ["chest", "skull", "sword", "storm", "ocean", "abyss"]
            return random.choice(word_list)

        def choose_hint(word):
            hints = {
                "chest": "This 5 letter word is associated with the upper part of your body ... It can also be related to a piece of furniture.",
                "skull": "This 5 letter word can protect your head especially your brain. What would it be?",
                "sword": "This 5 letter word is a weapon that was used in ancient times.",
                "storm": "This 5 letter word is a type of weather that you see when it rains.",
                "ocean": "This 5 letter word is a home to diverse rage of life and divided into zones like the abyssal and pelagic. What am I? ",
                "abyss": "refers to a deep and seemingly bottomless chasm or hole, often used metaphorically to describe a profound or infinite depth."
            }
            return hints[word]

        def get_guess():
            while True:
                    guess = input("Enter your 5-letter word guess: ").lower()
                    if len(guess) == 5 and guess.isalpha():
                        return guess
                    else:
                        print("Please enter a valid 5-letter word.")

        def evaluate_guess(hidden_word, guess):
            if guess == hidden_word:
                return "You guessed the word! Congratulations!"
            feedback = []
            for i in range(5):
                if guess[i] == hidden_word[i]:
                    feedback.append(guess[i])
                elif guess[i] in hidden_word:
                    feedback.append("O")
                else:
                    feedback.append(".")

            return " ".join(feedback)

        if game == "air_tank_riddle":

            # Select a random riddle
            random_riddle_name = random.choice(list(self.riddles_data.keys()))
            selected_riddle = self.riddles_data[random_riddle_name]

            # Display the riddle and get player's answer
            print(selected_riddle["riddle"])
            user_answer = input("Your answer: ")

            # Check if the answer is correct
            if user_answer.lower() == selected_riddle["answer"].lower():
                print("Correct! Your oxygen level increases by 5.")
                # player["oxygen_level"] += 5
            else:
                print("Incorrect. Your oxygen level decreases by 2.")
                # player["oxygen_level"] -= 2


        elif game == "scramble_word":
            original_word = random.choice(load_data('Words')).upper()
            print(original_word)
            scrambled_word = list(original_word)
            random.shuffle(scrambled_word)
            scrambled = ''.join(scrambled_word)

            print(f"Unscramble the following word:")
            print(scrambled)

            player_guess = input("Your guess: ")

            if player_guess.upper() == original_word:
                print("Correct! You unscrambled the word.")
            else:
                print("Incorrect. Try again.")

        elif game == "wordle":
            hidden_word = choose_random_word()
            hint = choose_hint(hidden_word)
            attempts = 6

            print("Welcome to Wordle! You have 6 chances to guess a randomly selected five-letter word.")
            print(hint)

            for attempt in range(1, attempts + 1):
                print(f"Attempt {attempt}:")
                guess = get_guess()
                result = evaluate_guess(hidden_word, guess)
                print(result)

                if result == "You guessed the word! Congratulations!":
                    break
                if attempt == attempts + 1:
                    print(f"Sorry, you're out of attempts. The word was '{hidden_word}'.")
        else:
            print("error")

    def parse_user_input(self, sameRoom = False):
        valid_commands = load_data('Verbs').get('valid_commands', [])
        exits = list(self.rooms_data.get(self.current_room, {}).get('exits', {}).keys())
        # if not self.load_game_state():
        # self.get_player_name()
        if not sameRoom:
            self.look()
        while True:
            user_input = input(
                f"{self.name}, you are in {self.current_room}. Oxygen: {self.oxygen}%\nEnter a command (or 'quit' to "
                f"exit): ")

            if user_input == 'quit':
                self.quit_game()

            # if user_input in self.rooms_data.get(self.current_room, {}).get('exits', {})
            if user_input in exits:
                self.go(user_input)
            elif user_input.split()[0] in valid_commands:
                command, *args = user_input.split()
                if command in ['go', 'move']:
                    direction = args[0]
                    self.go(direction)
                elif command in ['lookat', 'inspect']:
                    self.look_at(" ".join(args))
                elif command == 'look':
                    self.look()
                elif command in ['take', 'pickup', 'grab'] and len(args) == 1:
                    item_name = args[0]
                    self.take(item_name)
                elif command in ['drop', 'leave', 'discard'] and len(args) == 1:
                    item_name = args[0]
                    self.drop(item_name)
                elif command == 'eat' and len(args) == 1:
                    item_name = args[0]
                    self.eat(item_name)
                elif command == 'inventory':
                    if self.inventory:
                        self.display_inventory()
                    else:
                        print(f"{self.name}'s inventory is empty")
                elif command == 'savegame':
                    self.save_game()
                # elif command == 'loadgame':
                #     self.load_game_state()
                elif command == 'help':
                    self.display_help()
                # Add more commands as needed
                else:
                    print("Error: Invalid command format.")
            else:
                print("Error: Invalid command. Please enter a valid command.")


# Example usage:
game = Gameplay()
game.play("air_tank_riddle")
