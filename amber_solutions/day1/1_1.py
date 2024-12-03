# Historian Hysteria
# Day 1 Part 1
left_list = []
right_list = []

with open("input.txt", "r") as file:
    for line in file:
        x, y = line.replace("\n", "").replace("   ", " ").split(" ")
        left_list.append(int(x))
        right_list.append(int(y))

left_list.sort()
right_list.sort()

total_distance = 0

for n in range(len(left_list)):
    total_distance += abs(left_list[n] - right_list[n])

print(total_distance)
# solution accepted