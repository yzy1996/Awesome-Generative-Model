# 一文解读 VAE+ELBO

> [Auto-Encoding Variational Bayes](https://arxiv.org/abs/1312.6114)  *Diederik P Kingma, Max Welling*  **[`ICLR 2014`] (`Universiteit van Amsterdam`)**



我们先从 **AutoEncoder(AE)** 讲起，它的基本结构我们可以用下图来表示。

![figure_ae](https://raw.githubusercontent.com/yzy1996/Image-Hosting/master/figure_ae.svg)

$X$是原始输入图像，经过Encoder降维到一个Latent空间中的一点，表示为$z$，然后经过Decoder再还原回图像空间，表示为$\hat{X}$。通过$X$和$\hat{X}$之间的重建误差 (pixel MSE)，就能不断更新 Encoder 和 Decoder，最终得到一个好的降维模型，同时还能很好地进行**重建**。















![image-20221001170252672](https://raw.githubusercontent.com/yzy1996/Image-Hosting/master/image-20221001170252672.png)



背景介绍，VAE是属于【基于似然函数】的一类方法，还包括了有normalizing flows，EBM

VAEs maximize the mutual information between the input and latent variables,



首先我们有一批数据样本 $X= \{x_1, x_2, \dots, x_n\}$，假设这些数据是独立同分布的。我们的最终目的是生成更多也服从这个分布的新数据，因此我们想估计这个分布。对于所熟知的高斯分布，我们已经知道了它的表达式，对于来源于一个未知高斯分布的数据，我们只需要去估计出它的参数 $(\mu, \sigma)$ ，采样的方法就是极大化似然估计。

而对于一批任意数据（生成模型中主要是图像，一幅图像也可以看成是从一个分布中采样的结果），但现在我们甚至都不知道这个分布的参数化形式，因此直接对它估计是几乎不可能的。

我们先对这个问题进行数学建模，将数据分布记作：$p(x;\theta) \text{ or } p_\theta(x)$，其中 $\theta$ 就是我们要估计的参数。

那么很自然，我们可以用极大似然估计来求解（参考）：
$$
p(x;\theta) = \prod_{i=1}^{n} p\left(x_{i} ; \theta\right) \tag{1}
$$
一般实际使用的是求解一个极小化负的对数似然的问题：
$$
\theta^* = \arg\min_\theta -\sum_{i=1}^n \log p (x_i;\theta) \tag{2}
$$
但是这里的 $\theta$ 是会很复杂的，不再像高斯分布那样可以简单地用数学表达式来描述，因此我们引入一个新的变量来帮我们求解，称它为隐变量模型，同时也将上面的离散化形式改成连续化形式，记作：
$$
p(x) = \int p_\theta\left(x, z\right) dz = \int p\left(x| z;\theta\right) p(z)dz \tag{3}
$$
其中，$z$ 就是隐变量，通常假设 $z \sim \mathcal{N}(0, I)$，数据 $x$ 依赖 $z$ 生成：$x = f(z;\theta)$ 。这样就将一个概率密度估计问题转化成函数逼近问题，利用一个隐变量模型将一个简单的概率分布（高斯分布）映射到一个更复杂的任意分布（图像数据分布）上。实现一个从低维 latent vector $z \in \mathbb{R}^d$ 到高维 $x \in \mathbb{D}$ 的映射 $g: \mathcal{Z} \rightarrow \mathcal{X}$。





通过式子()我们可以发现，现在我们想得到 $p(x)$，我们可以先通过一个已知的简单模型分布，以及一个z到x的映射分布就行了。

借由贝叶斯定理，我们将所有定义写出来

- 先验分布 $p(z)$

- 后验分布 $p(z|x)$
- 似然分布 $p(x|z)$
- 证据分布 $p(x)$


$$
\text{posterior} = \frac{\text{likelihood} \times \text{prior}}{\text{evidence}} \quad p(z|x) = \frac{p(x|z) p(z)}{p(x)}
$$


$$
\begin{aligned}
K L\left(q\left(x, z\right) \| p\left(x, z\right)\right) 
&=\iint q(x,z) \log \frac{q(x,z)}{p(x,z)} dzdx\\
&=\iint q(z|x)p(x) \log \frac{q(z|x)p(x)}{p(x|z)p(z)} dzdx\\
&=\int p(x)\left[\int q(z|x) \log \frac{q(z|x)p(x)}{p(x|z)p(z)} d z\right] d x \\
&=\mathbb{E}_{x \sim p(x)}\left[\int q(z|x) \log \frac{q(z|x)p(x)}{p(x|z)p(z)} d z\right]\\
&=\mathbb{E}_{x \sim p(x)}\left[\int q(z|x) \left(\log p(x) + \log \frac{q(z|x)}{p(x|z)p(z)} \right)dz\right]\\
&=\mathbb{E}_{x \sim p(x)}\left[\int q(z|x) \log p(x) dz\right] + \mathbb{E}_{x \sim p(x)}\left[\int q(z|x)\log \frac{q(z|x)}{p(x|z)p(z)} dz\right]\\
&=\mathbb{E}_{x \sim p(x)}\left[\log p(x) \int q(z|x) dz\right] + \mathbb{E}_{x \sim p(x)}\left[\int q(z|x)\log \frac{q(z|x)}{p(x|z)p(z)} dz\right]\\
&=\mathbb{E}_{x \sim p(x)}\left[\log p(x) \right] +  \mathbb{E}_{x \sim p(x)}\left[\int q(z|x) \log \frac{q(z|x)}{p(z)} dz -\int q(z|x)\log p(x | z)dz \right]\\
&=\mathbb{E}_{x \sim p(x)}\left[\log p(x) \right] +  \mathbb{E}_{x \sim p(x)}\left[KL\left(q(z|x) \| p(z)\right) - \mathbb{E}_{z \sim q(z|x)}[\log p(x | z)]\right]
\end{aligned} \tag{10}
$$











像GAN一样（假设你已经很熟悉GAN了），VAE也是想要学习一个生成模型以VAE的优化目标是最大化数据集数据的似然：
$$
\log p(X) = \sum_{i=1}^N \log \int p\left(x_{i}, z\right) dz
$$

但这个目标很难去优化，因此采用最大化每个样本点边际似然的证据下界的方式：
$$
\log p(x_i) \ge \mathcal{L}(x_i) = \mathbb{E}_{z\sim q_\phi(z|x_i)} [-\log q_\phi(z|x_i) + \log p_\theta(x_i, z)]
$$
其中 $q_\phi(z \mid x)$ 是真实后验的变分近似。

利用重参数化的方式，将随机隐式变量 $z$ 用一个确定方程表示 $z = h_\phi(x, \epsilon)$ ，这其中的 $\epsilon$ 是一个任意分布的辅助变量。$p_\theta (z)$ 是零均值的正态分布，因此鼓励了隐变量都是在原点附近的。

关于似然 $p_\theta (x \mid z)$ ，根据前人工作，可以选择一个各相同性的正态分布，它的均值由decoder网络 $g_\theta(z)$ 提供，而方差是固定的。












我们要得到的结果是 $p_\theta (x|z)$ 然后都在讲 怎么推断 后验分布 $p(z|x)$

我们想借助隐变量 $z$ 来描述 $\mathbf{x}$ 的分布，建模成：
$$
q(x)=\int q(x, z) d z, \quad p(x, z)=p(x | z) p(z)
$$
$x$ 和 $z$ 的联合分布还可以写成 $q(x,z) = q(z|x) p(x)$。因此我们想用 $q(x,z)$ 来近似 $p(x,z)$。因此直接用KL散度来衡量（KL散度越小越好）：
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
&=\mathbb{E}_{x \sim p(x)}\left[\ln p(x) \right] +  \mathbb{E}_{x \sim p(x)}\left[\int p(z \mid x)\ln \frac{p(z \mid x)}{q(x \mid z)q(z)} dz\right]\\
&=\mathbb{E}_{x \sim p(x)}\left[\ln p(x) \right] +  \mathbb{E}_{x \sim p(x)}\left[\int p(z \mid x) \ln \frac{p(z \mid x)}{q(z)} dz -\int p(z \mid x)\ln q(x \mid z)dz \right]\\
&=\mathbb{E}_{x \sim p(x)}\left[\ln p(x) \right] +  \mathbb{E}_{x \sim p(x)}\left[KL\left(p(z \mid x) \| q(z)\right) - \mathbb{E}_{z \sim p(z \mid x)}[\ln q(x \mid z)]\right]
\end{aligned}
$$
移项后得到：
$$
K L(p(x, z) \| q(x, z)) - \mathbb{E}_{x \sim p(x)}\left[\ln p(x) \right] = \mathbb{E}_{x \sim p(x)}\left[KL\left(p(z \mid x) \| q(z)\right) - \mathbb{E}_{z \sim p(z \mid x)}[\ln q(x \mid z)]\right]
$$
左边的第一项是要最小化，第二项是要最大化（取负号后也是最小化），因此最小化左侧，等价于最小化右侧，所以我们的优化目标函数就是：
$$
\mathcal{L} = \mathbb{E}_{x \sim p(x)}\left[KL\left(p(z \mid x) \| q(z)\right) - \mathbb{E}_{z \sim p(z \mid x)}[\ln q(x \mid z)]\right]
$$
而右侧取负号会被称为 证据下界 Evidence lower bound (ELBO)，

> 因为 $p(x)$ 通常被称为 evidence，

是需要被最大化的
$$
ELBO = \mathbb{E}_{x \sim p(x)}\left[\mathbb{E}_{z \sim p(z \mid x)}[\ln q(x \mid z)] - KL\left(p(z \mid x) \| q(z)\right)\right]
$$
最终要优化的是两个网络的参数，



当我们希望$p(z|x)$ 是服从标准正态分布$\mathcal{N}(0, I)$时


$$
p(z)=\int p(z \mid x) p(x) \mathrm{d} x=\int \mathcal{N}(0, I) p(x) \mathrm{d} x=\mathcal{N}(0, I) \int p(x) \mathrm{d} x=\mathcal{N}(0, I)
$$


KL实现，如果没有这一项，网络会倾向于使得方差为0，



我们假设后验分布也是服从高斯的，encoder网络预测的就是高斯分布的均值和方差，（实际中预测的是 log ）



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
等号右边第一项不就是似然值吗？第二项只要实现把先验概率$p(Z)$定义好之后，也可以进行计算。



因为 $p(x|z)$ 形如 decoder，而 $q(z|x)$ 形如 Encoder，因此得名 VAE。和 Auto-Encoder 并没有那么大的关系


$$
KL(N(\mu, \sigma), N(0, 1)) = \log \frac{1}{\sigma} + \frac{\sigma^2 + \mu^2}{2} - \frac{1}{2}
$$



重参数化的作用

从 $q(z| x)$ 采样是无法计算梯度的

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









Auto-encoding variational bayes

Multi-level variational autoencoder: Learning disentangled representations from grouped observations

Extracting and composing robust features with denoising autoencoders

Semantic facial expression editing using autoencoded flow

betavae: Learning basic visual concepts with a constrained variational framework







VAE有一个总体指标，这个总指标越小效果就越好





两个多元高斯分布的KL散度计算：
$$
KL(p_1 \| p_2) = \frac{1}{2}\left(\operatorname{tr}\left(\boldsymbol{\Sigma}_{2}^{-1} \boldsymbol{\Sigma}_{1}\right)+\left(\boldsymbol{\mu}_{\mathbf{2}}-\boldsymbol{\mu}_{\mathbf{1}}\right)^{\top} \boldsymbol{\Sigma}_{1}^{-1}\left(\boldsymbol{\mu}_{\mathbf{2}}-\boldsymbol{\mu}_{\mathbf{1}}\right)-n+\log \frac{\operatorname{det}\left(\boldsymbol{\Sigma}_{\mathbf{2}}\right)}{\operatorname{det}\left(\boldsymbol{\Sigma}_{\mathbf{1}}\right)}\right)
$$

$$
D_{\mathrm{KL}}\left(q_{\phi}\left(\mathbf{z} \mid \mathbf{x}^{(i)}\right) \| p_{\theta}(\mathbf{z})\right)=\frac{1}{2} \sum_{j=0}^{n}\left(\left(\sigma_{j}^{(i)}\right)^{2}+\left(\mu_{j}^{(i)}\right)^{2}-1-\log \left(\left(\sigma_{j}^{(i)}\right)^{2}\right)\right)
$$








## 参考链接

[苏剑林-变分自编码器（一）：原来是这么一回事](https://kexue.fm/archives/5253)

[苏剑林-变分自编码器（二）：从贝叶斯观点出发](https://kexue.fm/archives/5343)



https://zhuanlan.zhihu.com/p/249296925

https://zhuanlan.zhihu.com/p/452743042
