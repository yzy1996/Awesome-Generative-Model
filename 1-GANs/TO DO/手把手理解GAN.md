# 手把手实现GAN





the generator’s distribution $p_g$ over data $x$

a prior on input noise variables $p_z(z)$

a mapping to data space as $G(z;\theta_g)$  a multilayer perceptron

a multilayer perceptron $D(x;\theta_d)$ outputs a single scalar

mapping $x = G(z)$



train $D$ to maximize the probability of assigning the correct label to both training examples and samples from $G$ and train $G$ to minimize $log(1 − D(G(z)))$



main function:
$$
\min _{G} \max _{D} V(D, G)=\mathbb{E}_{\boldsymbol{x} \sim p_{\mathrm{data}}(\boldsymbol{x})}[\log D(\boldsymbol{x})]+\mathbb{E}_{\boldsymbol{z} \sim p_{\boldsymbol{z}}(\boldsymbol{z})}[\log (1-D(G(\boldsymbol{z})))]
$$


Firstly, we fix Generative model and train Discriminative model:

We hope 

The model will be trained to output positive values for real images, and negative values for fake images.

如何理解这个式子呢？

- 固定G（generative model）训练D（discriminative model)

希望真实数据被判别为1，生成数据被判别为0；即希望 $D(x)$ 尽可能大，$D(z)$ 尽可能小。

- 固定D(discriminative model) 训练G(generative model）

希望生成数据被判别为1；即希望$D(z)$ 尽可能大。



## 推导全局最优解 $p_g(x) =p_{data}(x)$

首先固定生成器G，来求全局最优的判别器D

$$
\begin{align}
V(D, G) 
& =\mathbb{E}_{x \sim p_{data}(x)}[\log D(x)]+\mathbb{E}_{z \sim p_z(z)}[\log (1-D(G(z)))] \\
& = \int_{x} p_{\text {data}}(x) \log (D(x)) d x+\int_{z} p_{z}(z) \log (1-D(G(z))) dz \tag{1.1}\\
& = \int_{x} p_{\text {data}}(x) \log (D(x)) d x+\int_{x} p_{g}(x) \log (1-D(x)) d x \tag{1.2}\\
& = \int_{x} \left[p_{data}(x) \log (D(x))+p_{g}(x) \log (1-D(x))\right] dx
\end{align}
$$

现在要 $\max _{D} V(D, G)$，于是
$$
\begin{aligned}
\frac{\partial V(D,G)}{\partial D(x)}
& = \frac{\partial}{\partial D(x)}\left(p_{d a t a}(x) \log (D(x))+p_{g}(x) \log (1-D(x))\right)\\
& = \frac{p_{\text {data}}(x)}{D(x)}-\frac{p_{g}(x)}{1-D(x)}=0
\end{aligned}
$$

$$
D^*(x)=\frac{p_{data}(x)}{p_{data}(x)+p_{g}(x)}
$$

> 关于式（1.1）-（1.2）的推导
>
> 参考 [Radon-Nikodym Theorem](https://en.wikipedia.org/wiki/Radon–Nikodym_theorem) 以及 [law of the unconscious statistician](https://en.wikipedia.org/wiki/Law_of_the_unconscious_statistician) 
>
> 或者参考
> $$
> \begin{aligned}
> \int_{x} p_{g}(x) \log (1-D(x)) dx 
> & = \int_{x} \left[\int_{z} p_{g}(z,x) dz\right] \log (1-D(x)) dx \\
> & = \int_{x} \left[\int_{z} p_{z}(z)p_g(x|z) dz\right] \log (1-D(x)) dx \\
> & = \int_{x} \left[\int_{z} p_{z}(z) dz\right]p_g(x|z) \log (1-D(x)) dx \\
> & = \int_{z} p_{z}(z) \left[\int_{x}  p_g(x|z) \log (1-D(x)) dx \right] dz \\
> & = \int_{z} p_{z}(z) \left[\int_{x}  \delta(x - G(z)) \log (1-D(x)) dx \right] dz \\
> & = \int_{z} p_{z}(z) \left[\log(1-D(x)) \right]_{x=G(z)} dz \\
> & = \int_{z} p_{z}(z) \log(1-D(G(z))) dz
> \end{aligned}
> $$
> I have seen some other notes use the change of variables formula for this proof! That is incorrect, as to do a change of variables, one must calculate $G^{-1}$ which is not assumed to exist (and in practice for neural networks– does not exist!)

已经求得全局最优的判别器D（可以直接代入原式），现在再求全局最优生成器G
$$
\begin{aligned}
V(D^*, G)
& = \int_{x} \left[p_{data}(x) \log \left(\frac{p_{data}(x)}{p_{data}(x)+p_{g}(x)}\right)+p_{g}(x) \log \left(\frac{p_{g}(x)}{p_{data}(x)+p_{g}(x)}\right)\right] dx \\
& = \int_{x} \left[p_{data}(x) \log \left(\frac{p_{data}(x)}{\frac{p_{data}(x)+p_{g}(x)}{2}}\right)+p_{g}(x) \log \left(\frac{p_{g}(x)}{\frac{p_{data}(x)+p_{g}(x)}{2}}\right)\right] dx -\log(4) \\
& = KL\left[p_{data}(x)||\frac{p_{data}(x)+p_{g}(x)}{2}\right] + KL\left[p_{p}(x)||\frac{p_{data}(x)+p_{g}(x)}{2}\right] -\log(4) \\
& = 2JSD(p_{data}||p_g) - \log(4)
\end{aligned}
$$

现在要 $\min _{G} V(D^*, G)$，因为JS散度最小值为0（当且仅当两分布相等时），于是
$$
p_g(x) =p_{data}(x)
$$


$$
V(D^*, G) = 2JSD(p_r||p_g) - \log(4)
$$




## 算法流程

minibatch stochastic gradient descent train:

- Update the discriminator by ascending its stochastic gradient：

$$
\nabla_{\theta_{d}} \frac{1}{m} \sum_{i=1}^{m}\left[\log D\left(\boldsymbol{x}^{(i)}\right)+\log \left(1-D\left(G\left(\boldsymbol{z}^{(i)}\right)\right)\right)\right]
$$

- Update the generator by descending its stochastic gradient:

$$
\nabla_{\theta_{g}} \frac{1}{m} \sum_{i=1}^{m} \log \left(1-D\left(G\left(\boldsymbol{z}^{(i)}\right)\right)\right)
$$



---

错误证明：

$$
F_y(y) = P(Y \leq y) = P(f(X) \leq y) = P(X \leq f^{-1}(y)) = F_x(f^{-1}(y))
$$





Wasserstein Loss

JS散度存在一个严重的问题：两个分布没有重叠时，JS散度为零，而在训练初期，JS散度是有非常大的可能为零的。所以如果D被训练的过于强，loss会经常收敛到-2log2而没有梯度

对于这个问题，WGAN提出了一个新的loss
$$
W\left(P_{r}, P_{g}\right)=\inf _{r \sim \prod\left(P_{r}, P_{g}\right)} E_{(x, y) \sim r}\|x-y\|
$$
这个距离的直观含义是，将分布r移动到分布g所需要的距离，所以即使是两个分布没有重叠，这个loss也是有值的

可以证明，该距离可以转化为如下形式：
$$
W\left(P_{r}, P_{g}\right)=\sup _{\|f\|_{L \succeq 1}} E_{x \sim P_{r}}[f(x)]-E_{y \sim P_{g}}[f(y)]
$$
其中f必须满足1-Lipschitz连续，即：$\|f(x)-f(y)\| \leq\|x-y\|$  可以看到，符合1-Lipschitz连续的函数的梯度是受限的，可以有效的防止梯度的爆炸，使训练更加稳定

$$
KL(P_r\|P_g) = \sum_{x \in X} P_r(x) \log \frac{P_r(x)}{P_g(x)}
$$

$$
JS(P_r\|P_g)=\frac{1}{2} KL\left(P_r \| \frac{P_r+P_g}{2}\right)+\frac{1}{2} K L\left(P_g \| \frac{P_r+P_g}{2}\right)
$$
衍生

## 参考资料

[Collection of Keras implementations of GANs](https://github.com/eriklindernoren/Keras-GAN)

[GAN的损失函数](https://zhuanlan.zhihu.com/p/72195907)







GAN models share two common aspects: solving a challenging saddle point optimization problem, interpreted as an adversarial game between a generator and a discriminator functions.

a popular paradigm to learn the distribution of the observed data



Generative models aim to approximate samples from a complex high-dimensional target distribution $\mathbb{P}$. 

The adversarial mechanism reflects by a generator and a discriminator who compete against each other. Unlike other deep neural network models trained with a loss function until convergence, GAN train these two together to maintain a equilibrium finally.

The generator learns to map from a low-dimension space $\mathcal{Z}$ to a high-dimension space $\mathcal{X}$ with a model distribution $\mathbb{Q}$.

The discriminator learns to accurately distinguish between the synthesized data $\mathbf{Y}$ coming from $\mathbb{Q}$ and the real data $\mathbf{X}$ from $\mathbb{P}$. 

We can denote by $\mathbb{P}$ and $\mathbb{Q}$ the data and model distribution, respectively.



Generative Adversarial Network (GAN) is formulated as a two-player game between a gnerator (G) and a discriminator (D), where G targets at reproducing the distribution of observed data through synthesising new samples, and D competes with G by distinguishing the generated images from the real ones. In priciple, they are expected to reach an equilibrium where D cannot tell the real and fake images apart.



GAN use the reparametrization trick to sample from a complex probability distribution by learning a transformation $y=f(x), x\sim N(0, I)$, where f is the transformatioin function modelled by a neural network.



integral probability metrics (IPMs)

> a “well behaved” function with large amplitude where $P_x$ and$P_z$ differ most

- Wasserstein IPMs



Maximum Mean Discrepancies (MMDs)

> the critic function is a member of a reproducing kernel Hilbert space

### objective functions of GANs



**vanilla GAN**
$$
\min _{G} \max _{D} V(D, G)=\mathbb{E}_{\boldsymbol{x} \sim p_{\mathrm{data}}(\boldsymbol{x})}[\log D(\boldsymbol{x})]+\mathbb{E}_{\boldsymbol{z} \sim p_{\boldsymbol{z}}(\boldsymbol{z})}[\log (1-D(G(\boldsymbol{z})))]
$$

$$
\min J^G = \mathbb{E}_{\boldsymbol{z} \sim p_{\boldsymbol{z}}(\boldsymbol{z})}[\log (1-D(G(\boldsymbol{z})))]
$$

where $J^G$ is the cost of for generator, $\log D(x)$ is the cross-entropy between $[D(x) \quad 1-D(x)]^T$ and $[1 \quad 0]^T$. Likewise,  $\log (1-D(G(z)))$ is the cross-entropy between $[1-D(G(z)) \quad D(G(z))]^T$ and $[1 \quad 0]^T$. It’s because that the cross-entropy 

For a fixed generator $G$, the optimal discriminator $D$ is:
$$
D^*(x)=\frac{p_{data}(x)}{p_{data}(x)+p_{g}(x)},
$$
For this optimal $D^*$, the optimal $G$ satisfies:
$$
p_g(x) =p_{data}(x).
$$

> Problem: 
>
> The cross-entropy of $G$ can be expressed as follow:
> $$
> H^G = 1 * \log(1-D(G(z))) + 0*log(D(G(z))) = \log(1-D(G(z)))
> $$
> In early training progress, D can easily distinguish fake samples from real samples ($D(G(z)) \rightarrow 0$). This results in G not having sufficient gradient to improve, which is called **training instability**. Rather than training G in the way of Equation (2), another way of Equation (6) could provides larger gradients in early training.
> $$
> \min J^G = \mathbb{E}_{\boldsymbol{z} \sim p_{\boldsymbol{z}}(\boldsymbol{z})}[-\log (D(G(\boldsymbol{z})))]
> $$
> So a new cross-entropy of $G$ can be expressed as:
> $$
> H = 1 * \log(-D(G(z))) + 0*log(1 + D(G(z)))
> $$



blog 

https://www.freecodecamp.org/news/an-intuitive-introduction-to-generative-adversarial-networks-gans-7a2264a81394/

https://wiki.pathmind.com/generative-adversarial-network-gan









A GAN consists of a generator $G$ and a discriminator $D$, both are conducted by a neural network. $G$ takes a latent variable $z \sim p(z)$ sampled from a prior distribution and maps it to the observation space $\mathcal{X}$. $D$ takes an observation $x \in \mathcal{X}$ and produces a decision output over possible observation sources (either from $G$ or from the empirical data distribution). 



The generator and the discriminator in the standard GAN training procedure are trained by minimizing the following objectives:
$$
\begin{align}
&L_{D}=-\mathbb{E}_{x \sim p_{\text {data }}}[\log D(x)]-\mathbb{E}_{z \sim p(z)}[1-\log D(G(z))], \\
&L_{G}=-\mathbb{E}_{z \sim p(z)}[\log D(G(z))].
\end{align}
$$
This formulation is originally proposed by Goodfellow et al. (2014) as non-saturating (NS) GAN. A significant amount of research has been done on modifying this formulation in order to improve the training process. A notable example is the **hinge-loss** version of the adversarial loss:
$$
\begin{align}
&L_{D}=-\mathbb{E}_{x \sim p_{\text {data }}}[\min (0,-1+D(x))]-\mathbb{E}_{z \sim p(z)}[\min (0,-1-D(G(z)))], \\
&L_{G}=-\mathbb{E}_{z \sim p(z)}[D(G(z))].
\end{align}
$$
Another commonly adopted GAN formulation is the **Wassertein** GAN (WGAN), where the authors propose clipping the weights to enforce the continuous of Wassertein distance. The loss function of WGAN is:
$$
\begin{align}
&L_{D}=-\mathbb{E}_{x \sim p_{\text {data }}}[D(x)]+\mathbb{E}_{z \sim p(z)}[D(G(z))], \\
&L_{G}=-\mathbb{E}_{z \sim p(z)}[D(G(z))].
\end{align}
$$



[How to Train a GAN? Tips and tricks to make GANs work](https://github.com/soumith/ganhacks)
