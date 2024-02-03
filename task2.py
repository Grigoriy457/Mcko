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


# Generating report
for game_name in sorted(list(set(map(lambda t: t[0], data))), key=str):
    print(f"{game_name} - количество багов: {get_bugs_count_by_game_name(game_name, data)}")
