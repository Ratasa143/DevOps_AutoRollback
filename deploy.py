import shutil

def deploy(version):
    shutil.copy(f"versions/{version}/app.py", "app/app.py")
    print(f"{version} deployed!")

if __name__ == "__main__":
    v = input("Enter version (v1/v2): ")
    deploy(v)