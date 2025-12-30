import random

#get random roll number
def roll():
    minvlue = 1
    maxvalue = 6
    roll = random.randint(minvlue, maxvalue)
    return roll

while True:
    player = input("Enter Number of Player going to Play(2-4): ")
    if player.isdigit():
        player = int(player)
        if 2 <= player <= 4:
            break
        else:
            print("Number of Players Should be between 2 and 4")
    else:
        print("Invalid Format. Try Again!")

playerscore = [0 for i in range(player)]
max_score = 50

while max(playerscore) < max_score:
    for player_index in range(player):
        print("\nPlayer number", player_index+1, "chance has started\n")
        current_score = 0

        while True:
            is_rolling = input("Are you Going to roll Dices?(y) ")
            if is_rolling.lower() != "y":
                break
            else:
                value = roll()
            
            if value == 1:
                current_score = 0
                print("You rolled 01, So You are Done!")
                break
            else:
                current_score += value
                print("You Rolled:",value)
            print("Your Current Score is:", current_score)
        
        playerscore[player_index] += current_score
        print("Your Score is:", playerscore[player_index])

max_score = max(playerscore)
winning_index = playerscore.index(max_score)
print("Player Number", winning_index + 1, "is the winner of this game and socre is", max_score)
