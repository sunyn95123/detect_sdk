import os






def get_path():

    work_dir = '/Users/labtest/workpace_2.6.1/AgoraRTCEngine-test/AutoBuild/sdks'
    for root, dirs, files in os.walk(work_dir, topdown=False):

        for name in dirs:
            if name.endswith("DS_Store"):
                continue
            if 'Agora_Native_SDK_for' in str(dirs):
                d = ''.join(dirs)
                print(type(d))
                return dirs


if __name__ == '__main__':
    get_path()