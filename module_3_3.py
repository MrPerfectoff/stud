def print_params(a = 1, b = 'string', c = True):
    print(a, b, c)

print_params(b = 25)
print_params(c = [1, 2, 3])
print_params()

values_list = [1, 'string', True]
values_dict = {'a': 1, 'b': False, 'c': 'string'}

print_params(*values_list)
print_params(**values_dict)

values_list2 = [5, 'string']
print_params(*values_list2, True)