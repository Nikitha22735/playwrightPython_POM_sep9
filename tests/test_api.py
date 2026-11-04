import json
from pathlib import Path

from playwright.sync_api import sync_playwright, Playwright

from utils.jsonHandling import jsonhandling


def UI():
    with sync_playwright() as p:
       context= p.request.new_context()
       response = context.get("https://dummyjson.com/products")
    #    print(type(response))
       print(response.json())


def UI_2(playwright: Playwright):   
    context = playwright.request.new_context()
    response = context.get("https://dummyjson.com/products")
    data =response.json()
    assert response.status==200
    print(data["products"][0]["title"])


def API_3(playwright: Playwright):   
    context = playwright.request.new_context(http_credentials={
        "username":"tripura",
        "password":"12345"
    })
    # response = context.get("https://dummyjson.com/products", headers={ "Authorization": "Bearer 123456"})
    response = context.get("https://dummyjson.com/products", headers={ "x-api-key": "123456789900"}, params={
        "region": "apac"
    })
    response = context.get("https://dummyjson.com/products")
    data =response.json()
    assert response.status==200
    print(data["products"][0]["title"])


def test_API_4(playwright: Playwright):   
    context = playwright.request.new_context()
    host = "dummyjson.com"
    reqbody = jsonhandling("testData\\apiData.json")
    reqbody["title"]="iphone"
    response = context.post("https://dummyjson.com/products/add", headers={ "Authorization": "Bearer 123456"}, data=reqbody)
    data =response.json()
    assert response.status==201
    # print(data["products"][0]["title"])
    print(response.headers["content-type"])



def test_API_CSV_4(playwright: Playwright):   
    context = playwright.request.new_context()
    host = "dummyjson.com"
    reqbody = jsonhandling("testData\\apiData.json")
    reqbody["title"]="iphone"
    file_path = Path("testData\\credentails.csv")
    multipart = {
        key: json.dumps(value) if isinstance(value, (dict, list)) else value
        for key, value in reqbody.items()
    }
    multipart["file"] = {
        "name": file_path.name,
        "mimeType": "text/csv",
        "buffer": file_path.read_bytes(),
    }
    response = context.post("https://dummyjson.com/products/add", headers={ "Authorization": "Bearer 123456" }, multipart=multipart)
    data =response.json()
    assert response.status==201
    # print(data["products"][0]["title"])
    print(response.headers["content-type"])