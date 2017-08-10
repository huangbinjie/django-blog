import base64
import requests
from threading import Timer
from . import models

endpoint = "https://oauth.reddit.com"
grant_type = "password"
username = base64.b64decode("bGltUQ==")
password = base64.b64decode("aGJqMTQ0MzUxMg==")
client_id = base64.b64decode("QlpOQWtvWGpLcTB0ZHc=")
secret = base64.b64decode("SU1wRFQ4TXp4bGFUODFXSWVhLTlFclRLc3ZF")

payload = {
    "grant_type": grant_type,
    "username": username,
    "password": password
}

headers = {
    "Authorization": "Basic " + base64.b64encode(client_id + ":" + secret)
}


def listings(url):
    token = models.Reddit.objects.latest()
    headers = {"Authorization": token_type + " " + access_token}
    return requests.get(url, headers=headers).json()


def refresh():
    response = requests.post(
        "https://www.reddit.com/api/v1/access_token",
        data=payload,
        headers=headers)
    json = response.json()
    reddit = models.Reddit(
        token_type=json.token_type, access_token=json.access_token)
    reddit.save()
    print(json)
    return json
