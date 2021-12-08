import concurrent
import json
import os.path
import time
import requests
import base64
import _thread
import glob
from concurrent.futures import ThreadPoolExecutor
import threading

pic_path = 'pictures/'

upload_url = 'http://server:28000/api/upload/'

query_url = 'http://server:28000/api/query/'


def create_payload(b64_str, file_ext):
    prefix = 'data:image/'
    if file_ext == 'jpg':
        prefix += 'jpeg'
    elif file_ext == 'png':
        prefix += 'png'
    else:
        print('file type not supported')
        return
    prefix += ';base64,'
    b64_str = prefix + b64_str
    return b64_str


def evaluate(path):
    time_list = []
    tput_list = []
    uuid_list = []
    start_list = []
    finish_list = []

    filename = path + "cat.png"
    img = open(filename, 'rb')
    b64_string = base64.b64encode(img.read()).decode('utf-8')
    file_ext = os.path.splitext(filename)[1][1:]
    b64_string = create_payload(b64_string, file_ext)
    payload_size = len(b64_string) * 8
    data = {'image_b64': b64_string}
    data = json.dumps(data)
    for i in range(6):
        # print('-------------------------------')
        # print("send", i)
        start_time = time.time()
        start_list.append(start_time)
        r = requests.post(upload_url, data=data)
        # print(r.status_code)
        # print(r.json())
        uuid = r.json()['result']['uuid']
        uuid_list.append(uuid)
        # print(uuid)
    print("gate 0")

    for i in range(len(uuid_list)):
        uuid = uuid_list[i]
        r = requests.get(query_url + uuid)
        while r.status_code != 200 or r.json()['code'] != 0 or r.json()['result']['status'] != 2:
            r = requests.get(query_url + uuid)
        end_time = time.time()
        finish_list.append(end_time)
    # print(r.json())\
    print("gate 1")
    time_elapsed_list = []
    for i in range(len(start_list)):
        time_elapsed_list.append(finish_list[i] - start_list[i])
        tput_list.append(payload_size / 1000 / time_elapsed_list[i])
    print("gate 2")
    # print('Time Elapsed: ' + sstr(time_elapsed))
    # tput = payload_size / 1000 / time_elapsed
    # print("Throughput: " + str(tput))
    # time_list.append(time_elapsed)
    # tput_list.append(tput)
    f = open("tmp.txt", "a")
    msg = "Avg rtt: " + str(sum(time_elapsed_list) / len(time_elapsed_list))
    f.write(msg)
    msg = "Avg tput: " + str(sum(tput_list) / len(tput_list))
    f.write(msg)
    f.close()
    print("Avg rtt: ", sum(time_elapsed_list) / len(time_elapsed_list))
    print("Avg tput: ", sum(tput_list) / len(tput_list))


def test():
    f = open("tmp.txt", "w")
    f.write("")
    f.close()
    for client_num in [7]:
        print("----------------")
        print("client num: ", client_num)
        threads = []
        with ThreadPoolExecutor(max_workers=client_num) as pool:
            threads.append(pool.map(evaluate, [pic_path]))
        # for i in range(client_num):
        #    try:
        #        _thread.start_new_thread(evaluate, (pic_path,))
        #    except:
        #        print("unable to start new thread")


test()
