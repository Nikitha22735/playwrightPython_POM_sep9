
import json


def jsonhandling(filePath):
    with open(filePath) as data:
        creds = json.load(data)
        return creds