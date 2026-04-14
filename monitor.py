import time
import requests
from rollback import rollback
import logger

while True:
    try:
        r = requests.get("http://127.0.0.1:5000")
        if r.status_code != 200:
            logger.write("monitor", "Failure detected")
            rollback()
            break
    except:
        logger.write("monitor", "App not reachable")
        rollback()
        break

    time.sleep(3)