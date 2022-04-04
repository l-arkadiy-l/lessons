from github import Github

# главный класс, который мы будем использовать для изменения репозиториев
g = Github('TOKEN')
user = g.get_user('User name')
# получаем все наши репозитории
repos = user.get_repos()
for i in repos:
    repo_name = i.name
    # находим наш репозиторий по имени и получаем список его веток
    print(list(user.get_repo(repo_name).get_branches()))
