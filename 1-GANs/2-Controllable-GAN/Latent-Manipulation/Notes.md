# <p align=center>`Notes - Generative Model for Face Steerability` </p>

Due to the lack of Github support for LaTeX math formulas, it is recommended that you can download it and view it locally with your own Markdown editor.

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

<details><summary>Click to expand</summary>

<div align=center><img width="800" src="https://raw.githubusercontent.com/yzy1996/Image-Hosting/master/20201122155212.png"/></div>

> **Problem Statement**

a latent vector $\boldsymbol{z} \in \mathbb{R}^m$ from a known distribution $\mathcal{Z}$

a (<u>pretrained</u>) fixed GAN model consisting of a generator **G** and a discriminator **D**

to discover $N$ attributes or semantically meaningful latent-space direction (transformation matrix) $\boldsymbol{T} = \{\boldsymbol{d}_1, \dots,\boldsymbol{d}_N\}$, where $\boldsymbol{d}_i \in \mathbb{R}^m$

an assigned step size $\boldsymbol{\varepsilon}=\left\{\varepsilon_{1}, \ldots, \varepsilon_{N}\right\}$, where $\boldsymbol{\varepsilon}$ is drawn from a uniform distribution $[-1, 1]^N$

a (<u>pretrained</u>) regressor **R** predict image attributes values $\boldsymbol{\alpha}=\left\{\alpha_{1}, \ldots, \alpha_{N}\right\}$, where $\boldsymbol{\alpha} \in [0, 1]$ and a constraint $0 \le\boldsymbol{\alpha} + \boldsymbol{\varepsilon} \le 1$

> **Objective function**

$$
\min _{\boldsymbol{T}} \mathcal{L}=\lambda_{1} \mathcal{L}_{\mathrm{reg}}+\lambda_{2} \mathcal{L}_{\mathrm{disc}}+\lambda_{3} \mathcal{L}_{\mathrm{content}}
$$

where $\mathcal{L}_{\mathrm{reg}}$ assesses transformations performance, $\mathcal{L}_{\mathrm{disc}}$ assesses new generated images quality by discriminator **D**, and $\mathcal{L}_{\mathrm{content}}$ (perceptual loss) estimate the distance between two images (maintain the image identity)

> **Unique**

- multi-label simultaneous
- local transformation, different direction $d_i$ with different latent vector $z_i$

> **Implementation details**

- Datasets: 1) face - [FFHQ](), [CelebA](), [CelebA-HQ](); 2) natural scene - [Transient Attribute Database](), [MIT Places2]()

</p></details>

---

[GANSpace: Discovering Interpretable GAN Controls](https://arxiv.org/pdf/2004.02546.pdf)  
**[`NeurIPS 2020`] (`Aalto, Adobe, NVIDIA`)**  
*Erik Härkönen, Aaron Hertzmann, Jaakko Lehtinen, Sylvain Paris*

<details><summary>Click to expand</summary><p>

<div align=center><img width="700" src="https://raw.githubusercontent.com/yzy1996/Image-Hosting/master/20201121154059.png" /></div>

> **Keywords**

PCA	

> **Goal**

find useful directions in $z$ space

> **Pipeline**

sample $N$ random vector $z_{1:N}$, then compute the corresponding $w_i = M(z_i)$ value

compute PCA of these $w_{1:N}$ values, then get a basis $V$ for $W$

given a new image defined by $w$, edit it by varying PCA coordinates $x$
$$
w^{\prime} = w + Vx
$$

</p></details>

---

[Interpreting the Latent Space of GANs for Semantic Face Editing](https://arxiv.org/pdf/1907.10786.pdf)  
**[`CVPR 2020`] (`CUHK`)** [[:octocat:](https://github.com/genforce/interfacegan)]  
*Yujun Shen, Jinjin Gu, Xiaoou Tang, Bolei Zhou*

<details><summary>Click to expand</summary><p>

<div align=center><img width="300" src="https://raw.githubusercontent.com/yzy1996/Image-Hosting/master/20201119220419.png"/></div>

> **Assumption**

For any binary semantic (e.g., male v.s. female), there exists a **hyperplane** in the latent space serving as the **separation boundary**. Semantic remains the same when the latent code walks within the same side of the hyperplane yet turns into the opposite when across the boundary.

> **Formulation**

$$
\mathrm{d}(\mathbf{n}, \mathbf{z})=\mathbf{n}^{T} \mathbf{z}
$$

$$
f(g(\mathbf{z}))=\lambda \mathrm{d}(\mathbf{n}, \mathbf{z})
$$

$G$: use the Generator of [PGGAN]() and [StyleGAN]() which are pretrained on [CelebA-HQ]()

> **Framework**

latent code z -> image x -> label

latent code z -> label

then train five independent linear SVMs on pose, smile, age, gender, eyeglasses

finally find n and edit the latent code z with $z_{edit} = z + \alpha n$

</p></details>

---

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



