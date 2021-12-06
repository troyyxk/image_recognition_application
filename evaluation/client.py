import json
import os.path
import time
import requests
import base64
import glob

path = 'pictures/*'

upload_url = 'http://143.215.216.196:28000/api/upload/'

query_url = 'http://143.215.216.196:28000/api/query/'


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


for filename in glob.glob(pathname=path):
    print('-------------------------------')
    img = open(filename, 'rb')
    b64_string = base64.b64encode(img.read()).decode('utf-8')
    file_ext = os.path.splitext(filename)[1][1:]
    b64_string = create_payload(b64_string, file_ext)
    data = {'image_b64': b64_string}
    data = json.dumps(data)
    start_time = time.time()
    r = requests.post(upload_url, data=data)
    print(r.status_code)
    print(r.json())
    uuid = r.json()['result']['uuid']
    print(uuid)
    r = requests.get(query_url + uuid)
    while r.status_code != 200 or r.json()['code'] != 0 or r.json()['result']['status'] != 2:
        r = requests.get(query_url + uuid)
    end_time = time.time()
    print(r.json())
    print('Time Elapsed: ' + str(end_time - start_time))
