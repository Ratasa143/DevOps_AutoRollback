def log(msg):
    with open("system.log", "a") as f:
        f.write(msg + "\n")