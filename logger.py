def write(file, msg):
    with open(f"{file}.log", "a") as f:
        f.write(msg + "\n")