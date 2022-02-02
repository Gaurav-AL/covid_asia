from lib2to3.pgen2 import token
from github import Github
from covid_asia_omnicr.services import const
import os
import json
import urllib.request
import re

username="Gaurav-AL"
g=Github()
user=g.get_user(username)
'''
Github API is used because it provide easier access to get content of specific file.
'''
repo = user.get_repo("covid_asia")
covid_asia = repo.get_contents("")
def SourcePath():
    url = const.DOWNLOAD_SOURCES_GITHUB_URL

    try:
        response = urllib.request.urlopen(url) 
    except urllib.error.HTTPError:
        print("Error ! Http :) Not Found")

    path = os.getcwd()
    source_csv = open('sources', 'wb')
    source_csv.write(response.read())
    source_csv.close()
    return path+'/sources'


repo.create_file("test.txt","Created new file through API","22-jan-2022", branch="main")
        