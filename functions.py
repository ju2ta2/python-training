def hello(name):
    print("Hello there,", name)


def sum_nums(a, b):
    sum = a + b
    return sum
    print("Line is not executed")


def sum_nums_void(a, b):
    sum = a + b


hello('Alex')
first_num = sum_nums(10, 5)
print(first_num)
print(sum_nums(50.5, 29))
print(sum_nums(sum_nums(50.5, 29), 30))

sec_num = sum_nums_void(10, 5)
print(sec_num)
