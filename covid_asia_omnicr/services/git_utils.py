import sys
# from github import Github
from covid_asia_omnicr.services.const import DOWNLOAD_SOURCES_GITHUB_URL as gt
import os
import json
import urllib.request
import re
sys.path.append('../')
username="Gaurav-AL"

def SourcePath():
     url = gt

     try:
         response = urllib.request.urlopen(url) 
     except urllib.error.HTTPError:
         print("Error ! Http :) Not Found")

     path = os.getcwd()
     source_csv = open('sources', 'wb')
     source_csv.write(response.read())
     source_csv.close()
     return path+'/sources'



        