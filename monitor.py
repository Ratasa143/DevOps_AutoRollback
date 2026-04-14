import requests, time
from logger import log
from rollback import rollback

def monitor():
    while True:
        try:
            r = requests.get("http://127.0.0.1:5000", timeout=3)
            if r.status_code != 200:
                log("Bad response detected")
                rollback()
        except:
            log("App crashed/unreachable")
            rollback()
        time.sleep(5)