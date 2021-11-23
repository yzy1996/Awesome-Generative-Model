# <p align=center>`GAN Inversion`</p>

A collection of resources on GAN Inversion. 

Related material: [awesome-gan-inversion](https://github.com/weihaox/awesome-gan-inversion)



## Introduction

GAN inversion aims to invert a given image back into the latent space of a pretrained GAN model. This given image is always real. This post-processing remains a challenge because standard GAN model is initially designed for synthesizing images from random noises.



This is come from the real-world application with well-trained GANs





前提假设是：When z1; z2 2 Z are close in the Z space, the corresponding images x1; x2 2 X are visually similar.

given a real image x, find a  latent representation z*, which could generate an image x’ and is close to x





inverse problem:

deblurring, image inpainting, phase retrieval,



**为什么要做 GAN inversion**

给一张真实的原图，找到对应生成模型的 z*，保证生成的假图能和真实原图一致。在实现了这样的前提下，就可以对这张图做更多的操作，这是过去inversion的意义。

resemble real data， be applicable to real image editing without requiring ad-hoc supervision or expensive optimization.

**是怎么找 z* 的**



There are two main approaches to embed instances from the image space to the latent space

- learning based: learn an encoder (AE) 
  
  > train an extra encoder to learn the mapping from the image space to the latent space
  
  $$
  \theta_{E}^{*}=\underset{\theta_{E}}{\arg \min } \sum_{n} \mathcal{L}\left(G\left(E\left(x_{n} ; \theta_{E}\right)\right), x_{n}\right)
  $$
  
- optimization based: select a random initial latent code and optimize it using gradient descent

  > optimize the latent code by minimizing the reconstruction error through back-propagation.

$$
\mathbf{z}^{*}=\underset{\mathbf{z} \in \mathcal{Z}}{\arg \min} \ \mathcal{L}(G(\mathbf{z}), x)
$$

where $\mathcal{L}(\cdot, \cdot)$ denotes the objective function.



One is learning-based, which first synthesizes a collection of images with randomly sampled latent codes and then uses the images and codes as inputs and supervisions respectively to train a deterministic model

directly optimizing the latent code to minimize the pixel-wise reconstruction loss



To simplify the optimization, prior efforts also use a encoder to generate an initialization for optimization.

Train stage also 



还可以怎么来做呢？

GAN在这个问题里面，



multiple latent code

我们希望让 latent space 表征地足够充分 over-parameterization，同时可以了解到逐层表征的每一层都代表了什么含义。



### Basic Inspiration

> 基于一些研究发现能做得更好



- inverting a generative model from the image space to some intermediate feature space is much easier than to the 



### Applications

There are many real-world applications, such as: 

- images colorization
- super-resolution
- image inpainting
- semantic manipulation



## Literature

**GAN Inversion A Survey**



原理上的 2013 Signal recovery from pooling representations

All of these inverting efforts are instances of the pre-image problem, [The pre-image problem in kernel methods]()



Compressed Sensing using Generative Models



2017 Precise Recovery of Latent Vectors from Generative Adversarial Networks

2016 ECCV Generative visual manipulation on the natural image manifold.



[Inverting the generator of a generative adversarial network](https://arxiv.org/pdf/1611.05644.pdf)  
**[`NeurIPSW 2016`] (`Imperial College London`)**  
*Antonia Creswell, Anil Anthony Bharath*

[Generative visual manipulation on the natural image manifold](https://arxiv.org/pdf/1609.03552.pdf)  
**[`ECCV 2016`]**  
*Jun-Yan Zhu, Philipp Krähenbühl, Eli Shechtman, Alexei A. Efros*

[Inverting The Generator of A Generative Adversarial Network](https://arxiv.org/pdf/1611.05644.pdf)  
*Antonia Creswell, Anil Anthony Bharath*  
**[`NIPS 2016`] (`ICL`)** 

[How to Embed Images Into the StyleGAN Latent Space?](https://arxiv.org/pdf/1904.03189.pdf)  
*Rameen Abdal, Yipeng Qin, Peter Wonka*  
**[`ICCV 2019`] (`KAUST`)**	[[Code](https://github.com/NVlabs/stylegan)]



[Image Processing Using Multi-Code GAN Prior](https://arxiv.org/pdf/1912.07116.pdf)  
*Jinjin Gu, Yujun Shen, Bolei Zhou*  
**[CVPR 2020] (CUHK)**






<span id="Pixel2Style2Pixel"></span>
[Encoding in Style: a StyleGAN Encoder for Image-to-Image Translation](https://arxiv.org/pdf/2008.00951.pdf)  
**[`CVPR 2021`]**  
*Elad Richardson, Yuval Alaluf, Or Patashnik, Yotam Nitzan, Yaniv Azar, Stav Shapiro, Daniel Cohen-Or*



### learning-based (encoder)

[Invertible Conditional GANs for image editing](https://arxiv.org/pdf/1611.06355.pdf)  
*Guim Perarnau, Joost van de Weijer, Bogdan Raducanu, Jose M. Álvarez*  
**[`NeurIPS W 2016`]**

[Generative Visual Manipulation on the Natural Image Manifold](https://arxiv.org/pdf/1609.03552.pdf)  
*Jun-Yan Zhu, Philipp Krähenbühl, Eli Shechtman, Alexei A. Efros*  
**[`ECCV 2016`]**

Seeing what a gan cannot generate  
[ICCV 2019]

Inverting layers of a large generator  
[ICLR 2019]

### optimization-based

[Precise recovery of latent vectors from generative adversarial networks](https://arxiv.org/pdf/1702.04782.pdf)  
*Zachary C. Lipton, Subarna Tripathi*  
**[`ICLR W 2017`]**

[Inverting The Generator Of A Generative Adversarial Network](https://arxiv.org/pdf/1802.05701.pdf)  
*Antonia Creswell, Anil A Bharath*  
**[`TNNLS 2018`]**

[Invertibility of Convolutional Generative Networks from Partial Measurements](https://proceedings.neurips.cc/paper/2018/file/e0ae4561193dbf6e4cf7e8f4006948e3-Paper.pdf)  
*Fangchang Ma, Ulas Ayaz, Sertac Karaman*  
**[`NeurIPS 2018`]**

[Image2StyleGAN: How to Embed Images Into the StyleGAN Latent Space?](https://arxiv.org/pdf/1904.03189.pdf)  
*Rameen Abdal, Yipeng Qin, Peter Wonka*  
**[`ICCV 2019`]**

Precise recovery of latent vectors from generative adversarial networks  



### initialization

Semantic photo manipulation with a generative image prior  
[SIGGRAPH 2019]

[Seeing What a GAN Cannot Generate](https://arxiv.org/pdf/1910.11626.pdf)  
*David Bau, Jun-Yan Zhu, Jonas Wulff, William Peebles, Hendrik Strobelt, Bolei Zhou, Antonio Torralba*
**[`ICCV 2019`]**

[Inverting Layers of a Large Generator](https://debug-ml-iclr2019.github.io/cameraready/DebugML-19_paper_18.pdf)  
*David Bau, Jun-Yan Zhu, Jonas Wulff, William Peebles, Hendrik Strobelt, Bolei Zhou, Antonio Torralba* 
**[`ICLR W 2019`]**



### Training stage

[Adversarially Learned Inference](https://arxiv.org/pdf/1606.00704.pdf)  
*Vincent Dumoulin, Ishmael Belghazi, Ben Poole, Olivier Mastropietro, Alex Lamb, Martin Arjovsky, Aaron Courville*  
**[`ICLR 2017`] (`MILA`)**

[Adversarial Feature Learning](https://arxiv.org/pdf/1605.09782.pdf)  
*Jeff Donahue, Philipp Krähenbühl, Trevor Darrell*  
**[`ICLR 2017`]**

Latently invertible autoencoder with adversarial learning

[Glow: Generative Flow with Invertible 1x1 Convolutions](https://arxiv.org/pdf/1807.03039.pdf)  
*Diederik P. Kingma, Prafulla Dhariwal*  
**[`NurIPS 2018`]**





### others

multi latent code for one image

[Image Processing Using Multi-Code GAN Prior](https://arxiv.org/pdf/1912.07116.pdf)  
*Jinjin Gu, Yujun Shen, Bolei Zhou*  
**[`CVPR 2020`]**



> optimize the generator with latent code

[Exploiting Deep Generative Prior for Versatile Image Restoration and Manipulation](https://arxiv.org/pdf/2003.13659.pdf)  
*Xingang Pan, Xiaohang Zhan, Bo Dai, Dahua Lin, Chen Change Loy, Ping Luo*  
**[`ECCV 2020`]**



focus on stylegan

[Analyzing and Improving the Image Quality of StyleGAN](https://arxiv.org/pdf/1912.04958.pdf)  
*Tero Karras, Samuli Laine, Miika Aittala, Janne Hellsten, Jaakko Lehtinen, Timo Aila*  
**[`CVPR 2020`]**

[Image2StyleGAN++: How to Edit the Embedded Images?](https://arxiv.org/pdf/1911.11544.pdf)  
*Rameen Abdal, Yipeng Qin, Peter Wonka*  
**[`CVPR 2020`]**









### 思考

仅仅用像素层面的loss不足以，还应该考虑语义的层面



或者优化方式，如果仅仅由生成器来提供梯度优化，很可能产生 out-of-domain 的逆向，因为没有对 z 的任何约束；也更可能是很多的解



用一个 encoder 来提取所有 3D 信息

如何用一个 encoder 来提取呢



如果初始点选的不好，很有可能就卡在域外的局部点了



一个目标就是一个视角的



训练出一个带视角的解耦器，然后用来做 

看清楚 singleview 做的工作



one view real image -> share latent code + view latent code -> decoder - > 3D nerf



只在生成固定视角的时候需要 view code，如果只是为了生成3D nerf，是不需要的，用那一部分的共有code来做就行了。



区别在什么地方呢？



让一个模型，同时能在所有角度上

