# <p align=center>`awesome Generative Model for 3D-aware Generation`</p>

[![Awesome](https://cdn.rawgit.com/sindresorhus/awesome/d7305f38d29fed78fa85652e3a63e154dd8e8829/media/badge.svg)](https://github.com/sindresorhus/awesome)
[![Maintenance](https://img.shields.io/badge/Maintained%3F-yes-green.svg)](https://GitHub.com/Naereen/StrapDown.js/graphs/commit-activity)
[![PR's Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=flat)](http://makeapullrequest.com) 

A collection of resources on 3D generation (mainly on face).



## Contributing

Feedback and contributions are welcome! If you think I have missed out on something (or) have any suggestions (papers, implementations and other resources), feel free to pull a request or leave an issue. I have also released the [latex-pdf version](). 

markdown format:

``` markdown
[Paper Name](abs/pdf link)  
**[`Conference/Journal Year`] (`Institution`)** [[Github](link)] [[Project](link)]
*[Author 1](homepage), Author 2, and Author 3.*  
<details><summary>Click to expand</summary><p>
A summary here
</p></details>
```



## Introduction

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

utilize 3D-aware features to represent a scene, and apply a neural renderer, typically a CNN, on top of them for realistic image synthesis.



[HoloGAN: Unsupervised learning of 3D representations from natural images](https://arxiv.org/pdf/1904.01326.pdf)  
*Thu Nguyen-Phuoc, Chuan Li, Lucas Theis, Christian Richardt, Yong-Liang Yang*  
**[`ICCV 2019`] (`University of Bath`)**

[BlockGAN: Learning 3D Object-aware Scene Representations from Unlabelled Images](https://arxiv.org/pdf/2002.08988.pdf)  
*Thu Nguyen-Phuoc, Christian Richardt, Long Mai, Yong-Liang Yang, Niloy Mitra*  
**[`NeurIPS 2020`] (`University of Bath, Adobe`)**



- [GIF: Generative Interpretable Faces](https://arxiv.org/pdf/2009.00149.pdf)  
  *Partha Ghosh, Pravir Singh Gupta, Roy Uziel, Anurag Ranjan, Michael Black, Timo Bolkart*  
  **[`3DV 2020`] (`MPI`)** [[Code](https://github.com/ParthaEth/GIF)]

- [RGBD-GAN: Unsupervised 3D Representation Learning From Natural Image Datasets via RGBD Image Synthesis](https://arxiv.org/pdf/1909.12573.pdf)  
  *Atsuhiro Noguchi, Tatsuya Harada*  
  **[`ICLR 2020`] (`U Tokyo, RIKEN`)**  
  
- [Do 2D GANs Know 3D Shape? Unsupervised 3D shape reconstruction from 2D Image GANs](https://arxiv.org/pdf/2011.00844.pdf)  
  *Xingang Pan, Bo Dai, Ziwei Liu, Chen Change Loy, Ping Luo*  
  **[`ICLR 2021`] (`CUHK, NTU`)**  

- [Image GANs meet Differentiable Rendering for Inverse Graphics and Interpretable 3D Neural Rendering](https://arxiv.org/pdf/2010.09125.pdf)  
  *Yuxuan Zhang, Wenzheng Chen, Huan Ling, Jun Gao, Yinan Zhang, Antonio Torralba, Sanja Fidler*  
  **[`ICLR 2021`] (`NVIDIA, U Toronto`)**  

[Unsupervised Learning of Probably Symmetric Deformable 3D Objects from Images in the Wild](https://arxiv.org/abs/1911.11130)  
**[`CVPR 2020 (Best paper)`]**  
*Shangzhe Wu, Christian Rupprecht, Andrea Vedaldi*







Deep 3D Portrait from a Single Image



learn direct 3D representation of scenes and synthesize images under physical-based rendering process to achieve more strict 3D consistency.

use the volumetric rendering



- [Unsupervised Generative 3D Shape Learning from Natural Images](https://arxiv.org/pdf/1910.00287.pdf)  
  *Attila Szabó, Givi Meishvili, Paolo Favaro*  
  **[`arXiv 2019`] (`Bern`)**
- [GRAF: Generative Radiance Fields for 3D-Aware Image Synthesis](https://arxiv.org/pdf/2007.02442.pdf)  
  *Katja Schwarz, Yiyi Liao, Michael Niemeyer, Andreas Geiger*  
  **[`NeurIPS 2020`] (`MPI`)** [[Code](https://github.com/autonomousvision/graf)]
- [Lifting 2D StyleGAN for 3D-Aware Face Generation](https://arxiv.org/pdf/2011.13126.pdf)  
  *Yichun Shi, Divyansh Aggarwal, Anil K. Jain*  
  **[`CVPR 2021`] (`Michigan`)**
- [pi-GAN: Periodic Implicit Generative Adversarial Networks for 3D-Aware Image Synthesis](https://arxiv.org/pdf/2012.00926.pdf)  
  *Eric R. Chan, Marco Monteiro, Petr Kellnhofer, Jiajun Wu, Gordon Wetzstein*  
  **[`CVPR 2021`] (`Stanford`)**
- [Unconstrained Scene Generation with Locally Conditioned Radiance Fields](https://arxiv.org/pdf/2104.00670.pdf)  
  *Terrance DeVries, Miguel Angel Bautista, Nitish Srivastava, Graham W. Taylor, Joshua M. Susskind*  
  **[`ICCV 2021`] (`Apple`)**
- [CIPS-3D A 3D-Aware Generator of GANs Based on Conditionally-Independent Pixel Synthesis](https://arxiv.org/pdf/2110.09788.pdf)  
  *Peng Zhou, Lingxi Xie, Bingbing Ni, Qi Tian*  
  **[`Arxiv 2021`] [`SJTU`]**

- [GRAM: Generative Radiance Manifolds for 3D-Aware Image Generation](https://arxiv.org/pdf/2112.08867.pdf)  
  *Yu Deng, Jiaolong Yang, Jianfeng Xiang, Xin Tong*  
  **[`arXiv 2021`] (`Tsinghua, Microsoft`)**






#### 



