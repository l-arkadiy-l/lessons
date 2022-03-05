from random import randint

used_id = []
list_employees = ['man', 'man', 'man', 'man', 'girl']
len_employee = len(list_employees)
for i in range(len_employee):
    x = randint(0, len_employee)
    while x in used_id:
        x = randint(0, len_employee)
    used_id.append(x)
    list_employees[i] += ' ' + str(x)
print(list_employees)
