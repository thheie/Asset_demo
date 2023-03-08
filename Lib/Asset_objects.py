'''
Contains objects for exploring av testing Atlassian APIs
'''
import json
import requests
from requests.auth import HTTPBasicAuth
from csv import DictReader

import DecodeAssetResonses


def readFromCsv(filename):
    with open(filename, 'r') as f:
        dict_reader = DictReader(f)
        list_of_dict = list(dict_reader)
        print(list_of_dict)
    return list_of_dict

class AssetObjects:

    def __init__(self):
        # Opening JSON file
        f = open('setup.json', )
        setupparams = json.load(f)
        self.baseurl = setupparams['baseurl']
        self.username = setupparams['username']
        self.token = setupparams['token']
        wsurl = f'https://{self.baseurl}/rest/servicedeskapi/assets/workspace'
        self.headers = {"Accept": "application/json"}
        self.auth = HTTPBasicAuth(self.username, self.token)
        response = requests.request("GET", wsurl, headers=self.headers, auth=self.auth)
        jsondata = json.loads(response.text)
        self.workspaceId = jsondata['values'][0]['workspaceId']

    def get_workspaceId(self):
        return self.workspaceId

    def fetch_object_attribs(self, objectId):
        url = f'https://api.atlassian.com/jsm/assets/workspace/{self.workspaceId}/v1/objecttype/{objectId}/attributes/'
        response = requests.request("GET", url, headers=self.headers, auth=self.auth)
        jsondata = json.loads(response.text)
        objectTypeAttribs = DecodeAssetResonses.decodeAssetObjectTypeAttrib(jsondata)



def main():
    workspace = AssetObjects()
    print(workspace.get_workspaceId())
    workspace.fetch_object_attribs(71)
    readFromCsv('NewMobiles.csv')


if __name__ == "__main__":
    main()