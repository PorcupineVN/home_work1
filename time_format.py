name_grades = ['сек', 'мин', 'час', 'дн', 'мес', 'г.', 'век.', 'тыс.']
grades = [60, 60, 24, 365, 100, 1000]
month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
duration_grades = []
duration = int(input('Сколько секунд прошло?  '))
for i in range(len(grades)):
    if i == 3:
        number_month = duration%grades[i]
        j = 0
        while number_month > month[j]:
            number_month -= month[j]
            j+=1
        duration_grades.append(number_month)
        if j != 0:
            duration_grades.append(j)
    elif i == len(grades) - 1:
        duration_grades.append(duration%grades[i])
        if duration//grades[i] != 0:
            duration_grades.append(duration//grades[i])
        break
    else:
        duration_grades.append(duration%grades[i])
    duration//=grades[i]
    if duration == 0:
        break
result = ''
for i in range(len(duration_grades)-1, -1, -1):
    result += f'{duration_grades[i]} {name_grades[i]} '
print(result)