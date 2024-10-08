
from itertools import combinations

def find_column_combinations(matrix):
    rows = len(matrix)
    cols = len(matrix[0])
    valid_combinations = []

    # Проверяем все возможные комбинации столбцов
    for r in range(1, cols + 1):
        for cols_comb in combinations(range(cols), r):
            # Создаем множество покрытых строк
            covered_rows = set()
            
            for row in range(rows):
                # Проверяем, есть ли единица в выбранных столбцах
                if any(matrix[row][col] == 1 for col in cols_comb):
                    covered_rows.add(row)

            # Если все строки покрыты, добавляем комбинацию в результат
            if len(covered_rows) == rows:
                valid_combinations.append(cols_comb)

    return valid_combinations

def bin_to_implicants(element):

    implicant = ""

    key = {
        '0':'¬x',
        '1':'x'}

    for i in range(len(element)):
        implicant += key[element[i]] + str(i+1) + '∧'

    return implicant[:-1]

def num_to_implicants(elements):

    mass_bin = []

    maxLeng = len(bin(max(elements))[2:])

    for i in range(len(elements)):
        elements[i] = bin(elements[i])[2:]

        while (len(elements[i]) < maxLeng):
            elements[i] = '0' + elements[i]

        mass_bin.append(elements[i])
        elements[i] = bin_to_implicants(elements[i])

    return elements, mass_bin

def group(element1, element2):

    fl = 0

    element1, element2 = list(element1.split("∧")), list(element2.split("∧"))

    element = ""

    for i in range(len(element1)):
        if element1[i] != element2[i]:
            if (fl):
                return "0"
            else:
                fl = 1
                element += '--' + '∧'

        else:
             element += element1[i] + '∧'

    return element[:-1]

def implicants_to_group(elements):

    Couples = []
    work = False

    pars = []

    for element1 in elements:
        fl = 1
        for element2 in elements:

            if element1 != element2:

                couple = group(element1, element2)

                c = str(element1) + str(element2)

                if len(couple) > 1:
                    
                    work = True
                    fl = 0
                    if c not in pars:
                        print("Группируем " + str(element1) + "   " + str(element2) + " Получаем :" + str(couple))
                        pars.append(str(element2) + str(element1))
                        Couples.append(couple)
                    #time.sleep(2)
    

        if (fl):
            
            Couples.append(element1)
        

    return Couples, work

def accordance(func, impl):

    func = func.split("∧")

    for i in range(len(func)):
        #print(func[i])
        fl = 1
        if (str(impl)[i] == '0' and '¬' in func[i]) or '--' == func[i]:
            fl = 0
        if str(impl)[i] == '1' and '¬' not in func[i]:
            fl = 0

        if fl:
            return 0

    return 1
