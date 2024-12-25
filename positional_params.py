# Задача "Распаковка"
def print_params (a = 1, b = 'строка', c = True):
    print (a, b, c)                                 # функция должна выводить эти параметры

print_params()
print_params(2, 25, False)
print_params(b = 25)
print_params(c = [1,2,4])

# Задача "Распаковка параметров"
values_list = ['None', False, 17]
values_dict ={'a': 189.19, 'b': 'Истерика', 'c': False}

print_params(*values_list)
print_params(**values_dict)

# Задача "Распаковка + отдельные параметры"
values_list_2 = [36.92, 'Молва']
print_params(*values_list_2, 42)