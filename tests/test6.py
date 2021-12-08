import _thread
import time
import json
import os.path
import requests
import base64

pic_path = '../pictures/'

upload_url = 'http://server:28000/api/upload/'

query_url = 'http://server:28000/api/query/'

def print_time( threadName, delay):
   count = 0
   while count < 5:
      time.sleep(delay)
      count += 1
      print(threadName, ": ", time.ctime(time.time()))
    #   print "%s: %s" % ( threadName, time.ctime(time.time()) )

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


def evaluate(path, thread_id):
    # print("gate1")
    filename = path + "cat.png"
    img = open(filename, 'rb')
    b64_string = base64.b64encode(img.read()).decode('utf-8')
    file_ext = os.path.splitext(filename)[1][1:]
    b64_string = create_payload(b64_string, file_ext)
    # print("gate2")

    # send
    payload_size = len(b64_string) * 8
    data = {'image_b64': b64_string}
    data = json.dumps(data)
    start_time = time.time()
    r = requests.post(upload_url, data=data)
    uuid = r.json()['result']['uuid']
    # print("gate3")

    # send
    r = requests.get(query_url + uuid)
    while r.status_code != 200 or r.json()['code'] != 0 or r.json()['result']['status'] != 2:
        r = requests.get(query_url + uuid)
    end_time = time.time()
    time_elapsed = end_time - start_time
    print("thread ", thread_id, " Avg rtt: ", time_elapsed)
    # print("thread ", thread_id, " Avg tput: ", len(b64_string) * 8 / 1000 / time_elapsed)


if __name__ == "__main__":
    num_threads = 6
    for i in range(num_threads):
        # print("gate0")
        _thread.start_new_thread( evaluate, (pic_path, i) )
    while 1:
        pass
