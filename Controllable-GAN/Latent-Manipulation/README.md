# <p align=center>`GAN Latent Semantic Manipulation` </p>

[![Awesome](https://cdn.rawgit.com/sindresorhus/awesome/d7305f38d29fed78fa85652e3a63e154dd8e8829/media/badge.svg)](https://github.com/sindresorhus/awesome)
[![Maintenance](https://img.shields.io/badge/Maintained%3F-yes-green.svg)](https://GitHub.com/Naereen/StrapDown.js/graphs/commit-activity)
[![PR's Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=flat)](http://makeapullrequest.com) 

A collection of resources on GAN Latent Manipulation.

## Contributing

Feedback and contributions are welcome! If you think I have missed out on something (or) have any suggestions (papers, implementations and other resources), feel free to pull a request or leave an issue. I have also released the [latex-citation version](). 

markdown format:

``` markdown
[Paper Name](abs/pdf link)  
*[Author 1](homepage), Author 2, and Author 3.*  
**[`Conference/Journal Year`] (`Institution`)** [[Github](link)] [[Project](link)]
```

## Introduction

GANs can produce high-fidelity images visually indistinguishable from real ones.

Pre-trained GAN models spontaneously learn rich knowlegde in latent spaces such that moving latent codes towards some certain directions can cause corresponding attribute change in images. 

So we can control the generation process by identifying semantically meaningful latent subspaces.

this would help us understand the internal representation learned by GANs and futher control the generation process.

<Low-Rank GAN>



The question is how do we establish the relationship between the latent code and the image?



> We can first generate a collection of image synthesis, then label these images regarding a target attributesm, and finally find the latent separation boundary through supervised training.

[Ganalyze: Toward visual definitions of cognitive image properties](https://arxiv.org/pdf/1906.10112.pdf)  
*Lore Goetschalckx, Alex Andonian, Aude Oliva, Phillip Isola*  
**[`CVPR 2019`] (`MIT, KU Leuven`)**

[Interpreting the latent space of gans for semantic face editing](https://arxiv.org/pdf/1907.10786.pdf)  
*Yujun Shen, Jinjin Gu, Xiaoou Tang, Bolei Zhou*  
**[`CVPR 2020`] (`CUHK`)**



Interfacegan: Interpreting the disentangled face representation learned by GANs

> simple image transformations 

On the" steerability" of generative adversarial networks

Controlling generative models with continuous factors of variations





- using unsupervised manner such as PCA to find steerable direction

  Unsupervised discovery of interpretable directions in the GAN latent space

  Closed-form factorization of latent semantics in GANs

  Ganspace: Discovering interpretable GAN controls

  GAN steerability without optimization







Global semantics 不够，想要 particular image region, 最简单的也是依靠mask

Spatially controllable image synthesis with internal representation collaging

Editing in style: Uncovering the local semantics of GANs

Semantic photo manipulation with a generative image prior

Generative hierarchical features from synthesizing images

Decorating your own bedroom: Locally controlling image generation with generative adversarial networks



Semantic hierarchy emerges in deep generative representations for scene synthesis

In-domain GAN inversion for real image editing



Human-in-the-loop differential subspace search in high-dimensional latent space

A spectral regularizer for unsupervised disentanglement

The geometry of deep generative image models and its applications



**Definition:** Control a single attribute of interest, e.g. pose in our goal, without affecting other ones.

These change are most semantic

**main lines:**

- control the latent space of GAN

**Strength:** help to understand the generation process of GAN

**challenge:** reducing supervision. Supervised solutions are most effective [Aberman et al. 2019], but often impose infeasible data collection requirement

**Key words:** latent disentangle, traverse in the latent space, manifold



> **Disentanglement** can be defined as the ability to control a single factor, or feature, without affecting other ones. A properly disentangled representation can benefit semantic data mixing, transfer learning for downstream tasks, or even interpretability.  --《Face Identity Disentanglement via Latent Space Mapping》

> **GAN Inversion**: Interpreting the Latent Space of Pretrained Models



## Literature

> You can also ref the repo of [Papers on generative modeling](https://github.com/zhoubolei/awesome-generative-modeling).

Two Summaries:

- [GAN Inversion: A Survey](https://arxiv.org/pdf/2101.05278.pdf)  
*Weihao Xia, Yulun Zhang, Yujiu Yang, Jing-Hao Xue, Bolei Zhou, Ming-Hsuan Yang*

- [Challenging Common Assumptions in the Unsupervised Learning of Disentangled Representations](https://arxiv.org/pdf/1811.12359.pdf)
*Francesco Locatello, Stefan Bauer, Mario Lucic, Gunnar Rätsch, Sylvain Gelly, Bernhard Schölkopf, Olivier Bachem*

---

[Closed-Form Factorization of Latent Semantics in GANs](https://arxiv.org/pdf/2007.06600.pdf)  
**[`CVPR 2021`] (`CUHK`)**  
*Yujun Shen, Bolei Zhou*

[Generative Hierarchical Features from Synthesizing Images](https://arxiv.org/pdf/2007.10379.pdf)  
**[`CVPR 2021`] (`CUHK`)**  
*Yinghao Xu, Yujun Shen, Jiapeng Zhu, Ceyuan Yang, Bolei Zhou*

[Enjoy Your Editing: Controllable GANs for Image Editing via Latent Space Navigation](https://arxiv.org/pdf/2102.01187.pdf)  
**[`ICLR 2021`] (`UIUC`)**  
*Peiye Zhuang, Oluwasanmi Koyejo, Alexander G. Schwing*

[GANSpace: Discovering Interpretable GAN Controls](https://arxiv.org/pdf/2004.02546.pdf)  
**[`NeurIPS 2020`] (`Aalto, Adobe, NVIDIA`)**  
*Erik Härkönen, Aaron Hertzmann, Jaakko Lehtinen, Sylvain Paris*

[Interpreting the Latent Space of GANs for Semantic Face Editing](https://arxiv.org/pdf/1907.10786.pdf)  
**[`CVPR 2020`] (`CUHK`)** [[:octocat:](https://github.com/genforce/interfacegan)]  
*Yujun Shen, Jinjin Gu, Xiaoou Tang, Bolei Zhou*

[MaskGAN: Towards Diverse and Interactive Facial Image Manipulation](https://arxiv.org/pdf/1907.11922.pdf)  
**[`CVPR 2020`] (`SenseTime, CUHK`)**  
*Cheng-Han Lee, Ziwei Liu, Lingyun Wu, Ping Luo*

[Disentangled and Controllable Face Image Generation via 3D Imitative-Contrastive Learning](https://arxiv.org/pdf/2004.11660.pdf)  
**[`CVPR 2020`] (`Tsinghua`)**  
*Yu Deng, Jiaolong Yang, Dong Chen, Fang Wen, Xin Tong*

[Face Identity Disentanglement via Latent Space Mapping](https://arxiv.org/pdf/2005.07728.pdf)  
**[`TOG 2020`] (`Tel-Aviv University, Alibaba`)** [[:octocat:](https://github.com/YotamNitzan/ID-disentanglement)]  
*Yotam Nitzan, Amit Bermano, Yangyan Li, Daniel Cohen-Or*

[Optimizing the Latent Space of Generative Networks](https://arxiv.org/pdf/1707.05776.pdf)  
**[`ICML 2018`] (`Facebook`)**  
*Piotr Bojanowski, Armand Joulin, David Lopez-Paz, Arthur Szlam*



Interfacegan: Interpreting the disentangled face representation learned by gans

Interpreting the latent space of gans for semantic face editing

Editing in style: Uncovering the local semantics of gans

Image2stylegan: How to embed images into the stylegan latent space?

Stylespace analysis: Disentangled controls for stylegan image generation



> augmenting and regularizing the latent space

A free viewpoint portrait generator with dynamic styling

Disentangled image generation through structured noise injection

Gan-control: Explicitly controllable gans

## Main Research Group

- CUHK Zhou bolei



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



unsort



[Deforming autoencoders: Unsupervised disentangling of shape and appearance](https://arxiv.org/pdf/1806.06503.pdf)  
**[ECCV 2018] (Stony Brook University)**   
*Zhixin Shu, Mihir Sahasrabudhe, Alp Guler, Dimitris Samaras, Nikos Paragios, Iasonas Kokkinos*