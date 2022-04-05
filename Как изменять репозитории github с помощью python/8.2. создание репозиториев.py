from github import Github

# главный класс, который мы будем использовать для изменения репозиториев
g = Github('TOKEN')
user = g.get_user()
# получаем имя репозитория
repo = user.create_repo(name='repo_name')
