def remove_game(title):
    if title in game_library:
        del game_library[title]
        print(f"Game '{title}' removed from the library.")
    else:
        print(f"Game '{title}' not found in the library.")

def display_library():
    if not game_library:
        print("The library is empty.")
    else:
        print("Game Library:")
        for title, info in game_library.items():
            print(f"Title: {title}")
            print(f"Genre: {info['genre']}")
            print(f"Release Year: {info['release_year']}")
            print(f"Platforms: {', '.join(info['platforms'])}")
            print("-----------------------")

# Step 3: Test the functions
add_game("Super Mario Bros.", "Platformer", 1985, ["NES", "SNES", "Switch"])
add_game("The Legend of Zelda", "Action-Adventure", 1986, ["NES", "Switch"])
add_game("Final Fantasy VII", "RPG", 1997, ["PlayStation", "PC", "Switch"])
add_game("Minecraft", "Sandbox", 2011, ["PC", "Console", "Mobile"])

display_library()

remove_game("The Legend of Zelda")

display_library()
