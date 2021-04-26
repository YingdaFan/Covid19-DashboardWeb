import requests
import json


def get_data():
    url = "https://covid.cdc.gov/covid-data-tracker/COVIDData/getAjaxData?id=us_trend_data"
    response = requests.get(url)
    json_data = json.loads(response.content)
    date = []
    new_case = []
    for i in json_data['us_trend_data']:
        if i['state'] == 'United States':
            date.append(i['date'])
            new_case.append(i['New_case'])

    data = {'date': date, 'new_case': new_case}
    return data
