# Project: Escape Room Text Adventure Game
# Authors: Hiromi and Nick Tucker

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
        self.wordle_data = load_data('Wordle_words')
        self.wordle_hint_data = load_data('Wordle_hint')
        self.help_data = load_data('Help')

    def load_game_state(self, filename='saved_game.json'):
        if os.path.exists(filename):
            choice = input("Do you want to load the saved game? (yes/no): ").lower()

            if choice == 'yes':
                with open(filename, 'r') as file:
                    game_state = json.load(file)

                self.name = game_state.get('name', '')
                self.current_room = game_state.get('current_room', 'room1')
                self.oxygen = game_state.get('oxygen', 100)
                self.inventory = game_state.get('inventory', [])
                self.rooms_data = load_data('Rooms')
                self.objects_data = load_data('Objects')
                self.verbs_data = load_data('Verbs')
                self.features_data = load_data('Features')
                self.words_data = load_data('Words')
                self.riddles_data = load_data('Riddles')
                self.wordle_data = load_data('Wordle_words')
                self.wordle_hint_data = load_data('Wordle_hint')
                self.help_data = load_data('Help')

                print(f"Welcome back, {self.name}!")
                return True
            else:
                print("Starting a new game.")
                return False
        else:
            return False


    def go(self, direction):
        # Make go able to be used without keyword go, if a direction or exit is
        # described
        #
        exits = list(self.rooms_data.get(self.current_room, {}).get('exits', {}).keys())
        if self.rooms_data.get(self.current_room, {}).get('lock', {}) == "locked":
            print("The passage is locked. Please play a game to unlock the exit.")
        elif direction in exits and self.rooms_data.get(self.current_room, {}).get('lock', {}) == "unlocked":
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
            print(f"There is no exit in that direction.")

    def look(self):
        room_description = self.rooms_data.get(self.current_room, {}).get('long_description', {})
        print(room_description)

    def look_at(self, item_name):
        if item_name in self.inventory:
            item_description = self.objects_data.get(item_name, {}).get('description')
            print(item_description)
        elif self.objects_data.get(item_name, {}).get('room') == self.current_room:
            object_description = self.objects_data.get(item_name, {}).get('description')
            print(object_description)
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
                    else:
                        self.inventory.remove(item)
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
                print(f"{self.name}, that cannot be taken. \nObjects can be taken and Features can be inspected.")
        else:
            print(f"{self.name}, that cannot be taken. \nObjects can be taken and Features can be inspected.")

    def eat(self, item_name):
        if item_name in self.inventory and self.objects_data.get(item_name).get('edible') == "yes":
            self.inventory.remove(item_name)
            self.oxygen += 2
            print(f"{self.name} ate the {item_name}. It disappears from your inventory.\nYou gained 2 oxygen percent.")
        elif item_name in self.inventory:
            print(f"{self.name}, {item_name} is not edible")
        else:
            print(f"{self.name}, you don't have {item_name} in your inventory. \nPlease take the item first.")

    def read(self, item_name):
        if self.objects_data.get(item_name).get('readable') == "yes":
            hint = self.objects_data.get(item_name).get('hint')
            print(hint)
        else:
            print(f"{item_name} cannot be read...")
    def wear(self, item_name):
        if self.objects_data.get(item_name).get('wearable') == "yes":
            print("Congratulations! You won the game!")
            exit()
        else:
            print(f"{item_name} cannot be worn...")
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

    def game_over(self):
        print(f"{self.name}, you ran out of oxygen... sorry to let you go!")
        print("Do it better next time. Goodbye!")
        exit()

    def display_help(self):
        print("Available Commands")
        for key in self.help_data:
            print(self.help_data[key])

    def play(self, game):
        def choose_random_word():
            word = random.choice(load_data('Wordle_words'))
            return word

        def get_guess():
            while True:
                    guess = input("Enter your 5-letter word guess: ").lower()
                    if len(guess) == 5 and guess.isalpha():
                        return guess
                    else:
                        print("Please enter a valid 5-letter word.")

        def evaluate_guess(hidden_word, guess):
            if guess == hidden_word:
                print("Correct! Your oxygen level increases by 10.")
                self.oxygen += 10
                self.rooms_data[self.current_room]['lock'] = "unlocked"
                return "You guessed the word! Congratulations!"
            feedback = []
            for i in range(5):
                if guess[i] == hidden_word[i]:
                    feedback.append(guess[i])
                elif guess[i] in hidden_word:
                    feedback.append("O")
                else:
                    feedback.append(".")
            print(f"Try again. You lost oxygen by 2.")
            self.oxygen -= 2
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
                print("Correct! Your oxygen level increases by 10.")
                self.rooms_data[self.current_room]['lock'] = "unlocked"
                self.oxygen += 10
            else:
                print("Incorrect. Your oxygen level decreases by 5.")
                self.oxygen -= 5


        elif game == "scramble_word":
            original_word = random.choice(load_data('Words')).upper()
            scrambled_word = list(original_word)
            random.shuffle(scrambled_word)
            scrambled = ''.join(scrambled_word)

            print(f"Unscramble the following word:")
            print(scrambled)

            player_guess = input("Your guess: ")

            if player_guess.upper() == original_word:
                print("Correct! You unscrambled the word. Your oxygen level increases by 10.")
                self.rooms_data[self.current_room]['lock'] = "unlocked"
                self.oxygen += 10
            else:
                print("Incorrect. Your oxygen level decreases by 5. Try again")
                self.oxygen -= 5

        elif game == "wordle":
            hidden_word = choose_random_word()
            hint = self.wordle_hint_data[hidden_word]
            attempts = 6

            print(f"Welcome to Wordle! You have 6 chances to guess a randomly selected five-letter word. Let's begin!\n")
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
        objects = list(load_data('Objects').keys())
        features = list(load_data('Features').keys())
        if not self.load_game_state():
            pass
        # self.get_player_name()
        if not sameRoom:
            self.look()
        while True:
            exits = list(self.rooms_data.get(self.current_room, {}).get('exits', {}).keys())
            if self.oxygen == 0:
                self.game_over()
            user_input = input(
                f"{self.name}, you are in {self.current_room}. Oxygen: {self.oxygen}%\n{self.rooms_data.get(self.current_room, {}).get('summary')}\nEnter a command (or 'quit' to "
                f"exit): ")
            if user_input == 'quit':
                self.quit_game()

            # if user_input in self.rooms_data.get(self.current_room, {}).get('exits', {})
            if user_input in exits:
                self.go(user_input)
            elif user_input.split()[0] in valid_commands:
                command, *args = user_input.split()
                # command = user_input.split(' ',1)[0]
                # args = user_input.split(' ',1)[1]
                while " ".join(args) not in exits + objects + features:
                    if args == []:
                        break
                    if args[0]:
                        del args[0]

                args = " ".join(args)
                self.oxygen -= 5
                print("Every move means you lose 5% oxygen...")
                if command in ['go', 'move', 'jump','unlock','open']:
                    self.go(args)
                elif command in ['lookat', 'inspect']:
                    self.look_at(args)
                elif command == 'look':
                    self.look()
                elif command in ['get','take', 'pickup', 'grab', 'collect']:
                    item_name = args
                    self.take(item_name)
                elif command in ['drop', 'leave', 'discard', 'put']:
                    item_name = args
                    self.drop(item_name)
                elif command == 'eat':
                    item_name = args
                    self.eat(item_name)
                elif command == 'read':
                    item_name = args
                    self.read(item_name)
                elif command == 'wear':
                    item_name = args
                    self.wear(item_name)
                elif command == 'inventory':
                    if self.inventory:
                        self.display_inventory()
                    else:
                        print(f"{self.name}'s inventory is empty")
                elif command == 'save':
                    self.save_game()
                elif command == 'load':
                    self.load_game_state()
                elif command == 'help':
                    self.display_help()
                else:
                    print("Error: Invalid command format.")
            else:
                print("Error: Invalid command. Please enter a valid command.")


# Example usage:
game = Gameplay()
game.parse_user_input()
