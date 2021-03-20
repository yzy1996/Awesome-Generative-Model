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
**[`Conference/Journal Year`]**	 **(`Institution`)**	[[Github](link)]	[[Project](link)]  
*[Author 1](homepage), Author 2, and Author 3.*  
<details><summary>Click to expand</summary><p>
A summary here
</p></details>
```



## Introduction

**Definition:** Control a single attribute of interest, e.g. pose in our goal, without affecting other ones.

These change are most semantic

main lines:

- control the latent space of GAN



**Strength:** help to understand the generation process of GAN

latent disentangle

traverse in the latent space

latent space

manifold



Disentanglement can be defined as the ability to control a single factor, or feature, without affecting other ones [Locatello et al. 2018] A properly disentangled representation can benefit semantic data mixing [Johnson et al. 2016; Xiao et al. 2019], transfer learning for downstream tasks [Bengio et al. 2013; Tschannen et al. 2018], or even interpretability [Mathieu et al. 2018].

**challenge: reducing supervision**

supervised solutions are most effective [Aberman et al. 2019]

but often impose infeasible data collection requirement



Sematic work is InfoGAN



GAN Inversion: Interpreting the Latent Space of Pretrained Models

## Literature

GAN Inversion: A Survey

Challenging Common Assumptions in the Unsupervised Learning of Disentangled Representations



[Interpreting the Latent Space of GANs for Semantic Face Editing](https://arxiv.org/abs/1907.10786)  
**[`CVPR 2020`]**	**(`CUHK`)**	[[Github](https://github.com/genforce/interfacegan)]  
*Yujun Shen, Jinjin Gu, Xiaoou Tang, Bolei Zhou*



[Enjoy Your Editing: Controllable GANs for Image Editing via Latent Space Navigation](https://arxiv.org/abs/2102.01187)  
**[`ICLR 2021`]**  
*Peiye Zhuang, Oluwasanmi Koyejo, Alexander G. Schwing*



[Generative Hierarchical Features from Synthesizing Images](https://arxiv.org/abs/2007.10379)  
**[`CVPR 2021`]**	**(`CUHK`)**  
*Yinghao Xu, Yujun Shen, Jiapeng Zhu, Ceyuan Yang, Bolei Zhou*



[GANSpace: Discovering Interpretable GAN Controls](https://arxiv.org/abs/2004.02546)  
**[`NeurIPS 2020`]**



Generative Hierarchical Features from Synthesizing Images



Closed-Form Factorization of Latent Semantics in GANs



[Face Identity Disentanglement via Latent Space Mapping](https://arxiv.org/abs/2005.07728)  
**[`TOG 2020`]**	**(`Tel-Aviv University, Alibaba`)**	[[Github](https://github.com/YotamNitzan/ID-disentanglement)]  
*Yotam Nitzan, Amit Bermano, Yangyan Li, Daniel Cohen-Or*

