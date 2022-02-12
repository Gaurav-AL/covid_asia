from bs4 import BeautifulSoup as bs
import requests
import re
from covid_asia_omnicr.services import const


source = {
        0:{
        "Country" : "India",
        "Country_Code" : "IND",
        "source" : "https://www.mohfw.gov.in/",
        "type" : "HTML"
        },

        1:{
        "Country" : "China",
        "Country_Code" : "CHN",
        "source" : "https://www.worldometers.info/coronavirus/country/china/",
        "type" : "HTML"
        },
        2: {
        "Country" : "Pakistan",
        "Country_Code" : "PAK",
        "source" : "https://www.worldometers.info/coronavirus/country/Pakistan/",
        "type" : "HTML"
        },
        3 :{
        "Country" : "Bhutan",
        "Country_Code" : "BHU",
        "source" : "https://www.worldometers.info/coronavirus/country/bhutan/",
        "type" : "HTML"
        },
        4 : {
        "Country" : "Japan",
        "Country_Code" : "JPN",
        "source" : "https://www.worldometers.info/coronavirus/country/Japan/",
        "type" : "HTML"
        },
        6 : {
        "Country" : "Indonesia",
        "Country_Code" : "IDO",
        "source" : "https://www.worldometers.info/coronavirus/country/Indonesia/",
        "type" : "HTML"
        },
        7 : {
        "Country" : "Bangladesh",
        "Country_Code" : "BNG",
        "source" : "https://www.worldometers.info/coronavirus/country/bangladesh/",
        "type" : "HTML"
        },
        8 : {
        "Country" : "Turkey",
        "Country_Code" : "TY",
        "source" : "https://www.worldometers.info/coronavirus/country/turkey/",
        "type" : "HTML"
        },
        9 : {
        "Country" : "Nepal",
        "Country_Code" : "NPL",
        "source" : "https://www.worldometers.info/coronavirus/country/nepal/",
        "type" : "HTML"
        },
        10 : {
        "Country" : "Malaysia",
        "Country_Code" : "ML",
        "source" : "https://www.worldometers.info/coronavirus/country/malaysia/",
        "type" : "HTML"
        },
        11 : {
        "Country" : "Qatar",
        "Country_Code" : "QTR",
        "source" : "https://www.worldometers.info/coronavirus/country/qatar/",
        "type" : "HTML"
        },
}

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
    

def getdata():
    data = []
    for key,value in source.items():
        if(value['Country'] == "India"):
            data.append(getIExtractedData("India",value['source']))
        else:
            data.append(getWExtractedData(value["Country"],value['source']))
    return data
        
    
print(getdata())

