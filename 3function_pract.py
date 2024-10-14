def find_max(numbers):
    max_num = numbers[0] 

    for number in numbers:
        if number > max_num:
            max_num = number

    return max_num

def calculate_average(numbers):
    total = 0
    count = len(numbers)

    if count == 0:
        return 0

    for num in numbers:
        total += num

    return total / count

def get_player_statistics(player_scores):
    highest_score = find_max(player_scores)   
    average_score = calculate_average(player_scores)
    
    outstanding_player = None
    for score in player_scores:
        if score >= 95:
            outstanding_player = score
            break

    return highest_score 

player_scores = [50, 30, 60, 80, 90, 95, 70, 60, 100]

player_stats = get_player_statistics(player_scores)

print(f"The highest player score is: {player_stats['highest_score']}")
print(f"The average player score is: {player_stats['average_score']}")
if player_stats['outstanding_player'] is not None:
    print(f"An outstanding player scored: {player_stats['outstanding_player']}")
else:
    print("No outstanding players found.")
