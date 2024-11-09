with open('file-for-task1.txt', 'r') as file:
    numbers = [float(x) for x in file.readlines()]
with open('file-for-task1.txt', 'a') as files:
    file.write(str(sum(numbers)) + '\n')
    file.write(str(max(numbers)) + '\n')
print('Виконання task2 завершено')