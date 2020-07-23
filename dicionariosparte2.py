# import copy

# d1 = { 1: 'a', 2: 'b', 3: 'c', 'd' : ['Luiz', 'Otávio']}
# v = copy.deepcopy(d1)
# v[1] = 'Luiz'

# v['d'][0] = 'Joãozinho'

# print(d1)
# prin

d1 = {1:2,3:4,5:6}
d2 = {'a':'b','c':'d'}

d1.update(d2)
print(d1)