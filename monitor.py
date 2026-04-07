import requests
import time
import logging
from rollback import rollback

logging.basicConfig(filename='monitor.log', level=logging.INFO)

def check_health():
    try:
        r = requests.get("http://127.0.0.1:5000")
        return r.status_code == 200
    except:
        return False

while True:
    if not check_health():
        logging.error("App failure detected! Triggering rollback...")
        rollback()
        break
    time.sleep(5)