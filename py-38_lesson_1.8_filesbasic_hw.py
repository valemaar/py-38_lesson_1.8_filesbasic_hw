import os


from pprint import pprint


def read_cookbook():
    file_path = os.path.join(os.getcwd(), 'recipes.txt')
    cook_book = dict()
    with open(file_path, 'r', encoding='utf-8') as f:
        for line in f:
            dish_name = line.strip()
            count = int(f.readline())
            ing_list = list()
            for item in range(count):
                ingrs = {}
                ingr = f.readline().strip()
                ingrs['ingredient_name'], ingrs['quantity'], ingrs['measure'] = ingr.split('|')
                ingrs['quantity'] = int(ingrs['quantity'])
                ing_list.append(ingrs)
            f.readline()
            cook_book[dish_name] = ing_list
    return cook_book


print('cook_book:')
pprint(read_cookbook())

# task 2 (необходимо получить словарь из ингридиентов для заданного списка блюд и персон)
cook_book = read_cookbook()
print()
print('Task 2')


def get_shop_list_by_dishes(dishes, person_count):
    ingr_list = dict()
    for dish_name in dishes:  # итерируем список полученных блюд
        if dish_name in cook_book:
            for ings in cook_book[dish_name]:  # итерируем ингридиенты в блюде
                meas_quan_list = dict()
                if ings['ingredient_name'] not in ingr_list:
                    meas_quan_list['measure'] = ings['measure']
                    meas_quan_list['quantity'] = ings['quantity'] * person_count
                    ingr_list[ings['ingredient_name']] = meas_quan_list
                else:
                    ingr_list[ings['ingredient_name']]['quantity'] = ingr_list[ings['ingredient_name']]['quantity'] +\
                                                                     ings['quantity'] * person_count
        else:
            print(f'\n"Такого блюда нет в списке!"\n')
    return ingr_list


print('Словарь ингредиентов:')
pprint(get_shop_list_by_dishes(['Омлет', 'Фахитос'], 2))

# task 3 (даны три текст.файла, объедините их в один, отсортировав при этом по кол-ву строк
# и добавив служебную информацию)


def sort_files(path1, path2, path3):
    file1_path = os.path.join(os.getcwd(), path1)
    file2_path = os.path.join(os.getcwd(), path2)
    file3_path = os.path.join(os.getcwd(), path3)
    with open(file1_path, 'r', encoding='utf-8') as f1:
        file1 = f1.readlines()
    with open(file2_path, 'r', encoding='utf-8') as f2:
        file2 = f2.readlines()
    with open(file3_path, 'r', encoding='utf-8') as f3:
        file3 = f3.readlines()
    with open('sorted.txt', 'w', encoding='utf-8') as f_summ:
        if len(file1) < len(file2) and len(file1) < len(file3):
            f_summ.write(path1 + '\n')
            f_summ.write(str(len(file1)) + '\n')
            f_summ.writelines(file1)
            f_summ.write('\n')
        elif len(file2) < len(file1) and len(file2) < len(file3):
            f_summ.write(path2 + '\n')
            f_summ.write(str(len(file2)) + '\n')
            f_summ.writelines(file2)
            f_summ.write('\n')
        elif len(file3) < len(file1) and len(file3) < len(file2):
            f_summ.write(path3 + '\n')
            f_summ.write(str(len(file3)) + '\n')
            f_summ.writelines(file3)
            f_summ.write('\n')
        if len(file1) < len(file2) and len(file1) > len(file3) or len(file1) > len(file2) and len(file1) < len(file3):
            f_summ.write(path1 + '\n')
            f_summ.write(str(len(file1)) + '\n')
            f_summ.writelines(file1)
            f_summ.write('\n')
        elif len(file2) < len(file1) and len(file2) > len(file3) or len(file2) > len(file1) and len(file2) < len(file3):
            f_summ.write(path2 + '\n')
            f_summ.write(str(len(file2)) + '\n')
            f_summ.writelines(file2)
            f_summ.write('\n')
        elif len(file3) < len(file1) and len(file3) > len(file2) or len(file3) > len(file1) and len(file3) < len(file2):
            f_summ.write(path3 + '\n')
            f_summ.write(str(len(file3)) + '\n')
            f_summ.writelines(file3)
            f_summ.write('\n')
        if len(file1) > len(file2) and len(file1) > len(file3):
            f_summ.write(path1 + '\n')
            f_summ.write(str(len(file1)) + '\n')
            f_summ.writelines(file1)
        elif len(file2) > len(file1) and len(file2) > len(file3):
            f_summ.write(path2 + '\n')
            f_summ.write(str(len(file2)) + '\n')
            f_summ.writelines(file2)
        elif len(file3) > len(file1) and len(file3) > len(file2):
            f_summ.write(path3 + '\n')
            f_summ.write(str(len(file3)) + '\n')
            f_summ.writelines(file3)
    return


sort_files('1.txt', '2.txt', '3.txt')
