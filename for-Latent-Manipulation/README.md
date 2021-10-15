# Latent Space Image Manipulation

> We can also describe it as: "disentangled and meaningful image manipulations".
>
> To be specific, it's to control single/multi attributes of interest, e.g. pose, without affecting others. The common practice is to utilize the latent space of a pretrained generator for image manipulation.

steerable, interpretable, semantics

latent space navigation



都是需要 pre-trained models 



> **SOTA**:



Limitations：

- the discovered directions are independent of the latent code, i.e., paths that are linear.

- their evaluation relies either on visual inspection or on laborious human labeling.

  





Conventional generative models excel at generating **random** realistic samples with statistics resembling the training set. However, controllable and interactive matters rather than random. Therefore, a key problem of GM is to gain explicit control of the data synthesis process.





**challenge: reducing supervision**

Representation learning: A review and new perspectives

Challenging common assumptions in the unsupervised learning of disentangled representations



Disentanglement can be defined as the ability to control a single factor, or feature, without affecting other ones [Locatello et al. 2018] A properly disentangled representation can benefit semantic data mixing [Johnson et al. 2016; Xiao et al. 2019], transfer learning for downstream tasks [Bengio et al. 2013; Tschannen et al. 2018], or even interpretability [Mathieu et al. 2018].



## Introduction

> Despite their generative efficiency, GANs do not provide an inherent way of comprehending or controlling the underlying generative factors. 
>
> Related works study the structure of GAN’s latent space and attempt to find interpretable directions on it; that is, directions sampling across which are expected to generate images where only a few (ideally one) factors of variations are “activated”.
>
> --WarpedGANSpace



:dart:**Definition**

A disentangled representation in the context of generative learning can be defined as one where single latent units are sensitive to changes in single generative factors, while being relatively invariant to changes in other factors. --- [Representation learning: A review and new perspectives.]

We focus on the *disentanglement in the latent space* of a generative learning



:eyes: **What can we edit/control?**

Meaningful human interpretable directions can refer to either domain-specific factors (e.g., facial expressions) or domain-agnostic factors (e.g., zoom scale).



:pushpin:**Problem Statement**

a (<u>pretrained</u>) fixed GAN model consisting of a generator **G** and a discriminator **D**

latent vector $\boldsymbol{z} \in \mathbb{R}^m$ from a known distribution $P(\boldsymbol{z})$, and sample $N$ random vectors $\mathbb{Z} = \{\boldsymbol{z}^{(1)}, \dots, \boldsymbol{z}^{(N)}\}$







main method can be categorized into:

- 1. encode a given image into a latent representation of the manipulated image
- 2. find latent paths, traverse along them result in the desired manipulation
  
  - 2.1. use image annotations to find meaningful latent paths
  - 2.2. find meaningful directions without supervision and require manual annotation for each direction. 







## 存在性

2015 Radford et al. find GAN latent space processes semantically meaningful vector space arithmetic

Some work has observed the vector arithmetic property 

[Unsupervised representation learning with deep convolutional generative adversarial networks]()

[Deep feature interpolation for image content changes]()



Latent space of GANs is generally treated as Riemannian manifold

[2018 Metrics for deep generative models]() 

[Latent space oddity: on the curvature of deep generative models]()

[Latent space non-linear statistics]()



Prior work focused on exploring how to make the output image vary smoothly from one synthesis to another through interpolation in the latent space, regardless of whether the image is semantically controllable

[Feature-based metrics for exploring the latent space of generative models]()

[The riemannian geometry of deep generative models]()



[Optimizing the latent space of generative networks]()



**when linearly interpolating two latent codes z1 and z2, the appearance of the corresponding synthesis changes continuously, It implicitly means that the semantics contained in the image also change gradually**

> Unsupervised representation learning with deep convolutional generative adversarial networks

## What we do

the study on how a well-trained GAN is able to encode different semantics inside the latent space is still missing.



## 意义：

1. browse through the concepts that the GAN has learned
2. training a general model requires enormous computational resources, so interpret and extend the capabilities of existing GANs

对象：existing GANs



> interpreting well-trained GAN models



orthogonal image transformation



easy to distinguish and do not affect other attributes 

find more directions that do not interfere 



**One sentence to summary**: the latent space of GANs have semantically meaningful directions.

Which results moving in these directions corresponds to human-interpretable image transformations.

**Examples**: rotation, zooming or recoloring, 

exploitation of these directions would make image editing more straightforward



### Semantic image editing

> task is to transform a source image to a target image while modifying desired semantic attributes.

> for artistic visualization, design, photo enhancement

two primary goals

> providing continuous manipulation of multiple attributes simultaneously
>
> maintaining the original image’s identity as much as possible while ensuring photo-realism



Existing GAN-based approaches can be categorized roughly into two groups:

1) image-space editing

> These approaches often have high computational cost, and they primarily focus on binary attribute (on/off) changes, rather than providing continuous attribute editing abilities

2) latent-space editing

> lower-dimensional space
>







## 主要方法



The most straightforward way is to first generate a collection of image synthesis, then label these images regarding a target attribute, and finally find the latent separation boundary through supervised training.



In view of the annotation drawbacks of previous method, finding steerable directions of the latent space in an unsupervised manner is another direction, such as using PCA.



The common issue of the existing approaches is the limitation of global semantics, we would like to focus on some particular image region





current methods required 

- carefully designed loss functions

- introduction of additional attribute labels or features
- special architectures to train new models



## Literature

- [Supervised]() (require human labels, pre-trained models)

- [Self-supervised]() (image augmentations) - [simple transformations]

- [Unsupervised]() ()



>前两者can only discover researchers expectation directions. 需要想象力；后者能实现你所想不到
>



效果是：

orthogonal image transformations

different directions do not interfere with each other





The key of interpreting the latent space of GANs is to find the meaningful subspaces corresponding to the human-understandable attributes. Through that, moving the latent code towards the direction of a certain subspace can accordingly change the semantic occurring in the synthesized image. However, due to the high dimensionality of the latent space as well as the large diversity of image semantics, finding valid directions in the latent space is extremely challenging.



### :one:Supervised Learning

> domain-specific transformations (adding smile or glasses)
>
> **weakness**: need human labels or pretrained models, expensive to obtain

randomly sample a large amount of latent codes, then synthesize corresponding images and annotate them with labels, and finally use these labeled samples to learn a separation boundary in the latent space.

存在的问题：需要预定义的语义，需要大量采样

either by explicit human annotation, or by the use of pretrained semantic classifiers.

improves the memorability of the output image

- [Ganalyze: Toward visual definitions of cognitive image properties](https://arxiv.org/pdf/1906.10112.pdf)  
  *Lore Goetschalckx, Alex Andonian, Aude Oliva, Phillip Isola*  
  **[`CVPR 2019`] (`MIT, KU Leuven`)**

- [Interpreting the latent space of gans for semantic face editing](https://arxiv.org/pdf/1907.10786.pdf)  
  *Yujun Shen, Jinjin Gu, Xiaoou Tang, Bolei Zhou*  
  **[`CVPR 2020`] (`CUHK`)**

- [Semantic hierarchy emerges in deep generative representations for scene synthesis](https://arxiv.org/pdf/1911.09267.pdf)  
  *Ceyuan Yang, Yujun Shen, Bolei Zhou*  
  **[`IJCV 2021`] (`CUHK`)**

> explores the hierarchical semantics in the deep generative representations for scene synthesis

Use the classifiers pretrained on the CelebA dataset to predict certain face attributes

Add labels to latent space and separate a hyperplane. A normal to this hyperplane becomes a direction that captures the corresponding attribute.



### :two:Self-supervised Learning

> domain agnostic transformations (zooming or translation)



- [On the "steerability" of generative adversarial networks](https://arxiv.org/pdf/1907.07171.pdf)  
  *Ali Jahanian, Lucy Chai, Phillip Isola*  
  **[`ICLR 2020`] (`MIT`)**

- [Controlling generative models with continuous factors of variations](https://arxiv.org/pdf/2001.10238.pdf)  
  *Antoine Plumerault, Hervé Le Borgne, Céline Hudelot*  
  **[`ICLR 2020`] (`Université Paris-Saclay`)**

solve the optimization problem in the latent space that maximizes the score of the pretrained model, predicting image memorability



### :three:Unsupervised Learning

> are often less effective at providing semantic meaningful directions and all too often change image identity during an edit
>
> demanding training process that requires drawing large numbers of random latent codes and regressing the latent directions
>
> **weakness**: subjective visual inspection & laborious human labeling



- [GANSpace: Discovering Interpretable GAN Controls](https://arxiv.org/pdf/2004.02546.pdf)  
  *Erik Härkönen, Aaron Hertzmann, Jaakko Lehtinen, Sylvain Paris*  
  **[`NeurIPS 2020`] (`Adobe, NVIDIA`)** [[Code](https://github.com/harskish/ganspace)]

- [Unsupervised Discovery of Interpretable Directions in the GAN Latent Space](https://arxiv.org/pdf/2002.03754.pdf)  
  *Andrey Voynov, Artem Babenko*
  **[`ICML 2020`] (`Russia`)**  [[Code](https://github.com/anvoynov/GANLatentDiscovery)]

- [WarpedGANSpace: Finding non-linear RBF paths in GAN latent space](https://arxiv.org/pdf/2109.13357.pdf)  
  *Christos Tzelepis, Georgios Tzimiropoulos, Ioannis Patras*  
  **[`ICCV 2021`] (`QMUL`)** [[Code](https://github.com/chi0tzp/WarpedGANSpace)]





do not use any optimization

- [On the "steerability" of generative adversarial networks](https://arxiv.org/pdf/1907.07171.pdf)  
  *Ali Jahanian, Lucy Chai, Phillip Isola*  
  **[`ICLR 2020`] (`MIT`)**

- [GAN ”steerability” without optimization](https://arxiv.org/abs/2012.05328)  
  *Nurit Spingarn-Eliezer, Ron Banner, Tomer Michaeli*  
  **[`ICLR 2021`] (`Intel, IIT`)**







maps one *learnable* noise vector to each of the images in our dataset by minimizing a simple reconstruction loss.



an Autoencoder do assume two parametric models 1) $f: \mathcal{X} \rightarrow \mathcal{Z}$ and 2) $g: \mathcal{Z} \rightarrow \mathcal{X}$. 

we want to minimize the reconstruction loss $l(g(f(x)), x)$

sphere $S(\sqrt{d}, d, 2)$





## Tricks

[GLO](#GLO): 通常是假设 z 服从高斯分布，而这样导致点不太可能落在离球面 $\mathcal{S}(\sqrt{d}, d, 2)$ 太远的地方。又因为投影到球体上很容易且数值友好，因此会时刻让 z 映射到一个球体上。使用中，也会不使用 $\sqrt{d}$ 的球体，而是直接用单位球。





## Literature

**method1:**

2020 Face identity disentanglement via latent space mapping

2020 Encoding in style: a StyleGAN encoder for image-to-image translation

2021 Only a matter of style: Age transformation using a style-based regression model



**mathod2.1:**

2020 Interpreting the latent space of GANs for semantic face editing

2020 StyleFlow: attribute-conditioned exploration of StyleGANgenerated images using conditional continuous normalizing flows



**mathod2.2:**

2020 GANSpace: Discovering interpretable GAN controls

2020 Closed-form factorization of latent semantics in GANs

2020 Unsupervised discovery of interpretable directions in the GAN latent space

2021 A geometric analysis of deep generative image models and its applications



专门设一个 用 stylegan 的 

StyleSpace analysis: Disentangled controls for StyleGAN image generation





<span id="GLO"></span>
[Optimizing the Latent Space of Generative Networks](https://arxiv.org/pdf/1707.05776.pdf)  
**[`ICML 2018`] (`Facebook`)**  
*Piotr Bojanowski, Armand Joulin, David Lopez-Paz, Arthur Szlam*



global semantics

local semantics

<span id="LowRankGAN"></span>
[Low-Rank Subspaces in GANs](https://arxiv.org/pdf/2106.04488.pdf)  
**[`Arxiv 2021`] (`HKUST, Alibaba, USTC`)**  
*Jiapeng Zhu, Ruili Feng, Yujun Shen, Deli Zhao, Zhengjun Zha, Jingren Zhou, Qifeng Chen*





