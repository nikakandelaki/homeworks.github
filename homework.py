სახელი = "Nikoloz Kandelaki"
ხმოვნები = 0
for i in range(0,len(სახელი)):
    char = (სახელი[i])
    if char == "a" or char == "e" or char == "i" or char == "o":
        ხმოვნები += 1
print(ხმოვნები)