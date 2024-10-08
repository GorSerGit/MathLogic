import time

from Func import find_column_combinations
from Func import implicants_to_group
from Func import bin_to_implicants
from Func import num_to_implicants
from Func import group
from Func import accordance

# Запрашиваем у пользователя ввод данных
user_input = list(map(int, input("Введите список значений через пробел: ").split()))
print()

# Получаем список простых импликант
implicants, mass_bin = num_to_implicants(user_input)

work = True
to_implicants = implicants

while work:

    groups, work = implicants_to_group(to_implicants)

    to_implicants = groups

groups = list(set(groups))

print()
print("Получаем итоговые импликанты которые нельзя сократить:")
print()

for impl in groups:
    print(impl.replace('∧','').replace('--','') + "∨", end = "")

print()

# Строим таблицу соответствия импликантам

# Создаем матрицу с нулями
table = [[0 for j in range(len(groups))] for i in range(len(mass_bin))]

print()
print("Таблица покрытия импликант:")
print()

for i in range(len(mass_bin)):
    for j in range(len(groups)):
        table[i][j] = accordance(groups[j], mass_bin[i])
        print(table[i][j], end = " ")
    print()

combinations = find_column_combinations(table)

#1 2 3 4 5 6 9 11 13 15
print()
print("Получаем минимальные ДНФ:")
print()

# Выводим номера нужных столбцов для каждой уникальной комбинации
for i, combo in enumerate(combinations):
    for j in combo:
        print(groups[int(j)].replace('--','').replace('∧',''), end = "∨")
    print()

