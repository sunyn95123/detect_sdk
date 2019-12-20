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
        #     os.system('unzip -n -d /Users/labtest/workspace_git/AgoraRTCEngine-test/AutoBuild/sdks {}'.format(
        #                 file_path+local_addres))
            fz = zipfile.ZipFile(file_path + local_addres, 'r')
            if 'SDK_for_Mac' in str(file_path+info_name[-1][0]):
                os.system('unzip -n -d {}/sdks {}'.format(
                    os.path.split(os.path.realpath(__file__))[0],file_path+info_name[-1][0]))
            else:
                for file in fz.namelist():
                    fz.extract(file, file_path)
                if 'SDK_for_SDK_for_Windows' in str(local_addres):
                    sleep(5)

if __name__ == '__main__':

    file_path = os.path.split(os.path.realpath(__file__))[0] + '/' + 'sdks/'
    """遍历清空文件夹"""
    for i in range(10):
        while True:
            try:
                for root, dirs, files in os.walk(file_path, topdown=False):

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





    sleep(2)
    if len(sys.argv) >=3:
        file_path = sys.argv[2]
    if len(sys.argv) >= 2:
        get_AgoraSDK(file_path,sys.argv[1])