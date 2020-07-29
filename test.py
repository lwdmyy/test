#!/usr/bin/python
# -*- coding:utf-8 -*-
import os
import sys
import time
import threading
import importlib
importlib.reload(sys)

PACKAGE_NAME = "com.baidu.searchbox"
ACTIVITY_NAME = "com.baidu.searchbox.MainActivity"
class AutoBrowseTest(threading.Thread):
    def __init__(self, phone_id):
        threading.Thread.__init__(self)
        self.phone_id = phone_id
    def viewPage(self ,url,j):
        print('\nurl== '+ url)
        os.popen('adb -s ' + self.phone_id + ' shell am start -n ' + PACKAGE_NAME + '/' + ACTIVITY_NAME + ' -a android.intent.action.VIEW -d ' + url + '')
        time.sleep(5)
    def run(self):
        f = open("url.txt","r")
        for j,line in enumerate(f):
            print("num: ",j)
            url = line.strip()
            self.viewPage(url, j)
            time.sleep(3)
        f.close()
def get_phone_id(device_id):
    phone_id_list = []
    if device_id == "":
        shell_content = os.popen("adb devices | grep -v List | grep device").read()
        device_list = shell_content.split('\n')
        for index in range(0, len(device_list) - 1):
            phone_id_list.append(device_list[index].split()[0])  
    else:
        phone_id_list.append(device_id)
    return phone_id_list  
def main(device_id):
    print('Get Devices & Create Related Threads For Each Device & Prepare Email Content......')
    phone_id = get_phone_id(device_id)[0]  
    auto_browser_thread = AutoBrowseTest(phone_id)
    auto_browser_thread.start()
    auto_browser_thread.join()
    print('Done!!!!!!')
if __name__ == "__main__":
    device_id = ""
    if len(sys.argv) > 1:
        device_id = sys.argv[1]
    main(device_id) 
    os._exit(0)  