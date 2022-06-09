


from types import FunctionType


def arb_args(*names):
    print(*names)


arb_args('chester', 'cora', 'chis', 'rob')

def inner_func(int_one, int_two):

    def function_one(int_one, int_two):
        add_one = int_one + int_two
        return add_one

    
    
    def function_two(int_one, int_two):
        add_two = int_one - int_two
        return add_two

    return print(function_one(int_one, int_two) + function_two(int_one, int_two))


inner_func(5, 4)


def lunch_lady(students_name, lunch='Mystery Meat'):
    print(students_name, lunch)


lunch_lady('Chester')


def sum_n_product(int_one, int_two):
    output_one = int_one + int_two
    output_two = int_one * int_two
    return output_one, output_two


print(sum_n_product(3,3))


alias_arb_args = arb_args

def arb_mean(*numbers):
    total = 0
    for i in numbers:
        total += i
    print(total/len(numbers))

arb_mean(4, 4, 2)

def arb_longest_string(*strings):
    length = 0
    longest_length = 0
    longest_string = ""
    for i in strings:
        length = len(i)
        if length > longest_length:
            longest_length = length
            longest_string = i
    print(longest_string)

arb_longest_string('hello', 'goodbye', 'welcome', 'Have a nice day')

