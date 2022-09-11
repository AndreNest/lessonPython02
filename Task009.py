list_number = [1, 10, 9, 3, 4, 9, 43]
n = len(list_number)
for i in range(n - 1):
    for j in range(n - i - 1):
        if list_number[j] > list_number[j + 1]:
            list_number[j], list_number[j + 1] = list_number[j + 1], list_number[j]
print(list_number)
