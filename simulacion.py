import threading
import time
import json
import random
import argparse


def send_data(interval):
    while True:
        data = {
            "timestamp": int(time.time()),
            "message": {
                "id": "value",
                "value": ''.join(random.choices(
                    "abcdefghijklmnopqrstuvwxyz0123456789",
                    k=random.randint(1, 20)))
            }
        }
        print("ThreadID: ", threading.get_ident(), json.dumps(data))
        time.sleep(interval)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("num_threads", type=int, help="Number of threads to create")
    args = parser.parse_args()

    for i in range(args.num_threads):
        #interval = random.uniform(0.1, 5) #intervalo random 
        interval = 3
        t = threading.Thread(target=send_data, args=(interval,))
        t.daemon = True
        t.start()

    while True:
        time.sleep(1)
