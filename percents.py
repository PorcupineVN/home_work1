list_nothing = [1,]
list_a = [2, 3 , 4]
list_ov = [5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
for i in range(1, 21):
    if i in list_nothing:
        print(f'{i} процент')
    elif i in list_a:
        print(f'{i} процента')
    elif i in list_ov:
        print(f'{i} процентов')
