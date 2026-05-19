from datetime import datetime

def log(message):

    with open("trade_log.txt", "a") as file:

        file.write(f"{datetime.now()} - {message}\n")