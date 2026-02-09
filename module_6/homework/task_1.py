basketball_players = []

def add_players():
    while True:
        name = input("Введите имя баскетболиста: ")
        height = float(input("Введите рост баскетболиста: "))
        new_player = {"name": name, "height": height} 
        basketball_players.append(new_player)
        add_more = input(f"Баскетболист {name} добавлен в список. Хотите добавить следующего баскетболиста? (да/нет)")
        if add_more not in ("yes", "да"):
            break
    for i, player in enumerate(basketball_players, 1):
        print(f"{i}. {player['name']} - {player['height']}")
add_players()


def delete_player():
    name_to_remove = input("Кого необходимо удалить? ")
    if name_to_remove in basketball_players:
        del basketball_players[name_to_remove]
        print(f"Игрок '{name_to_remove}' успешно удалён.")
    else:
        print(f"Игрока '{name_to_remove}' нет в списке!")
delete_player()
print(basketball_players)