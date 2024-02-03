# Loading file game.txt data
with open("game.txt", "r", encoding="utf8") as file:
    data = list(map(lambda t: t.split("$"), file.read().split("\n")[1:]))


def get_bugs_count_by_game_name(game_name: str, logs: list) -> int:
    """
    Counting bugs in logs string by game name.

    :param game_name: Name of the needed game
    :param logs: games logs
    :return: Bugs count
    """
    return len([row for row in logs if row[0] == game_name])


# Updating information (adding bugs count to each log)
data = [row + [str(get_bugs_count_by_game_name(row[0], data))] for row in data]


# Saving new file game_new.csv
with open("game_counter.csv", "w", encoding="utf8") as file:
    file.write("GameName,characters,nameError,date,counter\n" + "\n".join(map(",".join, data)))
