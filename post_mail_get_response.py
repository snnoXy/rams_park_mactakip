import requests
import pandas
from appfolder.config import api_key

#Still in development
def post_mailList_to_url(excelList, url):
    data = pandas.read_excel(excelList)
    nameAndMailList = list()

    for i, row in data.iterrows():

        row = row.to_dict()

        if row not in nameAndMailList:
            nameAndMailList.append(row)

    response = requests.post(url, headers={'X-Api-Key': api_key}, json=nameAndMailList)
