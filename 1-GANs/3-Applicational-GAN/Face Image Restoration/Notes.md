# <p align=center>`Face Image Restoration`</p>

> The order is from the latest to the old

[GPEN](#GPEN)

---

<span id="GPEN"></span>
[GAN Prior Embedded Network for Blind Face Restoration in the Wild](https://arxiv.org/pdf/2105.06070.pdf)  
**[CVPR 2021]  (`DAMO, Alibaba, PolyU`)** [[Code](https://github.com/yangxy/GPEN)]  
*Tao Yang, Peiran Ren, Xuansong Xie, Lei Zhang *

<details><summary>Click to expand</summary><p>

<div align=center><img width="800" src="https://raw.githubusercontent.com/yzy1996/Image-Hosting/master/20210715113446.png"/></div>

> **Summary**

They solve the problem of **blind face restoration (BFR)**. They first use a CNN encoder to map the input degraded image to a desired latent code and then use a GAN to reproduce the desired HQ face image. 

> **Details**

They first pre-train a GAN using HQ face images following the training strategies of StyleGAN.

Using a set of synthesized LQ-HQ face images pairs to fine-tune the whole network.

Different from other methods with unchanged pre-trained GANs, they will fine-tune the GAN.



我们来讲解一下上图的(c)主框架，绿色梯形是一系列DNN，他们分别提取了 global face structure, local face structure and the background of face image. 也就是认为特征逐层加深。DNN的两路输出构成了StyleGAN输入所需的 z 和 noise。

但是这个训练过程吧，需要的数据还是很苛刻的，需要有清晰和模糊这样一对数据集。

They design a loss function that is similar to perceptual loss but it is based on the discriminator rather than the pre-trained VGG network. They use the total number of intermediate layers for feature extraction.



另外这项技术已经上线阿里云


</p></details>

---

