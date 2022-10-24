### Autoencoder (AE) & Autodecoder (AD)

reduces data dimensions by learning how to ignore the noise in the data

目前自编码器的应用主要有两个方面，第一是数据去噪，第二是为进行可视化而降维。配合适当的维度和稀疏约束，自编码器可以学习到比PCA等技术更有意思的数据投影。

对于2D的数据可视化，[t-SNE](https://en.wikipedia.org/wiki/T-distributed_stochastic_neighbor_embedding)（读作tee-snee）或许是目前最好的算法，但通常还是需要原数据的维度相对低一些。所以，可视化高维数据的一个好办法是首先使用自编码器将维度降低到较低的水平（如32维），然后再使用t-SNE将其投影在2D平面上

自编码器并不是一个真正的无监督学习的算法，而是一个自监督的算法。自监督学习是监督学习的一个实例，其标签产生自输入数据。

![img](https://miro.medium.com/max/700/1*P7aFcjaMGLwzTvjW3sD-5Q.jpeg)

find the function that maps $x$ to $x$, Mathematically,





自编码结构通常作假设：潜在空间应该是具有匹配对应先验的概率分布的；而现有的SOTA的GAN（比如StyleGAN）表明中间的潜在空间，它与直接输入距离得足够远，往往可以（学习）到更好的解耦属性；



[toc]



## Introduction

一些概述性的话，



[Optimizing the Latent Space of Generative Networks 2018]()

文中提到了在训练GAN的时候，同时优化 $G$ 的参数以及每张图片的潜在变量 $z_i$ 。

> we jointly learn the parameters $\theta$ in $\Theta$ of a generator $g_{\theta}$ and the optimal noise vector $z_i$ for each image $x_i$, by solving: ($\ell$ is a loss function)
> $$
> \min _{\theta \in \Theta} \frac{1}{N} \sum_{i=1}^N\left[\min _{z_{i} \in \mathcal{Z}} \ell\left(g_{\theta}\left(z_{i}\right), x_{i}\right)\right]
> $$

Autoencoder 是用一个参数化的模型 $f:\mathcal{X} \mapsto \mathcal{Z}$，然后最小化重建loss $\ell(g(f(x)),x)$。而上述过程是无参数的，不仅可以包含AE能找到的所有解的，也可以找到更新的解。

文中命名上，称为“encoder-less autoencoder” 或者 “discriminator-less GAN”









首先分别介绍两者结构，以下将用AE和AD分别指代全称

## AutoEncoder

Autoencoder represent an effective approach for computing the underlying factors characterizing datasets of different types.

autoencoder can be seen as an unsupervised learning method to reveal/expose the underlying factors controlling a given dataset.



![AutoEncoder](https://raw.githubusercontent.com/yzy1996/Image-Hosting/master/20210329100645.svg)



论文：

Reducing the Dimensionality of Data with Neural Networks *Hinton et al*.



训练过程是：

推断过程是：

采样过程？是随机像GAN那样采样还是从已经训练过的数据得到的z里面去组合采样



任务目标：

- 降维 dimension reduction

这个其实很好理解，中间的 bottleneck 隐变量 就是去掉了不重要的，留下最重要的表征，有点像PCA或者MF (Matrix Factorization)。

- 生成

## AutoDecoder

![AutoDecoder](https://raw.githubusercontent.com/yzy1996/Image-Hosting/master/20210329100810.svg)

训练过程是：

推断过程是：



## 优劣比较

AE是欠拟合的



- AD可以做到增量学习

知识库可以做到更新，训练数据不固定



> 思考？我们人的认知过程是AE还是AD呢？



黑夜中看到一个物体的棱角，我们是不会去想办法表征的，而是会去猜测，然后一步步走进加强（改进）这个猜测，而这里能够改变的就是z，而不是Decoder







## VAE 

> Variational Auto-Encoder，来自论文 
> 
> [Auto-Encoding Variational Bayes](https://arxiv.org/pdf/1312.6114.pdf)  
> *Diederik P Kingma, Max Welling*  
> **[`ICLR 2014`] (`Universiteit van Amsterdam`)**

首先我们有一批数据样本 $\mathbf{x}= \{x_1, x_2, \dots, x_n\}$，现要估计它的分布 $p(x)$。

我们要得到的结果是 $p_\theta (x|z)$ 然后都在讲 怎么推断 后验分布 p(z|x)

我们想借助隐变量 $z$ 来描述 $\mathbf{x}$ 的分布，建模成：
$$
q(x)=\int q(x, z) d z, \quad q(x, z)=q(x \mid z) q(z)
$$
$x$ 和 $z$ 的联合分布还可以写成 $p(x,z) = p(z|x) p(x)$。因此我们想用 $q(x,z)$ 来近似 $p(x,z)$。因此直接用KL散度来衡量（KL散度越小越好）：
$$
\begin{aligned}
K L(p(x, z) \| q(x, z)) &=
\iint p(x,z) \ln \frac{p(x,z)}{q(x,z)} dzdx\\
&=\int p(x)\left[\int p(z \mid x) \ln \frac{p(x) p(z \mid x)}{q(x, z)} d z\right] d x \\
&=\mathbb{E}_{x \sim p(x)}\left[\int p(z \mid x) \ln \frac{p(x) p(z \mid x)}{q(x, z)} d z\right]\\
&=\mathbb{E}_{x \sim p(x)}\left[\int p(z \mid x) \left(\ln p(x) + \ln \frac{p(z \mid x)}{q(x,z)} \right)dz\right]\\
&=\mathbb{E}_{x \sim p(x)}\left[\int p(z \mid x) \ln p(x) dz\right] + \mathbb{E}_{x \sim p(x)}\left[\int p(z \mid x)\ln \frac{p(z \mid x)}{q(x,z)} dz\right]\\
&=\mathbb{E}_{x \sim p(x)}\left[\ln p(x) \int p(z \mid x) dz\right] + \mathbb{E}_{x \sim p(x)}\left[\int p(z \mid x)\ln \frac{p(z \mid x)}{q(x,z)} dz\right]\\
&=\mathbb{E}_{x \sim p(x)}\left[\ln p(x) \right] + \mathbb{E}_{x \sim p(x)}\left[\int p(z \mid x)\ln \frac{p(z \mid x)}{q(x,z)} dz\right]\\
\end{aligned}
$$
注意第一项可以看成是一个常数。因此我们可以将求KL散度的问题转化为一个新的损失函数为：
$$
\begin{aligned}
\mathcal{L} 
&= \mathbb{E}_{x \sim p(x)}\left[\int p(z \mid x)\ln \frac{p(z \mid x)}{q(x,z)} dz\right]\\
&= \mathbb{E}_{x \sim p(x)}\left[\int p(z \mid x)\ln \frac{p(z \mid x)}{q(x \mid z)q(z)} dz\right]\\
&= \mathbb{E}_{x \sim p(x)}\left[-\int p(z \mid x)\ln q(x \mid z)dz + \int p(z \mid x) \ln \frac{p(z \mid x)}{q(z)} dz\right]\\
&= \mathbb{E}_{x \sim p(x)}\left[\mathbb{E}_{z \sim p(z \mid x)}[-\ln q(x \mid z)]+KL\left(p(z \mid x) \| q(z)\right)\right]
\end{aligned}
$$
最终目的就是优化 $q(x \mid z), q(z)$ 让 $\mathcal{L}$ 最小。



（先休息一下）



现在我们有 $q(z), q(x|z), p(z|x)$ 是未知的，因此实验中我们要确定他们的形式。

- $q(z)$：我们直接假设 $z \sim N(0, I)$
- $p(z|x)$：也假设是正态分布，均值和方差是可学习的参数。
- $q(x|z)$： 也假设是正态分布，均值和方差是可学习的参数。



因为要计算 $\mathbb{E}_{z \sim p(z \mid x)}[-\ln q(x \mid z)]$，就需要对 $z \sim p(z|x)$ 进行采样，VAE论文说只需要每次采样一个就够了，每个循环都是随机的，因此采样是足够充分的。所以最终 $\mathcal{L}$ 变成了：
$$
\mathcal{L}=\mathbb{E}_{x \sim p(x)}[-\ln q(x \mid z)+K L(p(z \mid x) \| q(z))], \quad z \sim p(z \mid x)
$$
MSE, 


$$
\begin{gathered}
D_{K L}(q(Z \mid X) \| p(Z \mid X))=\mathbb{E}[\log (q(Z \mid X))-\log (p(Z \mid X))] \\
=\mathbb{E}\left[\log (q(Z \mid X))-\log \left(\frac{p(X \mid Z) p(Z)}{p(X)}\right)\right] \\
=\mathbb{E}[\log (q(Z \mid X))-\log (p(X \mid Z)-\log (p(Z)))]+\log (p(X)) \\
=\mathbb{E}\left[\log \left(\frac{q(Z \mid X)}{p(Z)}\right)-\log (p(X \mid Z))\right]+\log (p(X)) \\
=D_{K L}[q(Z \mid X)|| p(Z)]-\mathbb{E}[\log (p(X \mid Z))]+\log (p(X))
\end{gathered}
$$
等号右边第一项不就是似然值吗？第二项只要实现把先验概率 ![[公式]](https://www.zhihu.com/equation?tex=p%28Z%29) 定义好之后，也可以进行计算。



因为 $p(x|z)$ 形如 decoder，而 $q(z|x)$ 形如 Encoder，因此得名 VAE。和 Auto-Encoder 并没有那么大的关系







重参数化的作用

如果直接从多元正态分布去采样，破坏了连续性，



![img](https://pic1.zhimg.com/80/v2-f60be7abe507be3c176135d875864280_1440w.jpg?source=1940ef5c)





## VAE++

提到



我们可以统一VAE以及变种的模型，第一项保证重建的准确率高，第二项保证编码到的latent 分布和先验的是一致的。
$$
L_{\text{VAE}} (\theta, \phi) = L_{\text{recons}}(\theta, \phi) + L_{\text{KLD}}(\theta, \phi)
$$
The reconstruction loss is:
$$
L_{\text{recons}}(\theta, \phi) = \frac{1}{N} \sum_{i=1}^N \| \hat{\mathbf{x}_i} - \mathbf{x}_i \|_2^2
$$
The regularization loss is:
$$
L_{\text{KLD}}(\theta, \phi) = D_{\text{KL}} \left(q_\phi(\mathbf{z}|\mathbf{x}) \| p(\mathbf{z}) \right)
$$
another $\beta$-VAE uses the following formulation:
$$
L_{\text{VAE}} (\theta, \phi) = L_{\text{recons}}(\theta, \phi) + \beta L_{\text{KLD}}(\theta, \phi)
$$
$\beta > 1$ would encourages the independence of the dimensions of the latent space and leads to better disentanglement.




## VAD 



因为重构是有噪声的，噪声来自于方差，如果要想提升最后的重建效果，网络会想要让方差=0，也就是没有噪声了，每次都是一个确定的值，模型就在向着普通AE退化，

因为我们需要增加一个额外的约束，希望每一个后验分布都接近标准正态分布

希望能够实现先验，
$$
p(Z) = \sum_X p(Z|X)p(X) = \sum_X \mathcal{N}(0, 1)p(X) = \mathcal{N}(0, 1)
$$

$$
D_{KL}(N(\mu_1, \sigma_1^2) \| N(\mu_2, \sigma_2^2)) = 
\log \frac{\sigma_{2}}{\sigma_{1}}+\frac{\sigma_{1}^{2}+\left(\mu_{1}-\mu_{2}\right)^{2}}{2 \sigma_{2}^{2}}-\frac{1}{2}
$$

$$
D_{KL}(N(\mu, \sigma^2)\|N(0, 1^2)) = 
\frac{1}{2} \left(\mu^{2}+\sigma^{2}-\log \sigma^{2}-1\right)
$$

$$
D_{KL}(N(\mu, \sigma^2)\|N(0, 0.01^2)) = 
5000 (\mu^2 + \sigma^2)-\log\sigma - 5
$$



其实就是希望在常规AE基础上，加上一个高斯噪声，使得decoder能够具有鲁棒性，重构过程希望无噪声，KL希望有噪声，所以也有一个对抗性在里面。







一点原理性的理解：

The original AE only obtain a reduced representation space - latent space



Some efforts provide frameworks that attempt to shape the latent space to be efficient with respect to factor disentanglement or to make it conducive to latent space interpolation. Especially the variational autoencoder (VAE) and its derivatives.

> Principle: For multimodal distributions, such as MNIST. The KL term tends to cluster the modes in the latent space close to each other.  

[Avoiding Latent Variable Collapse With Generative Skip Models](https://arxiv.org/pdf/1807.04863.pdf)  
Adji B. Dieng, Yoon Kim, Alexander M. Rush, David M. Blei  
**[`AISTATS 2019`] (`Columbia, Harvard`)**

**multimodal distribution 本身就是混合的，因此每个单峰里面取样本插值本身就有意义**

如果分布本身是单峰的，unimodal distribution / the generating factors are continuous ; 会导致 KL Loss 驱使 manifold 折叠起来，变得很稠密|非凸。









Auto-encoding variational bayes

Multi-level variational autoencoder: Learning disentangled representations from grouped observations

Extracting and composing robust features with denoising autoencoders

Semantic facial expression editing using autoencoded flow

betavae: Learning basic visual concepts with a constrained variational framework











## Denoising Autoencoder(DAE)

参考 https://blog.keras.io/building-autoencoders-in-keras.html
https://www.tensorflow.org/tutorials/generative/cvae









## 参考链接

[苏剑林-变分自编码器（一）：原来是这么一回事](https://kexue.fm/archives/5253)

[苏剑林-变分自编码器（二）：从贝叶斯观点出发](https://kexue.fm/archives/5343)
