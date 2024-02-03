# Loading file game.txt data
with open("game.txt", "r", encoding="utf8") as file:
    data = list(map(lambda t: t.split("$"), file.read().split("\n")[1:]))


# Generating report and updating information
new_data = data.copy()
for i, row in enumerate(data):
    # Checking nameError numeric code
    if row[2].split(":")[1] == "55":
        print(f"У персонажа\t{row[1]}\tв игре\t{row[0]}\tнашлась ошибка с кодом:\t {row[2]}.\tДата фиксации:\t {row[3]}")
        new_data[i] = [row[0], row[1], "Done", "0000-00-00"]


# Saving new file game_new.csv
with open("game_new.csv", "w", encoding="utf8") as file:
    file.write("\n".join(map("$".join, new_data)))
