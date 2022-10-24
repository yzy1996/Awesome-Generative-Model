[TOC]

### GAN: Vanilla GAN

> NeurIPS 2014 
>
> 

---

### CGAN: Conditional GAN

> CoRR abs/1411.1784 2014

Conditional GAN [18, 26] extends the GAN by feeding the labels to both G and D to generate images conditioned on the label, which can be the class label, modality information, or even partial data for inpainting. It has been used to generate MNIST digits conditioned on the class label and to learn multi-modal models. In conditional GAN, D is trained to classify a real image with mismatched conditions to a fake class. In DR-GAN, D classifies a real image to the corresponding class based on the labels.



The conditional GAN[10] concatenates condition vector into the input of the generator and the discriminator. Variants of this method was successfully applied in [7, 11, 14]. [7] obtained visually discriminative vector representation of text descriptions and then concatenated that vector into every layer of the discriminator and the noise vector of the generator. [11] used a similar method to generate face images from binary attribute vectors such as hair styles, face shapes, etc. In [14], Structure-GAN generates surface normal maps and then they are concatenated into noise vector of Style-GAN to put styles in those maps.







---

### WGAN-GP: Improved Training of Wasserstein GANs

**[`2017`]** **[`NIPS`]** **[[:memo:]()]** **[[:octocat:](https://github.com/igul222/improved_wgan_training)]**

<details><summary>Click to expand</summary><p>


**The main work:**

> To solve the problem of classification which is vulnerable to adversarial perturbations: carefully crafted small perturbations can cause misclassification of legitimate images. I can archive it into the field of **Machine deception**. (small perturbations do not affect human recognition but machine classifier)
>
> I can summarize their work as follows: given a picture with deception, GAN is used to generate the picture without deception, and finally classifier is used to classify.
>
> They use the GD of reconstruction error ($ \|G(\mathbf{z})-\mathbf{x}\|_{2}^{2} $) to find optimal $ G(z) $ 

**The methods it used:** 

- [ ] Several ways of attack: Fast Gradient Sign Method (FGSM), Randomized Fast Gradient Sign Method (RAND+FGSM), The Carlini-Wagner (CW) attack
- [ ] Lebesgue-measure

**Its contribution:**

> They proposed a novel defense strategy utilizing GANs to enhance the
> robustness of classification models against black-box and white-box adversarial attacks

**My Comments:**

> This work can be referred to using AE (Auto Encoder) for noise reduction. It’s just an easy application of GANs.
>

</p></details>

---





---

InfoGAN





---





**[`CG-GAN: An Interactive Evolutionary GAN-based Approach for Facial Composite Generation`]**

**[`2020`]** **[`AAAI`]** 

<details><summary>Click to expand</summary><p>


**The main work:**

> Facial Composite is to synthesize two target pictures into one pictures 

**The methods it used:** 

> - [ ] using **pg-GAN** to create high-resolution human faces
> - [x] using Latent Variable Evolution (**LVE**) to guide the search through a process of interactive evolution 

**Its contribution:**

> It extends LVE with the ability to freeze certain features discovered during the search, and enables a more controlled user-recreation of target images.

**My Comments:**

> It’s a new 

</p></details>

---

**[`$R^2GAN$ Recipe Retrieval Generative Adversarial Network`]**

**[`2019`]** **[`CVPR`]**

<details><summary>Click to expand</summary><p>


**The main work:**

> Aim at exploring the feasibility of generating image from procedure text for retrieval problem. The specific content of the text is food recipe

It belongs to **NLP**, to solve a problem of information retrieval

The simplest way is linear scan

index the document-boolean retrieval model 

**The methods it used:** 

This paper studies food-to-recipe and recipe-to-food retrieval

>They specially use a GAN with one generator and dual discriminators

two-level ranking loss



**My Comments:**

> It’s a new 

</p></details>

---

**[`Self-Attention Generative Adversarial Networks`]**

**[`2019`]** **[`PMLR`]** **[[:octocat:](https://github.com/heykeetae/Self-Attention-GAN)]**

<details><summary>Click to expand</summary><p>


**The main work:**

> It firstly introduced **Attention** into GAN, mainly apply on high-resolution detail generation.
>
> [ref_blog](https://zhuanlan.zhihu.com/p/55741364)



**The methods it used:** 

![img](https://media.arxiv-vanity.com/render-output/2954637/fig/framework.png)



**My Comments:**

> It’s a new 

</p></details>



$$
\begin{aligned}
{\omega}_{k+1}^{i}
&={\omega}_{k}-\alpha \bar{\nabla} f_{i}\left({\omega}_{k}, D_{i n}^{i}\right)\qquad (4)\\
&={\omega}_{k}-\beta_{k} \frac{1}{B} \sum_{i \in B_{k}}\left(I-\alpha \tilde{\nabla}^{2} f_{i}\left({\omega}_{k}, \mathcal{D}_{h}^{i}\right)\right) \tilde{\nabla} f_{i}\left({\omega}_{k+1}^{i}, \mathcal{D}_{o}^{i}\right)\qquad (5)
\end{aligned}
$$

### AC-GAN(2017)

**[`2017`]** **[`ICLR`]** **[[:memo:](./Defense-GAN.pdf)]** **[[:octocat:](https://github.com/kabkabm/defensegan)]**

<details><summary>Click to expand</summary><p>


**The main work:**

> 

**The methods it used:** 

- [ ] 

**Its contribution:**

> They proposed a novel defense strategy utilizing GANs to enhance the
> robustness of classification models against black-box and white-box adversarial attacks

**My Comments:**

> 
>

</p></details>

---



### SRGAN

Photo-Realistic Single Image Super-Resolution Using a Generative Adversarial Network

[CVPR 2017]

[[:octocat:](https://github.com/JustinhoCHN/SRGAN_Wasserstein)]

---

### PGGAN

[[:octocat:](https://github.com/ptrblck/prog_gans_pytorch_inference)] [[:octocat:](https://github.com/nashory/pggan-pytorch)]



## BigGAN

[Large Scale GAN Training for High Fidelity Natural Image Synthesis](https://arxiv.org/abs/1809.11096)

**`[ICLR 2019]`**  **`(DeepMind)`**

<details><summary>Click to expand</summary><p>


**Main method**

the intermediate layers take the latent vector as input:
$$
\mathbf{y}_{i}=G_{i}\left(\mathbf{y}_{i-1}, \mathbf{z}\right)
$$
which is called Skip-z inputs



Skip-z inputs

</p></details>







<span id="StyleGAN"></span>
[A Style-Based Generator Architecture for Generative Adversarial Networks]()  
*Tero Karras, Samuli Laine*  
**[`CVPR 2019`]  (NVIDIA)**	[[:octocat:](https://github.com/NVlabs/stylegan)]

<details><summary>Click to expand</summary><p>


![image-20201031134802945](https://raw.githubusercontent.com/yzy1996/Image-Hosting/master/20201031134812.png)

**need to know**:

- [ ] (AdaIN) adaptive instance normalization operation after each convolution layer

**summary**:

do not provide input layer with a latent code $z$, start from a learned constant and map $z$ to a intermediate latent space $w$, donated by $f: \mathcal{Z} \rightarrow \mathcal{W}$, where $f$ is an MLP.

> The intermediate latent space is much less entangled than the input latent space.

</p></details>

---



<span id="StyleGAN2"></span>
[Analyzing and Improving the Image Quality of StyleGAN](https://arxiv.org/abs/1912.04958)  
*Tero Karras, Samuli Laine*  
**[`CVPR 2020`]  (NVIDIA)**  [[:octocat:](https://github.com/NVlabs/stylegan2)]

<details><summary>Click to expand</summary><p>


**Projection method**

Given a target image $x$, seek to find the corresponding $w \in \mathcal{W}$ and per-layer noise maps.

1. compute $\mu_{\mathrm{w}}=\mathbb{E}_{\mathrm{z}} f(\mathrm{z})$ by running 10000 random $z$ 
2. computing $\sigma_{\mathrm{w}}^{2}=\mathbb{E}_{\mathrm{z}}\left\|f(\mathrm{z})-\mu_{\mathrm{w}}\right\|_{2}^{2}$ 
3. begin optimize with $\mathrm{w} = \mu_{\mathrm{w}}$ and $n_i = \mathcal{N}(0, \mathrm{I})$ 
4. $L_{image} = D_{LPIPS}[x, g(\tilde{\mathrm{w}}, n_0, n_1, \dots)]$

</p></details>

---





InfoGAN

Promote disentanglement by explicitly maximizing the mutual information between a subset of latent variables and the generated images.



<span id="EigenGAN"></span>
[EigenGAN: Layer-Wise Eigen-Learning for GANs](https://arxiv.org/pdf/2104.12476.pdf)  
*Zhenliang He, Meina Kan, Shiguang Shan*  
**[`ICCV 2021`]**

![image-20220301170824876](https://raw.githubusercontent.com/yzy1996/Image-Hosting/master/image-20220301170824876.png)

对每层网络有： $\begin{aligned} \phi_{i} &=\mathbf{U}_{i} \mathbf{L}_{i} \mathbf{Z}_{i}+\mu_{i} \\ &=\sum_{j=1}^{q} z_{i j} l_{i j} \mathbf{u}_{i j}+\mu_{i} \end{aligned}$， $\mathbf{h}_{i+1}=\operatorname{Conv} 2 \mathrm{x}\left(\mathbf{h}_{i}+f\left(\phi_{i}\right)\right)$

> 其中 $\mathbf{U}_{i}=\left[\mathbf{u}_{i 1}, \ldots, \mathbf{u}_{i q}\right], \mathbf{u}_{i j} \in \mathbb{R}^{H_{i} \times W_{i} \times C_i}$ 是正交基底； $\mathbf{L}_{i}=\operatorname{diag}\left(l_{i 1}, \ldots, l_{i q}\right)$是正交基的权重；$\mathbf{z}_i \in \mathbb{R}^q$ 是潜在变量，正态分布；$\mu_i$是子空间的原点；上图起点处的$\epsilon$是除开子空间但对结果依旧有作用的剩下潜在变量。

正交约束有：$\left\|\mathbf{U}_{i}^{\mathrm{T}} \mathbf{U}_{i}-\mathbf{I}\right\|_{F}^{2}$

EigenGAN有两种潜在变量，$\mathbf{z}$和$\epsilon$，实验发现两者都可以具备表示一些特征，前者捕捉到一些更重要的信息，后者可以捕捉到一些基本subtle的信息。

