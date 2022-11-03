import random

players = []
board = [
    "START",
    {
        "Cust of sale": 200,
        "Cust for rent": 25,
        "Owner": None
    },
    {
        "Cust of sale": 180,
        "Cust for rent": 12,
        "Owner": None
    },
    {
        "Cust of sale": 400,
        "Cust for rent": 35,
        "Owner": None
    },
    {
        "Cust of sale": 1000,
        "Cust for rent": 250,
        "Owner": None
    },
    {
        "Cust of sale": 700,
        "Cust for rent": 59,
        "Owner": None
    },
    {
        "Cust of sale": 850,
        "Cust for rent": 60,
        "Owner": None
    },
    {
        "Cust of sale": 950,
        "Cust for rent": 78,
        "Owner": None
    },
    {
        "Cust of sale": 620,
        "Cust for rent": 45,
        "Owner": None
    },
    {
        "Cust of sale": 500,
        "Cust for rent": 37,
        "Owner": None
    },
    {
        "Cust of sale": 1100,
        "Cust for rent": 100,
        "Owner": None
    },
    {
        "Cust of sale": 690,
        "Cust for rent": 44,
        "Owner": None
    },
    {
        "Cust of sale": 350,
        "Cust for rent": 13,
        "Owner": None
    },
    {
        "Cust of sale": 1480,
        "Cust for rent": 600,
        "Owner": None
    },
    {
        "Cust of sale": 200,
        "Cust for rent": 12,
        "Owner": None
    },
    {
        "Cust of sale": 170,
        "Cust for rent": 11,
        "Owner": None
    },
    {
        "Cust of sale": 111,
        "Cust for rent": 9,
        "Owner": None
    },
    {
        "Cust of sale": 850,
        "Cust for rent": 90,
        "Owner": None
    },
    {
        "Cust of sale": 788,
        "Cust for rent": 55,
        "Owner": None
    },
    {
        "Cust of sale": 320,
        "Cust for rent": 28,
        "Owner": None
    },
    {
        "Cust of sale": 100,
        "Cust for rent": 10,
        "Owner": None
    }
]


def check_ballance(player_position: int, value_of_withdrawal: int):
    if players[player_position]["balance"] < value_of_withdrawal:
        print("Lower balance")
        return False
    else:
        players[player_position]['balance'] = players[player_position]['balance'] - value_of_withdrawal
        print(f"Current balance: {players[player_position]['balance']}")
        return True


def play():
    num_of_players = int(input("How many players: [only integers] "))
    for i in range(num_of_players):
        players.append({
            "Player": i,
            "balance": 300,
            "last_position": 0
        })

    start = int(input("Type 1 start: "))
    if start == 1:
        print(90*"*")

        while len(players) > 1:
            for i in players:
                print(f'Info of player -> {i}')
                print(40*"*")
                roll_the_dice = int(input("Type 2 to roll the dice: "))
                value_of_dice_returned = 0
                if roll_the_dice == 2:
                    value_of_dice_returned = random.randint(1, 6)

                print(f"**** Value of the dice -> {value_of_dice_returned} ****")

                if i["last_position"] == 0:
                    i["last_position"] = value_of_dice_returned
                else:
                    value_of_dice_returned = i["last_position"] + value_of_dice_returned
                    i["last_position"] = value_of_dice_returned
                    if value_of_dice_returned > 20:
                        value_of_dice_returned = value_of_dice_returned - 20

                print(90*"-")
                print(f"Player {i['Player']}, you stopped at: Property {board[value_of_dice_returned]}")
                print(90 * "-")

                if not board[value_of_dice_returned]["Owner"]:
                    option = int(input("Type 3 to buy the property | Type 4 to pass :"))
                    if option == 3:
                        check = check_ballance(i["Player"], board[value_of_dice_returned]["Cust of sale"])
                        if check:
                            print(f"Congratulations you bought a property at position {value_of_dice_returned} for "
                                  f"{board[value_of_dice_returned]['Cust of sale']}")

                            board[value_of_dice_returned]["Owner"] = i

                            print("\n")
                            print("* New Round *")

                        else:
                            print("No money enough!")
                            print("\n")
                            print("* New Round *")
                            continue
                    else:
                        print("\n")
                        print("* New Round *")
                        continue

                else:
                    pay_rent = check_ballance(i["Player"], board[value_of_dice_returned]["Cust for rent"])
                    if not pay_rent:
                        print(f"Player {i['Player']} - Game Over")
                        players.pop(i)
                        continue
                    else:
                        continue

        print(f"End of Game - Player {players[0]['Player']} is the champ!")
        return True

    else:
        return False


if __name__ == '__main__':
    play()
