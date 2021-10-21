# <p align=center>`awesome Generative Model for Face Steerability` </p>

[![Awesome](https://cdn.rawgit.com/sindresorhus/awesome/d7305f38d29fed78fa85652e3a63e154dd8e8829/media/badge.svg)](https://github.com/sindresorhus/awesome)
[![Maintenance](https://img.shields.io/badge/Maintained%3F-yes-green.svg)](https://GitHub.com/Naereen/StrapDown.js/graphs/commit-activity)
[![PR's Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=flat)](http://makeapullrequest.com) 

A collection of resources on Application of Generative Model in Face Steerability.

edit face (facial features)

## Contributing

Feedback and contributions are welcome! If you think I have missed out on something (or) have any suggestions (papers, implementations and other resources), feel free to pull a request or leave an issue. I have also released the [latex-citation version](). 

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

## Main Research Group

- CUHK Zhou bolei







unsort



[Deforming autoencoders: Unsupervised disentangling of shape and appearance](https://arxiv.org/pdf/1806.06503.pdf)  
**[ECCV 2018] (Stony Brook University)**   
*Zhixin Shu, Mihir Sahasrabudhe, Alp Guler, Dimitris Samaras, Nikos Paragios, Iasonas Kokkinos*