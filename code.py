import requests
from win32com.client import Dispatch                                # pip install win32
from requests import *
import json
speak =Dispatch("SAPI.SpVoice")

def getnews(num):
    '''This function take an integer as input and return same number of top news headlines '''
    j = 1
    p =0
    api_key = "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"                                                                  # replace xxxxx....  with your API Key.
    url = "https://newsapi.org/v2/top-headlines?country=in&category=general&apiKey="
    req =  requests.get(f"{url}{api_key}")
    news =  json.loads(req.text)
    read_news =""
    for i in news["articles"] :
        if p == num:
            break
        else :
            read_news = read_news + f"News {j} is {i['title']}\n"
        j+= 1
        p +=1
    return read_news    

def speaker(command):
    '''This funtion takes a string as input and speak it.'''
    speak.Speak(command)

if __name__ == '__main__':                                                #main menu 
    while True :
        d = int(input("How many top news you want ?\t"))
        nnews = getnews(d)
        print(f"\nTodays top {d} News are : \n")
        speaker(f"\nTodays top {d} News are : \n")
        print(nnews)
        speaker(nnews)
        break
