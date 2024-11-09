places = []
with open("tickets.txt") as file:
    for line in file:
        places.append([x for x in line.split()])

vacant_places = 0
for row in places:
    vacant_places += sum(1 for x in row if x == '0')
print('Кількість вільних місць -', vacant_places)

r, p = [int(x) - 1 for x in input('Введіть номер ряду та місця через пробіл: ').split()]
if r < len(places) and p < len(places[r]):
    if places[r][p] == '0':
        print('Місце вільне')
    else:
        print('Місце зайняте')
else:
    print('В залі відсутне таке місце')