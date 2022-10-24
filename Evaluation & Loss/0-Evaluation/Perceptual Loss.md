# Perceptual Loss

https://github.com/ForrestPi/Tricks/tree/master/loss





大体意思是用已经训练好的网络的某些layer提取图像特征，然后loss比较。一般会使用的是VGG19，InceptionV3

给定两张图，我们不直接比较他们的像素级差异，而是均将他们放入同一网络中，获取某一中间层的输出特征图，然后再用一些传统的loss计算特征图之间的差异即可



## 基本原理





相关文献：

最早出现在什么文章

Perceptual losses for real-time style transfer and super-resolution 2016

详细介绍一下这篇文章，

本文用到的是VGG16，当然也可以使用其他的网络模型 ResNet, GoogLeNet，VGG19；但秉持的原则是能用就好



![img](https://pica.zhimg.com/80/v2-14c2f167f71b5872f17afe6d23aa3cb7_1440w.jpg?source=1940ef5c)

出自：PIRM Challenge on Perceptual Image Super-resolution



后面在什么文章中被用到


$$
L_{j}=\frac{\left\|V_{j}(\hat{Y})-V_{j}(Y)\right\|^{2}_{2}}{C_{j} * H_{j} * W_{j}}
$$
其中 V 是特征，分母是形状大小



优点：

- 稳定训练
- 图像质量



缺点：

- Computational overhead
- Texture and color bias
- Constrained diversity



基本用法：



## 代码

[LPIPS](https://github.com/richzhang/PerceptualSimilarity) 库，用于评价两幅图像之间的相似度，使用方法

```python
!pip install lpips

import lpips
loss_fn_alex = lpips.LPIPS(net='alex')
d = loss_fn_alex(img0, img1)
```











![image-20210831160229388](C:\Users\zhiyuyang4\AppData\Roaming\Typora\typora-user-images\image-20210831160229388.png)

![img](https://github.com/boschresearch/OASIS/raw/master/iclr2021_oasis_poster.png)



[Perceptual Losses for Real-Time Style Transfer and Super-Resolution](https://arxiv.org/pdf/1603.08155.pdf)  
*Justin Johnson, Alexandre Alahi, Li Fei-Fei*  
**[`ECCV 2016`] ()**

[Generating Images with Perceptual Similarity Metrics based on Deep Networks](https://arxiv.org/pdf/1602.02644.pdf)  
*Alexey Dosovitskiy, Thomas Brox*  
**[`NeurIPS 2016`] ()**





measure the low-level (pixel space) & high-level (feature space) similarity between two images 

different layers of the VGG neural network extract the image features at different scales and can be separated into content and style.



