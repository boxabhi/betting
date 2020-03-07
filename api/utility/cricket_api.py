import requests
from api.models import cricketApi
import json

def get_cricket_data():
    URL = "https://cricapi.com/api/matches?apikey=joVatepAe8aeyxlC0jIEPdMo9d93"
    result  = requests.get(URL)
    data = result.json()
    data_json = json.dumps(data)
    save_result = cricketApi(data = data_json)
    save_result.save()
    