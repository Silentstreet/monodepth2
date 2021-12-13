from __future__ import absolute_import, division, print_function
# 加上这些，如果你的python版本是python2.X，你也得按照python3.X那样使用这些函数
import os
import argparse

file_dir = os.path.dirname(__file__)
# 在运行的时候如果输入完整的执行的路径，则返回.py文件的全路径如：
# python c:/test/test.py 则返回路径 c:/test ，如果是python test.py 则返回空
# 这样就保证定位到了脚本所在的文件夹

"""
argparse是一个Python模块：命令行选项、参数和子命令解析器。使用步骤为３步
1. 创建解析器 
    ap = argparse.ArgumentParser(description=" ")
2. 添加参数
    ap.add_argument(...)
3. 解析参数
    ap.parse_args(...)
"""



class MonodepthOptions:
    def __init__(self):
        self.parser = argparse.ArgumentParser(description="Monodepthv2 options")

        # PATHS　这里更改好默认数据文件夹
        self.parser.add_argument("--data_path",
                                 type=str,
                                 help="path to the training data",
                                 dedault=os.path.join(file_dir, "my_data"))
        self.parser.add_argument("--log_dir",
                                 type=str,
                                 help="log directory",
                                 default=os.path.join(os.path.expanduser("~"), "tmp"))
        # os中的这个os.path.expanduser("~")很有意思
        # 本质上就是在Linux下面，如果是使用你自己的电脑，一般可以用~来代替/home/用户名
        # 但是python是不认识这个符号的，所以要用os.path.expanduser("～")来把~展开

        # Training options
        self.parser.add_argument("--model_name",
                                type=str,
                                help="the name of the folder to save the model in",
                                default="mdp")
        self.parser.add_argument("--split",
                                type=str,
                                help="which training split to use",
                                choices=["eigen_zhou", "eigen_full", "odm", "benchmark"],
                                default="eigen_zhou")
        self.parser.add_argument("--num_layers",
                                 type=int,
                                 help="number of resnet layers",
                                 default=18,
                                 choices=[18, 34, 50, 101, 152])
        #这里没理解
        self.parser.add_argument("--dataset",
                                 type=str,
                                 help="dataset to train on",
                                 default="kitti",
                                 choices=["kitti", "kitti_odom", "kitti_depth", "kitti_test"])
        self.parser.add_argument("--png",
                                 help="if set ,trains from raw KITTI png files(instead of jpg)",
                                 action="store_true")
        #这里默认图片高度怎么会是192呢
        self.parser.add_argument("--height",
                                 type=int,
                                 help="input image height",
                                 default=192)
        self.parser.add_argument("--width",
                                 type=int,
                                 help="input image width",
                                 default=640)
        #这里不清楚了这个参数是处理图片什么的
        self.parser.add_argument("--disparity_smoothness",
                                 type=float,
                                 help="disparity smoothness weight",
                                 default=1e-3)
        self.parser.add_argument("--scales",
                                 nargs="+",
                                 type=int,
                                 help="scales used in loss",
                                 default=[0, 1, 2, 3])
        self.parser.add_argument("--min_depth",
                                 type=float,
                                 help="minimum depth",
                                 default=0.1)
        self.parser.add_argument("--max_depth",
                                 type=float,
                                 help="maximum depth",
                                 default=100.0)
        self.parser.add_argument("--use_sterro",
                                 help="if set, uses stereo pair for training",
                                 action="store_true")
        #这个参数要注意，和采用单目、双目训练有关
        self.parser.add_argument("--frame_ids",
                                 nargs="+",
                                 type=int,
                                 help="frames to load",
                                 default=[0, -1, 1])

        # OPTIMIZATION options
        #内存大小有关，每个数据集的大小
        self.parser.add_argument("--batch_size",
                                 type=int,
                                 help="batch size",
                                 default=12)
        self.parser.add_argument("--learning_rate",
                                 type=float,
                                 help="learning rate",
                                 default=1e-4)
        self.parser.add_argument("--num_epochs",
                                 type=int,
                                 help="number of epochs",
                                 default=20)
        self.parser.add_argument("--scheduler_step_size",
                                 type=int,
                                 help="step size of the scheduler",
                                 default=15)
        
        # ABLATION options
        """
        """

        # System options
        self.parser.add_argument("--no_cuda",
                                 help="if set disables CUDA",
                                 action="store_true")
        self.parser.add_argument("--num_workers",
                                 type=int,
                                 help="number of dataloader workers",
                                 default=12)
        # Loading options
        self.parser.add_argument("--load_weight_folder",
                                 type=str,
                                 help="name of model to load")
        self.parser.add_argument("--models_to_load",
                                 nargs="+",
                                 type=str,
                                 help="model to load",
                                 default=["encoder", "depth", "pose_encoder", "pose"])

        # Logging options
        self.parser.add_argument("--log_frequency",
                                 type=int,
                                 help="number of batchs between each tensorboard log",
                                 default=250)
        self.parser.add_argument("--save_frequency",
                                 type=int,
                                 help="number of epochs between each save",
                                 default=1)

        # Evaluation options
        """
        """

        def parse(self):
            self.options = self.parser.parse_args()
            return self.options
