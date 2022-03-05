list_1 = [1, 2, 3, 4]
list_2 = [10, 20, 30, 40]


def power(x, y):
    return x * y


ans_lambda = list(map(lambda x, y: x * y, list_1, list_2))
ans_def = list(map(power, list_1, list_2))
print(ans_lambda, ans_def)
