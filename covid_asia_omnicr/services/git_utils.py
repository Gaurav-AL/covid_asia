from lib2to3.pgen2 import token
from github import Github

username="Gaurav-AL"
g=Github()
user=g.get_user(username)

repo = user.get_repo("covid_asia")
print(repo)