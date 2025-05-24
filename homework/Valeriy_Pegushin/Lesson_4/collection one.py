my_dict = {'tuple': (1, 'two', 3, 4.12, False),
           'list': [1, 'two', 3, 4.12, False],
           'dict': {'one': 1, 'two': 'two', 'three': 3, 'four': 4.12, 'five': False},
           'set': {1, 'two', 3, 4.12, False}}
print(my_dict['tuple'][-1])
my_dict['list'].append(True)
my_dict['list'].pop(1)
my_dict['dict'][('i am a tuple',)] = 'any value'
my_dict['dict'].pop('one')
my_dict['set'].add(6)
my_dict['set'].pop()

print(my_dict)
