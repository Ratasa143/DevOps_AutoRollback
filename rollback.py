import shutil
import logging

logging.basicConfig(filename='rollback.log', level=logging.INFO)

def rollback():
    shutil.copy("versions/v1/app.py", "app/app.py")
    logging.info("Rollback to v1 successful!")
    print("Rolled back to stable version!")