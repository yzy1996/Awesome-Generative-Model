# Major pitfalls in GANs

GAN虽然效果好，但难训练一直是困扰学者的问题 

While GAN can be powerful for building generators, they have some major pitfalls.

主要就是三个问题



### 1. Unstable Convergence

训练不稳定，理论上决定的，对抗性的平衡很难达到

unstable equilibrium point rather than an equilibrium



### 2. Gradient Vanishing

梯度消失，通常发生在训练初始阶段，因为一开始D很自信，会判断真样本为1，假样本为0，因此梯度会饱和，处于一段平坦的状态，无法提供足够的梯度来更新G，flat region can only provide small, vanishing gradients.

这一点通过设计损失函数已经得到了解决。



### 3. Mode Collapse

模式崩塌，也就是生成样本的多样性不足，

因为如果所有的z都映射到一个$\hat{x}$，而这个假样本恰好能欺骗D，那么G就一直这样了，不想再努力了，

 local minima

解决办法是惩罚G生成同样的结果



很多个高斯分布，可能从一个高斯跳到了另一个高斯





有关文献的整理笔记，详见：





## Introduction

> What does the problem look like?

**Mode collapse** (local equilibria) on $Generator$



> Why it's a problem? 

GAN need to find a Nash equilibrium of a non-convex game in a continuous and high dimensional parameter space. It's not tractable. 

As $Discriminator$ is more likely to be overfitting on the datasets, thus unable to provide meaningful gradients to train $Generator$.



> Which direction should we analyze?

We often use a divergence between real and generated distribution to measure the performance of GAN, and we hope to minimize this distance.



There are some approaches to improve:

- **Objectives** (details see [**]())
  
  - WGAN, Geometric gan, LSGAN
  
- **Normalization**
  
  - **Spectral normalization** (weight matrices in the discriminator are divided by an approximation of their largest singular value) 另一种让函数满足 1-Lipschitz continuity 的方式
- **Regularization** (mainly on gradients)
  
  - **Wasserstein** (penalize the gradient norm of straight lines between real data and generated data)
  
  - [^Roth2017] (directly regularize the squared gradient norm for both the training data and the generated data.) 
  
  - **[DRAGAN](#DRAGAN)** (penalize the gradients at Gaussian perturbations of training data) 
  
  - Consistency regularization ()
  
    > pros & cons: simple to implement, not particularly computationally burdensome, and relatively insensitive to hyper-parameters

regularization evolves non-trivial computational overheads

- **Self-Supervision on $D$**
  
  > about self-supervised learning, please see [*]()
  >
  > In GANs, we first use a deformation function to deform real/fake samples and then use an auxiliary classifier to distinguish the 





Q1. Will simultaneous regularization and normalization improve GANs performance?

> Won't. Both regularization and normalization are motivated by controlling Lipschitz constant of the discriminator
>
> --- A large-scale study on regularization and normalization in GANs





2017 On Convergence and Stability of GANs

2018 Which training methods for GANs do actually converge





## Literature

[CR-GAN](#CR-GAN)

[ICR-GAN](#ICR-GAN)



[SSGAN](#SSGAN)

---

### ICR-GAN

[Improved Consistency Regularization for GANs](https://arxiv.org/pdf/2002.04724.pdf)

**`[AAAI 2020]`**	**`(Google)`**	**`[Zhengli Zhao, Han Zhang]`**	**([:memo:]())**	**[[:octocat:](https://github.com/google/compare_gan)]**

<details><summary>Click to expand</summary><p>


![image-20201219215131885](https://raw.githubusercontent.com/yzy1996/Image-Hosting/master/20201219215132.png)

> **Summary**

They improve [CR-GAN](#CR-GAN) in two ways (apply forms of consistency regularization to the generated images, the latent vector space, and the generator):

- Balanced Consistency Regularization, in which generator samples are also augmented along with training data.
- Latent Consistency Regularization, in which draws from the prior are perturbed, and the sensitivity to those perturbations is discouraged and encouraged for the discriminator and the generator, respectively.

> **Details**

balanced consistency regularization (bCR)

</p></details>

---




### CR-GAN

[Consistency regularization for generative adversarial networks](https://arxiv.org/pdf/1910.12027.pdf)

**`[ICLR 2020]`**	**`(Google)`**	**`[Han Zhang, Honglak Lee]`**	**([Code]())**

<details><summary>Click to expand</summary><p>


> **Summary**

They propose a training stabilizer based on **consistency regularization**. In particular, they **augment data** passing into the GAN discriminator and **penalize the sensitivity** of the discriminator to these augmentations.

**Consistency regularization** is widely used in semi-supervised learning to ensure that the classifier output remains unaffected for an unlabeled example even it is augmented in semantic-preserving ways.

The pipeline is to first augment images with semantic-preserving augmentations before they are fed into the discriminator and penalize the sensitivity of the discriminator to these augmentations.

> **Details**

$T(x)$ donates a stochastic data augmentation function. $D(x)$ donates the last layer before the activation function. The proposed regularization is given by
$$
\min_{D} L_{c r} = \min_{D} \|D(x)-D(T(x))\|^{2}
$$
The overall consistency regularized GAN (CR-GAN) objective is written as
$$
L_{D}^{c r}=L_{D}+\lambda L_{c r}, \quad L_{G}^{c r}=L_{G}.
$$

> **Augmentation type**

1 Gaussian Noise; 2 **Random shift & flip**; 3 Cutout; 4 Random shift & flip with cutout

The experiment shows that No.2 performs best.



</p></details>

---

[A large-scale study on regularization and normalization in GANs](https://arxiv.org/pdf/1807.04720.pdf)

**`[ICML 2019]`**	**`(Google)`**	**`[Karol Kurach, Sylvain Gelly]`**	**([:memo:]())**	**[[:octocat:](https://github.com/google/compare_gan)]**

<details><summary>Click to expand</summary><p>


**Summary**

> 

</p></details>

---

### DRAGAN

[On Convergence and Stability of GANs](https://arxiv.org/pdf/1705.07215.pdf)

**`[None 2017]`**	**`(Gatech)`**	**`[Naveen Kodali, James Hays]`**	**([:memo:]())**	**[[:octocat:](https://github.com/kodalinaveen3/DRAGAN)]**

<details><summary>Click to expand</summary><p>


> **Summary**

They find local equilibria often exhibit sharp gradients of the discriminator function around some real data points. So they use a gradient penalty scheme called **DRAGAN** (Deep Regret Analytic Generative Adversarial
Networks) to avoid.

faster training, improved stability, fewer mode collapses, better model performance



> **Details**

$$
\lambda \cdot \mathbb{E}_{x \sim P_{\text {real }}, \delta \sim N_{d}(0, c I)}\left[\left\|\nabla_{\mathbf{x}} D_{\theta}(x+\delta)\right\|-k\right]^{2}
$$

</p></details>

---







<span id="SSGAN"></span>[Self-supervised GAN: Analysis and Improvement with Multi-class Minimax Game](https://arxiv.org/pdf/1911.06997.pdf)  
**[`NeurIPS 2019`]** **(`SUTD`)** [[:octocat:](https://github.com/tntrung/msgan)] (*Ngoc-Trung Tran, Viet-Hung Tran, Ngoc-Bao Nguyen, Linxiao Yang, Ngai-Man Cheung*)

<details><summary>Click to expand</summary><p>


> **Summary**

self-supervised learning need a transformation $\mathcal{T}$







Which training methods for gans do actually converge?



[^Roth2017]: Stabilizing training of generative adversarial networks through regularization



推荐阅读：

https://blog.csdn.net/w55100/article/details/88091704

https://atcold.github.io/pytorch-Deep-Learning/en/week09/09-3/