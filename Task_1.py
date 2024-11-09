numbers = [float(x) for x in input('Введіть список дійсних чисел через пробіл ').split()]
with open('file-for-task1.txt', 'w') as file:
    file.write(str(numbers) + '\n')