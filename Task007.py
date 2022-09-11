list_number = [1, 8, 16, 3, 5, 9, 4]
min_index = list_number.index(min(list_number))
max_index = list_number.index(max(list_number))
if min_index < max_index:
    result = sum(list_number[min_index:max_index + 1])
    print(result)
else:
    result = sum(list_number[max_index:min_index + 1])
    print(result)