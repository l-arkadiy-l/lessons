list_ages = [['user1', 90], ['user2', 78], ['user3', 40], ['user4', 3]]
result_sum = list(filter(lambda current_user: current_user[-1] > 50, list_ages))
print(result_sum)
