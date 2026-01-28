
from git import Repo

PATH_OF_GIT_REPO = 'https://github.com/Gaurav-AL/covid_asia'  # make sure .git folder is properly configured
COMMIT_MESSAGE = 'comment from python script'

def git_push():
    try:
        repo = Repo.init(PATH_OF_GIT_REPO)
        repo.git.add(update=True)
        repo.index.commit(COMMIT_MESSAGE)
        origin = repo.remote(name='origin')
        origin.push()
    except:
        print('Some error occured while pushing the code')    

git_push()

# user = "Gaurav-AL "
# g = Github(user)
# repo = g.get_user().get_repo('incovid19') # repo name
# file_list = ['C:\\Users\gaura']
# file_names = ['test.txt']
# commit_message = 'python commit demo'
# master_ref = repo.get_git_ref('heads/master')
# master_sha = master_ref.object.sha
# base_tree = repo.get_git_tree(master_sha)

# element_list = list()
# for i, entry in enumerate(file_list):
#     element = InputGitTreeElement(file_names[i], '100644', 'blob', data)
#     element_list.append(element)

# tree = repo.create_git_tree(element_list, base_tree)
# parent = repo.get_git_commit(master_sha)
# commit = repo.create_git_commit(commit_message, tree, [parent])
# master_ref.edit(commit.sha)