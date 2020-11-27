# read in game intro from text file
def read_intro():
    try:
        with open('game_instructions.txt', 'r') as f:
            data = f.read()
        print(data)
    except FileNotFoundError as err:
        print(err)


def show_image():
    try:
        with open('textAdventureImage.txt', 'r') as i:
            image = i.read()
        print(image)
    except FileNotFoundError as err:
        print(err)


read_intro()
show_image()

# Dictionary of player with current inventory and location
player = {
    "inventory": [],
    "location": ['foyer', 'library', 'parlor', 'kitchen', 'pantry']
}
current_location = player["location"][0]

# Dictionary for 5 rooms each having description, items, and exits
rooms = {
    "foyer": {
        'description': 'A large spacious meeting area as you first '
                       'enter building',
        'items': ['knife', 'gum', 'shoes'],
        'exits': ['parlor', 'library']},
    "parlor": {
        'description': 'A room for entertainment of guests',
        'items': ['champagne', 'record', 'cogniac'],
        'exits': ['foyer', 'kitchen']},
    "library": {
        'description': 'An exquisite room filled wall to wall with a '
                       'broad collection of books',
        'items': ['magazine', 'book', 'cigars'],
        'exits': ['foyer', 'kitchen']},
    "kitchen": {
        'description': "A large chef's kitchen with a large center "
                       "island with seating",
        'items': ['knife', 'cleaver', 'blender'],
        'exits': ['parlor', 'library', 'pantry']},
    "pantry": {
        'description': 'A walking closet stored with misc stored '
                       'foods and accessories',
        'items': ['bread', 'utensils', 'beans'],
        'exits': ['kitchen']
    }
}

# a variable for command info
command_info = "Enter a command like 'enter [room]', 'inventory', " \
               "'take all items', 'take [item]', " \
               "'items', 'conversation', 'map', 'quit'\n"

# variable for monster intro
monster_dialogue = "To slay him you must " \
                   "hit and also hypnotize him (Use the commands " \
                   "'karate chop' or 'hypnotize'):\n "

# ghost intro
ghost_intro = "Hello, Im a ghost in the library. I am lonely.  " \
              "I like conversation.  " \
              "If you really dont want to converse type 'stop'"

# set game to true
game = True

# create infinite loop
while game:

    # a variable for current location of player
    print("\nYou are currently in the " + current_location)

    # ask player for command
    player_command = input(command_info).lower()

    # check to see  if player input anything as well as correct command
    if len(player_command) < 1 or player_command.isdigit():
        print("You have to enter a command!")

    # check to see if player input inventory
    if player_command == 'inventory':
        print("Your current inventory is: " + str(player['inventory']))

    # check to see if player input map
    if player_command == 'map':
        show_image()

    # check to see if player input quit
    if player_command == 'quit':
        game = False

    # checks for player input of conversation
    if player_command == 'conversation':
        try:
            print("Here is the conversation you had with the ghost: ")
            with open('textAdventureGhostConvo.txt', 'r') as i:
                data = i.read()
            print(data)
        except FileNotFoundError as err:
            print(err)

    # checks to see if player input enter room and verifies they can
    # exit to said room
    if current_location == 'foyer':
        if player_command == "enter parlor" or \
                player_command == "enter library":
            room = player_command.split()
            if room[1] == 'parlor':
                current_location = player["location"][2]
                print("ok, you have moved to: " + current_location)
            elif room[1] == 'library':
                current_location = player["location"][1]
                print("ok, you have moved to: " + current_location)
        else:
            print("sorry can't move there")
    elif current_location == 'library':
        if player_command == "enter foyer" or \
                player_command == "enter kitchen":
            room = player_command.split()
            if room[1] == 'foyer':
                current_location = player["location"][0]
                print("ok, you have moved to: " + current_location)
            elif room[1] == 'kitchen':
                current_location = player["location"][3]
                print("ok, you have moved to: " + current_location)
        else:
            print("sorry can't move there")
    elif current_location == 'parlor':
        if player_command == "enter foyer" or \
                player_command == "enter kitchen":
            room = player_command.split()
            if room[1] == 'foyer':
                current_location = player["location"][0]
                print("ok, you have moved to: " + current_location)
            elif room[1] == 'kitchen':
                current_location = player["location"][3]
                print("ok, you have moved to: " + current_location)
        else:
            print("sorry can't move there")
    elif current_location == 'kitchen':
        if player_command == "enter parlor" or \
                player_command == "enter library" or \
                player_command == "enter pantry":
            room = player_command.split()
            if room[1] == 'parlor':
                current_location = player["location"][2]
                print("ok, you have moved to: " + current_location)
            elif room[1] == 'library':
                current_location = player["location"][1]
                print("ok, you have moved to: " + current_location)
            elif room[1] == 'pantry':
                current_location = player["location"][4]
                print("ok, you have moved to: " + current_location)
        else:
            print("sorry can't move there")
    elif current_location == 'pantry':
        if player_command == "enter kitchen":
            room = player_command.split()
            if room[1] == 'kitchen':
                current_location = player["location"][3]
        else:
            print("sorry can't move there")

    # checks players location for specific room commands
    if current_location == 'foyer':

        # check to see if player input items
        if player_command == 'items':
            print("The items in the foyer are: " +
                  str(rooms["foyer"]["items"]))

        # adds all items to players inventory
        if player_command == 'take all items':
            player['inventory'].extend(rooms["foyer"]["items"])
            print("ok, you have added " +
                  str(list(rooms["foyer"]["items"])) + " to your inventory")

        # checks to see player wants to add a specific item
        if player_command == 'take knife' or player_command == 'take gum' or \
                player_command == 'take shoes':
            foyer_choice = player_command.split()
            if foyer_choice[1] == 'knife':
                player['inventory'].append(rooms["foyer"]["items"][0])
                print("ok you have added " +
                      str(rooms["foyer"]["items"][0]) + " to your inventory")
            elif foyer_choice[1] == 'gum':
                player['inventory'].append(rooms["foyer"]["items"][1])
                print("ok you have added " +
                      str(rooms["foyer"]["items"][1]) + " to your inventory")
            elif foyer_choice[1] == 'shoes':
                player['inventory'].append(rooms["foyer"]["items"][2])
                print("ok you have added " +
                      str(rooms["foyer"]["items"][2]) + " to your inventory")
    if current_location == 'parlor':
        # check to see if player input items
        if player_command == 'items':
            print("The items in the parlor are: " +
                  str(rooms["parlor"]["items"]))

        # adds all items to players inventory
        if player_command == 'take all items':
            player['inventory'].extend(rooms["parlor"]["items"])
            print("ok, you have added " +
                  str(list(rooms["parlor"]["items"])) + " to your inventory")

        # checks to see player wants to add a specific item
        if player_command == 'take champagne' or \
                player_command == 'take record' or \
                player_command == 'take cogniac':
            parlor_choice = player_command.split()
            if parlor_choice[1] == 'champagne':
                player['inventory'].append(rooms["parlor"]["items"][0])
                print("ok you have added " +
                      str(rooms["parlor"]["items"][0]) + " to your inventory")
            elif parlor_choice[1] == 'record':
                player['inventory'].append(rooms["parlor"]["items"][1])
                print("ok you have added " +
                      str(rooms["parlor"]["items"][1]) + " to your inventory")
            elif parlor_choice[1] == 'cogniac':
                player['inventory'].append(rooms["parlor"]["items"][2])
                print("ok you have added " +
                      str(rooms["parlor"]["items"][2]) + " to your inventory")
    if current_location == 'kitchen':
        # check to see if player input items
        if player_command == 'items':
            print("The items in the kitchen are: " +
                  str(rooms["kitchen"]["items"]))

        # adds all items to players inventory
        if player_command == 'take all items':
            player['inventory'].extend(rooms["kitchen"]["items"])
            print("ok, you have added " +
                  str(list(rooms["kitchen"]["items"])) + " to your inventory")

        # checks to see player wants to add a specific item
        if player_command == 'take knife' or \
                player_command == 'take cleaver' or \
                player_command == 'take blender':
            kitchen_choice = player_command.split()
            if kitchen_choice[1] == 'knife':
                player['inventory'].append(rooms["kitchen"]["items"][0])
                print("ok you have added " +
                      str(rooms["kitchen"]["items"][0]) + " to your inventory")
            elif kitchen_choice[1] == 'cleaver':
                player['inventory'].append(rooms["kitchen"]["items"][1])
                print("ok you have added " +
                      str(rooms["kitchen"]["items"][1]) + " to your inventory")
            elif kitchen_choice[1] == 'blender':
                player['inventory'].append(rooms["kitchen"]["items"][2])
                print("ok you have added " +
                      str(rooms["kitchen"]["items"][2]) + " to your inventory")
    if current_location == 'library':
        print(ghost_intro)
        ghost_convo = True
        while ghost_convo:
            try:
                with open('textAdventureGhostConvo.txt', 'w') as g:
                    play_ghost_response = input("Talk to me ")
                    while play_ghost_response != "stop":
                        g.write('Ghost: Talk to me\n')
                        g.write('Adventurer: ' + play_ghost_response + '\n')
                        g.write("Ghost: That's interesting "
                                "talk to me some more \n")
                        play_ghost_response = \
                            input("That's interesting talk to me some more ")
                    if play_ghost_response == "stop":
                        ghost_convo = False
            except FileNotFoundError as err:
                print(err)

        # check to see if player input items
        if player_command == 'items':
            print("The items in the library are: " +
                  str(rooms["library"]["items"]))

        # adds all items to players inventory
        if player_command == 'take all items':
            player['inventory'].extend(rooms["library"]["items"])
            print("ok, you have added " +
                  str(list(rooms["library"]["items"])) + " to your inventory")

        # checks to see player wants to add a specific item
        if player_command == 'take magazine' or \
                player_command == 'take book' or \
                player_command == 'take cigars':
            library_choice = player_command.split()
            if library_choice[1] == 'magazine':
                player['inventory'].append(rooms["library"]["items"][0])
                print("ok you have added " +
                      str(rooms["library"]["items"][0]) + " to your inventory")
            elif library_choice[1] == 'book':
                player['inventory'].append(rooms["library"]["items"][1])
                print("ok you have added " +
                      str(rooms["library"]["items"][1]) + " to your inventory")
            elif library_choice[1] == 'cigars':
                player['inventory'].append(rooms["library"]["items"][2])
                print("ok you have added " +
                      str(rooms["library"]["items"][2]) + " to your inventory")
    if current_location == 'pantry':
        monster_health = 3

        print("Watch out! A monster is attacking you! ")
        # monster info
        while monster_health > 0:

            # get input from player asking what to do
            player_monster_command = input(monster_dialogue).lower()
            if player_monster_command == 'karate chop' or \
                    player_monster_command == 'hypnotize':
                if player_monster_command == 'karate chop':
                    monster_health -= 1
                    print("Good job, you have injured the monster. "
                          "His health is now " + str(monster_health))
                elif player_monster_command == 'hypnotize':
                    monster_health -= 1
                    print("Good job, you have driven the monster crazy. "
                          "His sanity is now " + str(monster_health))
        if monster_health == 0:
            print("There is a monster in this room but you slayed it")

        # check to see if player input items
        if player_command == 'items':
            print("The items in the pantry are: " +
                  str(rooms["pantry"]["items"]))

        # adds all items to players inventory
        if player_command == 'take all items':
            player['inventory'].extend(rooms["pantry"]["items"])
            print("ok, you have added " +
                  str(list(rooms["pantry"]["items"])) + " to your inventory")

        # checks to see player wants to add a specific item
        if player_command == 'take bread' or \
                player_command == 'take utensils' or \
                player_command == 'take beans':
            pantry_choice = player_command.split()
            if pantry_choice[1] == 'bread':
                player['inventory'].append(rooms["pantry"]["items"][0])
                print("ok you have added " +
                      str(rooms["pantry"]["items"][0]) + " to your inventory")
            elif pantry_choice[1] == 'utensils':
                player['inventory'].append(rooms["pantry"]["items"][1])
                print("ok you have added " +
                      str(rooms["pantry"]["items"][1]) + " to your inventory")
            elif pantry_choice[1] == 'beans':
                player['inventory'].append(rooms["pantry"]["items"][2])
                print("ok you have added " +
                      str(rooms["pantry"]["items"][2]) + " to your inventory")
