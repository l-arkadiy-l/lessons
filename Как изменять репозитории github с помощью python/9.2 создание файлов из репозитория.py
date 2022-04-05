from github import Github

# главный класс, который мы будем использовать для изменения репозиториев
g = Github('TOKEN')
user = g.get_user('User name')
repo = user.get_repo("repo_name")
# создаем файл с именем "file_name.txt", коммитом "init commit" и содержимым "file_content ------ "
repo.create_file("file_name.txt", "init commit", "file_content ------ ")
