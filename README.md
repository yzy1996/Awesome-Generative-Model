<h1 <p align=center>Awesome 2D Generative Model</h1>
<div align="center">

[![Awesome](https://cdn.rawgit.com/sindresorhus/awesome/d7305f38d29fed78fa85652e3a63e154dd8e8829/media/badge.svg)](https://github.com/sindresorhus/awesome)
[![Maintenance](https://img.shields.io/badge/Maintained%3F-yes-green.svg)](https://GitHub.com/Naereen/StrapDown.js/graphs/commit-activity)
[![PR's Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=flat)](http://makeapullrequest.com) 
</div>

A collection of resources on 2D Generative Model which utilize generator functions that map low-dimensional latent codes to high-dimensional data outputs..



## Contributing

Feedback and contributions are welcome! If you think I have missed out on something (or) have any suggestions (papers, implementations and other resources), feel free to pull a request or leave an issue. I will release the [latex-pdf version]() in the future. :arrow_down:markdown format:

``` markdown
[Paper Name](abs link)  
*[Author 1](homepage), Author 2, and Author 3*
**[`Conference/Journal Year`] (`Institution`)** [[Github](link)] [[Project](link)]
```

:smile: Now you can use this [script](https://github.com/yzy1996/Python-Code/tree/master/Python%2BarXiv) to automatically generate the above text.



## Contents

**GAN related sources** has been moved to **[GAN](https://github.com/yzy1996/Awesome-GANs)**

**3D-Aware Generation** has been moved to **[Learn 3D from 2D](https://github.com/yzy1996/Awesome-Learn-3D-From-2D)** 



1. [Variational AutoEncoder (VAE)](./1-Variational%20AutoEncoder%20(VAE))
2. [Diffusion Model](./2-Diffusion%20Model)
3. [Energy-Based Model (EBM)](./3-Energy-Based%20Model%20(EBM))
4. [Flow](./4-Flow)
5. [Representation Learning](./5-Representation%20Learning)
6. [Disentangled Representation](./6-Disentangled%20Representation)
7. [Text-to-Image](./7-Text-to-Image)
9. [Others](./Others)



## Introduction

![img](https://raw.githubusercontent.com/yzy1996/Image-Hosting/master/generative-overview.png)



<details><summary>中文介绍</summary><p>

表征（representation）和重构（reconstruction）一直是不分家的两个研究话题。

核心目标是重构，但就像我看到一幅画面，想要转述给另一个人，让他也想象出这个画面的场景，人会将这幅画抽象为一些特征，例如这幅画是自然风光，有很多树，颜色很绿，等等。然后另一个人再根据这些描述，通过自己预先知道的人生阅历，就能还原这幅画。或者就像公安在找犯人的时候，需要通过描述嫌疑人画像。是通过一些特征在刻画的。

机器同样也需要这样一套范式，只不过可能并不像人一样的语意理解。为了可解释性，以及可控性，我们是希望机器能按照人能理解的一套特征来。

</p>
</details>



The ability to generate and manipulate photorealistic image content (**high resolution** & **content controllable**) is a long-standing goal of computer vision and graphics. We try to model the real world by generating realistic samples from latent representations. 





Existing generative modeling techniques can largely be grouped into two categories based on how they represent probability distributions.

1. **likelihood-based models**, which directly learn the distribution’s probability density (or mass) function via (approximate) maximum likelihood. Typical likelihood-based models include autoregressive models, normalizing flow models , energy-based models (EBMs), and variational auto-encoders (VAEs).
2. **implicit generative models**, where the probability distribution is implicitly represented by a model of its sampling process. The most prominent example is generative adversarial networks (GANs), where new samples from the data distribution are synthesized by transforming a random Gaussian vector with a neural network.

> From Song Yang 



Deep generative models can be divided broadly into three categories:

- **Generative Adversarial Networks**

  > use discriminator networks that are trained to distinguish samples from generator networks and real examples

- **Likelihood-based Model**

  > directly optimize the model log-likelihood or the evidence lower bound.

  - Variational autoencoder (VAE) 

    > :yum: fast | tractable sampling | easy-to-access encoding networks 

  - normalizing flows

  - autoregressive models

- **Energy-based Models**

  > estimate a scalar energy for each example that corresponds to an unnormalized log-probability
  





Generative models are widely used for image synthesis and various image-processing tasks, such as editing, inpainting, colorization, deblurring, and superresolution. Generative models have the potential to streamline the workflow of photographers and digital artists and enable new levels of creativity. Similarly, they might allow content creators to efficiently generate virtual 3D content for games, animated movies, or the metaverse. 



生成模型应该具备的特点：

- **High-quality sampling**：需要生成的足够真实，无法区分真假。
- **Mode coverage and sample diversity**：如果数据是具有多样性的，则生成模型也应该具备多样性，而且是在不损失质量的前提下。
- **Fast and computationally inexpensive sampling**：一些应用需要实时性，例如实时编辑。



![Three key requirements for generative models and how different frameworks trade off between them](https://developer-blogs.nvidia.com/wp-content/uploads/2022/04/GANs_Diffusion_Autoencoders.png)

