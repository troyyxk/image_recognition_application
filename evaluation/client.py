import json
import os.path
import time
import requests
import base64
import glob
import concurrent.futures
import threading

path = 'pictures/*'

upload_url = 'http://165.124.51.192:28000/api/upload/'

query_url = 'http://165.124.51.192:28000/api/query/'


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


#def upload():
    #session = get_session()
uuid_list = []
starttime_list = []
payloadsize_list = []
for filename in glob.glob(pathname=path):
    print('-------------------------------')
    img = open(filename, 'rb')
    b64_string = base64.b64encode(img.read()).decode('utf-8')
    file_ext = os.path.splitext(filename)[1][1:]
    b64_string = create_payload(b64_string, file_ext)
    payloadsize_list.append(len(b64_string) * 8)
    data = {'image_b64': b64_string}
    data = json.dumps(data)
    start_time = time.time()
    starttime_list.append(start_time)
    r = requests.post(upload_url, data=data)
    print(r.status_code)
    print(r.json())
    uuid = r.json()['result']['uuid']
    uuid_list.append(uuid)
    print(uuid)


idx = 0
for uuid in uuid_list:
    r = requests.get(query_url + uuid)
    while r.status_code != 200 or r.json()['code'] != 0 or r.json()['result']['status'] != 2:
        r = requests.get(query_url + uuid)
    end_time = time.time()
    print("--------------------------------------")
    print(r.json())
    time_elapsed = end_time - starttime_list[idx]
    print('Time Elapsed : ' + str(end_time - starttime_list[idx]))
    tput = payloadsize_list[idx] / time_elapsed / 1000  # tput in kbps
    print("Throughput: ", tput)
    idx += 1


#thread_local = threading.local


#def get_session():
#    if not hasattr(thread_local, "session"):
#        thread_local.session = requests.Session()
#    return thread_local.session