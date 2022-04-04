from github import Github

# главный класс, который мы будем использовать для изменения репозиториев
g = Github('TOKEN')
user = g.get_user('User name')
# получаем все наши репозитории
repos = user.get_repos()
for i in repos:
    repo_name = i.name
    print('-->', repo_name)
    print(f"---- views traffic: {user.get_repo(repo_name).get_views_traffic()['count']}")
    print(f"---- clones traffic: {user.get_repo(repo_name).get_clones_traffic()['count']}")

