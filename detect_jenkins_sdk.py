#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import sys
from urllib import request
import urllib
import zipfile
from time import sleep
"""
时间排序
"""

def get_AgoraSDK(file_path,downlod_addres):

        local_addres = str(downlod_addres).split("/")[-1]
        urllib.request.urlretrieve(downlod_addres, file_path+local_addres)
        print(file_path+local_addres)
        sleep(2)
        """解压zip"""
        zip_file = zipfile.is_zipfile(file_path+local_addres)
        if zip_file:
            fz = zipfile.ZipFile(file_path + local_addres, 'r')
            if 'SDK_for_Mac' in str(local_addres):
                os.system('unzip -n -d ~/workspace/AgoraRTCEngine-test/AutoBuild/sdks_path {}'.format(
                    file_path + local_addres))
            else:
                for file in fz.namelist():
                    fz.extract(file, file_path)
                if 'SDK_for_SDK_for_Windows' in str(local_addres):
                    sleep(5)

if __name__ == '__main__':

    print(len(sys.argv))
    print(sys.argv[1])
    if len(sys.argv) >=2:
        clear_file_path = '/Users/labtest/workspace/AgoraRTCEngine-test/AutoBuild/sdks_path/'

        """遍历清空文件夹"""
    for i in range(10):
        while True:
            try:
                for root, dirs, files in os.walk(clear_file_path, topdown=False):

                    for name in files:
                        if name.endswith("DS_Store"):
                            continue
                        os.remove(os.path.join(root, name))
                    for name in dirs:
                        if name.endswith("DS_Store"):
                            continue
                        os.rmdir(os.path.join(root, name))
            except Exception as e:
                continue
            break
        sleep(1)
    get_AgoraSDK(clear_file_path,sys.argv[1])


