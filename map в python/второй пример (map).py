from random import randint

used_id = []
list_employees = ['man', 'man', 'man', 'man', 'girl']


def get_random_id(user_now):
    global list_employees
    x = randint(0, len(list_employees))
    while x in used_id:
        x = randint(0, len(list_employees))
    used_id.append(x)
    return user_now + ' ' + str(x)


if __name__ == '__main__':
    print(list(map(get_random_id, list_employees)))
    
