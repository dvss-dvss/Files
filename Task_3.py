def is_float(number_in_str:  str) -> bool:
    number_in_str = number_in_str.strip()
    if number_in_str.isnumeric():
        return True
    else:
        if number_in_str.count('.') == 1:
            number_in_str_without_dot = number_in_str.replace('.', '')
            if number_in_str_without_dot.isnumeric() and ('.' in number_in_str[1:-1]):
                return True
    return False


with open('file-for-task1.txt', 'r') as file:
    numbers = [float(x) for x in file.readlines() if is_float(x)]
with open('file-for-task1.txt', 'a') as files:
    file.write(str(sum(numbers)) + '\n')
    file.write(str(max(numbers)) + '\n')
print('Виконання task3 завершено')