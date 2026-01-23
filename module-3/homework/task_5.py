numbers = [2,3,4,5,6,-2,-1,0,0,33]
maximum = max(numbers)
minimum = min(numbers)
negative_numbers = 0
positive_numbers = 0
zero_numbers = 0
for number in numbers:
    if number < 0:
        negative_numbers +=1
    elif number > 0:
        positive_numbers +=1
    else:
        zero_numbers +=1
print(f'Масимальное число в списке: {maximum}')
print(f'Минимальное число число в списке: {minimum}')
print(f'Количество положительных чисел: {positive_numbers}')
print(f'Количество отрицательных чисел: {negative_numbers}')
print(f'Количество нулей: {zero_numbers}')