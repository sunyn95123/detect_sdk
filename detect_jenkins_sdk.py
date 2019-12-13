#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import sys
from urllib import request
import urllib
import re
import datetime
import zipfile
from time import sleep
"""
时间排序
"""

def get_AgoraSDK(file_path,downlod_addres):

        local_addres = str(downlod_addres).split("/")[-1]

        print(local_addres)
        urllib.request.urlretrieve(downlod_addres, local_addres)
        """解压zip"""
        zip_file = zipfile.is_zipfile(file_path+local_addres)
        if zip_file:
            fz = zipfile.ZipFile(file_path+local_addres, 'r')
            for file in fz.namelist():
                fz.extract(file, file_path)
        else:
            print('This is not zip')





if __name__ == '__main__':

    file_path = '/Users/labtest/workspace_git/AgoraRTCEngine-test/AutoBuild/sdks/'
    """遍历清空文件夹"""
    for root, dirs, files in os.walk(file_path, topdown=False):
        for name in files:
            os.remove(os.path.join(root, name))
        for name in dirs:
            os.rmdir(os.path.join(root, name))
    sleep(2)
    if len(sys.argv) >=3:
        file_path = sys.argv[2]
    if len(sys.argv) >= 2:

        get_AgoraSDK(file_path,sys.argv[1])
    else:
        print(sys.argv[1])
        print("请输入版本号,如'v2.9.0.50'")