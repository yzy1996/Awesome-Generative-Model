# <p align=center>`Awesome 2D Generative Model` </p>

[![Awesome](https://cdn.rawgit.com/sindresorhus/awesome/d7305f38d29fed78fa85652e3a63e154dd8e8829/media/badge.svg)](https://github.com/sindresorhus/awesome)
[![Maintenance](https://img.shields.io/badge/Maintained%3F-yes-green.svg)](https://GitHub.com/Naereen/StrapDown.js/graphs/commit-activity)
[![PR's Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=flat)](http://makeapullrequest.com) 

A collection of resources on 2D Generative Model.

A collection of resources on generative models which utilize generator functions that map low-dimensional latent codes to high-dimensional data outputs.



We would define a prior distribution for the latent space, however this prior may not match the true and agnostic data manifold. It’s an obstacles yielding less accurate generation.

## Contributing

Feedback and contributions are welcome! If you think I have missed out on something (or) have any suggestions (papers, implementations and other resources), feel free to pull a request or leave an issue. I will release the [latex-pdf version]() in the future. :arrow_down:markdown format:

``` markdown
[Paper Name](abs link)  
*[Author 1](homepage), Author 2, and Author 3*
**[`Conference/Journal Year`] (`Institution`)** [[Github](link)] [[Project](link)]
```

:smile: Now you can use this [script](https://github.com/yzy1996/Python-Code/tree/master/Python%2BarXiv) to automatically generate the above text.

## Category

**3D-Aware Generation** has been moved to **[Learn 3D from 2D](https://github.com/yzy1996/Awesome-Learn-3D-From-2D)** 

**GAN related sources** has been moved to **[GAN](https://github.com/yzy1996/Awesome-GANs)**



## Introduction

photorealistic image synthesis

- high resolution cc
- content controllable



compositional nature of scenes

- individual objects' shapes
- appearances
- background



Modern computer graphics (CG) techniques have achieved impressive results and are industry standard in gaming and movie productions. However, they are very hardware and computing expensive and require substantial repetitive labor. 

Therefore, the ability to generate and manipulate photorealistic image content is a long-standing goal of computer vision and graphics.

There models try to model the real world by generating realistic samples from latent representations.



<Generating images with sparse representations> divide deep generative models broadly into three categories:

- Generative Adversarial Networks

  > use discriminator networks that are trained to distinguish samples from generator networks and real examples

- Likelihood-based Model

  > directly optimize the model log-likelihood or the evidence lower bound.

  - Variational autoencoder (VAE) 

    > :yum: fast | tractable sampling | easy-to-access encoding networks 

  - normalizing flows

  - autoregressive models

- Energy-based Models

  > estimate a scalar energy for each example that corresponds to an unnormalized log-probability
  
  

### VAE

The majority of the research efforts on improving VAEs is dedicated to the statistical challenges, such as:

- reducing the gap between approximate and true posterior distribution
- formulatig tighter bounds
- reducing the gradient noise
- extending VAEs to discrete variables
- tackling posterior collapse
- designing special network architectures
  - previous work just borrows the architectures from the classification tasks



VAEs maximize the mutual information between the input and latent variables, requiring the networks to retain the information content of the input data as much as possible.

Information maximization in noisy channels: A variational approach  
**[`NeurIPS 2017`]**

Deep variational information bottleneck  
**[`ICLR 2017`]**





表征（representation）和重构（reconstruction）一直是不分家的两个研究话题。

核心目标是重构，但就像我看到一幅画面，想要转述给另一个人，让他也想象出这个画面的场景，人会将这幅画抽象为一些特征，例如这幅画是自然风光，有很多树，颜色很绿，等等。然后另一个人再根据这些描述，通过自己预先知道的人生阅历，就能还原这幅画/

或者就像公安在找犯人的时候，需要通过描述嫌疑人画像。是通过一些特征在刻画的。

机器同样也需要这样一套范式，只不过可能并不像人一样的语意理解

为了可解释性，以及可控性，我们是希望机器能按照人能理解的一套特征来

![image-20220612154943172](https://raw.githubusercontent.com/yzy1996/Image-Hosting/master/image-20220612154943172.png)



AutoDecoder





这里又需要提及一下重建loss



## Introduction

Generative models can be divided into two classes:

- implicit generative models (IGMs)
- explicit generative models (EGMs)



Our goal is to train a model $\mathbb{Q}_{\theta}$ which aims to approximate a target distribution $\mathbb{P}$ over a space $\mathcal{X} \subseteq \mathbb{R}^{d}$.

Normally we define $\mathbb{Q}_{\theta}$ by a generator function $G_{\theta}: \mathcal{Z} \rightarrow \mathcal{X}$, implemented as a deep network with parameters $\theta$, where $\mathcal{Z}$ is a space of latent vectors, say $\mathcal{R}^{128}$. We assume a fixed Gaussian distribution on $\mathcal{Z}$, and call $\mathbb{Q}_{\theta}$ the distribution of $G_{\theta}(Z)$. 

The optimization process is to learn by minimizing a discrepancy $\mathcal{D}$ between distributions , with the property $\mathcal{D}(\mathbb{P}, \mathbb{Q}_{\theta}) \geq 0$ and $\mathcal{D}(\mathbb{P}, \mathbb{P})=0$.



we can build loss $\mathcal{D}$ based on the Maximum Mean Discrepancy,
$$
\operatorname{MMD}_{k}(\mathbb{P}, \mathbb{Q})=\sup _{f:\|f\|_{\mathcal{H}_{k}} \leq 1} \mathbb{E}_{X \sim \mathbb{P}}[f(X)]-\mathbb{E}_{Y \sim \mathbb{Q}}[f(Y)]
$$
where $\mathcal{H}_k$ is the reproducing kernel Hilbert space with a kernel $k$.





Wasserstein distance
$$
\mathcal{W}(\mathbb{P}, \mathbb{Q})=\sup _{f:\|f\|_{\text {Lip }} \leq 1} \mathbb{E}_{X \sim \mathbb{P}}[f(X)]-\mathbb{E}_{Y \sim \mathbb{Q}}[f(Y)]
$$





There are three main methods: 

- VAE

- GAN
- Flow

They both learn from the training data and use the learned model to generate or predict new instances.



相同点：都用到了随机噪声，然后度量噪声和真实数据的分布差异

不同点：GAN为了拟合数据分布，VAE为了找到数据的隐式表达，Flow建立训练数据和生成数据之间的关系

GAN 和 Flow 的输入和输出都是一一对应的，而VAE不是



训练的损失函数上：

VAE最大化ELBO，其目的是要做最大似然估计，最大似然估计等价于最小化KL，但这个KL不是数据和噪声的KL，而是model给出的![[公式]](https://www.zhihu.com/equation?tex=p%28x%29)和数据所展示的![[公式]](https://www.zhihu.com/equation?tex=p%28x%29)之间的KL。

GAN是最小化JS，这个JS也是model给出的![[公式]](https://www.zhihu.com/equation?tex=p%28x%29)和数据所展示的![[公式]](https://www.zhihu.com/equation?tex=p%28x%29)之间的。

流模型训练也非常直接，也是最大似然估计。只不过因为流模型用的是可逆神经网络，因此，相比于其他两者，学习inference即学习隐含表示非常容易，




## GAN 2014

Generative Adversarial Networks (GANs) emerge as a powerful class of generative models. In particular, they are able to synthesize photorealistic images at high resolutions ($$1024 \times 1024$$) pixels which can not be distinguished. 



GANs and its variants 



train with adversarial methods, bypass the need of computing densities, at the expense of a good density estimation

Generative adversarial networks (GANs) represent a zero-sum game between two machine players, a generator and a discriminator, designed to learn the distribution of data.



> 只要能骗过Discriminator就好



## VAE 2013

at the cost of learning two neural networks





## VAE-GAN

combine VAE with GAN



## Bijective GNN



## Flow



## Inverse Rendering / Graphics

Given 2D image observations, these approaches aim to infer a 3D-structure-aware representation of the underlying scene that enables prior-based predictions about occluded parts.



参考：

https://www.jeremyjordan.me/variational-autoencoders/

https://www.jeremyjordan.me/autoencoders/
