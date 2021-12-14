import os 
def makefile(path, content):
    if os.path.exists(path):
        if os.path.isdir(path):
            f = open('/home/nld/桌面/code/video/images/train_files.txt', 'a+')
            f.write(content)
            f.write('\n')
            #file.seek(0)是重新定位在文件的第0位及开始位置
            f.seek(0)
            read = f.readline()
            f.close()
            print(read)
        else:
            print("please input the dir name")
    else:
        print("the path is not exists")





if __name__ == '__main__':
    path = '/home/nld/桌面/code/video/images'
    count = 1
    print('11111')
    while count < 656:
        # r"" 的作用是去除转义字符.
        content = r"2021_09_17 {} l".format(count)
        makefile(path,content)
        count = count + 1