import string


# Loading file game.txt data
with open("game.txt", "r", encoding="utf8") as file:
    data = list(map(lambda t: t.split("$"), file.read().split("\n")[1:]))


def get_hash(game_name: str, character_name: str, p=64, m=10**9 + 9) -> int:
    """
    Generating hash (by game name and character name)

    :param game_name: Name of the needed game
    :param character_name: Name of the character
    :param p:
    :param m:
    :return: Bugs count
    """
    ALPHABET = string.ascii_letters + string.digits + ":-"

    # Creating string without spaces
    string_for_hash = (game_name + character_name).replace(" ", "").replace("'", "").replace(".", "")
    # Creating hash
    return sum([ALPHABET.index(s) * p ** i for i, s in enumerate(string_for_hash)]) % m


# Updating information (adding hash to each log)
data = [[str(get_hash(row[0], row[1]))] + row for row in data]


# Saving new file game_new.csv
with open("game_with_hash.csv", "w", encoding="utf8") as file:
    file.write("Hash$GameName$characters$nameError$date\n" + "\n".join(map(",".join, data)))
