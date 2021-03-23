from win32com.client import Dispatch
import requests
import json
def speak(str):
    speak =Dispatch("SAPI.SpVoice")
    speak.speak(str)


url = "https://newsapi.org/v2/top-headlines?" \
      "country=us&category=business&" \
      "apiKey=d783ae74ba0e49fbb3d834acebfeee56"
r = requests.get(url)
text = r.text
my_j = json.loads(text)
for i in range(0,11):
    speak(my_j['articles'][i]['title'])
