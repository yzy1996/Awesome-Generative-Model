# Principle of GANs


About  Generative Adversarial Network (GAN), GANs (GAN and its variants)

</div>



train a discriminator to distinguish real samples in the training dataset from fake samples synthesized by the generator. the generator aims to deceive the discriminator by producing ever more realistic samples. The training procedure continues until the generator wins the adversarial game; that is, the discriminator cannot make a better decision than randomly guessing whether a particular sample is fake or real.



GANs perform a challenging generative process, which projects a standard distribution to
a much more complex high-dimensional real-world data distribution



Dataset: CelebA, LSUN, and ImageNet



mode collapse problem: 最早论文定义的，我的定义

the generator can only learn some limited patterns from the large-scale target datasets, or assigns all of its probability mass to a small region in the space [1](https://arxiv.org/pdf/1703.00573.pdf)



vanishing gradient problem 

if the generated distribution and the target data distribution do not substantially overlap (usually at the beginning of training), the generator gradients

When the discriminator rejects generated samples with high confidence

eliminate vanishing gradient



measure the distance between the generated distribution and the target data distribution：

Jensen–Shannon divergence (JSD)

least squares

absolute deviation

Kullback–Leibler divergence (KLD) : KL divergence largely eliminates the vanishing gradient
issue, it easily results in mode collapse

Wasserstein distance: Wasserstein distance greatly improves training stability but can
have nonconvergent limit cycles near equilibrium



each distance has its own pros and cons



## 待： 关于衡量的距离

vanilla GAN

## Learning path

The original paper [Generative Adversarial Networks](https://arxiv.org/abs/1406.2661) 2014 Lan Goodfellow

存在着训练困难、生成器和判别器的loss无法只是训练进程、生成样本缺乏多样性等问题



CNN + GAN = DCGAN，依靠的是对判别器和生成器的构架进行实验枚举，最终找到一组比较好的网络架构设置。

[DCGAN paper](https://arxiv.org/abs/1511.06434)

[DCGAN-tensorflow code](https://github.com/carpedm20/DCGAN-tensorflow)



[GAN学习指南：从原理入门到制作生成Demo](https://zhuanlan.zhihu.com/p/24767059)



Wasserstein GAN（WGAN）

- 彻底解决GAN训练不稳定的问题，不再需要小心平衡生成器和判别器的训练程度
- 基本解决了collapse mode的问题，确保了生成样本的多样性
- 训练过程中终于有一个像交叉熵、准确率这样的数值来指示训练的进程，这个数值越小代表GAN训练得越好，代表生成器产生的图像质量越高（如题图所示）
- 以上一切好处不需要精心设计的网络架构，最简单的多层全连接网络就可以做到

[paper](https://arxiv.org/abs/1701.07875)

[code](https://github.com/martinarjovsky/WassersteinGAN)

?? What is Wasserstein. 

[Read-through: Wasserstein GAN](https://www.alexirpan.com/2017/02/22/wasserstein-gan.html)

[想要算一算Wasserstein距离？这里有一份PyTorch实战](https://www.jiqizhixin.com/articles/19031102)



GAN的本质其实是优化真实样本分布和生成样本分布之间的差异，并最小化这个差异。特别需要指出的是，优化的目标函数是两个分布上的Jensen-Shannon距离，但这个距离有这样一个问题，如果两个分布的样本空间并不完全重合，这个距离是无法定义的。

作者接着证明了“真实分布与生成分布的样本空间并不完全重合”是一个极大概率事件，并证明在一些假设条件下，可以从理论层面推导出一些实际中遇到的现象。

既然知道了问题的关键所在，那么应该如何解决问题呢？该文章提出了一种解决方案：使用Wasserstein距离代替Jensen-Shannon距离。并依据Wasserstein距离设计了相应的算法，即WGAN。新的算法与原始GAN相比，参数更加不敏感，训练过程更加平滑。



### Application in picture-DCGAN

DCGAN采用一个随机噪声向量作为输入，如高斯噪声。输入通过与CNN类似但是相反的结构，将输入放大成二维数据。通过采用这种结构的生成模型和CNN结构的判别模型，DCGAN在图片生成上可以达到相当可观的效果。如下是一些生成的案例照片。



GAN最开始是设计用于生成连续数据





Since GANs invention, it has yield impressive results, especially for image generation.

Recent work can synthesize random high-resolution portraits that are often indistinguishable from real faces.



Generative models aim to approximate samples from a complex high-dimensional target distribution $\mathbb{P}$. 

The adversarial mechanism reflects by a generator and a discriminator who compete against each other. Unlike other deep neural network models trained with a loss function until convergence, GAN train these two together to maintain a equilibrium finally.

The generator learns to map from a low-dimension space $\mathcal{Z}$ to a high-dimension space $\mathcal{X}$ with a model distribution $\mathbb{Q}$.

The discriminator learns to accurately distinguish between the synthesized data $\mathbf{Y}$ coming from $\mathbb{Q}$ and the real data $\mathbf{X}$ from $\mathbb{P}$. 



## Training Instability + Convergence

Please see [file](Training Instability + Convergence)











## Distance metrics

> This topic studies the distance between target distribution $P_x$ and model distribution $P_z(G)$ 



$z$ is a distribution and $x$ is a distribution and $x^{\prime}$ is also a distribution



 high-dimensional 



integral probability metrics (IPMs)

> a “well behaved” function with large amplitude where $P_x$ and$P_z$ differ most

- Wasserstein IPMs



Maximum Mean Discrepancies (MMDs)

> the critic function is a member of a reproducing kernel Hilbert space



[On gradient regularizers for MMD GANs](https://arxiv.org/pdf/1805.11565.pdf)

**`[NeurIPS 2018]`**	**`(UCL)`**	**`[Michael Arbel, Arthur Gretton]`**	**([:memo:]())**	**[[:octocat:]()]**

<details><summary>Click to expand</summary><p>



</p></details>

---





GAN的遗忘性，真样本的作用可以看作是一种防止遗忘的效果，



### GAN Theory

- [Energy-based generative adversarial network] [[Paper\]](https://arxiv.org/pdf/1609.03126v2.pdf)[[Code\]](https://github.com/buriburisuri/ebgan)(Lecun paper)
- [Improved Techniques for Training GANs] [[Paper\]](https://arxiv.org/abs/1606.03498)[[Code\]](https://github.com/openai/improved-gan)(Goodfellow’s paper)
- [Mode Regularized Generative Adversarial Networks] [[Paper\]](https://openreview.net/pdf?id=HJKkY35le)(Yoshua Bengio , ICLR 2017)
- [Improving Generative Adversarial Networks with Denoising Feature Matching] [[Paper\]](https://openreview.net/pdf?id=S1X7nhsxl)[[Code\]](https://github.com/hvy/chainer-gan-denoising-feature-matching)(Yoshua Bengio , ICLR 2017)
- [Sampling Generative Networks] [[Paper\]](https://arxiv.org/abs/1609.04468)[[Code\]](https://github.com/dribnet/plat)
- [How to train Gans] [[Docu\]](https://github.com/soumith/ganhacks#authors)
- [Towards Principled Methods for Training Generative Adversarial Networks] [[Paper\]](https://openreview.net/forum?id=Hk4_qw5xe)(ICLR 2017)
- [Unrolled Generative Adversarial Networks] [[Paper\]](https://arxiv.org/abs/1611.02163)[[Code\]](https://github.com/poolio/unrolled_gan)(ICLR 2017)
- [Least Squares Generative Adversarial Networks] [[Paper\]](https://arxiv.org/abs/1611.04076)[[Code\]](https://github.com/pfnet-research/chainer-LSGAN)(ICCV 2017)
- [Wasserstein GAN] [[Paper\]](https://arxiv.org/abs/1701.07875)[[Code\]](https://github.com/martinarjovsky/WassersteinGAN)
- [Improved Training of Wasserstein GANs] [[Paper\]](https://arxiv.org/abs/1704.00028)[[Code\]](https://github.com/igul222/improved_wgan_training)(The improve of wgan)
- [Towards Principled Methods for Training Generative Adversarial Networks] [[Paper\]](https://arxiv.org/abs/1701.04862)
- [Generalization and Equilibrium in Generative Adversarial Nets] [[Paper\]](https://arxiv.org/abs/1703.00573)（ICML 2017）
- 
