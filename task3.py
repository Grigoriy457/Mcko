# Loading file game.txt data
with open("game.txt", "r", encoding="utf8") as file:
    data = list(map(lambda t: t.split("$"), file.read().split("\n")[1:]))


def find_games_by_character(character_name: str, logs: list) -> list[str]:
    """
    Finding games in what character is.

    :param character_name: The name of character
    :param logs: games logs
    :return: List of games in what character is
    """
    return sorted(list(set(row[0] for row in logs if row[1] == character_name)))


while True:
    # Getting character name
    character_name = input("Write character name: ")
    # If word is 'game' exit program
    if character_name == "game":
        break

    games = find_games_by_character(character_name, data)
    if len(games) == 0:
        # Can't find games with this character name
        print("Этого персонажа не существует")
        print()
    else:
        # Printing games with this character name
        print(f"Персонаж {character_name} встречается в играх:")
        print(*games[:5], sep="\n")
        if len(games) > 5:
            print("и др.")
        print()
