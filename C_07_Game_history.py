
# initialise list to hold game history
game_history = []


# Get data (base component does this already, code below fore testing purposes)

while True:
    rounds_played = input("Round? ")
    if rounds_played == "":
        break



    user_points = int(input("User points? "))
    comp_points = int(input("User points? "))
    winner = input("Who won? ")
    user_score = int(input("User points? "))
    comp_score = int(input("Computer points? "))

    game_results = (f"Round {rounds_played}: User Points {user_points} | "
                    f"Computer Points {comp_points}, {winner} wins (15 | 0)")




    game_history.append(game_results)

print("Game history")

for item in game_history:
    print(item)

