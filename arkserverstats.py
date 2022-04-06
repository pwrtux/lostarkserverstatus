import time
import requests
from bs4 import BeautifulSoup
import time
import pprint
import json



headers = {
   "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                 "Chrome/74.0.3729.169 Safari/537.36",
}

class LostA_servers:

    @staticmethod
    def get_server_status(monitored_servers):
        """Checks whether a server is full or not. Default server to check is Una.
        A specific server can be set in the function argument."""
        True

        url = "https://www.playlostark.com/en-us/support/server-status"
        html = requests.get(url, headers=headers)
        try:
            soup = BeautifulSoup(html.content, "lxml")
            status = html.status_code

        except:
            print("An error occurred. Trying again in 5 seconds")
            time.sleep(5)

        server_list = soup.find_all('div',
                                    class_='ags-ServerStatus-content-responses-response-server')

        new_status = {}

        for server in server_list:
            server_name = server.find('div',
                                      class_='ags-ServerStatus-content-responses-response-server-name').text.strip()
            if server_name in monitored_servers:
                if server.find('div',
                               class_='ags-ServerStatus-content-responses-response-server-status '
                                      'ags-ServerStatus-content-responses-response-server-status--good'):
                    new_status[server_name] = '✅ Ok'
                if server.find('div',
                               class_='ags-ServerStatus-content-responses-response-server-status '
                                      'ags-ServerStatus-content-responses-response-server-status--busy'):
                    new_status[server_name] = '❌ Busy'
                if server.find('div',
                               class_='ags-ServerStatus-content-responses-response-server-status '
                                      'ags-ServerStatus-content-responses-response-server-status--maintenance'):
                    new_status[server_name] = '🛠️ Maintenance ️'
                if server.find('div',
                               class_='ags-ServerStatus-content-responses-response-server-status '
                                      'ags-ServerStatus-content-responses-response-server-status--full'):
                    new_status[server_name] = '⚠️ Full'

        

        data = {"status": status, "data": new_status}


        if status != 200:
            raise Exception("API response: {}".format(status))
        return data
       

    @staticmethod
    def get_server_list_status():
        """gets all servers into one list"""
        True

        url = "https://www.playlostark.com/en-us/support/server-status"
        html = requests.get(url, headers=headers)
        try:
            soup = BeautifulSoup(html.content, "lxml")
            status = html.status_code

        except:
            print("An error occurred. Trying again in 5 seconds")
            time.sleep(5)

        server_list = soup.find_all('div',
                                    class_='ags-ServerStatus-content-responses-response-server')

        new_status = {}

        for server in server_list:
            server_name = server.find('div',
                                      class_='ags-ServerStatus-content-responses-response-server-name').text.strip()
            if server.find('div',
                           class_='ags-ServerStatus-content-responses-response-server-status '
                                  'ags-ServerStatus-content-responses-response-server-status--good'):
                new_status[server_name] = '✅ Ok'
            if server.find('div',
                           class_='ags-ServerStatus-content-responses-response-server-status '
                                  'ags-ServerStatus-content-responses-response-server-status--busy'):
                new_status[server_name] = '❌ Busy'
            if server.find('div',
                           class_='ags-ServerStatus-content-responses-response-server-status '
                                  'ags-ServerStatus-content-responses-response-server-status--maintenance'):
                new_status[server_name] = '🛠️ Maintenance ️'
            if server.find('div',
                           class_='ags-ServerStatus-content-responses-response-server-status '
                                  'ags-ServerStatus-content-responses-response-server-status--full'):
                new_status[server_name] = '⚠️ Full'

        data = {"status": status, "data": new_status}

        if status != 200:
            raise Exception("API response: {}".format(status))
        return data

        



