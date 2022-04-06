## 前言

平时喜欢用Typora记录一些笔记，有时会有将本地markdown文章搬到freebuf的需求，但是freebuf自带的markdown编辑器上传图片比较繁琐，而且一张一张上传也比较耗费时间，所以就打算写一个自动将本地的markdown文章图片转化为freebuf图片的工具。

这里参考了[此文](https://forum.butian.net/share/1172)，造了个轮子。

## 原理

实现原理也比较简单：

首先读取local_article文件夹下的markdown文件，并且使用正则去提取其中的本地图片路径存进列表中

然后发包，将图片上传到freebuf，并且提取返回包中的图片路径存在列表中

最后将原文件中的本地图片路径替换为上传至freebuf后的图片路径，并且生成新文件到freebuf_article文件夹中

## 使用

首先，打开typora，`文件`→`偏好设置`→`图像`，进行如下设置

![image-20220406003217373.png](https://image.3001.net/images/20220406/1649214703_624d04efb84895aa14785.png!small)

然后将我们要上传到freebuf的文章放到`local_article`目录下

![image-20220406003506792.png](https://image.3001.net/images/20220406/1649214704_624d04f0206b66812e381.png!small)

然后运行脚本：

```
python3 TyporaToFreebuf.py
```

![image-20220406104821082.png](https://image.3001.net/images/20220406/1649214704_624d04f06709fbaf1432e.png!small)

在`freebuf_article`文件夹下就会生成适用于freebuf的markdown文章：

![image-20220406104910917.png](https://image.3001.net/images/20220406/1649214704_624d04f0d602c0a1db4db.png!small)

复制文章内容，在freebuf的markdown编辑框粘贴即可。

![image-20220406104941569.png](https://image.3001.net/images/20220406/1649214705_624d04f1b75da3ee7c860.png!small)

![image-20220406105011997.png](https://image.3001.net/images/20220406/1649214706_624d04f20686b35438635.png!small)



**最后工具下载：**





