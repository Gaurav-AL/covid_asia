from bs4 import BeautifulSoup as bs
import requests
import re
from covid_asia_omnicr.models import CumulativeStats 
from covid_asia_omnicr.models import Countries
from covid_asia_omnicr.models import DeltaStats
from django.db.models import Q

# This be de dynamically called, and Database can be used to Store this data
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
        5 : {
        "Country" : "Indonesia",
        "Country_Code" : "IDO",
        "source" : "https://www.worldometers.info/coronavirus/country/Indonesia/",
        "type" : "HTML"
        },
        6 : {
        "Country" : "Bangladesh",
        "Country_Code" : "BNG",
        "source" : "https://www.worldometers.info/coronavirus/country/bangladesh/",
        "type" : "HTML"
        },
        7 : {
        "Country" : "Turkey",
        "Country_Code" : "TY",
        "source" : "https://www.worldometers.info/coronavirus/country/turkey/",
        "type" : "HTML"
        },
        8 : {
        "Country" : "Nepal",
        "Country_Code" : "NPL",
        "source" : "https://www.worldometers.info/coronavirus/country/nepal/",
        "type" : "HTML"
        },
        9 : {
        "Country" : "Malaysia",
        "Country_Code" : "ML",
        "source" : "https://www.worldometers.info/coronavirus/country/malaysia/",
        "type" : "HTML"
        },
        10 : {
        "Country" : "Qatar",
        "Country_Code" : "QTR",
        "source" : "https://www.worldometers.info/coronavirus/country/qatar/",
        "type" : "HTML"
        },
        11 : {
        "Country" : "South Korea",
        "Country_Code" : "SKR",
        "source" : "https://www.worldometers.info/coronavirus/country/south-korea/",
        "type" : "HTML"
        },
        12 : {
        "Country" : "Afghanistan",
        "Country_Code" : "SKR",
        "source" : "https://www.worldometers.info/coronavirus/country/afghanistan/",
        "type" : "HTML"
        },
        13 : {
        "Country" : "Israel",
        "Country_Code" : "SKR",
        "source" : "https://www.worldometers.info/coronavirus/country/Israel/",
        "type" : "HTML"
        },
        14 : {
        "Country" : "Maldives",
        "Country_Code" : "SKR",
        "source" : "https://www.worldometers.info/coronavirus/country/Maldives/",
        "type" : "HTML"
        },
        15 : {
        "Country" : "Oman",
        "Country_Code" : "SKR",
        "source" : "https://www.worldometers.info/coronavirus/country/Oman/",
        "type" : "HTML"
        },
        16 : {
        "Country" : "Laos",
        "Country_Code" : "SKR",
        "source" : "https://www.worldometers.info/coronavirus/country/Laos/",
        "type" : "HTML"
        },
        17 : {
        "Country" : "Syria",
        "Country_Code" : "SKR",
        "source" : "https://www.worldometers.info/coronavirus/country/Syria/",
        "type" : "HTML"
        },
        18 : {
        "Country" : "Yemen",
        "Country_Code" : "SKR",
        "source" : "https://www.worldometers.info/coronavirus/country/Yemen/",
        "type" : "HTML"
        },
        19 : {
        "Country" : "Jordan",
        "Country_Code" : "SKR",
        "source" : "https://www.worldometers.info/coronavirus/country/Jordan/",
        "type" : "HTML"
        },
        20 : {
        "Country" : "Mongolia",
        "Country_Code" : "SKR",
        "source" : "https://www.worldometers.info/coronavirus/country/Mongolia/",
        "type" : "HTML"
        }
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
    data = {}
    for key,value in source.items():
        if(value['Country'] == "India"):
            data[value["Country"]] = getIExtractedData(value["Country"],value["source"])
        else:
            data[value["Country"]] = getWExtractedData(value["Country"],value['source'])
    return data


def updateCountries(Source):
    for key,value in Source.items():
        update = Countries(aid = key, Country = value["Country"])
        update.save()       

# updateCountries(source)
    
def earlierCumulativeStats(data):
    k = 0
    for key,value in data.items():
        cumulative = CumulativeStats(aid = k, Country = key, Confirmed = value[f"{key}"]["ConfirmedCases"], Recovered = value[f"{key}"]["RecoveredCases"],Deaths = value[f"{key}"]["Deaths"])
        cumulative.save()
        k += 1
        

# earlierCumulativeStats(getdata())

def updateDeltaStats_CumulativeStats():
    data = {}
    data = getdata()
    api_data = {}
    for key,value in data.items():

        earlier_confirmed = CumulativeStats.objects.get(Country = key).Confirmed.strip().replace(',','')
        earlier_recovered = CumulativeStats.objects.get(Country = key).Recovered.strip().replace(',','')
        earlier_Deaths = CumulativeStats.objects.get(Country = key).Deaths.strip().replace(',','')


        latest_confirmed = value[f"{key}"]["ConfirmedCases"].strip().replace(',','')
        latest_recovered = value[f"{key}"]["RecoveredCases"].strip().replace(',','')
        latest_Deaths = value[f"{key}"]["Deaths"].strip().replace(',','')

        Delta_recoverd = str(int(latest_recovered) - int(earlier_recovered))
        Delta_active = str(int(latest_confirmed) - int(earlier_confirmed))
        Delta_deaths = str(int(latest_Deaths) - int(earlier_Deaths))

        api_data[key] = {"CumulativeConfirmed" : latest_confirmed, "CumulativeRecovered":latest_recovered, "CumulativeDeaths":latest_Deaths,"Delta_active":Delta_active, "Delta_Deaths" :Delta_deaths,"Delta_Recovered":Delta_recoverd}

        deltastats = DeltaStats(Country = key, Active = Delta_active, Death = Delta_deaths, Recovered = Delta_recoverd,Latest_Confirmed = latest_confirmed, Latest_Recovered = latest_recovered,Latest_Deaths = latest_Deaths)
        deltastats.save()

        earlierCumulativeStats(data)

    return api_data

        

# updateDeltaStats_CumulativeStats() 












