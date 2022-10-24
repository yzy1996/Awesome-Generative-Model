# <p align=center>`Controllable Generation`</p>

[![Awesome](https://cdn.rawgit.com/sindresorhus/awesome/d7305f38d29fed78fa85652e3a63e154dd8e8829/media/badge.svg)](https://github.com/sindresorhus/awesome)
[![Maintenance](https://img.shields.io/badge/Maintained%3F-yes-green.svg)](https://GitHub.com/Naereen/StrapDown.js/graphs/commit-activity)
[![PR's Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=flat)](http://makeapullrequest.com) 

A collection of resources on Controllable Generation (Latent Space Manipulation). Specific attribute-pose is summarized in [3D-Aware-Generation](../3D-Aware-Generation)

> Some key words: interpreting, latent space navigation, steerable, steerability, interpretable, semantics, manual annotation, meaningful directions, semantic image editing, independence, exclusiveness.

*PS: this repo does **not** contains style transfer, I would tend to classify it as artistic creation (mix and interpolate features from different images).*



## Contributing

Feedback and contributions are welcome! If you think I have missed out on something (or) have any suggestions (papers, implementations and other resources), feel free to pull a request or leave an issue. I will release the [latex-pdf version]() in the future. :arrow_down:markdown format:

``` markdown
[Paper Name](abs link)  
*[Author 1](homepage), Author 2, and Author 3*
**[`Conference/Journal Year`] (`Institution`)** [[Github](link)] [[Project](link)]
```

:smile: Now you can use this [script](https://github.com/yzy1996/Python-Code/tree/master/Python%2BarXiv) to automatically generate the above text.



## Introduction

Conventional generative models excel at generating random realistic samples with statistics resembling the training set. However, controllable and interactive matters rather than random. GANs do not provide an inherent way of comprehending or controlling the underlying generative factors. But some researches show that a well-trained GAN is able to encode different semantics inside the latent space. Therefore, a key problem of generative models is to gain explicit control of the synthesis process or results.

The goal is to generate or modify images satisfying our specific requirements. The requirement should be semantical meaningful interpretable and easy to distinguish without affecting other attributes (e.g. object pose,). The manipulation could be single or multi attributes of interest.

The first line proposes conditional GANs to generate with $p(z \mid y)$ or employ auxiliary classifiers to enforce the gan network to generate desired results.

Another line is to utilize the latent space of a pretrained generator for image manipulation. In this line, we could also control and modify a given real image by inverting the image into latent code (**inversion**). The main idea behind this method is to disentangle the latent space. A common practice is to analyze and dissect GANs’ latent spaces, finding disentangled latent variables suitable for editing. The disentangled latent variables sometimes are interpretable directions $d$. Careful modifications of the latent embeddings then translate to desired changes in the generated output.

$$
x = G(z_0) \rightarrow x' = G(z_0 + \alpha d)
$$

These directions should be orthogonal which do not interfere with each other, moving in these directions corresponds to attributes variation. These valid direction could also be seen as some manifold of the latent space, meaningful subspaces corresponding to the human-understandable attributes.



GANs can produce high-fidelity images visually indistinguishable from real ones. However, the generated images are not controllable but controlling over the generated images brings many interesting applications. 

Such control can be obtained by first learning the manifold and then realizing image editing through latent space traversal. Moving latent codes towards some certain directions can cause corresponding attribute change in images.

Many works have examined semantic directions in the latent spaces spontaneously learned by pre-trained GANs. The widely used StyleGAN is a common choice for its high-quality synthesis and remarkable latent-based editing quality through its rich and highly disentangled latent space.

Some using full-supervision in the form of semantic labels, others find meaningful directions in a self-supervised fashion, and, finally, recent works present unsupervised methods to achieve the same goal. 



**Disentanglement** can be defined as the ability to control a single factor, or feature, without affecting other ones. A properly disentangled representation can benefit semantic data mixing, transfer learning for downstream tasks, or even interpretability.  --《Face Identity Disentanglement via Latent Space Mapping》





:dart: **Summary**

We mainly focus on the *disentanglement in the latent space* of a generative model. We hope:

- keep high-quality after editing

- disentangle in an unsupervised manner
- find more disentangled directions that do not interfere with each other
- provide continuous manipulation of multiple attributes simultaneously
- high-pricision

One more thing is the interaction mode:

- provide segmentation mask to change specific area.



:eyes: **What can we edit/control?**

Meaningful human interpretable directions can refer to either domain-specific factors (e.g., facial expressions) or domain-agnostic factors (e.g., zoom scale). Some examples including:

- change facial expressions in portraits
- change view-point or shapes and textures of cars
- interpolate between different images

some simple transformation (rotation, zooming)

[add some image]



:paperclip: **Futher Impact**

- browse through the concepts that the GAN has learned, internal representation

- training a general model requires enormous computational resources, so interpret and extend the capabilities of existing GANs

- for artistic visualization, design, photo enhancement

- solving many other downstream tasks, including face verification, landmark detection, layout prediction, transfer learning, style mixing, image editing, *etc*.





## Methods Taxonomy

This is the summary of controllable GAN including;

- [training stage] conditional GAN mode 
- [test stage] modify a pre-trained GAN model
- [test stage] modify a latent code of a given image



- Conditional GANs and Auxiliary Classifier

  > different conditioning lead different outputs
  >
  > auxiliary attribute classifiers to guide synthesis 
  >
  > :speech_balloon: requires large labeled datasets. These methods are limited to image types for which large annotated datasets are available, like **portraits**. Limited editing control 

- Analyze and dissect GANs’ latent spaces, finding disentangled latent variables suitable for editing

  > :speech_balloon: **do not enable detailed editing and are often slow**.
  >
  > used in real-time on different images and with different edits

- change network weight




前两者can only discover researchers expectation directions. 需要想象力；后者能实现你所想不到





:pushpin: **Problem Statement**

A (<u>pretrained</u>) fixed GAN model consisting of a generator **G** and a discriminator **D**，latent vector $\boldsymbol{z} \in \mathbb{R}^m$ from a known distribution $P(\boldsymbol{z})$, and sample $N$ random vectors $\mathbb{Z} = \{\boldsymbol{z}^{(1)}, \dots, \boldsymbol{z}^{(N)}\}$

We want to discover K non-linear interpretable paths on the latent space. The most straightforward way is to first generate a collection of image synthesis, then label these images regarding a target attribute, and finally find the latent separation boundary through supervised training. In view of the annotation drawbacks of previous method, finding steerable directions of the latent space in an unsupervised manner is another direction, such as using PCA. The common issue of the existing approaches is the limitation of global semantics, we would like to focus on some particular image region.



current methods required 

- carefully designed loss functions

- introduction of additional attribute labels or features
- special architectures to train new models



### Metrics

> 我们需要一些，其实也是面对整个大的解耦学习 Disentanglement Learning 

Inspired by Bengio, we cam adopt the notion of disentangled representation learning as "a process of decorrelating information in the data into separate informative representations, each of which corresponds to a concept defined by humans".

So the three important properties can be summarized as **informativeness**, **separability**, and **interpretability**.



[Measuring Disentanglement: A Review of Metrics](https://arxiv.org/pdf/2012.09276.pdf)  
Julian Zaidi, Jonathan Boilard, Ghyslain Gagnon, Marc-André Carbonneau  

[Theory and Evaluation Metrics for Learning Disentangled Representations](https://arxiv.org/pdf/1908.09961.pdf)  
*Kien Do, Truyen Tran*  
**[`ICLR 2020`]**



### Tricks

[(GLO) Optimizing the Latent Space of Generative Networks](https://arxiv.org/pdf/1707.05776.pdf)  
**[`ICML 2018`] (`Facebook`)**  
*Piotr Bojanowski, Armand Joulin, David Lopez-Paz, Arthur Szlam*

<details><summary>Click to expand</summary>

通常是假设 z 服从高斯分布，而这样导致点不太可能落在离球面 $\mathcal{S}(\sqrt{d}, d, 2)$ 太远的地方。又因为投影到球体上很容易且数值友好，因此会时刻让 z 映射到一个球体上。使用中，也会不使用 $\sqrt{d}$ 的球体，而是直接用单位球。

</details>


## Literature



### Survey

[Representation Learning: A Review and New Perspectives](https://arxiv.org/abs/1206.5538)  
*Yoshua Bengio, Aaron Courville, Pascal Vincent*

[Challenging Common Assumptions in the Unsupervised Learning of Disentangled Representations](https://arxiv.org/pdf/1811.12359.pdf)
*Francesco Locatello, Stefan Bauer, Mario Lucic, Gunnar Rätsch, Sylvain Gelly, Bernhard Schölkopf, Olivier Bachem*

### 1.1 Conditional GAN

- [StarGAN: Unified Generative Adversarial Networks for Multi-Domain Image-to-Image Translation](https://arxiv.org/pdf/1711.09020.pdf)  
  Yunjey Choi, Minje Choi, Munyoung Kim, Jung-Woo Ha, Sunghun Kim, Jaegul Choo  
  **[`CVPR 2018`] (`Korea University`)**

- [MaskGAN: Towards Diverse and Interactive Facial Image Manipulation](https://arxiv.org/pdf/1907.11922.pdf)  
  *Cheng-Han Lee, Ziwei Liu, Lingyun Wu, Ping Luo*  
  **[`CVPR 2020`] (`SenseTime, CUHK`)**

- [Cascade EF-GAN: Progressive Facial Expression Editing with Local Focuses](https://arxiv.org/pdf/2003.05905.pdf)  
  *Rongliang Wu, Gongjie Zhang, Shijian Lu, Tao Chen*  
  **[`CVPR 2020`] (`NTU`)**

- [SEAN: Image Synthesis with Semantic Region-Adaptive Normalization](https://arxiv.org/pdf/1911.12861.pdf)  
  Peihao Zhu, Rameen Abdal, Yipeng Qin, Peter Wonka  
  [CVPR 2020]

- [Deep Generation of Face Images from Sketches](https://arxiv.org/pdf/2006.01047.pdf)  
  *Shu-Yu Chen, Wanchao Su, Lin Gao, Shihong Xia, Hongbo Fu*   
  **[`TOG 2020`] (`CAS, CityU`)**

- [Semantic Image Synthesis with Spatially-Adaptive Normalization](https://arxiv.org/pdf/1903.07291.pdf)  
  *Taesung Park, Ming-Yu Liu, Ting-Chun Wang, Jun-Yan Zhu* 
  **[`CVPR 2019`] (`UCB, NVIDIA`)**

- [High-Resolution Image Synthesis and Semantic Manipulation with Conditional GANs](https://arxiv.org/pdf/1711.11585.pdf)  
  *Ting-Chun Wang, Ming-Yu Liu, Jun-Yan Zhu, Andrew Tao, Jan Kautz, Bryan Catanzaro*   
  **[`CVPR 2018`] (`NVIDIA`)**



### 1.2 Auxiliary Classifier

- [GuidedStyle: Attribute Knowledge Guided Style Manipulation for Semantic Face Editing](https://arxiv.org/pdf/2012.11856.pdf)  
  *Xianxu Hou, Xiaokang Zhang, Linlin Shen, Zhihui Lai, Jun Wan*  

- [AttGAN: Facial Attribute Editing by Only Changing What You Want](https://arxiv.org/pdf/1711.10678.pdf)  
  *Zhenliang He, Wangmeng Zuo, Meina Kan, Shiguang Shan, Xilin Chen*  
  **[`TIP 2019`] (`CAS`)**



### 2.1 Encode

> encode a given image into a latent representation of the manipulated image

- [Face Identity Disentanglement via Latent Space Mapping](https://arxiv.org/pdf/2005.07728.pdf)  
  *Yotam Nitzan, Amit Bermano, Yangyan Li, Daniel Cohen-Or*  
  **[`TOG 2020`] (`Tel-Aviv University`)**

- [Encoding in Style: a StyleGAN Encoder for Image-to-Image Translation](https://arxiv.org/pdf/2008.00951.pdf)  
  *Elad Richardson, Yuval Alaluf, Or Patashnik, Yotam Nitzan, Yaniv Azar, Stav Shapiro, Daniel Cohen-Or*  
  **[`CVPR 2021`] (`Penta-AI, Tel-Aviv University`)**

- [Only a Matter of Style: Age Transformation Using a Style-Based Regression Model](https://arxiv.org/pdf/2102.02754.pdf)  
  *Yuval Alaluf, Or Patashnik, Daniel Cohen-Or*  
  **[`SIGGRAPH 2021`] (`Tel-Aviv University`)**
  
- Designing an Encoder for StyleGAN Image Manipulation



### 2.2 Modify GAN Model

control GANs' network parameters

> Good: one model can produce countless new images following the modified rules.



- [Rewriting a Deep Generative Model](https://arxiv.org/pdf/2007.15646.pdf)  
  *David Bau, Steven Liu, Tongzhou Wang, Jun-Yan Zhu, Antonio Torralba*  
  **[`ECCV 2020`] (`MIT, Adobe`)**

- [Navigating the GAN Parameter Space for Semantic Image Editing](https://arxiv.org/pdf/2011.13786.pdf)  
  *Anton Cherepkov, Andrey Voynov, Artem Babenko*  
  **[`CVPR 2021`] (`MIPT`)**

- [Semantic Photo Manipulation with a Generative Image Prior](https://arxiv.org/pdf/2005.07727.pdf)  
  *David Bau, Hendrik Strobelt, William Peebles, Jonas Wulff, Bolei Zhou, Jun-Yan Zhu, Antonio Torralba*  
  **[`ECCV 2020`] (`MIT`)**  



### 2.3 Modify Latent Space

> analyze and dissect latent space,finding disentangled latent variables suitable for editing.

the discovered directions   linear / nonlinear path | their evaluation relies either on visual inspection or on laborious human labeling.

- [EditGAN: High-Precision Semantic Image Editing](https://arxiv.org/pdf/2111.03186.pdf)  
  *Huan Ling, Karsten Kreis, Daiqing Li, Seung Wook Kim, Antonio Torralba, Sanja Fidler*  
  **[`NeurIPS 2021`] (`NVIDIA, Toronto`)**

- [DatasetGAN: Efficient Labeled Data Factory with Minimal Human Effort](https://arxiv.org/pdf/2104.06490.pdf)  
  *Yuxuan Zhang, Huan Ling, Jun Gao, Kangxue Yin, Jean-Francois Lafleche, Adela Barriuso, Antonio Torralba, Sanja Fidler*  
  **[`CVPR 2021`] (`NVIDIA, Toronto`)**

- [Semantic Segmentation with Generative Models: Semi-Supervised Learning and Strong Out-of-Domain Generalization](https://arxiv.org/pdf/2104.05833.pdf)  
  *Daiqing Li, Junlin Yang, Karsten Kreis, Antonio Torralba, Sanja Fidler*  
  **[`CVPR 2021`] (`NVIDIA, Toronto`)**





#### 2.3.1 Supervised 

> domain-specific transformations (adding smile or glasses)
>
> **weakness**: need human labels or pretrained models, expensive to obtain

pipeline: randomly sample a large amount of latent codes, then synthesize corresponding images and annotate them with labels, and finally use these labeled samples to learn a separation boundary in the latent space.

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

- [InterFaceGAN: Interpreting the Disentangled Face Representation Learned by GANs](https://arxiv.org/pdf/2005.09635.pdf)  
  *Yujun Shen, Ceyuan Yang, Xiaoou Tang, Bolei Zhou*  
  **[`TPAMI 2020`] (`CUHK`)**

- [Disentangled Image Generation Through Structured Noise Injection](https://arxiv.org/pdf/2004.12411.pdf)  
  *Yazeed Alharbi, Peter Wonka*  
  **[`CVPR 2020`] (`KAUST`)**

- [GAN Dissection: Visualizing and Understanding Generative Adversarial Networks](https://arxiv.org/pdf/1811.10597.pdf)  
  *David Bau, Jun-Yan Zhu, Hendrik Strobelt, Bolei Zhou, Joshua B. Tenenbaum, William T. Freeman, Antonio Torralba*  
  **[`ICLR 2019`] (`MIT, CUHK`)**

- [Semantic Photo Manipulation with a Generative Image Prior](https://arxiv.org/pdf/2005.07727.pdf)  
  *David Bau, Hendrik Strobelt, William Peebles, Jonas Wulff, Bolei Zhou, Jun-Yan Zhu, Antonio Torralba*   
  **[`TOG 2019`] (`MIT`)**

- [Controlling generative models with continuous factors of variations](https://arxiv.org/pdf/2001.10238.pdf)  
  *Antoine Plumerault, Hervé Le Borgne, Céline Hudelot*  
  **[`ICLR 2020`] (`CEA`)**



> explores the hierarchical semantics in the deep generative representations for scene synthesis

Use the classifiers pretrained on the CelebA dataset to predict certain face attributes

Add labels to latent space and separate a hyperplane. A normal to this hyperplane becomes a direction that captures the corresponding attribute.



- [StyleFlow: Attribute-conditioned Exploration of StyleGAN-Generated Images using Conditional Continuous Normalizing Flows](https://arxiv.org/pdf/2008.02401.pdf)  
  *Rameen Abdal, Peihao Zhu, Niloy Mitra, Peter Wonka*  
  **[`TOG 2021`] (`KAUST, UCL`)**



#### 2.3.2 Self-Supervised Learning

> domain agnostic transformations (zooming or translation)
>
> (image augmentations) - [simple transformations]



- [On the "steerability" of generative adversarial networks](https://arxiv.org/pdf/1907.07171.pdf)  
  *Ali Jahanian, Lucy Chai, Phillip Isola*  
  **[`ICLR 2020`] (`MIT`)**

- [Controlling generative models with continuous factors of variations](https://arxiv.org/pdf/2001.10238.pdf)  
  *Antoine Plumerault, Hervé Le Borgne, Céline Hudelot*  
  **[`ICLR 2020`] (`Université Paris-Saclay`)**

solve the optimization problem in the latent space that maximizes the score of the pretrained model, predicting image memorability



#### 2.3.3 Unsupervised

> are often less effective at providing semantic meaningful directions and all too often change image identity during an edit
>
> demanding training process that requires drawing large numbers of random latent codes and regressing the latent directions
>
> **weakness**: subjective visual inspection & laborious human labeling
>
> using unsupervised manner such as PCA to find steerable direction



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

- [Closed-Form Factorization of Latent Semantics in GANs](https://arxiv.org/pdf/2007.06600.pdf)  
  *Yujun Shen, Bolei Zhou*  
  **[`CVPR 2021`] (`CUHK`)**

A geometric analysis of deep generative image models and its applications



<span id="LowRankGAN"></span>
[Low-Rank Subspaces in GANs](https://arxiv.org/pdf/2106.04488.pdf)  
*Jiapeng Zhu, Ruili Feng, Yujun Shen, Deli Zhao, Zhengjun Zha, Jingren Zhou, Qifeng Chen*  
**[`NeurIPS 2021`] (`HKUST, Alibaba, USTC`)**  







GAN models could capture the natural statistics while isolate independent factors of variation. These factors can be used used to control the outcome, but those perturbation will affect the global statistic of the images. So we want the manipulation occur at the localized level. The general methods will depend on the annotations of the independent factors. 

We aim to learn spatially and semantically independent latent factors without the need for any annotation.



VAE-based methods use the total correlation of the latent variable distributions as the penalty

InfoGAN-based methods maximize the mutual information between latent factors ad related observations.

Usually the extra terms lead to worse generation quality for these typical disentanglement methods.

GAN-based methods discover semantically meaningful directions in the style space of StyleGAN by analysing the distribution of teh first-layer output or layer weights.





[Generative Hierarchical Features from Synthesizing Images](https://arxiv.org/pdf/2007.10379.pdf)  
**[`CVPR 2021`] (`CUHK`)**  
*Yinghao Xu, Yujun Shen, Jiapeng Zhu, Ceyuan Yang, Bolei Zhou*

Editing in style: Uncovering the local semantics of GANs

Decorating your own bedroom: Locally controlling image generation with generative adversarial networks

Spatially controllable image synthesis with internal representation collaging

Human-in-the-loop differential subspace search in high-dimensional latent space

A spectral regularizer for unsupervised disentanglement

The geometry of deep generative image models and its applications

[Enjoy Your Editing: Controllable GANs for Image Editing via Latent Space Navigation](https://arxiv.org/pdf/2102.01187.pdf)  
**[`ICLR 2021`] (`UIUC`)**  
*Peiye Zhuang, Oluwasanmi Koyejo, Alexander G. Schwing*

[Disentangled and Controllable Face Image Generation via 3D Imitative-Contrastive Learning](https://arxiv.org/pdf/2004.11660.pdf)  
**[`CVPR 2020`] (`Tsinghua`)**  
*Yu Deng, Jiaolong Yang, Dong Chen, Fang Wen, Xin Tong*



> augmenting and regularizing the latent space

A free viewpoint portrait generator with dynamic styling

Disentangled image generation through structured noise injection

Gan-control: Explicitly controllable gans



[Deforming autoencoders: Unsupervised disentangling of shape and appearance](https://arxiv.org/pdf/1806.06503.pdf)  
**[`ECCV 2018`] (`Stony Brook University`)**   
*Zhixin Shu, Mihir Sahasrabudhe, Alp Guler, Dimitris Samaras, Nikos Paragios, Iasonas Kokkinos*



| For Face |
| ------------------------------------------------------------ |
| [MaskGAN: Towards Diverse and Interactive Facial Image Manipulation](https://arxiv.org/pdf/1907.11922.pdf)  <br />**[`CVPR 2020`]** Cheng-Han Lee, Ziwei Liu, Lingyun Wu, Ping Luo |

