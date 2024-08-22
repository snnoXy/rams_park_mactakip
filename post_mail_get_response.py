import requests
import pandas
from appfolder.config import api_key,excelFilePath

def post_mailList_to_url(excelList, url):
    data = pandas.read_excel(excelList)
    nameAndMailList = list()

    for i, row in data.iterrows():

        row = row.to_dict()

        if row not in nameAndMailList:
            nameAndMailList.append(row)

    response = requests.post(url, headers={'X-Api-Key': api_key}, json=nameAndMailList)

    if response.status_code == 200 or response.status_code == 201:
        print(f"Data has been posted correctly. {response.json()}")
    else:
        print(f"Something went wrong {response.status_code} {response.text}")

post_mailList_to_url(excelFilePath, "http://127.0.0.1:5000/post_matches")