# Latent Space Image Manipulation



## Introduction

To tackle the instability of the training procedure...



These methods can be divided into two categories:

- ...



## Literature

unsorted

[Challenging common assumptions in the unsupervised learning of disentangled representations](https://arxiv.org/abs/1811.12359)



 



[GLO](#GLO)

[SeFa](#SeFa)

[Enjoy Your Editing](#Enjoy-Your-Editing)

[GANSpace](#GANSpace)

[Unsupervised](#Unsupervised) 

[InterFaceGAN](#InterFaceGAN)

[GANalyze](#GANalyze)

[Factors of Variations](#Factors-of-Variations)

[GAN_Steerability](#GAN_Steerability)







---

<span id="GLO"></span>
[Optimizing the Latent Space of Generative Networks](https://arxiv.org/pdf/1707.05776.pdf)  
**[`ICML 2018`] (`Facebook`)**  
*Piotr Bojanowski, Armand Joulin, David Lopez-Paz, Arthur Szlam*

<details><summary>Click to expand</summary>

> **Summary**

> **Details**

compare the $\ell_2$ loss and the Laplacian pyramid Lap_1 loss, finally use a weighted combination of them.
$$
\operatorname{Lap}_{1}\left(x, x^{\prime}\right)=\sum_{j} 2^{2 j}\left|L^{j}(x)-L^{j}\left(x^{\prime}\right)\right|_{1}
$$
where $L^j(x)$ is the $j$-th level of the Laplacian pyramid representation of $x$. -[ref](Diffusion distance for histogram comparison)



</details>

---

### SeFa

[SeFa: Closed-Form Factorization of Latent Semantics in GANs]()

**[`CVPR 2021`]**



---

### Enjoy Your Editing

[Enjoy Your Editing: Controllable GANs for Image Editing via Latent Space Navigation](https://arxiv.org/pdf/2102.01187.pdf)

**[`ICLR 2021`]**

<details><summary>Click to expand</summary><p>



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

## GANSpace

[GANSpace: Discovering Interpretable GAN Controls](https://arxiv.org/abs/2004.02546)

**`[NeurIPS 2020]`**	**`(Adobe&NVIDIA)`**	**`[Erik Härkönen, Aaron Hertzmann]`**	**([:memo:]())**	**[[:octocat:](https://github.com/harskish/ganspace)]**

<details><summary>Click to expand</summary><p>


<div align=center><img width="700" src="https://raw.githubusercontent.com/yzy1996/Image-Hosting/master/20201121154059.png" /></div>

> **Keywords**

performs PCA on deep features at the early layers of the **generator** and finds directions in the latent space that best map to those deep PCA vectors, arriving at a set of nonorthogonal
directions in the latent space.

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



<span id="Unsupervised"></span>
[Unsupervised Discovery of Interpretable Directions in the GAN Latent Space](https://arxiv.org/pdf/2002.03754.pdf)  
*Andrey Voynov, Artem Babenko*
**[`ICML 2020`] (`Russia`)**  [[Code](https://github.com/anvoynov/GANLatentDiscovery)]

<details><summary>Click to expand</summary><p>



![A9Rlu0i5j_139dt6w_ea4](https://raw.githubusercontent.com/yzy1996/Image-Hosting/master/20201101155344.png)


Features: **unsupervised, background removal**

> **Framework**

via jointly learning **a set of directions** and a **model** to distinguish the corresponding image transformations



based on InfoGAN



有一个解耦开的矩阵 $A \in \mathbb{R}^{d \times K}$

一个网络R，用来判断是哪个解耦出来的分量

Self-supervised learning

![mylatex20201030_110850](https://raw.githubusercontent.com/yzy1996/Image-Hosting/master/20201030110908.svg)



</p></details>

---

## InterFaceGAN

[Interpreting the Latent Space of GANs for Semantic Face Editing](https://arxiv.org/abs/1907.10786)

**`[CVPR 2020]`**	**`(CUHK)`**	**`[Yujun Shen, Bolei Zhou]`**	**([:memo:]())**	**[[:octocat:](https://github.com/genforce/interfacegan)]**

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

## GANalyze

[GANalyze: Toward visual definitions of cognitive image properties](https://arxiv.org/abs/1906.10112)

**`[CVPR 2019]`**	**`(MIT)`**	**`[Lore Goetschalckx, Alex Andonian]`**	**([:memo:]())**	**[[:octocat:](https://github.com/LoreGoetschalckx/GANalyze)]**

<details><summary>Click to expand</summary><p>



<div align=center><img width="1000" src="https://raw.githubusercontent.com/yzy1996/Image-Hosting/master/20201119164859.png"/></div>

> **Formulation**

$$
\operatorname{argmin}_{\theta} \mathcal{L}(\theta)=\mathbb{E}_{\mathbf{z}, \mathbf{y}, \alpha}\left[\left(A\left(G\left(T_{\theta}(\mathbf{z}, \alpha), \mathbf{y}\right)\right)-(A(G(\mathbf{z}, \mathbf{y}))+\alpha)\right)^{2}\right]
$$

$$
T_{\theta}(\mathbf{z}, \alpha)=\mathbf{z}+\alpha \theta
$$

$G$: use the Generator of [BigGAN]() which is pretrained on ImageNet

$A$: use a CNN of [MemNet]() to assesses an image property of memorability

$T$: moves the input $\mathbf{z}$ along a certain direction $\theta$ 

learn to increase (or decrease) the memorability with a certain amount $\alpha$



</p></details>

---

## Factors of Variations

[Controlling generative models with continuous factors of variations](https://arxiv.org/abs/2001.10238)

**`[ICLR 2020]`**	**`(France)`**	**`[Antoine Plumerault, Hervé Le Borgne]`**	**([:memo:]())**	**[[:octocat:](https://github.com/AntoinePlumerault/Controlling-generative-models-with-continuous-factors-of-variations)]**

<details><summary>Click to expand</summary><p>



>**Framework**

for an original generation: $I = G(z_0)$

want a transformation: $I \rightarrow \mathcal{T}_{t}(I)$ (e.g. $\mathcal{T}$ is a rotation, then $t$ is the angle)

approximate $z_T$ by $G(z_T) \approx \mathcal{T}_{t}(I)$ -> [invert the generator]()

then estimate the direction encoding the factor of variation described by $\mathcal{T}$ with the difference between $z_0$ and $z_T$ 

**given $\mathcal{T}$ to get $z_T$** 

> **Difficulty**

- reconstruction error
  $$
  \hat{z}=\underset{z \in \mathcal{Z}}{\arg \min } \mathcal{L}(I, G(\boldsymbol{z}))
  $$
  choose the error of the MSE on images in the frequency domain

- recursive estimation of the trajectory

  decomposing the transformation

> **Dataset**

[dSprites]() and [ILSVRC]()

> **GAN model**

[BigGAN](): two vector input (a latent vector **z** and a one-hot vector **c** to generate conditional categories)



</p></details>

---

## GAN_Steerability

[On the "steerability" of generative adversarial networks](https://arxiv.org/abs/1907.07171)

**`[ICLR 2020]`**	**`(MIT)`**	**`[Ali Jahanian, Lucy Chai, Phillip Isola]`**	**([:memo:]())**	**[[:octocat:](https://ali-design.github.io/gan_steerability/)]**

<details><summary>Click to expand</summary><p>



<div align=center><img width="800" src="https://raw.githubusercontent.com/yzy1996/Image-Hosting/master/20201121120437.png"/></div>

> **Formulation**

$$
w^{*}=\underset{w}{\arg \min } \mathbb{E}_{z, \alpha}[\mathcal{L}(G(z+\alpha w), \operatorname{edit}(G(z), \alpha))]
$$

objective $\mathcal{L}$ could be [$L2$ loss]() or [LPIPS perceptual image similarity metric]()



> **Pipeline**

GAN model: BigGAN and StyleGAN




</p></details>

---

<span id="WarpedGANSpace"></span>
[WarpedGANSpace: Finding non-linear RBF paths in GAN latent space](https://arxiv.org/pdf/2109.13357.pdf)  
*Christos Tzelepis, Georgios Tzimiropoulos, Ioannis Patras*  
**[`ICCV 2021`] (`QMUL`)** [[Code](https://github.com/chi0tzp/WarpedGANSpace)]

<details><summary>Click to expand</summary><p>


<div align=center><img width="800" src="https://raw.githubusercontent.com/yzy1996/Image-Hosting/master/20211014111653.png"/></div>

> :dart:**Summary**

They learn non-linear warpings on the latent space. Each warping is parameterized by a set of RBF-based latent space warping functions.

Based on [Paper](Unsupervised Discovery of Interpretable Directions in the GAN Latent Space)

Lead to steeper, more disentangled and interpretable changes.



trained in an unsupervised manner and provide more complex generative factors.

> **:pushpin:Details**

They have K warping functions, the gradients of which define the directions of the paths at each latent code. This gradients is non-linear.



---

<span id="LowRankGAN"></span>
[Low-Rank Subspaces in GANs](https://arxiv.org/pdf/2106.04488.pdf)  
**[`NeurIPS 2021`] (`HKUST, Alibaba, USTC`)**  
*Jiapeng Zhu, Ruili Feng, Yujun Shen, Deli Zhao, Zhengjun Zha, Jingren Zhou, Qifeng Chen*


<div align=center><img width="700" src="https://raw.githubusercontent.com/yzy1996/Image-Hosting/master/20210911170730.png"/></div>

|      Name       |                 Symbol                  |
| :-------------: | :-------------------------------------: |
| the real image  | $\boldsymbol{x} \in \mathbb{R}^{d_{x}}$ |
| the latent code |  $\boldsymbol{z} \in \mathbb{R}^{d_z}$  |
|  the Generator  |               $G(\cdot)$                |



The Jacobian matrix $\boldsymbol{J}_z$ of the $G$ with respect to $\boldsymbol{z}$ is defined as $\left(\boldsymbol{J}_{z}\right)_{j, k}=\frac{\partial G(\boldsymbol{z})_{j}}{\partial z_{k}}$

$$
\boldsymbol{x} = G(\boldsymbol{z})
\\
\boldsymbol{x}^{edit} = G(\boldsymbol{z} + \alpha \boldsymbol{n})
\\
G(\boldsymbol{z} + \alpha \boldsymbol{n}) = G(\boldsymbol{z}) + \alpha \boldsymbol{J}_z \boldsymbol{n} + o(\alpha)
$$
the perturbation on the attribute direction only has effect on a specific region.



the low rank is $r_a$, the rest attribute vectors $d_z - r_a$





attribute matrix on region $\boldsymbol{A} = [\boldsymbol{a}_1, \boldsymbol{a}_2, \dots, \boldsymbol{a}_{d_z}]$, has $r_a$ attribute vectors can change the region, the rest $d_z - r_a$ attribute vectors has no effect on region A.

attribute matrix on region $\boldsymbol{B} = [\boldsymbol{b}_1, \boldsymbol{b}_2, \dots, \boldsymbol{b}_{d_z}]$, has $r_b$ attribute vectors can change the region, the rest $d_z - r_b$ attribute vectors has no effect on region B.



They project the specific attribute vector $v_i$ of region A into a space where the perturbation on the attribute direction has no effect on region B yet has an influence on region.



The null space 
