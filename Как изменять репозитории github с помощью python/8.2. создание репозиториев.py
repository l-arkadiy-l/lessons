from github import Github

# главный класс, который мы будем использовать для изменения репозиториев
g = Github('TOKEN')
user = g.get_user()  # не указываем имя, так как ('NamedUser' object has no attribute 'create_repo')
# получаем имя репозитория
repo = user.create_repo(name='repo_name')
