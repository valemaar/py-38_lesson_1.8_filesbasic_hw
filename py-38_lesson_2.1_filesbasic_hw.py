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
    for dish_name in dishes: # итерируем список полученных блюд
        if dish_name in cook_book:
            for ings in cook_book[dish_name]: # итерируем ингридиенты в блюде
                meas_quan_list = dict()
                if ings['ingredient_name'] not in ingr_list:
                    meas_quan_list['measure'] = ings['measure']
                    meas_quan_list['quantity'] = ings['quantity'] * person_count
                    ingr_list[ings['ingredient_name']] = meas_quan_list
                else:
                    ingr_list[ings['ingredient_name']]['quantity'] = ingr_list[ings['ingredient_name']]['quantity'] + ings['quantity'] * person_count
        else:
            print(f'\n"Такого блюда нет в списке!"\n')
    return ingr_list

print('Словарь ингредиентов:')
pprint(get_shop_list_by_dishes(['Омлет', 'Фахитос'], 2))

# task 3 (даны три текст.файла, объедините их в один, отсортировав при этом по кол-ву строк
# и добавив служебную информацию)

# def sort_files():
#     file1_path = os.path.join(os.getcwd(), '1.txt')
#     file2_path = os.path.join(os.getcwd(), '2.txt')
#     file3_path = os.path.join(os.getcwd(), '3.txt')
#     with open(file1_path, 'r', encoding='utf-8') as f:
#         file1 = f.read()