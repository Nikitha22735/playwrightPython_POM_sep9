import csv
import json
import os

from dotenv import load_dotenv
from openpyxl import load_workbook
import pytest

# @pytest.mark.dh
def test_jsonhandling():
    with open('testData\\creds.json') as data:
        creds = json.load(data)
        print(creds["NegitiveCreds"]["username"])


# @pytest.mark.dh
def test_csvHandling():
    with open('testData\\credentails.csv') as data:
        creds = csv.DictReader(data)
        l1 = []
        for i in creds:
            l1.append(i)
        print(l1[2]["username"])


#pip install openpyxl

def test_handlingExcel():
    workbook = load_workbook('testData\\sample_creds.xlsx')
    sheetData = workbook["Sheet2"]
    l1 = []
    for i in sheetData.iter_rows(min_row=2,values_only=True):
        l1.append(i)

    print(l1[2][0])

# @pytest.mark.dh
def test_handlingExcelWrite():
    workbook = load_workbook('testData\\sample_creds.xlsx')
    sheetData = workbook["Sheet2"]
    # sheetData["A4"]="trpiura"
    # sheetData.delete_rows(2,sheetData.max_row)
    # sheetData.append(["tripra123","data123"])
    sheetData.insert_rows(2)
    sheetData["A2"]="helo"
    sheetData["B2"]="how"
    workbook.save('testData\\sample_creds.xlsx')

# set sep9usName=testUser&&set sep9pw=testPassword&&pytest -m dh -s
# @pytest.mark.dh
def test_cli():
    username = os.getenv('sep9usName')
    password = os.getenv('sep9pw')
    print(username)
    print(password)

#pip install python-dotenv
# set file=.env.dev&&pytest -m dh -s
@pytest.mark.dh
def test_env():
    load_dotenv(os.getenv('file'))
    username = os.getenv('sep9usName_env1')
    password = os.getenv('sep9pw_env1')
    print(username)
    print(password)


