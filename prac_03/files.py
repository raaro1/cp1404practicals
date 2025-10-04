# # 1.
# out_file = open("name.txt", "w")
# name = input("Enter your name: ")
# print(name, file=out_file)
# out_file.close()

# 2.
# in_file = open("name.txt", "r")
# line = in_file.read()
# print(line)
# in_file.close()

# 3.
# with open("numbers.txt", "r") as out_file:
#     line_one = out_file.readline()
#     line_two = out_file.readline()
#     total = int(line_one) + int(line_two)
#     print(f"{total}")

# # 4.
# with open('numbers.txt', 'r') as out_file:
#     total = 0
#     for line in out_file:
#         total += int(line)
#
#     print(total)


