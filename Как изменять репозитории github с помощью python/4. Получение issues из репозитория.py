from github import Github

# главный класс, который мы будем использовать для изменения репозиториев
g = Github('TOKEN')
user = g.get_user('User name')
# получаем все наши репозитории
repos = user.get_repos()
for i in repos:
    repo_name = i.name
    print('-->', repo_name)
    repo = user.get_repo(repo_name)
    # выводим список "issues" для репозитория с именем "repo_name"
    print(list(repo.get_issues()))
