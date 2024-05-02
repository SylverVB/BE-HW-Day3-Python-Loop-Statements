# Lesson 4: Assignments | Python Loop Statements

# 1. The Range Riddle

import random

moods = ["Happy", "Sad", "Energetic", "Calm"]
days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

# Option 1.

for i in range(len(days)):
    print(f'On {days[i]}, you were feeling {random.choice(moods)}')

print("=======================================")

# Option 2.

for i in range(len(days)):
    if days[i] == "Sunday":
        print(f'On Sunday, you were feeling {random.choice(moods)}')
        break                                                         # After reaching Sunday and printing the message it exits the loop
    print(f'On {days[i]}, you were feeling {random.choice(moods)}')
print("=======================================")

# 2. Double Scoop with Nested Loops

import random

moods = ["Happy", "Sad", "Energetic", "Calm"]
days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
times = ["morning", "afternoon", "evening"]

# Option 1.

for i in range(len(days)):
    for time in times:
        print(f'On {days[i]} {time}, you were feeling {random.choice(moods)}')
print("=======================================")

# Option 2. Mood and time of the day are random choices. The loop iterates over each day of the week and only one random time of the day.

for i in range(len(days)):
    for time in times:
        if days[i] == "Sunday":
            print(f'On Sunday {random.choice(times)}, you were feeling {random.choice(moods)}')
            break
        print(f'On {days[i]} {random.choice(times)}, you were feeling {random.choice(moods)}')
        break
print("=======================================")

# Option 3. Mood is the only random choice. The loop iterates over each day of the week and each time of the day.

for i in range(len(days)):
    for time in times:
        if days[i] == "Sunday":
            print(f'On Sunday {time}, you were feeling {random.choice(moods)}')
            break
        print(f'On {days[i]} {time}, you were feeling {random.choice(moods)}')