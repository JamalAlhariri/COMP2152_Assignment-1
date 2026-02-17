"""
Author: Jamal Alhariri
Assignment: #1
"""

# Step b: Create 4 variables

gym_member = "Alex Alliton"      # str
preferred_weight_kg = 20.5       # float
highest_reps = 25                # int
membership_active = True         # bool




# Step c: Create a dictionary named workout_stats
workout_stats = {
    "Alex": (30, 45, 20),
    "Jamie": (40, 50, 35),
    "Taylor": (35, 40, 25)
}





# Step d: Calculate total workout minutes using a loop and add to dictionary
for friend, minutes in list(workout_stats.items()):
    total_minutes = sum(minutes)
    workout_stats[friend + "_Total"] = total_minutes





# Step e: Create a 2D nested list called workout_list
workout_list = []

for friend, minutes in workout_stats.items():
    if isinstance(minutes, tuple):
        workout_list.append(list(minutes))






# Step f: Slice the workout_list

#yoga and running
print("Yoga and Running minutes for all friends:")
for row in workout_list:
    print(row[0], row[1])

#weightlifitng
print("Weightlifting minutes for the last two friends:")
for row in workout_list[-2:]:
    print(row[2])



# Step g: Check if any friend's total >= 120
for key in workout_stats:
    if key.endswith("_Total"):
        if workout_stats[key] >= 120:
            name = key.replace("_Total", "")
            print("Great job staying active,", name + "!")




# Step h: User input to look up a friend

# Ensure that the name entered is in the dictionary 
search_name = input("Enter friend's name: ")

if search_name in workout_stats:

    minutes = workout_stats[search_name]
    total = workout_stats[search_name + "_Total"]

    print("Workout details for", search_name)
    print("Yoga:", minutes[0])
    print("Running:", minutes[1])
    print("Weightlifting:", minutes[2])
    print("Total:", total)

else:
    print("Friend", search_name, "not found in the records.")






# Step i: Friend with highest and lowest total workout minutes

# declaring start values
highest_total = 0
lowest_total = 9999
highest_friend = " "
lowest_friend = " "

for key in workout_stats:
    if key.endswith("_Total"):
#finds the highest
        if workout_stats[key] > highest_total:
            highest_total = workout_stats[key]
            highest_friend = key.replace("_Total", "")
# finds the lowest
        if workout_stats[key] < lowest_total:
            lowest_total = workout_stats[key]
            lowest_friend = key.replace("_Total", "")

print("Friend with highest total workout minutes:", highest_friend)
print("Friend with lowest total workout minutes:", lowest_friend)
