import os


file_path = '/Users/labtest/workspace/AgoraRTCEngine-test/AutoBuild/Results/'
"""遍历清空文件夹"""
for root, dirs, files in os.walk(file_path, topdown=False):

    for name in files:
        if name.endswith("DS_Store"):
            continue
        os.remove(os.path.join(root, name))

    for name in dirs:
        if name.endswith("DS_Store"):
            continue
        os.rmdir(os.path.join(root, name))