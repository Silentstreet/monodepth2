import os 
##只是这台电脑需要移除掉python中的ros代码
import sys
sys.path.remove('/opt/ros/kinetic/lib/python2.7/dist-packages')
import cv2

def video2frames(pathIn='',
                 pathOut='',
                 only_output_video_info=False,
                 extract_time_point=None,
                 initial_extract_time=0,
                 end_extract_time=None,
                 extract_time_interval=-1,
                 output_prefix='frame',
                 jpg_quality=100,
                 isColor=True):
    '''
    pathIn　输入的视频路径
    pathOut 输出的图片路径
    only_output_video_info　如果为True，只输出视频信息(长度、帧率、帧数)，不提取图片
    extract_time_point 提取的时间点，单位为秒，为元组数据，比如(2,3,5)表示只提取第２s、３s、５s的数据
    initial_extract_time　开始提取时间,默认为0
    end_extract_time　提取结束时间,默认为None(视频终点)
    extract_time_interval　提取帧之间的时间间隔，默认为-1(提取所有帧)
    output_prefix　图片的前缀名，默认为frame，图片的名称为frame_00000001.jpg
    jpg_quality 输出图片的质量
    isColor　True表示彩色，我们需要黑白
    '''

    cap = cv2.VideoCapture(pathIn)
    n_frame = int(cap.get(cv2.CAP_PROP_FRAME_COUNT)) #得到视频的帧数
    fps = cap.get(cv2.CAP_PROP_FPS)
    #print('the fps of this video is {}'.format(fps))
    dur = n_frame / (fps)

    if only_output_video_info:
        print('only output video information (without extract frames) :::::')
        print('Duration of the video: {}second'.format(dur))
        print('Number of frames: {}'.format(n_frame))
        print('Frames per second(FPS): {}'.format(fps))

    elif extract_time_point is not None:
        #提取特定时间戳下的frame，留待后续完成
        print('22222')
    else:
        if initial_extract_time > dur:
            raise NameError('提取帧时间超过源视频长度')
        if end_extract_time is not None:
            if end_extract_time > dur:
                raise NameError("end extract time is larger than the video duration...")
            if initial_extract_time > end_extract_time:
                raise NameError("end extract time is less than the initial extract time ...")
        #时间范围内的每张图片都要输出
        if extract_time_interval == -1:
            if initial_extract_time > 0:
                #这里不是很明白
                cap.set(cv2.CAP_PROP_POS_MSEC, (1000 * initial_extract_time))
            
            try:
                os.mkdir(pathOut)
            except OSError:
                pass
            print('Converting a viedo into frames ......')
            
            if end_extract_time is not None:
                print("end_extract_time is {}, and initial_extract_time is {}".format(end_extract_time, initial_extract_time))
                N = (end_extract_time - initial_extract_time) * fps + 1
                print("N is {}".format(N))
                success = True
                count = 0
                while success and count < N:
                    success, image=cap.read()
                    if success:
                        if not isColor:
                            image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
                        print("Write a new frame1: {}, {}/{}".format(success, count + 1, n_frame))
                        cv2.imwrite(os.path.join(pathOut, "{:010d}.jpg".format(count+1)), image,
                                    [int(cv2.IMWRITE_JPEG_QUALITY), jpg_quality])
                        count = count + 1

            else:
                success = True
                count = 0
                while success:
                    success, image = cap.read()
                    if success:
                        if not isColor:
                            image = cv2.cvtColor(iamge, cv2.COLOR_BGR2GRAY)
                        print('Write a new frame2: {}, {}th'.format(success, count+1))
                        cv2.imwrite(os.path.join(pathOut, "{}_{:06d}.jpg".format(output_prefix, count+1)), image,
                                    [int(cv2.IMWRITE_JPEG_QUALITY), jpg_quality])     #save frame as jpg
                        count = count + 1
        else:
            #时间范围内并不是每帧都输出
            print('333333')

#### 测试
#import cv2 as cv 
#cap = cv.VideoCapture('/data_1/dataset/')

if __name__ == '__main__':
    pathIn = '/home/nld/桌面/code/video/3520201223_120135.mkv'
    pathOut = '/home/nld/桌面/code/video/images'
    print('11111')
    video2frames(pathIn, pathOut, only_output_video_info=False)
"""
if __name__ == '__main__':
    dir_all_zip = '/home/max/'
    unzip_all_file(dir_all_zip)
"""

"""
１．我们首先需要在train.py的当前文件夹下新建文件夹corridor_dataset,然后将我们得到的训练图片放在上面的data文件夹下
２．然后我们需要将options.py下面的--data_path的默认参数从kitti修改为corridor_dataset
3 .除此之外我们还要创建训练集和验证集的文本文档放置在split/eigen_zhou/下面
"""

"""
视频中有时候会有黑屏的镜头，需要再写一个脚本，重新编号。
"""
