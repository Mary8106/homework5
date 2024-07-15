#immutable_var = 1, 4, 'a', 'c'
#print(immutable_var)
#immutable_var[0] = 150 # кортеж не поддерживает обращение по элементам, он неизменяемый
mutable_list = [2, 'яблока']
mutable_list[0] = 3
print(mutable_list)