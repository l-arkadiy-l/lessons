from github import Github

# главный класс, который мы будем использовать для изменения репозиториев
g = Github('TOKEN')
user = g.get_user('User name')
# получаем имя репозитория
repo = user.get_repo('repo name')
repo.create_file(path='test.txt', message='hi', content='this is content')
