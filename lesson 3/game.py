import random


FINISH_LINE = 100


def show_track(player_distance, opponent_distance):
    """Display both bikes on a simple 20-part race track."""
    track_length = 20
    player_position = min(track_length, int(player_distance / FINISH_LINE * track_length))
    opponent_position = min(track_length, int(opponent_distance / FINISH_LINE * track_length))

    print("\nFinish |" + "=" * track_length + "|")
    print("You    |" + "-" * player_position + "B" + "-" * (track_length - player_position) + "|")
    print("Rival  |" + "-" * opponent_position + "R" + "-" * (track_length - opponent_position) + "|")


def get_player_move():
    while True:
        move = input("Choose: [b]oost, [r]ide, or [s]low down: ").lower().strip()
        if move in ("b", "r", "s"):
            return move
        print("Please type b, r, or s.")


def bike_race():
    player_distance = 0
    opponent_distance = 0
    energy = 5

    print("=== BIKE RACE ===")
    print("Reach 100 km before your rival.")
    print("Boost is fast but uses 1 energy. Riding normally restores energy.")

    while player_distance < FINISH_LINE and opponent_distance < FINISH_LINE:
        show_track(player_distance, opponent_distance)
        print("Your energy:", energy)
        move = get_player_move()

        if move == "b":
            if energy > 0:
                player_distance += random.randint(14, 22)
                energy -= 1
                print("You boost forward!")
            else:
                player_distance += random.randint(4, 7)
                print("No energy left for a boost. Your bike moves slowly.")
        elif move == "r":
            player_distance += random.randint(8, 13)
            energy = min(5, energy + 1)
            print("You ride at a steady speed.")
        else:
            player_distance += random.randint(3, 6)
            energy = min(5, energy + 2)
            print("You slow down and recover energy.")

        opponent_distance += random.randint(7, 15)
        print("Rival distance:", min(opponent_distance, FINISH_LINE), "km")

    show_track(player_distance, opponent_distance)
    if player_distance >= FINISH_LINE and opponent_distance >= FINISH_LINE:
        print("It is a photo finish!")
    elif player_distance >= FINISH_LINE:
        print("Congratulations! You won the bike race! 🏆")
    else:
        print("Your rival won this race. Try again!")


if __name__ == "__main__":
    bike_race()
