# Normalizing flow

需要补充的知识点：

Variational inference 变分推论

ELBO（evidence lower bound）



一般我们想计算 后验概率 $p(z|x)$， 根据贝叶斯公式，$p(z|x) = \frac{p(z)p(x|z)}{p(x)}$，以及 $p(x) = \int p(x, z) \mathrm{d} z$



现在想用一族 parameterized distributions $\mathcal{D}=\left\{q_{\theta}(z)\right\}$ 来近似真实的后验分布



写成一个优化问题就是
$$
\theta^{*}=\underset{\theta}{\arg \min } \mathrm{KL}\left(q_{\theta}(z) \| p(z \mid x)\right)
$$
等价于
$$
\theta^{*}=\underset{\theta}{\arg \max } \mathbb{E}_{q}\left[\log p(x, z)-\log q_{\theta}(z)\right]
$$






posterior $p(z|x)$



Normalizing flows transform simple densities (like Gaussians) into rich complex distributions.

Change of variables, change of volume







## 精确推断



MAP(Maximum a posteriori estimation) 最大后验概率







Negative Log Liklihood NLL 负对数似然



