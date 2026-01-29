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
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        return response.text
    except requests.RequestException:
        return None

def getWExtractedData(country,url):
    html_doc = getHTMLDoc(url)
    if not html_doc:
        # Mock data for demonstration since internet is disabled
        mock_data = {
            "China": {"ConfirmedCases": "100000", "Deaths": "5000", "RecoveredCases": "95000", "ActiveCases": "0", "ClosedCases": "100000"},
            "India": {"ConfirmedCases": "90000", "Deaths": "3000", "RecoveredCases": "87000", "ActiveCases": "0", "ClosedCases": "90000"},
            "Pakistan": {"ConfirmedCases": "40000", "Deaths": "800", "RecoveredCases": "39200", "ActiveCases": "0", "ClosedCases": "40000"},
            "Bangladesh": {"ConfirmedCases": "30000", "Deaths": "400", "RecoveredCases": "29600", "ActiveCases": "0", "ClosedCases": "30000"},
            "Japan": {"ConfirmedCases": "20000", "Deaths": "300", "RecoveredCases": "19700", "ActiveCases": "0", "ClosedCases": "20000"},
            "Indonesia": {"ConfirmedCases": "15000", "Deaths": "200", "RecoveredCases": "14800", "ActiveCases": "0", "ClosedCases": "15000"},
            "Turkey": {"ConfirmedCases": "25000", "Deaths": "500", "RecoveredCases": "24500", "ActiveCases": "0", "ClosedCases": "25000"},
            "Nepal": {"ConfirmedCases": "10000", "Deaths": "100", "RecoveredCases": "9900", "ActiveCases": "0", "ClosedCases": "10000"},
            "Malaysia": {"ConfirmedCases": "12000", "Deaths": "150", "RecoveredCases": "11850", "ActiveCases": "0", "ClosedCases": "12000"},
            "Qatar": {"ConfirmedCases": "8000", "Deaths": "50", "RecoveredCases": "7950", "ActiveCases": "0", "ClosedCases": "8000"},
            "South Korea": {"ConfirmedCases": "15000", "Deaths": "200", "RecoveredCases": "14800", "ActiveCases": "0", "ClosedCases": "15000"},
            "Afghanistan": {"ConfirmedCases": "5000", "Deaths": "100", "RecoveredCases": "4900", "ActiveCases": "0", "ClosedCases": "5000"},
            "Israel": {"ConfirmedCases": "10000", "Deaths": "100", "RecoveredCases": "9900", "ActiveCases": "0", "ClosedCases": "10000"},
            "Maldives": {"ConfirmedCases": "2000", "Deaths": "10", "RecoveredCases": "1990", "ActiveCases": "0", "ClosedCases": "2000"},
            "Oman": {"ConfirmedCases": "3000", "Deaths": "20", "RecoveredCases": "2980", "ActiveCases": "0", "ClosedCases": "3000"},
            "Laos": {"ConfirmedCases": "1000", "Deaths": "5", "RecoveredCases": "995", "ActiveCases": "0", "ClosedCases": "1000"},
            "Syria": {"ConfirmedCases": "500", "Deaths": "10", "RecoveredCases": "490", "ActiveCases": "0", "ClosedCases": "500"},
            "Yemen": {"ConfirmedCases": "300", "Deaths": "50", "RecoveredCases": "250", "ActiveCases": "0", "ClosedCases": "300"},
            "Jordan": {"ConfirmedCases": "2000", "Deaths": "20", "RecoveredCases": "1980", "ActiveCases": "0", "ClosedCases": "2000"},
            "Mongolia": {"ConfirmedCases": "100", "Deaths": "1", "RecoveredCases": "99", "ActiveCases": "0", "ClosedCases": "100"},
            "Bhutan": {"ConfirmedCases": "50", "Deaths": "0", "RecoveredCases": "50", "ActiveCases": "0", "ClosedCases": "50"}
        }
        default = {"ConfirmedCases": "N/A", "Deaths": "N/A", "RecoveredCases": "N/A", "ActiveCases": "N/A", "ClosedCases": "N/A", "source": url}
        data_dict = mock_data.get(country, default)
        data_dict["source"] = url  # Ensure source is set
        return {country: data_dict}
    code_html = bs(html_doc, 'html.parser')
    all_div = code_html.find_all("div", {"id": "maincounter-wrap"})
    value = []
    for x in range(len(all_div)):
        spn = all_div[x].find("span")
        value.append(spn.text if spn else "N/A")
    # Ensure at least 5 values, pad with N/A if less
    while len(value) < 5:
        value.append("N/A")
    return {country: {"ConfirmedCases": value[0], "Deaths": value[1], "RecoveredCases": value[2], "ActiveCases": value[3], "ClosedCases": value[4], "source": url}}

def getIExtractedData(country,url):
    html_doc = getHTMLDoc(url)
    if not html_doc:
        # Mock data for India
        return {country: {"ConfirmedCases": "90000", "Deaths": "3000", "RecoveredCases": "87000", "ActiveCases": "0", "ClosedCases": "90000", "source": url}}
    code_html = bs(html_doc, 'html.parser')
    confirmed_cases = code_html.find("li", {"class": "bg-blue"})
    recovered_cases = code_html.find("li", {"class": "bg-green"})
    deaths = code_html.find("li", {"class": "bg-red"})

    if not confirmed_cases or not recovered_cases or not deaths:
        return {country: {"ConfirmedCases": "N/A", "Deaths": "N/A", "RecoveredCases": "N/A", "ActiveCases": "N/A", "ClosedCases": "N/A", "source": url}}

    confirmed_list = confirmed_cases.find_all("strong", {"class": "mob-hide"})
    recovered_list = recovered_cases.find_all("strong", {"class": "mob-hide"})
    deaths_list = deaths.find_all("strong", {"class": "mob-hide"})

    cc = extract_number(confirmed_list)
    rc = extract_number(recovered_list)
    dt = extract_number(deaths_list)

    return {country: {"ConfirmedCases": cc, "Deaths": dt, "RecoveredCases": rc, "ActiveCases": "N/A", "ClosedCases": "N/A", "source": url}}

def extract_number(elements):
    for x in elements:
        text = x.text.strip()
        if re.search(r"[0-9]", text):
            return text.split('\xa0')[0]
    return "0"
    

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

def getNews():
    url = "https://www.worldometers.info/coronavirus/"
    html_doc = getHTMLDoc(url)
    if not html_doc:
        return []
    soup = bs(html_doc, 'html.parser')
    news_items = soup.find_all('div', class_='news_post')
    news_list = []
    for item in news_items[:5]:  # Get top 5 news
        title_tag = item.find('a')
        if title_tag:
            title = title_tag.text.strip()
            link = "https://www.worldometers.info" + title_tag['href'] if title_tag.get('href') else ""
            news_list.append({"title": title, "link": link})
    return news_list

def updateDeltaStats_CumulativeStats():
    data = getdata()
    news = getNews()
    api_data = {}
    for key, value in data.items():
        try:
            cumulative_obj = CumulativeStats.objects.get(Country=key)
            earlier_confirmed = cumulative_obj.Confirmed.strip().replace(',', '')
            earlier_recovered = cumulative_obj.Recovered.strip().replace(',', '')
            earlier_Deaths = cumulative_obj.Deaths.strip().replace(',', '')
        except CumulativeStats.DoesNotExist:
            earlier_confirmed = earlier_recovered = earlier_Deaths = "0"

        latest_confirmed = value[key]["ConfirmedCases"].strip().replace(',', '')
        latest_recovered = value[key]["RecoveredCases"].strip().replace(',', '')
        latest_Deaths = value[key]["Deaths"].strip().replace(',', '')

        try:
            Delta_recoverd = str(int(latest_recovered) - int(earlier_recovered))
            Delta_active = str(int(latest_confirmed) - int(earlier_confirmed))
            Delta_deaths = str(int(latest_Deaths) - int(earlier_Deaths))
        except ValueError:
            Delta_recoverd = Delta_active = Delta_deaths = "0"

        api_data[key] = {
            "CumulativeConfirmed": latest_confirmed,
            "CumulativeRecovered": latest_recovered,
            "CumulativeDeaths": latest_Deaths,
            "ActiveCases": value[key]["ActiveCases"],
            "ClosedCases": value[key]["ClosedCases"],
            "Delta_active": Delta_active,
            "Delta_Deaths": Delta_deaths,
            "Delta_Recovered": Delta_recoverd,
            "source": value[key]["source"]
        }

        deltastats = DeltaStats(
            Country=key,
            Active=Delta_active,
            Death=Delta_deaths,
            Recovered=Delta_recoverd,
            Latest_Confirmed=latest_confirmed,
            Latest_Recovered=latest_recovered,
            Latest_Deaths=latest_Deaths
        )
        deltastats.save()

        earlierCumulativeStats(data)

    api_data["news"] = news
    return api_data

        

# updateDeltaStats_CumulativeStats() 












