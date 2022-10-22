from pprint import pprint
# Task 1
def cook_dict(file):
    with open(file, 'r', encoding='utf-8') as f:
        cook_book = {}
        ingr = []
        key_ = []
        value = []
        n = 0
        m = 0
        # Creating the list of type ingr = [{}, {}, ... {}].
        # The list will be used to create list of values for the dict
        for line in f:
            if line == '\n':
                pass
            elif '|' in line:
                data = line.split(' | ')
                for d in data:
                    if "\n" in d:
                        data[2] = d.strip("\n")
                ingr.append({'ingredient_name': data[0],
                            'quantity': data[1],
                            'measure': data[2]})
            # Creating the list of type key_ = [key, numb_ingr, key, ...] 
            # This list will be used for the keys of dict 
            # AND creating the list of values
            else:
                line = line.strip('\n')
                key_.append(line)
        # Creating the list of type value = [[{}, {}... *y times], [{}, ...*y], ...] 
        # where y is the number of ingr for the dish
        while True:
            ingr1 = list(ingr[m:m+int(key_[1 + n])])
            value.append(ingr1)
            if key_[1 + n] is key_[-1]:
                n = 0
                break
            m += int(key_[1 + n])
            n += 2
        # key_ list and value list are ready
        while True:
            cook_book[key_[0 + 2*n]] = value[0 + n]
            if value[0 + n] is value[-1]:
                break
            n += 1
        # pprint(cook_book)
        return cook_book
# cook_dict('data.txt')

# Task 2
def get_shop_list_by_dishes(dishes, pers_count):
    cook_book = cook_dict(input("Choose the file you want to analyze: "))
    cooked_dishes = {}
    ingr_q = []
    ingr_name = []
    n = 0
    for dish in dishes:
        for ingr in cook_book[dish]:
            ingr['quantity'] = int(ingr['quantity'])
            ingr['quantity'] *= pers_count
            ingr_name.append(ingr['ingredient_name'])
            del ingr['ingredient_name']
            ingr_q.append(ingr)
    while True:
        cooked_dishes[ingr_name[n]] = ingr_q[n]
        if ingr_q[n] is ingr_q[-1]:
            break
        n += 1
    pprint(cooked_dishes)

get_shop_list_by_dishes(['Омлет', 'Утка по-пекински'], 3)