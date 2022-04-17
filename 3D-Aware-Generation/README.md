# <p align=center>`awesome 3D-aware Generation`</p>

[![Awesome](https://cdn.rawgit.com/sindresorhus/awesome/d7305f38d29fed78fa85652e3a63e154dd8e8829/media/badge.svg)](https://github.com/sindresorhus/awesome)
[![Maintenance](https://img.shields.io/badge/Maintained%3F-yes-green.svg)](https://GitHub.com/Naereen/StrapDown.js/graphs/commit-activity)
[![PR's Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=flat)](http://makeapullrequest.com) 

A collection of resources on 3D generation. This collection is organized as follows:

- [Introduction]()
- [Literature]()
  - [Neural Implicit Representation]()
  - [Voxel Representation]()
  - [Depth Representation]()
  - [Hybrid Representation]()
  - [3D Control]()



## Contributing

Feedback and contributions are welcome! If you think I have missed out on something (or) have any suggestions (papers, implementations and other resources), feel free to pull a request or leave an issue. I will release the [latex-pdf version]() in the future. 

markdown format:

``` markdown
[Paper Name](abs/pdf link)  
*[Author 1](homepage), Author 2, and Author 3*  
**[`Conference/Journal Year`] (`Institution`)** [[Code](link)] [[Project](link)]
```



## Introduction

[中文版介绍](知乎)

>2D GAN 的训练集是一系列2D图像（celeba），机理是从一个隐向量经过一个生成器映射到一幅图像，通常这些图像是单视角的。3D-aware的含义是指对于同一object的多视角图像，因此机理依旧是从一个隐向量经过一个生成器，再结合一个视角信号，得到在某一视角下的2D图像，然后通过修改视角信号，可以得到不同视角下的2D图像。(满足这一定义的都会归属到这一类)
>
>通过3D表征，得到图像背后的3D shape 或者 scene，然后通过 differentiable renderer 就可以映射回2D图像
>
>[如何表征3D] [如何映射回去]
>
>有两种，一种是不生成中间3D shape, 直接到多视角图像，某些feature直接控制了视角，
>
>另一种是生成中间3D shape, 这样的效果会更好一些，是先升维后再降维的。
>
>These methods can be categorized into two types. The first type utilize the generator to learn how to systheses images with different pose. Several methods explicitly add additional modules or regulariztions during training stage. Other methods investigate the latent space and disentangle the feature that control the pose attribute. The second type generate 3D-aware images and output the 3D shape model at the same time. This intermediate 3D shape provides high quality.

A very important research direction is to control over the generation process in order to be able to adjust some semantic attributes in the generated images. 

Among these attributes, 3D information such as pose, is what we care. Its applicability includes face recognition.

So how do we learn the 3D information from 2D. several attempts try to disentangle by leveraging external supervion such as pose labels, landmarks, and masks.



have shown ability to generate images with high visual quality under assigned poses. and we hope we preserve the identity when we change the pose parameters.



A feasible solution is to build generative models with 3D shapes. We need to rendered images and real images.



- feature manipulation based methods (latent space disentanglement and control)



> from 2D original image, we need to distill `view points, light direction, surface normal map.`



2D GANs lack knowledge of 3D structure. 3D aware generation brings much more xx into generative models. The core insight is to use a 3D representation approach.









generative 3D face model

- FLAME
- 

The problem of learning discriminative 3D models from 2D images

3D properties such as camera viewpoint or object pose

最终要的还是2D照片，但学到的是3D表征，最后用一个相机固定2D视角，因此可以生成多个角度的图像

implicit or explicit

learn model for **single** or **multiple** objects.





Given an unstructured 2D image collection, GANs are trained to synthesize geometrically-consistent multiview imagery of novel instances. 

Given uncontrolled 2D image collections, 3D-aware image generation methods aim to learn a generative model that can explicitly control the camera viewpoint of the generated content.





- Neural radiance field is overhead in rendering for both training and inference, a workaround to alleviate this cost is to only render images **patches**, but using a patch discriminator may lead to inferior synthesis quality. [GRAF]





> **Problem settings:**

Given a collection of real images, we learn a 3D-aware image generator $G$ which takes a random noise $z \in \mathbb{R}^d \sim p_z$ and a camera pose $\theta \in \mathbb{R}^3 \sim p_{\theta}$ as input, and outputs an image $I$ of a synthetic instance under pose $\theta$:

$$
G: (z, \theta) \in \mathbb{R}^{d+3} \rightarrow I \in \mathbb{R}^{H \times W \times 3}
$$

> **Training Strategy**

Using a non-saturating GAN loss with R1 regularization:
$$
\mathcal{L}(D, G)=\mathbb{E}_{\boldsymbol{z} \sim p_{z}, \boldsymbol{\theta} \sim p_{\theta}}[f(D(G(\boldsymbol{z}, \boldsymbol{\theta})))] +\mathbb{E}_{I \sim p_{\text {real }}}\left[f(-D(I))+\lambda\|\nabla D(I)\|^{2}\right]
$$
add a pose regularization term:
$$
\mathcal{L}_{\text {pose }}= \mathbb{E}_{\boldsymbol{z} \sim p_{z}, \boldsymbol{\theta} \sim p_{\theta}}\left\|D_{p}(G(\boldsymbol{z}, \boldsymbol{\theta}))-\boldsymbol{\theta}\right\|^{2} +\mathbb{E}_{I \sim p_{\text {real }}}\left\|D_{p}(I)-\hat{\boldsymbol{\theta}}\right\|^{2}
$$



## Literature

[without 3D shape]()

[with 3D shape](#with-3D-shape)





### with 3D shape





utilize 3D-aware features to represent a scene, and apply a neural renderer, typically a CNN, on top of them for realistic image synthesis.

### Voxel Representation

[HoloGAN: Unsupervised learning of 3D representations from natural images](https://arxiv.org/pdf/1904.01326.pdf)  
*Thu Nguyen-Phuoc, Chuan Li, Lucas Theis, Christian Richardt, Yong-Liang Yang*  
**[`ICCV 2019`] (`University of Bath`)**

[BlockGAN: Learning 3D Object-aware Scene Representations from Unlabelled Images](https://arxiv.org/pdf/2002.08988.pdf)  
*Thu Nguyen-Phuoc, Christian Richardt, Long Mai, Yong-Liang Yang, Niloy Mitra*  
**[`NeurIPS 2020`] (`University of Bath, Adobe`)**



### Depth

[RGBD-GAN: Unsupervised 3D Representation Learning From Natural Image Datasets via RGBD Image Synthesis](https://arxiv.org/pdf/1909.12573.pdf)  
*Atsuhiro Noguchi, Tatsuya Harada*  
**[`ICLR 2020`] (`U Tokyo, RIKEN`)**  

[3D-Aware Indoor Scene Synthesis with Depth Priors](https://arXiv.org/abs/2202.08553)  
*Zifan Shi, Yujun Shen, Jiapeng Zhu, Dit-Yan Yeung, Qifeng Chen*  
**[`arXiv 2022`] ()**  [Code](https://github.com/VivianSZF/depthgan) [Project Page](https://vivianszf.github.io/depthgan/)



### Neural Implicit Representation

[GRAF: Generative Radiance Fields for 3D-Aware Image Synthesis](https://arxiv.org/abs/2007.02442)  
*Katja Schwarz, Yiyi Liao, Michael Niemeyer, Andreas Geiger*  
**[`NeurIPS 2020`] (`MPI`)** [[Code](https://github.com/autonomousvision/graf)]

[NeRF-VAE: A Geometry Aware 3D Scene Generative Model](https://arxiv.org/pdf/2104.00587)  
*Adam R. Kosiorek, Heiko Strathmann, Daniel Zoran, Pol Moreno, Rosalia Schneider, Soňa Mokrá, Danilo J. Rezende*  
**[`ICML 2021`] (``)**

[GIRAFFE: Representing Scenes as Compositional Generative Neural Feature Fields](https://arxiv.org/pdf/2011.12100)  
*Michael Niemeyer, Andreas Geiger*  
**[`CVPR 2021`] (``)** [[Code](https://github.com/autonomousvision/giraffe)]

[pi-GAN: Periodic Implicit Generative Adversarial Networks for 3D-Aware Image Synthesis](https://arxiv.org/abs/2012.00926)  
*Eric R. Chan, Marco Monteiro, Petr Kellnhofer, Jiajun Wu, Gordon Wetzstein*  
**[`CVPR 2021`] (`Stanford`)**

[Lifting 2D StyleGAN for 3D-Aware Face Generation](https://arxiv.org/pdf/2011.13126.pdf)  
*Yichun Shi, Divyansh Aggarwal, Anil K. Jain*  
**[`CVPR 2021`] (`Michigan`)**

[Unconstrained Scene Generation with Locally Conditioned Radiance Fields](https://arxiv.org/pdf/2104.00670.pdf)  
*Terrance DeVries, Miguel Angel Bautista, Nitish Srivastava, Graham W. Taylor, Joshua M. Susskind*  
**[`ICCV 2021`] (`Apple`)**

[A Shading-Guided Generative Implicit Model for Shape-Accurate 3D-Aware Image Synthesis](https://arxiv.org/pdf/2110.15678)  
*Xingang Pan, Xudong Xu, Chen Change Loy, Christian Theobalt, Bo Dai*  
**[`NeurIPS 2021`] (``)** [[Code](https://github.com/xingangpan/shadegan)]

[Generative Occupancy Fields for 3D Surface-Aware Image Synthesis](https://arxiv.org/pdf/2111.00969)  
*Xudong Xu, Xingang Pan, Dahua Lin, Bo Dai*  
**[`NeurIPS2021 2021`] (``)** [[Code](https://github.com/SheldonTsui/GOF_NeurIPS2021)]

[CIPS-3D A 3D-Aware Generator of GANs Based on Conditionally-Independent Pixel Synthesis](https://arxiv.org/abs/2110.09788)  
*Peng Zhou, Lingxi Xie, Bingbing Ni, Qi Tian*  
**[`Arxiv 2021`] [`SJTU`]** [[Code](https://github.com/PeterouZh/CIPS-3D)]

[CAMPARI: Camera-Aware Decomposed Generative Neural Radiance Fields](https://arxiv.org/pdf/2103.17269)  
*Michael Niemeyer, Andreas Geiger*  
**[`arXiv 2021`] (``)** [[Code](https://github.com/autonomousvision/campari)]

[StyleNeRF: A Style-based 3D-Aware Generator for High-resolution Image Synthesis](https://arxiv.org/pdf/2110.08985)  
*Jiatao Gu, Lingjie Liu, Peng Wang, Christian Theobalt*  
**[`ICLR 2021`] (``)** [[Code](https://github.com/facebookresearch/StyleNeRF)]

[GRAM: Generative Radiance Manifolds for 3D-Aware Image Generation](https://arxiv.org/abs/2112.08867)  
*Yu Deng, Jiaolong Yang, Jianfeng Xiang, Xin Tong*  
**[`CVPR 2022`] (`Tsinghua, Microsoft`)**

[StyleSDF: High-Resolution 3D-Consistent Image and Geometry Generation](https://arxiv.org/pdf/2112.11427)  
*Roy Or-El, Xuan Luo, Mengyi Shan, Eli Shechtman, Jeong Joon Park, Ira Kemelmacher-Shlizerman*  
**[`CVPR 2022`] (``)** 

[Pix2NeRF: Unsupervised Conditional $π$-GAN for Single Image to Neural Radiance Fields Translation](https://arxiv.org/pdf/2202.13162)  
*Shengqu Cai, Anton Obukhov, Dengxin Dai, Luc Van Gool*  
**[`CVPR 2022`] (``)**

[GIRAFFE HD: A High-Resolution 3D-aware Generative Model](https://arxiv.org/pdf/2203.14954)  
*Yang Xue, Yuheng Li, Krishna Kumar Singh, Yong Jae Lee*  
**[`CVPR 2022`] (``)**

[Multi-View Consistent Generative Adversarial Networks for 3D-aware Image Synthesis](https://arxiv.org/pdf/2204.06307)  
*Xuanmeng Zhang, Zhedong Zheng, Daiheng Gao, Bang Zhang, Pan Pan, Yi Yang*  
**[`CVPR 2022`] (``)**

[VoLux-GAN: A Generative Model for 3D Face Synthesis with HDRI Relighting](https://arxiv.org/pdf/2201.04873)  
*Feitong Tan, Sean Fanello, Abhimitra Meka, Sergio Orts-Escolano, Danhang Tang, Rohit Pandey, Jonathan Taylor, Ping Tan, Yinda Zhang*  
**[`arXiv 2022`] (``)** 



### Hybrid

[3D-aware Image Synthesis via Learning Structural and Textural Representations](https://arxiv.org/pdf/2112.10759)  
*Yinghao Xu, Sida Peng, Ceyuan Yang, Yujun Shen, Bolei Zhou*  
**[`CVPR 2021`] (``)** [[Code](https://github.com/genforce/volumegan)]

[Efficient Geometry-aware 3D Generative Adversarial Networks](https://arxiv.org/pdf/2112.07945)  
*Eric R. Chan, Connor Z. Lin, Matthew A. Chan, Koki Nagano, Boxiao Pan, Shalini De Mello, Orazio Gallo, Leonidas Guibas, Jonathan Tremblay, Sameh Khamis, Tero Karras, Gordon Wetzstein*  
**[`CVPR 2021`] (``)** [[Code](https://github.com/NVlabs/eg3d)]







[3D-GIF: 3D-Controllable Object Generation via Implicit Factorized Representations](https://arxiv.org/pdf/2203.06457)  
*Minsoo Lee, Chaeyeon Chung, Hojun Cho, Minjung Kim, Sanghun Jung, Jaegul Choo, Minhyuk Sung*  
**[`arXiv2022`] (``)** 



- [GIF: Generative Interpretable Faces](https://arxiv.org/pdf/2009.00149.pdf)  
  *Partha Ghosh, Pravir Singh Gupta, Roy Uziel, Anurag Ranjan, Michael Black, Timo Bolkart*  
  **[`3DV 2020`] (`MPI`)** [[Code](https://github.com/ParthaEth/GIF)]

- 
  
- [Do 2D GANs Know 3D Shape? Unsupervised 3D shape reconstruction from 2D Image GANs](https://arxiv.org/pdf/2011.00844.pdf)  
  *Xingang Pan, Bo Dai, Ziwei Liu, Chen Change Loy, Ping Luo*  
  **[`ICLR 2021`] (`CUHK, NTU`)**  

- [Image GANs meet Differentiable Rendering for Inverse Graphics and Interpretable 3D Neural Rendering](https://arxiv.org/pdf/2010.09125.pdf)  
  *Yuxuan Zhang, Wenzheng Chen, Huan Ling, Jun Gao, Yinan Zhang, Antonio Torralba, Sanja Fidler*  
  **[`ICLR 2021`] (`NVIDIA, U Toronto`)**  
  
- 

[Unsupervised Learning of Probably Symmetric Deformable 3D Objects from Images in the Wild](https://arxiv.org/abs/1911.11130)  
**[`CVPR 2020 (Best paper)`]**  
*Shangzhe Wu, Christian Rupprecht, Andrea Vedaldi*











learn direct 3D representation of scenes and synthesize images under physical-based rendering process to achieve more strict 3D consistency.

use the volumetric rendering



- [Unsupervised Generative 3D Shape Learning from Natural Images](https://arxiv.org/pdf/1910.00287.pdf)  
  *Attila Szabó, Givi Meishvili, Paolo Favaro*  
  **[`arXiv 2019`] (`Bern`)**
- 
- 
- 
- 
- 
  
- 





Disentangled and controllable face image generationvia 3d imitative-contrastive learning

Config:Controllable neural face image generation



