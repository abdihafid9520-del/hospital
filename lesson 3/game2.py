import random


def get_shot():
    """Ask the player which lane to shoot."""
    while True:
        try:
            lane = int(input("Shoot a lane (1-5), or type 0 to quit: "))
            if 0 <= lane <= 5:
                return lane
            print("Choose a number from 1 to 5.")
        except ValueError:
            print("Please enter a number.")


def bird_shooter():
    score = 0
    shots_left = 10

    print("=== BIRD SHOOTER ===")
    print("A bird flies through one of five lanes. Hit it to earn points!")

    while shots_left > 0:
        bird_lane = random.randint(1, 5)
        bird_points = random.choice((10, 10, 15, 20))

        print("\nSky lanes:  1     2     3     4     5")
        print("             ~     ~     ~     ~     ~")
        print("Shots left:", shots_left, "| Score:", score)
        shot = get_shot()

        if shot == 0:
            break

        shots_left -= 1
        if shot == bird_lane:
            score += bird_points
            print("Hit! You scored", bird_points, "points.")
        else:
            print("Miss! The bird was in lane", bird_lane)

    print("\nGame over!")
    print("Final score:", score)
    if score >= 100:
        print("Excellent shooting! 🏆")
    elif score >= 50:
        print("Good job! Keep practising.")
    else:
        print("Try again and aim carefully!")


if __name__ == "__main__":
    bird_shooter()
