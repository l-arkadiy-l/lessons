from github import Github

# главный класс, который мы будем использовать для изменения репозиториев
g = Github('TOKEN')
user = g.get_user('User name')
# получаем все наши репозитории
repos = user.get_repos()
for i in repos:
    repo_name = i.name
    # получаем имя нашего репозитория и делаем его приватным
    user.get_repo(repo_name).edit(private=True)
