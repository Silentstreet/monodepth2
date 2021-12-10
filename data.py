#从KITTI数据集下载下来的数据，解压为.png

import os
import zipfile
import shutil

dir_one_zip_example = '/home/max/'

def unzip_one_file(dir_one_zip=dir_one_zip_example):
    dir_path = os.path.zipfile(dir_one_zip)[0]
    if not zipfile.is_zipfile(dir_one_zip):
        print(dir_one_zip, 'is not a zipfile')
        return

    with zipfile.Zipfile(dir_one_zip) as zf:
        if 'drive' in dir_one_zip:
            dir_date_first = dir_one_zip.split('_drive')[0] #/home/max/campus/2011_09_28_driver_0016/2011_09_28
            prefix_name = os.path.split(dir_date_first)[-1] #2011_09_28
            if not os.path.exists(dir_date_first):
                os.mkdir(dir_date_first)
            temp_dir = os.path.join(dir_path, 'temp_dir') #存放解压文件的临时文件夹
            dir_date_second = os.path.join(temp.dir, prefix_name)
            if not os.path.exists(temp.dir):
                os.mkdir(temp.dir)

            zf.extractall(temp_dir)  #解压到临时文件夹中去
            obj_dir = os.listdir(dir_date_second)
            if len(obj_dir == 1):
                src_dir = os.path.join(dir_date_second, obj_dir[0])
                shutil.move(src_dir, dir_date_first)
                shutil.retree(dir_date_second)


def unzip_all_file(dir_all_zip):
    dir_zip_list = os.listdir(dir_all_zip)
    for index, zip_item in enumerate(dir_zip_list):
        dir_one_zip = os.path.join(dir_all_zip, zip_item)
        unzip_one_file(dir_one_zip)
        print(index+1, dir_one_zip)


if __name__ == '__main__':
    dir_all_zip = '/home/max/'
    unzip_all_file(dir_all_zip)