#import requests 
#requests.get ("https://randomuser.me/api/")

import os 
import time
def shutdown(offPC=19):
    while time.gmtime().tm_hour < offPC:
        time.sleep(5)
        os.system("shutdown /s /t 10")


shutdown()