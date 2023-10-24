# test_line.py

from bs4 import BeautifulSoup
from datetime import datetime
import requests
import time

url = "https://powerapi.tsinghua.tw/n1";
status = -1
i = 0
pre_value = -1
while(1):
  response = requests.get(url);
  data = response.json();
  print("Current time:", data['time'], " ", "Current Load:", data['value'], "kW");
  
  # send time and power
  headers = {
    "Authorization": "Bearer " + "mVO97RfsTkgQHmbgC2jcS2NznBbeo5825HgNu2RKChR",
    "Content-Type": "application/x-www-form-urlencoded"
  }
  params = {"message": f"\n{data['value']} kW時間:\n {data['time']}"}
  requests.post("https://notify-api.line.me/api/notify", headers=headers, params=params)

  
  pre_status = status
  if(data['value'] < 6700):
    status = 0
  if (data['value'] > 6700 and data['value'] < 6800):
    status = 1
  if (data['value'] >= 6800 and data['value'] < 6850):
    status = 2
  if (data['value'] >= 6850 and data['value'] < 6900):
    status = 3
  if (data['value'] > 6900):
    status = 4
  print(status, pre_status)
  if ((status == 2 or status == 3 or status == 4) and pre_value != data['value']):
    headers = {
      "Authorization": "Bearer " + "mVO97RfsTkgQHmbgC2jcS2NznBbeo5825HgNu2RKChR",
      "Content-Type": "application/x-www-form-urlencoded"
    }
    params = {"message": f"\n{data['value']} kW時間:\n {data['time']}"}
    requests.post("https://notify-api.line.me/api/notify", headers=headers, params=params)
  if (status == 0 and pre_status != 0):
    headers = {
      "Authorization": "Bearer " + "mVO97RfsTkgQHmbgC2jcS2NznBbeo5825HgNu2RKChR",
      "Content-Type": "application/x-www-form-urlencoded"
    }
    params = {"message": f"\n低於6700 kW\n資料提取時間:\n {data['time']}\n瓦數:\n{data['value']} kW"}
    requests.post("https://notify-api.line.me/api/notify", headers=headers, params=params)
  if (status == 1 and pre_status != 1):
      headers = {
        "Authorization": "Bearer " + "mVO97RfsTkgQHmbgC2jcS2NznBbeo5825HgNu2RKChR",
        "Content-Type": "application/x-www-form-urlencoded"
      }
      params = {"message": f"\n超過6700 kW\n資料提取時間:\n {data['time']}\n瓦數:\n{data['value']} kW"}
      requests.post("https://notify-api.line.me/api/notify", headers=headers, params=params)
  if (status == 2 and pre_status != 2):
      headers = {
        "Authorization": "Bearer " + "mVO97RfsTkgQHmbgC2jcS2NznBbeo5825HgNu2RKChR",
        "Content-Type": "application/x-www-form-urlencoded"
      }
      params = {"message": f"\n超過6800 kW\n資料提取時間:\n {data['time']}\n瓦數:\n{data['value']} kW"}
      requests.post("https://notify-api.line.me/api/notify", headers=headers, params=params)
  if (status == 3 and pre_status != 3):
      headers = {
        "Authorization": "Bearer " + "mVO97RfsTkgQHmbgC2jcS2NznBbeo5825HgNu2RKChR",
        "Content-Type": "application/x-www-form-urlencoded"
      }
      params = {"message": f"\n超過6850 kW\n資料提取時間:\n {data['time']}\n瓦數:\n{data['value']} kW"}
      requests.post("https://notify-api.line.me/api/notify", headers=headers, params=params)
  if (status == 4 and pre_status != 4):
      headers = {
        "Authorization": "Bearer " + "mVO97RfsTkgQHmbgC2jcS2NznBbeo5825HgNu2RKChR",
        "Content-Type": "application/x-www-form-urlencoded"
      }
      params = {"message": f"\n超過6900 kW\n資料提取時間:\n {data['time']}\n瓦數:\n{data['value']} kW"}
      requests.post("https://notify-api.line.me/api/notify", headers=headers, params=params)
  pre_value = data['value']
  time.sleep(60)
