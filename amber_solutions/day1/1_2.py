# Historian Hysteria
# Day 1 Part 2
left_list = []
right_list = []

with open("input.txt", "r") as file:
    for line in file:
        x, y = line.replace("\n", "").replace("   ", " ").split(" ")
        left_list.append(int(x))
        right_list.append(int(y))

left_list.sort()
right_list.sort()

similarity_score = 0

for n in left_list:
    n_count = 0
    for k in right_list:
        if n == k:
            n_count+=1
    similarity_score += n * n_count

print(similarity_score)
# solution accepted