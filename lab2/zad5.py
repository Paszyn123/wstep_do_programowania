# with open("notowania_gieldowe.txt") as f:
#     for line in f:
#         print(line, end="")



with open("notowania_gieldowe.txt", "a") as file:
    file.write("\n ALR, 113")
with open("notowania_gieldowe.txt", "r") as file:
    for line in file:
        print(line, end="")