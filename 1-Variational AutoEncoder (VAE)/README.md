# Variational Auto-Encoder (VAE)

学习资料

https://jaan.io/what-is-variational-autoencoder-vae-tutorial/



The goal of VAEs is to train a genrative model in the form of $p(x, z) = p(z) p(x|z)$ where $p(z)$ is a prior distribution over latent variables $z$ and $p(x|z)$ is the likelihood function or decoder that generates data $x$ given latent variables $z$. 

Since the true posterior $p(z|x)$ is in general intractable, the generative model is trained with the aid of an approximate posterior distribution or encoder $q(z|x)$.



[Wasserstein Auto-Encoders](https://arxiv.org/pdf/1711.01558.pdf)  
*Ilya Tolstikhin, Olivier Bousquet, Sylvain Gelly, Bernhard Schoelkopf*  
**[`ICLR 2018`] (`MPI, Google`)**



[Learning Representations and Generative Models for 3D Point Clouds](https://arxiv.org/pdf/1707.02392.pdf)  
*Panos Achlioptas, Olga Diamanti, Ioannis Mitliagkas, Leonidas Guibas*  
**[`ICML 2018`] (`Stanford`)**





## Hierarchical VAEs

> to increase the expressiveness

the latent variables are partitioned into disjoint groups $z = \{ z_1, z_2, \dots, z_L\}$, where $L$ is the number of groups. Then the prior is represented by $p(z) = \prod_{l} p\left(z_{l} \mid z_{<l}\right)$.



有一个mean和一个log_var



当目标分布是 $\mathcal{N}(0,1^2)$ 时，mean=0, log_var=0

当目标分布是 $\mathcal{N}(0,0.01^2)$ 时，mean=0, log_var=-9

而当mean和log_var也是分布的时候，比如初始化都是 $\mathcal{N}(0, 1^2)$

就应该分别变化到，$\mathcal{N}(0, 0.01^2)$ $\mathcal{N}(-9, 0.01^2)$ 波动小比较好





[NVAE: A Deep Hierarchical Variational Autoencoder](https://arxiv.org/pdf/2007.03898.pdf)  
*Arash Vahdat, Jan Kautz*  
**[`NeurIPS 2020`] (`NVIDIA`)**





VQ-VAE

[Neural Discrete Representation Learning]()  
*Aaron van den Oord, Oriol Vinyals, Koray Kavukcuoglu*  
**[`NeurIPS 2017`] (`DeepMind`)**



VAE可以理解为通过网络学习出每个属性正太分布的mean和std编码，然后通过mean和std和N ( 0,1 )正态分布恢复每个属性的正态分布，最后随机采样得到每个属性的离散值。VAE相对于AutoEncoder的好处是，当采样输入不同时，VAE对于任意采样都能重构出鲁棒的图片。VAE的生成过程是可控的，对输入噪声不敏感，我们可以预先知道每个属性都是服从正态分布的。

VQVAE通过Encoder学习出中间编码，然后通过最邻近搜索将中间编码映射为codebook中K个向量之一，然后通过Decoder对latent code进行重建。另外由于最邻近搜索使用argmax来找codebook中的索引位置，导致不可导问题，VQVAE通过stop gradient操作来避免最邻近搜索的不可导问题，也就是通过stop gradient操作，将decoder输入的梯度复制到encoder的输出上。



什么是 Vector Quantization

计算机智能处理离散的数字信号，所以在将模拟信号转换为数字信号时，可以用区间内的某一个值去代替一个区间，比如：[0, 1]上的值全变为0，[1,2]上的值全变为1。这样VQ就将一个向量空间中的点用其中一个有限子集来进行编码的过程。

【这样其实实现的是一种压缩的效果】

