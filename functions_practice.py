


def hello():
    print('hello')

hello()


def pack(arg_one, arg_two, arg_three):
    arg_list = [arg_one, arg_two, arg_three]
    return arg_list

print(pack('ron', 'kla', 'cora'))

def eat_lunch(list_one):
    for i in list_one:

        print(f'First I eat {i}')
    print('My lunchbox is empty!')


list_main = ['apple', 'bannana', 'sandwich', 'watermellon']

eat_lunch(list_main)




