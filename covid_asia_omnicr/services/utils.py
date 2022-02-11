from bs4 import BeautifulSoup as bs
import requests
import re
from covid_asia_omnicr.services import const


def getHTMLDoc(url):
    response = requests.get(url)
    return response.text

def getWExtractedData(country,url):
    value = []
    code_html =  bs(getHTMLDoc(url), 'html.parser')
    all_div = code_html.find_all("div", {"id": "maincounter-wrap"})
    for x in range(len(all_div)-1):
        spn = all_div[x].find("span")
        value.append(spn.text)
    return {country:{"ConfirmedCases":value[0],"Deaths":value[1],"RecoveredCases":value[2]}}

def getIExtractedData(country,url):
    value = []
    code_html = bs(getHTMLDoc(url),'html.parser')
    confirmed_cases = code_html.find("li", {"class": "bg-blue"})
    recovered_cases = code_html.find("li",{"class":"bg-green"})
    deaths = code_html.find("li",{"class":"bg-red"})
    
    confirmed_cases = confirmed_cases.find_all("strong",{"class":"mob-hide"})
    recovered_cases = recovered_cases.find_all("strong",{"class":"mob-hide"})
    deaths = deaths.find_all("strong",{"class":"mob-hide"})

    cc,rc,dt = 0,0,0
    for x in confirmed_cases:
        if(re.search("[0-9]",x.text)):
            cc = x.text.split('\xa0')[0]
    
    for x in recovered_cases:
        if(re.search("[0-9]",x.text)):
            rc = x.text.split('\xa0')[0]
    
    for x in deaths:
        if(re.search("[0-9]",x.text)):
            dt = x.text.split('\xa0')[0]
        
    return {country:{"ConfirmedCases":cc,"Deaths":dt,"RecoveredCases":rc}}
    

def getdata(dict):
    for key,value in dict.items():
        print(key,value)
print(const.source)

