from github import Github

# главный класс, который мы будем использовать для изменения репозиториев
g = Github('TOKEN')
user = g.get_user('User name')
repo = user.get_repo("school-lessons")
contents = repo.get_contents("(ваша папака/файл) или просто (файл)", ref="main")
# contents.path - путь до файла в вашем репозитории, который нужно удалить
# remove test - имя коммита для удаления
# contents.sha - хэщ коммита
# branch - название ветки
repo.delete_file(contents.path, "remove test", contents.sha, branch="main")
