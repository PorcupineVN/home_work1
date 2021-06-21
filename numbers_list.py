number_list = [i**3 for i in range(1, 1001, 2)]
sum_div_7 = 0
sum_div_7_17 = 0
for number in number_list:
    numb = number
    numb_17 = number + 17
    sum_div = 0
    sum_div_17 = 0
    while numb != 0:
        sum_div += numb%10
        numb//=10
    while numb_17 != 0:
        sum_div_17 += numb_17%10
        numb_17 //=10
    if sum_div % 7 == 0:
        sum_div_7 += number
    if sum_div_17 % 7 == 0:
        sum_div_7_17 += number+17
print(f'Сумма чисел из списка кубов, сумма цифр которых делится нацело на 7: {sum_div_7}')
print(f'Сумма чисел из списка кубов (увеличенных на +17), сумма цифр которых делится нацело на 7: {sum_div_7_17}')