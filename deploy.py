import shutil
import os
import logging

logging.basicConfig(filename='deploy.log', level=logging.INFO)

def deploy(version):
    src = f"versions/{version}/app.py"
    dest = "app/app.py"

    shutil.copy(src, dest)
    logging.info(f"Deployed version {version}")

if __name__ == "__main__":
    version = input("Enter version to deploy (v1/v2): ")
    deploy(version)