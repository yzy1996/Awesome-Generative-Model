# <p align=center>`awesome Generative Adversarial Networks (GANs)`</p>

A collection of resources on Generative Adversarial Networks (GANs).



## Table of Contents

- [Introduction](#Introduction)

- [1. Basic](#Basic-Knowledge)

  - [For-Beginner](0-For-Beginner)
  - [GANs Structure Variances](1-GANs-Structure-Variances)
  - [Conditional GAN](1-Conditional-GAN)
  - Pitfalls: mode collapse and vanishing gradient
  - [Evaluation Metrics](1-Evaluation-Metrics)
  - [GANs comparation](1-GANs-comparation)

- [2. Research Branch](#Research-Branch)

  - [Semantic image synthesis](2-Semantic-image-synthesis)

    the goal is to generate multi-modal photorealistic images in alignment with a given semantic label map
    
  - Super-resolution, colorisation, text-guided generation

  - [Few-shot & Limited Data](2-Few-shot-&-Limited-Data)

  - [Pre-trained GAN](2-Pre-trained-GANs)



## Introduction

The purpose of GAN is to generate/synthesize fake but photo-real images (synthesize high-resolution portraits that are often indistinguishable from real faces). GANs are popular partly because they tackle the important unsolved challenge of unsupervised learning.

If intelligence was a cake, unsupervised learning would be the cake, supervised learning would be the icing on the cake, and reinforcement learning would be the cherry on the cake. We know how to make the icing and the cherry, but we don’t know how to make the cake. – Yann LeCun, 2016.

To quickly touch GAN, [Stylegan: Demo](https://thispersondoesnotexist.com/)



![GAN Development](https://raw.githubusercontent.com/yzy1996/Image-Hosting/master/GAN%20Development.png)



Some review to help you know this field

[Generative Adversarial Networks in Computer Vision: A Survey and Taxonomy]()

[A Review on Generative Adversarial Networks: Algorithms, Theory, and Applications]() 

[Generative Adversarial Networks for Image and Video Synthesis: Algorithms and Applications]()

[Generative adversarial network in medical imaging: A review]()



### SOTA

**`[BigGAN]`** [Large scale GAN training for high fidelity natural image synthesis](https://arxiv.org/abs/1809.11096) **`[ICLR 2019]`**

**`[StyleGAN]`** [A style-based generator architecture for generative adversarial networks](https://arxiv.org/abs/1812.04948) **`[CVPR 2019]`**

**`[StyleGAN2]`** [Analyzing and Improving the Image Quality of StyleGAN](https://arxiv.org/abs/1912.04958) **`[CVPR2020]`**

> able to generate good-looking high-resolution images (even can not be distinguished from real ones)

https://paperswithcode.com/task/image-generation

https://paperswithcode.com/sota/image-generation-on-lsun-bedroom-256-x-256



## Basic Knowledge

mode collapse: diversity the generator can only learn some limited patterns from the large-scale target datasets, or assigns all of its probability mass to a small region in the space.

vanishing gradient: 

details of the derivation or the difficult of GAN’s training

**Evaluation metrics of GAN**

> paper: https://arxiv.org/pdf/1806.07755.pdf
>
> code: https://github.com/xuqiantong/GAN-Metrics
>
> blog: https://zhuanlan.zhihu.com/p/99375611



- [Training Strategy](./Training Strategy )



**Conditional GAN (CGAN)**

开山之作为2014发表在CVPR上的 **Conditional Generative Adversarial Nets**

之后在他的基础上有了

2017 Image-to-image translation with conditional adversarial networks

2017 Conditional image synthesis with auxiliary classifier gans



### Dataset

CelebA

FFHQ

CelebV-HQ: A Large-Scale Video Facial Attributes Dataset



## Research Branch

- Few-shot & Limited data

- Semantic synthesis

- Other domain synthesis

- Pre-trained GAN

- In&Out painting 

- Text2image

- High&Super Reselution

- Animation

- image editing

  https://gandissect.csail.mit.edu/

- video generation

- image-to-image translation 风格迁移

- 用GAN帮助分类

  [Unsupervised and Semi-supervised Learning with Categorical Generative Adversarial Networks](https://arxiv.org/abs/1511.06390)  
  *Jost Tobias Springenberg*  
  **[`arXiv 2015`] (``)**

[Semi-supervised learning based on generative adversarial network: a comparison between good GAN and bad GAN approach](https://arxiv.org/abs/1905.06484)  
*Wenyuan Li, Zichen Wang, Jiayun Li, Jennifer Polson, William Speier, Corey Arnold*  
**[`CVPR 2019`] (``)** 

[Good Semi-supervised Learning that Requires a Bad GAN](https://arxiv.org/abs/1705.09783)  
*Zihang Dai, Zhilin Yang, Fan Yang, William W. Cohen, Ruslan Salakhutdinov*  
**[`NIPS 2017`] (``)** 



**Inverion**

> full list please see [GAN Inversion]()
>
> We can find a common latent code, and we can also find a seperate code for each layer of the generator.

It is easy and better to manipulate a given image in the latent feature space.

- [Image2StyleGAN: How to Embed Images Into the StyleGAN Latent Space?](https://arxiv.org/pdf/1904.03189.pdf)  
  *Rameen Abdal, Yipeng Qin, Peter Wonka*  
  **[`ICCV 2019`]**



- **model interpretability**

  - the structure of latent spaces

    semantic meaningful directions

    1.existence: exist such directions

    2.domain agnostic transformations (zooming or translation) & domain-specific transformations (adding smile or glasses)

  - disentangled latent spaces

- Disentanglement learning



- Interpretable directions in the latent space

  [InfoGAN]()  enforces the generated images to preserve information about the latent code coordinates by maximizing the corresponding mutual information.

  [$\beta$-VAE]()  put more emphasis on the $KL$-term in the standard VAE's ELBO objective.

  [2019-Oogan](Disentangling gan with one-hot sampling and orthogonal regularization)  forces the code vector $c$ to be one-hot, simplifying the task for a GAN discriminators' head to predict the code.

  [2020-VAE-GAN](High-fidelity synthesis with disentangled representation)  combine VAE and GAN to achieve a disentanglement images representation by the VAE and then pass the discovered code to the GAN model.



## Some Awesome Codes

[studioGAN](https://github.com/POSTECH-CVLab/PyTorch-StudioGAN)
