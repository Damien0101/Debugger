
player_scores = [50, 30, 60, 80, 90, 20, 70, 60, 100]


highest_score = 0
message = "The highest score among players is: "


for score in player_scores:
    if score < highest_score:
        highest_score = score

message += str(highest_score)
print(message)
