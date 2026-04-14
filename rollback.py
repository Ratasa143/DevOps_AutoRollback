import shutil
import logger

def rollback():
    shutil.copy("versions/v1/app.py", "app/app.py")
    logger.write("rollback", "Rollback to v1 done")

if __name__ == "__main__":
    rollback()