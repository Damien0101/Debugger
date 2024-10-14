ages = [15, 21, 13, 17]

total_age = 0
message = "The total sum of ages in the group is: "

for i in range(len(ages)+1):
    total_age += ages[i]

message += str(total_age)
print(message)
