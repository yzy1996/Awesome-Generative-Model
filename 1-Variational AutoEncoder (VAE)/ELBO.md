# Evidence Lower Bound (ELBO)

> 

论证什么是，以及为什么要用ELBO，





边缘分布，也就意味着不只有一个变量，这两个变量的联合概率密度为 $p(z,y)$，其中一个变量的边缘分布则为给定其他变量的条件概率分布$p(x) = \sum_y p(x,y) = \sum_y p(x|y)p(y)$



给出一组独立同分布的样本点 $X= \{x_1, x_2, \dots, x_n\}$，其中$x_i \sim p(x;\theta)$，而 $\theta$ 也可以被看成是一个随机变量，服从一个分布 $\theta \sim p(\theta; \phi)$，边缘似然是在刻画 $p(X;\phi)$
$$
p(X;\phi) = \int_\theta p(X;\theta)p(\theta;\phi) d\theta
$$




边缘似然 (Marginal likelihood)，也被叫做模型证据 (Model Evidence)：





Given a set of independent identically distributed data points: $X= \{x_1, x_2, \dots, x_n\}$, where $x_i \sim p_(x;\theta)$. 


$$
0< b_t <1
$$










首先是问题的设定：针对带有隐变量的概率模型

我们有随机变量 $X, Z$，他们服从一个联合分布 $p(X,Z;\theta)$，我们的数据只有对 $X$ 实现的观测，对 $Z$ 是不知道的。因此一般我们有两个任务想要实现：

- 给定 $\theta$ ，计算后验分布 $p(Z|X;\theta)$。变分推断就是用在这个任务上。
- 用最大似然估计 $\theta$，$\arg \max_\theta \{ \log p(x;\theta) = \log \int_z p(x,z;\theta) dz\}$







**Evidence (证据)** 定义的就是 似然函数 $\log p(x;\theta)$。之所以被称为 证据，是因为它能反应我们对模型的估计好坏程度。





如果我们知道了 $Z$ 服从的分布 $q$，(在后面的表示中，为了简化我们省去了 $\theta$)

$$
\begin{align}
\log p(x) 
&= \log \int p(x,z) dz \\
&= \log \int p(x,z) \frac{q(z)}{q(z)} dz \\
&= \log \mathbb{E}_{z \sim \mathcal{Z}} \left[ \frac{p(x, z)}{q(z)} \right] \\
&\ge \mathbb{E}_{z \sim \mathcal{Z}} \log \left[ \frac{p(x, z)}{q(z)} \right]
\end{align}
$$

$$
ELBO := \mathbb{E}_{z \sim \mathcal{Z}} \log \left[ \frac{p(x, z)}{q(z)} \right]
$$


The gap between the evidence and the ELBO is the Kullback-Leibler Divergence between $p(z|x)$ and $q(z)$:
$$
\begin{aligned}
KL(q(z) \| p(z \mid x)) 
&:= \mathbb{E}_{z \sim \mathcal{Z}} \log \left[ \frac{q(z)}{p(z \mid x)} \right] \\
&= \mathbb{E}_{z \sim \mathcal{Z}} \left[\log q(z)\right] - \mathbb{E}_{z \sim \mathcal{Z}} \left[\log p(x,z)\right] + \mathbb{E}_{z \sim \mathcal{Z}} \left[\log p(x)\right] \\
&= \log p(x) - \mathbb{E}_{z \sim \mathcal{Z}} \log \left[ \frac{p(x, z)}{q(z)} \right] \\
&= \text{Evidence} - \text{ELBO}
\end{aligned}
$$







We want to use a $q(z)$ approximate $p(z|x)$ and get an optimal $q^*(z)$


$$
\text{KL }(q(z) \| p(z \mid x)) = \mathbb{E}[\log q (z)] - \mathbb{E}[\log p (z, x)] + \log p(x)
$$
add 
$$
KL() \ge 0
$$
so

$$
ELBO(q) = \mathbb{E}[\log p (z, x)] - \mathbb{E}[\log q (z)]
$$





吉布斯不等式 

若 $\sum_{i=1}^n p_i = \sum_{i=1}^n p_i = 1$，且 $p_i, q_i \in (0, 1]$，则有：
$$
-\sum_{i=1}^{n} p_{i} \log p_{i} \leq-\sum_{i=1}^{n} p_{i} \log q_{i} \text { ，等号成立当且仅当 } p_{i}=q_{i} \ \forall i
$$


最小化KL散度等价于最大化ELBO



杰森不等式 Jensen's Inequality







如果我们从后验的角度来看，首先什么是后验，

在生成模型中，我们是从一个z得到一个x，后验概率就是 p(z|x)


$$
P(Z \mid X)=\frac{p(X, Z)}{\int_{z} p(X, Z=z) d z}
$$
所以变分推断 (Variational Inference)，是为了 推断 z 



因此我们想引入一个参数化模型 $p(z;\lambda)$ 来近似 p(z|x)，相当于是用一个简单分布去拟合了一个复杂分布
$$
\lambda^{*}=\arg \min _{\lambda} \text { divergence }(p(z \mid x), q(z ; \lambda))
$$
这个度量一般就是用KL散度，
$$
D_{K L}(p \| q)=\sum_{i=1}^{N}\left[p\left(x_{i}\right) \log p\left(x_{i}\right)-p\left(x_{i}\right) \log q\left(x_{i}\right)\right] = \sum_{i=1}^{N} p\left(x_{i}\right) \log \left(\frac{p\left(x_{i}\right)}{q\left(x_{i}\right)}\right)
$$

> 因为KL散度大于0，很好用梯度下降



所以我们的目标是最小化 $\min _{\lambda} K L(q(z ; \lambda) \| p(z \mid x))$

直接求很难，让我们回到贝叶斯公式


$$
p(x) = \frac{p(x,z)}{p(z|x)}
$$
两边取log，
$$
\begin{aligned}
\log P(x) &=\log P(x, z)-\log P(z \mid x) \\
&=\log \frac{P(x, z)}{Q(z ; \lambda)}-\log \frac{P(z \mid x)}{Q(z ; \lambda)}
\end{aligned}
$$
然后再对q求期望
$$
\begin{aligned}
\mathbb{E}_{q(z ; \lambda)} \log P(x) &=\mathbb{E}_{q(z ; \lambda)} \log P(x, z)-\mathbb{E}_{q(z ; \lambda)} \log P(z \mid x) \\
\log P(x) &=\mathbb{E}_{q(z ; \lambda)} \log \frac{p(x, z)}{q(z ; \lambda)}-\mathbb{E}_{q(z ; \lambda)} \log \frac{p(z \mid x)}{q(z ; \lambda)} \\
&=K L(q(z ; \lambda) \| p(z \mid x))+\mathbb{E}_{q(z ; \lambda)} \log \frac{p(x, z)}{q(z ; \lambda)}
\end{aligned}
$$

$$
\max _{\lambda} \mathbb{E}_{q(z ; \lambda)} \log \frac{p(x, z)}{q(z ; \lambda)}
$$

$$
\log P(x)=K L(q(z ; \lambda) \| p(z \mid x))+E L B O
$$
Any procedure which uses optimization to approximate a density can be termed ``variational inference''.

Jordan (2008) 曾经对 Variational Inference 给出来一个直观的定义：



Variational Bayes is a particular variational method which aims to find some approximate joint distribution Q(x; θ) over hidden variables x to approximate the true joint P(x), and defines ‘closeness’ as the KL divergence KL[Q(x; θ)||P(x)].



概率模型中的后验分布推断常见的方法是：MAP、EM算法、变分推断(Variational Inference, VI)和蒙特卡洛推断(Monte Carlo Inference, MCI)。可以粗暴地、不严谨地理解为，EM是VI的特例，VI是MCI的特例。


$$
\log p(x)=E L B O+K L D
$$




先说结论，
$$
\text{ELBO} = E_{q} \log p(\theta, \beta, z, w \mid \alpha, \eta)-E_{q} \log q(\beta, z, \theta \mid \lambda, \phi, \gamma)
$$









$$
\begin{aligned}
    \log p(x) &=\log p(x) \int q(z | x) d z & &\left(\text { Multiply by } 1=\int q(z | x) d z\right) \\
    &=\int q(z | x)(\log p(x)) d z & & (\text { Bring evidence into integral }) \\
    &=\mathbb{E}_{q(z | x)}[\log p(x)] & & (\text { Definition of Expectation } )\\
    &=\mathbb{E}_{q(z | x)}\left[\log \frac{p(x, z)}{p(z | x)}\right] & & (\text { Apply Equation 2 } )\\
    &=\mathbb{E}_{q(z | x)}\left[\log \frac{p(x, z) q(z | x)}{p(z | x) q(z | x)}\right] & &\left(\text { Multiply by } 1=\frac{q(z | x)}{q(z | x)}\right) \\
    &=\mathbb{E}_{q(z | x)}\left[\log \frac{p(x, z)}{q(z | x)}\right]+\mathbb{E}_{q(z | x)}\left[\log \frac{q(z | x)}{p(z | x)}\right] & & (\text { Split the Expectation })  \\
    &=\mathbb{E}_{q(z | x)}\left[\log \frac{p(x, z)}{q(z | x)}\right]+KL\left(q(z | x) \| p(z | x)\right) & & (\text { Definition of KL Divergence})  \\
    &\geq \mathbb{E}_{q(z | x)}\left[\log \frac{p(x, z)}{q(z | x)}\right] & &(\text { KL Divergence always } \geq 0)
    \end{aligned}
$$

$$
\begin{aligned}
    \text{ELBO} &:= \mathbb{E}_{q(z \mid x)}\left[\log \frac{p(x, z)}{q(z \mid x)}\right] \\&=\mathbb{E}_{q(z \mid x)}\left[\log \frac{p(x \mid z) p(z)}{q(z \mid x)}\right] \\
    &=\mathbb{E}_{q(z \mid x)}\left[\log p(x \mid z)\right]+\mathbb{E}_{q(z \mid x)}\left[\log \frac{p(z)}{q(z \mid x)}\right] \quad \text { (Split the Expectation) } \\
    &=\underbrace{\mathbb{E}_{q(z \mid x)}\left[\log p(x \mid z)\right]}_{\text {reconstruction term }}-\underbrace{KL\left(q(z \mid x) \| p(z)\right)}_{\text {prior matching term }} \quad \text { (Definition of KL Divergence) }
    \end{aligned}
$$








我们有可以观察到的有限个样本 $\boldsymbol{x}$ ，我们希望最大化它的似然 $p(x)$

表示似然有两种方式，
$$
p(x) = \int p(x, z) dz
\\
p(x) = \frac{p(x,z)}{p(z|x)}
$$
但这两种都无法直接求解

因此我们引入一个新的 $q_\phi(z|x)$ 来拟合真实的后验 $p(z|x)$ 


$$
\begin{aligned}
\log p(\boldsymbol{x}) &=\log p(\boldsymbol{x}) \int q_\phi(\boldsymbol{z} \mid \boldsymbol{x}) d z & &\text { (Multiply by } \left.1=\int q_\phi(\boldsymbol{z} \mid \boldsymbol{x}) d \boldsymbol{z}\right) \\
&=\int q_\phi(\boldsymbol{z} \mid \boldsymbol{x})(\log p(\boldsymbol{x})) d z & & \text { (Bring evidence into integral) } \\
&=\mathbb{E}_{q_\phi(\boldsymbol{z} \mid \boldsymbol{x})}[\log p(\boldsymbol{x})] & & \text { (Definition of Expectation) } \\
&=\mathbb{E}_{q_\phi(\boldsymbol{z} \mid \boldsymbol{x})}\left[\log \frac{p(\boldsymbol{x}, \boldsymbol{z})}{p(\boldsymbol{z} \mid \boldsymbol{x})}\right] & & \text { (Apply Equation 2) } \\
&=\mathbb{E}_{q_\phi(\boldsymbol{z} \mid \boldsymbol{x})}\left[\log \frac{p(\boldsymbol{x}, \boldsymbol{z}) q_\phi(\boldsymbol{z} \mid \boldsymbol{x})}{p(\boldsymbol{z} \mid \boldsymbol{x}) q_\phi(\boldsymbol{z} \mid \boldsymbol{x})}\right] & &\text { (Multiply by } \left.1=\frac{q_\phi(\boldsymbol{z} \mid \boldsymbol{x})}{q_\phi(\boldsymbol{z} \mid \boldsymbol{x})}\right) \\
&=\mathbb{E}_{q_\phi(\boldsymbol{z} \mid \boldsymbol{x})}\left[\log \frac{p(\boldsymbol{x}, \boldsymbol{z})}{q_\phi(\boldsymbol{z} \mid \boldsymbol{x})}\right]+\mathbb{E}_{q_\phi(\boldsymbol{z} \mid \boldsymbol{x})}\left[\log \frac{q_\phi(\boldsymbol{z} \mid \boldsymbol{x})}{p(\boldsymbol{z} \mid \boldsymbol{x})}\right] & & \text { (Split the Expectation) } \\
&=\mathbb{E}_{q_\phi(\boldsymbol{z} \mid \boldsymbol{x})}\left[\log \frac{p(\boldsymbol{x}, \boldsymbol{z})}{q_\phi(\boldsymbol{z} \mid \boldsymbol{x})}\right]+D_{\mathrm{KL}}\left(q_\phi(\boldsymbol{z} \mid \boldsymbol{x}) \| p(\boldsymbol{z} \mid \boldsymbol{x})\right) & & \text { (Definition of KL Divergence) } \\
&\geq \mathbb{E}_{q_\phi(\boldsymbol{z} \mid \boldsymbol{x})}\left[\log \frac{p(\boldsymbol{x}, \boldsymbol{z})}{q_\phi(\boldsymbol{z} \mid \boldsymbol{x})}\right] & &\text { (KL Divergence always } \geq 0)
\end{aligned}
$$


其实我们是想要最小化KL散度的，因此最大化ELBO其实就是间接最小化了KL散度，因为他们的和是一个定值，与优化目标以及参数无关



This approach is variational, because we optimize for the best q φ(z | x) amongst a family of potential posterior distributions parameterized by φ .




$$
\begin{aligned}
\text{ELBO} &:= \mathbb{E}_{q_\phi(\boldsymbol{z} \mid \boldsymbol{x})}\left[\log \frac{p(\boldsymbol{x}, \boldsymbol{z})}{q_\phi(\boldsymbol{z} \mid \boldsymbol{x})}\right] \\&=\mathbb{E}_{q_\phi(\boldsymbol{z} \mid \boldsymbol{x})}\left[\log \frac{p_{\boldsymbol{\theta}}(\boldsymbol{x} \mid \boldsymbol{z}) p(\boldsymbol{z})}{q_{\boldsymbol{\phi}}(\boldsymbol{z} \mid \boldsymbol{x})}\right] \\
&=\mathbb{E}_{q_\phi(\boldsymbol{z} \mid \boldsymbol{x})}\left[\log p_{\boldsymbol{\theta}}(\boldsymbol{x} \mid \boldsymbol{z})\right]+\mathbb{E}_{q_\phi(\boldsymbol{z} \mid \boldsymbol{x})}\left[\log \frac{p(\boldsymbol{z})}{q_\phi(\boldsymbol{z} \mid \boldsymbol{x})}\right] \quad \text { (Split the Expectation) } \\
&=\underbrace{\mathbb{E}_{q_\phi(\boldsymbol{z} \mid \boldsymbol{x})}\left[\log p_{\boldsymbol{\theta}}(\boldsymbol{x} \mid \boldsymbol{z})\right]}_{\text {reconstruction term }}-\underbrace{D_{K L}\left(q_\phi(\boldsymbol{z} \mid \boldsymbol{x}) \| p(\boldsymbol{z})\right)}_{\text {prior matching term }} \quad \text { (Definition of KL Divergence) }
\end{aligned}
$$


the encoder of VAE is commonly chosen to model a multivariate Gaussian with diagonal covariance, and the prior is often selected to be a standard multivariate Gaussian:
$$
\begin{aligned}
q_{\boldsymbol{\phi}}(\boldsymbol{z} \mid \boldsymbol{x}) &=\mathcal{N}\left(\boldsymbol{z} ; \boldsymbol{\mu}_{\boldsymbol{\phi}}(\boldsymbol{x}), \boldsymbol{\sigma}_{\boldsymbol{\phi}}^2(\boldsymbol{x}) \mathbf{I}\right) \\
p(\boldsymbol{z}) &=\mathcal{N}(\boldsymbol{z} ; \mathbf{0}, \mathbf{I})
\end{aligned}
$$


用 Monte Carlo 采样是可以计算重建项的
$$
\underset{\phi, \boldsymbol{\theta}}{\arg \max } \mathbb{E}_{q_\phi(\boldsymbol{z} \mid \boldsymbol{x})}\left[\log p_{\boldsymbol{\theta}}(\boldsymbol{x} \mid \boldsymbol{z})\right]-D_{\mathrm{KL}}\left(q_\phi(\boldsymbol{z} \mid \boldsymbol{x}) \| p(\boldsymbol{z})\right) \approx \underset{\phi, \boldsymbol{\theta}}{\arg \max } \sum_{l=1}^L \log p_{\boldsymbol{\theta}}\left(\boldsymbol{x} \mid \boldsymbol{z}^{(l)}\right)-D_{\mathrm{KL}}\left(q_\phi(\boldsymbol{z} \mid \boldsymbol{x}) \| p(\boldsymbol{z})\right)
$$
其中 latent $\{z^{l}\}$ 是从 $q_\phi(z|x)$ 中采样的



重参数化
$$
\boldsymbol{z}=\boldsymbol{\mu}_\phi(\boldsymbol{x})+\boldsymbol{\sigma}_\phi(\boldsymbol{x}) \odot \boldsymbol{\epsilon} \quad \text { with } \boldsymbol{\epsilon} \sim \mathcal{N}(\boldsymbol{\epsilon} ; \mathbf{0}, \mathbf{I})
$$







边缘似然









我们看参数估计里的贝叶斯公式，是我们想得到一个模型来刻画我们的观测数据，这里面是有两部分在的，一步是确定模型（是高斯模型，还是伯努利模型…），第二步是确定模型的参数（是标准高斯，还是非标准高斯…）。
$$
p(\theta|x) = \frac{p(x|\theta) p(\theta)}{p(x)} \quad \text{posterior} = \frac{\text{likelihood} \times \text{prior}}{\text{model evidence}}
$$








右边分子部分的含义是：用特定参数 $\theta$ 能多好地刻画数据

右边分母部分的含义是：用所有的参数能多好地刻画数据，也即与参数无关，你建的模型好不好。
$$
p(x) = \int p(x|\phi) p(\phi) d\phi
$$
它也叫 marginal likelihood or model evidence 是需要使用所有参数的，由先验进行加权。因此放在分母，起到一个归一化的作用，因为分母是分子加权求和后的结果，而对于一个最佳参数，它的后验概率应该是最大的。

