import requests
#from urllib import urlopen
import time
from bs4 import BeautifulSoup
import requests
import json
import configparser as cfg
import re
from datetime import date

def getlecture (dep, deg):
    today = date.today()
    today = str(today)
    url ="https://www.unibz.it/it/timetable/?sourceId=unibz&department="+ dep +"&degree="+ deg +"&fromDate=" + today + "&toDate=" + today
    response = requests.get(url)
    elem = []
    lectures = []
    timm = []
    lecturestimes = []
    soup = BeautifulSoup(response.text, features="html.parser")
    lects = soup.find_all("h3")
    lects = str(lects)
    elem = lects.split(",")
    for i in elem:
        if '"u-h5 u-push-btm-1">' in i:
            res = re.search('"u-h5 u-push-btm-1">(.*)</h3>',i).group(1)   
            lectures.append(res) 
    times = soup.find_all('p')
    times = str(times)
    tim = times.split('<p class="u-push-btm-none u-tt-caps u-fs-sm u-fw-bold">')
    for i in tim[1:]:
        temp = i[0:30]
        temp = temp.replace(" ","")
        temp = temp.replace("\n", "")
        timm.append(temp)
    
    for i in range(len(lectures)):
        lecturestimes.append({"lecture" : lectures[i], "times" : timm[i]})

    return lectures, timm


class telegram_chatbot():

    def __init__(self, config):
        self.token = self.read_token_from_config_file(config)
        self.base = "https://api.telegram.org/bot{}/".format(self.token)

    def get_updates(self, offset=None):
        url = self.base + "getUpdates?timeout=100"
        if offset:
            url = url + "&offset={}".format(offset + 1)
        r = requests.get(url)
        return json.loads(r.content)

    def send_message(self, msg, chat_id):
        url = self.base + "sendMessage?chat_id={}&text={}".format(chat_id, msg)
        if msg is not None:
            requests.get(url)

    def read_token_from_config_file(self, config):
        parser = cfg.ConfigParser()
        parser.read(config)
        return parser.get('creds', 'token')