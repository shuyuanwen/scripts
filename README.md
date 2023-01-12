# 各类脚本

## BeihangLogin 服务器自动登录脚本
上网不涉密，涉密不上网！

北航网络认证

### 用户名和密码的存放
请将 `account.example` 文件复制为 `account` 文件，并存放于脚本同目录，然后在其中输入你的学号和密码。

### 检测并自动登录

两个 try-connect 脚本可以检测当前是否已登录，如果没有登录就自动登录。

* `try-connect.sh` 通过 ping 百度来检测登录状态
* `try-connect-v2.sh` 通过访问网关 API 来检测登录状态

### Usage:

#### 登录：

 ```./login-v2.sh login ```

#### 注销：

 ```./login-v2.sh logout ```


## matlab 脚本
- bmp2jpg.m    .bmp转.jpg
- rgb_2_gray.m    rgb2gray

## python 脚本
- json2txt.py labelme标注json转yolo-pose归一化数据集
- make_dataset.py 读取txt生成yolo-pose数据集
- rename.py AVT相机采图重命名
- video2pic.py 视频<->图片

## shell 脚本
- aar.sh 进程自启动脚本
