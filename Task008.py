list_number = [1, 10, 9, 3, 4, 9, 43]
count = 0
max_num = max(list_number)
#max_num10 = max_num * 0.1
for i in list_number: 
    if i != max_num:
        if( max_num - i ) <= i:
            count += 1

print(count)
