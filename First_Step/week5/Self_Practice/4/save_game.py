import json

user_info = {
    "user" : "wow12",
    "level" : 12,
    "health": 7,
    "coin" : 100
}

with open("save_game.json", 'w') as file:
    json.dump(user_info,file ,indent=4)

print('--- Save file created! ---')

with open('save_game.json', "r") as file:
    game_data = json.load(file)

print("Current coins:", game_data["coin"])
print("Current health:", game_data["health"])
print("Current level:", game_data["level"])

print("=" * 50)
print("___ new addition in process ___")
add_data = game_data["level"] + 1
add_coin = game_data["coin"] + 100
add_health = game_data["health"] + 1

game_data["coin"] = add_coin
game_data["health"] = add_health
game_data["level"] = add_data

with open("save_game.json", 'w', encoding = "utf-8") as file:
    json.dump(game_data,file ,indent=4)
print(f"add_data: {add_data}\nadd_coin: {add_coin}\nadd_health: {add_health}")
print("=" * 50)
print("___ LEVEL 13 ___")
print(f"level13 , your level: {add_data}")
print(f"level13 , your health: {add_health}")
print(f"level13 , your coin: {add_coin}")