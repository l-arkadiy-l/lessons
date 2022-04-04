from github import Github

g = Github('TOKEN')
user = g.get_user('User name')
# получаем все наши репозитории
for i in user.get_repos():
    repo_name = i.name
    # список имен репозиториев, которые хотим удалить
    if repo_name in ['-', '-3', 'ex1', 'bot', 'bot_', 'flask']:
        repo = user.get_repo(repo_name)
        repo.delete()
