my_list = [1, 2, 3, 4, 5]
if len(my_list) == len(set(my_list)):
    print("All elements are unique")


c = 0
for i in range(3):
    for j in range(3):
        if i == j:
            c = c + 1

print(c)
