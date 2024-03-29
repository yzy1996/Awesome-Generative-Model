

![image-20220916170030066](https://raw.githubusercontent.com/yzy1996/Image-Hosting/master/image-20220916170030066.png)



## 前向过程（加噪声）

$\boldsymbol{x}_0$ 是原图，往后 $\boldsymbol{x}_{t-1} \rightarrow \boldsymbol{x}_t$ 是一个不断加噪声的过程。相邻两个变量之间是一个线性关系，我们可以建模成
$$
\boldsymbol{x}_t = a_t\boldsymbol{x}_{t-1} + b_t \boldsymbol{\varepsilon}_t, \quad \boldsymbol{\varepsilon}_t \sim \mathcal{N}(\mathbf{0}, \mathbf{I}) \tag{1}
$$
我们先看一下这两个系数，因为$x_{t-1}$具有的信息更多，因此$a_t$是一个衰减系数，值应该满足 $0<a_t<1$；同样的噪声系数也满足 $0<b_t<1$。

当我们用 $\boldsymbol{x}_{t-1} = a_{t-1}\boldsymbol{x}_{t-2} + b_{t-1} \boldsymbol{\varepsilon}_{t-1}$ 不断展开这个式子，可以得到
$$
\begin{aligned}
\boldsymbol{x}_t 
&=a_{t}\boldsymbol{x}_{t-1} + b_t \boldsymbol{\varepsilon}_{t}\\
&=a_{t}(a_{t-1}\boldsymbol{x}_{t-2} + b_{t-1} \boldsymbol{\varepsilon}_{t-1}) + b_t \boldsymbol{\varepsilon}_{t}\\
&=a_{t}a_{t-1}\boldsymbol{x}_{t-2} + a_{t} b_{t-1} \boldsymbol{\varepsilon}_{t-1} + b_t \boldsymbol{\varepsilon}_{t}\\
&=\dots\\
&=(a_{t}\dots a_1) \boldsymbol{x}_{0} + (a_{t}\dots a_2)b_1\boldsymbol{\varepsilon}_{1} + (a_{t}\dots a_3)b_2\boldsymbol{\varepsilon}_{2}+\dots+a_{t} b_{t-1} \boldsymbol{\varepsilon}_{t-1} + b_t \boldsymbol{\varepsilon}_{t}
\end{aligned} \tag{2}
$$
除开第一项，后面是多个独立正态噪声的和，利用叠加性，他们的和也是一个正态分布，均值为0，方差为各项系数的平方和 $(a_{t}\dots a_2)^2b_1^2 + (a_{t}\dots a_3)^2b_2^2 + \dots + a_{t}^2 b_{t-1}^2  + b_t^2$。

这样原式就可以写成
$$
\boldsymbol{x}_t = (a_{t}\dots a_1) \boldsymbol{x}_{0} + \sqrt{(a_{t}\dots a_2)^2b_1^2 + (a_{t}\dots a_3)^2b_2^2 + \dots + a_{t}^2 b_{t-1}^2  + b_t^2} \bar{\boldsymbol{\varepsilon}}_t, \quad \bar{\boldsymbol{\varepsilon}}_t \sim \mathcal{N}(\mathbf{0}, \mathbf{I}) \tag{3}
$$
这里还有一个细节，如果我们把系数的平方和都加起来
$$
\begin{aligned}
&(a_{t}\dots a_1)^2 + (a_{t}\dots a_2)^2b_1^2 + (a_{t}\dots a_3)^2b_2^2 + \dots + a_{t}^2 b_{t-1}^2  + b_t^2\\
=& (a_{t}\dots a_2)^2 a_1^2 + (a_{t}\dots a_2)^2b_1^2 + (a_{t}\dots a_3)^2b_2^2 + \dots + a_{t}^2 b_{t-1}^2  + b_t^2\\
=& (a_{t}\dots a_2)^2(a_1^2 + b_1^2) + (a_{t}\dots a_3)^2b_2^2 + \dots + a_{t}^2 b_{t-1}^2  + b_t^2\\
=& (a_{t}\dots a_3)^2 \left(a_2^2(a_1^2 + b_1^2)+b_2^2\right) + \dots + a_{t}^2 b_{t-1}^2  + b_t^2\\
=& a_t^2\left(a_{t-1}^2 \left(\dots\left(a_2^2(a_1^2 + b_1^2)+b_2^2\right)+\dots\right) +b_{t-1}^2\right) + b_t^2
\end{aligned} \tag{4}
$$
可以发现，如果我们加一个约束将会极大简化这个式子，即要求 $a_t^2 + b_t^2 =1$，这样上面的平方和就等于1了。如果我们记 $\bar{a}_t = (a_{t}\dots a_1)^2$，平方和的后面部分（也即式3的方差部分）就可以表示为$1-\bar{a}$。这样我们就可以将式(3)写成
$$
\boldsymbol{x}_t =\sqrt{ \bar{a}_t} \boldsymbol{x}_0 + \sqrt{1- \bar{a}_t}\bar{\boldsymbol{\varepsilon}}_t, \quad \bar{\boldsymbol{\varepsilon}}_t \sim \mathcal{N}(\mathbf{0}, \mathbf{I})\\\tag{5}
$$
这样是不是就舒服多了，到这里我们就重写一下第一个式子，也是和原论文一致了。
$$
\boldsymbol{x}_t = \sqrt{\alpha_t} \boldsymbol{x}_{t-1} + \sqrt{1-\alpha_t} \boldsymbol{\varepsilon}_t, \quad \boldsymbol{\varepsilon}_t \sim \mathcal{N}(\mathbf{0}, \mathbf{I}) \tag{6}
$$

> 这里写这么多的原因是，其他资料都是直接给出了这个式子，没有解释为什么系数是这样设置的（平方和为1）。同时呢，这里还有一个点，最后的 $\boldsymbol{x}_T \sim \mathcal{N}(\mathbf{0}, \mathbf{I})$ 我们可以认为是一个标准正态分布的，因此前一项的 $a_T$ 接近0，后项应该设计成一个 $(1-a_t)$ 的形式。也有作者提到，这样设计是为了保证方差都在一个尺度上，具有variance-preserving。

上面的线性过程，也可以看成是从一个高斯分布中采样，具体实现也是借助重参数化的技巧。我们写出完整的一步正向转移过程
$$
\boldsymbol{x}_t \sim q\left(\boldsymbol{x}_t | \boldsymbol{x}_{t-1}\right)=\mathcal{N}\left(\boldsymbol{x}_t ; \sqrt{\alpha_t} \boldsymbol{x}_{t-1}, (1-\alpha_t) \mathbf{I}\right) \tag{7}
$$

> 这里注意 $\alpha_t$ 不是学习的参数，原文中还有一个符号是 $\beta_t$，两者关系是 $\alpha_t = 1 - \beta_t$。

同时还能写出式(5)的概率形式
$$
\boldsymbol{x}_t \sim q(\boldsymbol{x}_t | \boldsymbol{x}_{0})=\mathcal{N}(\boldsymbol{x}_t ; \sqrt{\bar{\alpha}_t} \boldsymbol{x}_0 , (1- \bar{\alpha}_t)\mathbf{I})) ,\quad \bar{\alpha}_t=\prod_{s=1}^t \alpha_s \tag{8}
$$
整个前向过程是一个后验估计，被表示为
$$
q(\boldsymbol{x}_{1:T}|\boldsymbol{x}_0) = \prod_{t=1}^T q(\boldsymbol{x}_{t}|\boldsymbol{x}_{t-1}) \tag{9}
$$



## 逆向过程（去噪声，生成）

我们所熟知的生成模型VAE，编码和解码(生成)过程是一步到位的
$$
\text{编码: }x \rightarrow z, \quad \text{解码: }z \rightarrow x
$$
涉及到的三个分布：编码器模型 $q(z|x)$，解码器模型 $p(x|z)$，先验分布 $q(z)$。这样形式简单的同时，也注定了它的生成效果有限。扩散模型可以看成是Hierarchical Variational Autoencoder (HVAE)。也就是将编码和解码过程拆分成 $T$ 步
$$
\text{编码: } x_0 \rightarrow x_1 \rightarrow x_2 \rightarrow \dots \rightarrow x_T
\\
\text{解码: } x_T \rightarrow x_{T_1} \rightarrow x_{T-2} \rightarrow \dots \rightarrow x_0
$$
而分布关系是类似的，只不过每一步都由 $q(x_t|x_{t-1}), p(x_{t-1}|x_{t})$ 来刻画，这样的好处就有点像用分段线性函数去逼近曲线，提升了生成效果。

借由VAE的理论解释，这一类生成模型都是属于 Likelihood-based Model，因此优化目标是**最大化**真实数据分布的似然估计 $p_\theta(\boldsymbol{x}_0)$。



> 预先铺垫一些知识。
>
> 首先我们将每一步逆向过程建模成 $p_{\boldsymbol{\theta}}(\boldsymbol{x}_{t-1}|\boldsymbol{x}_{t})$，与上面介绍的正向过程类似，他们之间的线性关系我们同样可以建模成一个高斯分布，只不过前面是确定性的参数，而此刻不确定，因此我们先记作：$p_{\boldsymbol{\theta}}(\boldsymbol{x}_{t-1}|\boldsymbol{x}_{t})=\mathcal{N}(\boldsymbol{x}_{t-1};\mathbf{\mu}_\theta(\boldsymbol{x}_{t}, t), \mathbf{\Sigma}_\theta(\boldsymbol{x}_{t}, t))$。
>
> 整个逆向过程表示成一个联合概率分布 $p_\theta(\boldsymbol{x}_{0:T}) = p(\boldsymbol{x}_T)\prod_{t=1}^Tp_\theta(\boldsymbol{x}_{t-1}|\boldsymbol{x}_{t})$。



依照全概率公式，我们写出想求解的似然函数：
$$
\begin{aligned}
    \log p_\theta(\boldsymbol{x}_0) 
    &=\log \int p_\theta(\boldsymbol{x}_{0}, \boldsymbol{x}_{1},\dots, \boldsymbol{x}_{T}) d \boldsymbol{x}_{1}d \boldsymbol{x}_{2}\dots d \boldsymbol{x}_{T} \\
    &=\log \int p_\theta\left(\boldsymbol{x}_{0: T}\right) d \boldsymbol{x}_{1: T} \\
    &=\log \int \frac{p_\theta(\boldsymbol{x}_{0: T}) q(\boldsymbol{x}_{1: T} | \boldsymbol{x}_0)}{q(\boldsymbol{x}_{1: T} | \boldsymbol{x}_0)} d \boldsymbol{x}_{1: T} \\
    &=\log \mathbb{E}_{q(\boldsymbol{x}_{1: T} | \boldsymbol{x}_0)}\left[\frac{p_\theta(\boldsymbol{x}_{0: T})}{q(\boldsymbol{x}_{1: T} | \boldsymbol{x}_0)}\right] \\
    & \geq \mathbb{E}_{q(\boldsymbol{x}_{1: T} | \boldsymbol{x}_0)}\left[\log \frac{p_\theta(\boldsymbol{x}_{0: T})}{q(\boldsymbol{x}_{1: T} | \boldsymbol{x}_0)}\right] \\
    &=\mathbb{E}_{q(\boldsymbol{x}_{1: T} | \boldsymbol{x}_0)}\left[\log \frac{p(\boldsymbol{x}_T) \prod_{t=1}^T p_{\theta}(\boldsymbol{x}_{t-1} | \boldsymbol{x}_t)}{\prod_{t=1}^T q(\boldsymbol{x}_t | \boldsymbol{x}_{t-1})}\right] \\
    &=\mathbb{E}_{q(\boldsymbol{x}_{1: T} | \boldsymbol{x}_0)}\left[\log \frac{p(\boldsymbol{x}_T) p_{\theta}(\boldsymbol{x}_0 | \boldsymbol{x}_1) \prod_{t=2}^T p_{\theta}(\boldsymbol{x}_{t-1} | \boldsymbol{x}_t)}{q(\boldsymbol{x}_T | \boldsymbol{x}_{T-1}) \prod_{t=1}^{T-1} q(\boldsymbol{x}_t | \boldsymbol{x}_{t-1})}\right] \\
    &=\mathbb{E}_{q(\boldsymbol{x}_{1: T} | \boldsymbol{x}_0)}\left[\log \frac{p(\boldsymbol{x}_T) p_{\theta}(\boldsymbol{x}_0 | \boldsymbol{x}_1) \prod_{t=1}^{T-1} p_{\theta}(\boldsymbol{x}_t | \boldsymbol{x}_{t+1})}{q(\boldsymbol{x}_T | \boldsymbol{x}_{T-1}) \prod_{t=1}^{T-1} q(\boldsymbol{x}_t | \boldsymbol{x}_{t-1})}\right] \\
    &=\mathbb{E}_{q(\boldsymbol{x}_{1: T} | \boldsymbol{x}_0)}\left[\log \frac{p(\boldsymbol{x}_T) p_{\theta}(\boldsymbol{x}_0 | \boldsymbol{x}_1)}{q(\boldsymbol{x}_T | \boldsymbol{x}_{T-1})}\right]+\mathbb{E}_{q(\boldsymbol{x}_{1: T} | \boldsymbol{x}_0)}\left[\log \prod_{t=1}^{T-1} \frac{p_{\theta}(\boldsymbol{x}_t | \boldsymbol{x}_{t+1})}{q(\boldsymbol{x}_t | \boldsymbol{x}_{t-1})}\right] \\
    &=\mathbb{E}_{q(\boldsymbol{x}_{1: T} | \boldsymbol{x}_0)}\left[\log p_{\theta}(\boldsymbol{x}_0 | \boldsymbol{x}_1)\right]+\mathbb{E}_{q(\boldsymbol{x}_{1: T} | \boldsymbol{x}_0)}\left[\log \frac{p(\boldsymbol{x}_T)}{q(\boldsymbol{x}_T | \boldsymbol{x}_{T-1})}\right]+\mathbb{E}_{q(\boldsymbol{x}_{1: T} | \boldsymbol{x}_0)}\left[\sum_{t=1}^{T-1} \log \frac{p_{\theta}(\boldsymbol{x}_t | \boldsymbol{x}_{t+1})}{q(\boldsymbol{x}_t | \boldsymbol{x}_{t-1})}\right] \\
    &=\mathbb{E}_{q(\boldsymbol{x}_{1: T} | \boldsymbol{x}_0)}\left[\log p_{\theta}(\boldsymbol{x}_0 | \boldsymbol{x}_1)\right]+\mathbb{E}_{q(\boldsymbol{x}_{1: T} | \boldsymbol{x}_0)}\left[\log \frac{p(\boldsymbol{x}_T)}{q(\boldsymbol{x}_T | \boldsymbol{x}_{T-1})}\right]+\sum_{t=1}^{T-1} \mathbb{E}_{q(\boldsymbol{x}_{1: T} | \boldsymbol{x}_0)}\left[\log \frac{p_{\theta}(\boldsymbol{x}_t | \boldsymbol{x}_{t+1})}{q(\boldsymbol{x}_t | \boldsymbol{x}_{t-1})}\right] \\
    &=\mathbb{E}_{q(\boldsymbol{x}_{1} | \boldsymbol{x}_0)}\left[\log p_{\theta}(\boldsymbol{x}_0 | \boldsymbol{x}_1)\right]+\mathbb{E}_{q(\boldsymbol{x}_{T-1},\boldsymbol{x}_{T} | \boldsymbol{x}_0)}\left[\log \frac{p(\boldsymbol{x}_T)}{q(\boldsymbol{x}_T | \boldsymbol{x}_{T-1})}\right]+\sum_{t=1}^{T-1} \mathbb{E}_{q(\boldsymbol{x}_{t-1}, \boldsymbol{x}_{t}, \boldsymbol{x}_{t+1} | \boldsymbol{x}_0)}\left[\log \frac{p_{\theta}(\boldsymbol{x}_t | \boldsymbol{x}_{t+1})}{q(\boldsymbol{x}_t | \boldsymbol{x}_{t-1})}\right] \\
    &=\mathbb{E}_{q(\boldsymbol{x}_{1} | \boldsymbol{x}_0)}\left[\log p_{\theta}(\boldsymbol{x}_0 | \boldsymbol{x}_1)\right]-\mathbb{E}_{q(\boldsymbol{x}_{T-1} | \boldsymbol{x}_0)} \mathbb{E}_{q(\boldsymbol{x}_{T} | \boldsymbol{x}_{T-1})}\left[\log \frac{q(\boldsymbol{x}_T | \boldsymbol{x}_{T-1})}{p(\boldsymbol{x}_T)}\right]-\sum_{t=1}^{T-1} \mathbb{E}_{q(\boldsymbol{x}_{t-1}, \boldsymbol{x}_{t+1} | \boldsymbol{x}_0)} \mathbb{E}_{q(\boldsymbol{x}_{t}| \boldsymbol{x}_{0})}\left[\log \frac{q(\boldsymbol{x}_t | \boldsymbol{x}_{t-1})}{p_{\theta}(\boldsymbol{x}_t | \boldsymbol{x}_{t+1})}\right] \\
    &= \underbrace{\mathbb{E}_{q(\boldsymbol{x}_1 | \boldsymbol{x}_0)}\left[\log p_\theta(\boldsymbol{x}_0 | \boldsymbol{x}_1)\right]}_{\text {reconstruction term }}-\underbrace{\mathbb{E}_{q(\boldsymbol{x}_{T-1} | \boldsymbol{x}_0)}\left[D_{\mathrm{KL}}(q(\boldsymbol{x}_T | \boldsymbol{x}_{T-1}) \| p(\boldsymbol{x}_T))\right]}_{\text {prior matching term }} -\sum_{t=1}^{T-1} \underbrace{\mathbb{E}_{q(\boldsymbol{x}_{t-1}, \boldsymbol{x}_{t+1} | \boldsymbol{x}_0)}\left[D_{\mathrm{KL}}(q(\boldsymbol{x}_t | \boldsymbol{x}_{t-1}) \| p_\theta(\boldsymbol{x}_t | \boldsymbol{x}_{t+1}))\right]}_{\text {consistency term}}
\end{aligned} \tag{10}
$$
上述目标函数的优化是采用蒙特卡洛估计。但最后一项，要去计算 $q(\boldsymbol{x}_{t}|\boldsymbol{x}_{t-1}), p_{\boldsymbol{\theta}}(\boldsymbol{x}_{t}|\boldsymbol{x}_{t+1})$，涉及到三个随机变量，会极大增加估计的方差，因此我们希望能缓解这一问题。

> 此时我们的优化目标含义是 最小化 【真实的正向从 $\boldsymbol{x}_{t-1}$ 加噪声到 $\boldsymbol{x}_{t}$】and 【估计的逆向从 $\boldsymbol{x}_{t+1}$ 去噪声到 $\boldsymbol{x}_{t}$】。

此时可以想到 $\boldsymbol{x}_0$ 是确定的，同时因为马尔可夫链的关系，额外增加一项对结果是没有影响的，因此借助
$$
q\left(\boldsymbol{x}_t | \boldsymbol{x}_{t-1}, \boldsymbol{x}_0\right)=\frac{q\left(\boldsymbol{x}_{t-1}| \boldsymbol{x}_t, \boldsymbol{x}_0\right) q\left(\boldsymbol{x}_t | \boldsymbol{x}_0\right)}{q\left(\boldsymbol{x}_{t-1} | \boldsymbol{x}_0\right)} \tag{11}
$$
这样我们可以重写上面的优化目标，**（从第四行开始有变化）**
$$
\begin{aligned}
        \log p_\theta(\boldsymbol{x}_0) 
        &\geq \mathbb{E}_{q(\boldsymbol{x}_{1: T} | \boldsymbol{x}_0)}\left[\log \frac{p_\theta(\boldsymbol{x}_{0: T})}{q(\boldsymbol{x}_{1: T} | \boldsymbol{x}_0)}\right]\\
        &=\mathbb{E}_{q(\boldsymbol{x}_{1: T} | \boldsymbol{x}_0)}\left[\log \frac{p(\boldsymbol{x}_T) \prod_{t=1}^T p_{\theta}(\boldsymbol{x}_{t-1} | \boldsymbol{x}_t)}{\prod_{t=1}^T q(\boldsymbol{x}_t | \boldsymbol{x}_{t-1})}\right]\\
        &=\mathbb{E}_{q(\boldsymbol{x}_{1: T} | \boldsymbol{x}_0)}\left[\log \frac{p(\boldsymbol{x}_T) p_{\theta}(\boldsymbol{x}_0 | \boldsymbol{x}_1) \prod_{t=2}^T p_{\theta}(\boldsymbol{x}_{t-1} | \boldsymbol{x}_t)}{q(\boldsymbol{x}_1 | \boldsymbol{x}_0) \prod_{t=2}^T q(\boldsymbol{x}_t | \boldsymbol{x}_{t-1})}\right]\\
        &=\mathbb{E}_{q(\boldsymbol{x}_{1: T} | \boldsymbol{x}_0)}\left[\log \frac{p(\boldsymbol{x}_T) p_{\theta}(\boldsymbol{x}_0 | \boldsymbol{x}_1) \prod_{t=2}^T p_{\theta}(\boldsymbol{x}_{t-1} | \boldsymbol{x}_t)}{q(\boldsymbol{x}_1 | \boldsymbol{x}_0) {\color{Red}\prod_{t=2}^T q(\boldsymbol{x}_t | \boldsymbol{x}_{t-1}, \boldsymbol{x}_0)}}\right]\\
        &=\mathbb{E}_{q(\boldsymbol{x}_{1: T} | \boldsymbol{x}_0)}\left[\log \frac{p_{\theta}(\boldsymbol{x}_T) p_{\theta}(\boldsymbol{x}_0 | \boldsymbol{x}_1)}{q(\boldsymbol{x}_1 | \boldsymbol{x}_0)}+\log \prod_{t=2}^T \frac{p_{\theta}(\boldsymbol{x}_{t-1} | \boldsymbol{x}_t)}{q(\boldsymbol{x}_t | \boldsymbol{x}_{t-1}, \boldsymbol{x}_0)}\right]\\
        &=\mathbb{E}_{q(\boldsymbol{x}_{1: T} | \boldsymbol{x}_0)}\left[\log \frac{p(\boldsymbol{x}_T) p_{\theta}(\boldsymbol{x}_0 | \boldsymbol{x}_1)}{q(\boldsymbol{x}_1 | \boldsymbol{x}_0)} +\log \prod_{t=2}^T \frac{p_{\theta}(\boldsymbol{x}_{t-1} | \boldsymbol{x}_t)}{\color{Red}{\frac{q(\boldsymbol{x}_{t-1} | \boldsymbol{x}_t, \boldsymbol{x}_0) q(\boldsymbol{x}_t | \boldsymbol{x}_0)}{q(\boldsymbol{x}_{t-1} | \boldsymbol{x}_0)}}}\right] \\
        &= \mathbb{E}_{q(\boldsymbol{x}_{1: T} | \boldsymbol{x}_0)}\left[\log \frac{p(\boldsymbol{x}_T) p_{\theta}(\boldsymbol{x}_0 | \boldsymbol{x}_1)}{q(\boldsymbol{x}_1 | \boldsymbol{x}_0)} + \log \prod_{t=2}^T \frac{q(\boldsymbol{x}_{t-1} | \boldsymbol{x}_0)} {q(\boldsymbol{x}_{t} | \boldsymbol{x}_0)} + \log \prod_{t=2}^T \frac{p_{\theta}(\boldsymbol{x}_{t-1} | \boldsymbol{x}_t)}{q(\boldsymbol{x}_{t-1} | \boldsymbol{x}_t, \boldsymbol{x}_0) }\right] \\
        &= \mathbb{E}_{q(\boldsymbol{x}_{1: T} | \boldsymbol{x}_0)}\left[\log \frac{p(\boldsymbol{x}_T) p_{\theta}(\boldsymbol{x}_0 | \boldsymbol{x}_1)}{q(\boldsymbol{x}_1 | \boldsymbol{x}_0)} + \log \frac{q(\boldsymbol{x}_{1} | \boldsymbol{x}_0)} {q(\boldsymbol{x}_{2} | \boldsymbol{x}_0)}\frac{q(\boldsymbol{x}_{2} | \boldsymbol{x}_0)} {q(\boldsymbol{x}_{3} | \boldsymbol{x}_0)}\dots \frac{q(\boldsymbol{x}_{T-1} | \boldsymbol{x}_0)} {q(\boldsymbol{x}_{T} | \boldsymbol{x}_0)} + \log \prod_{t=2}^T \frac{p_{\theta}(\boldsymbol{x}_{t-1} | \boldsymbol{x}_t)}{q(\boldsymbol{x}_{t-1} | \boldsymbol{x}_t, \boldsymbol{x}_0) }\right] \\
        &= \mathbb{E}_{q(\boldsymbol{x}_{1: T} | \boldsymbol{x}_0)}\left[\log \frac{p(\boldsymbol{x}_T) p_{\theta}(\boldsymbol{x}_0 | \boldsymbol{x}_1)}{q(\boldsymbol{x}_1 | \boldsymbol{x}_0)}+ \log \frac{q(\boldsymbol{x}_{1} | \boldsymbol{x}_0)} {q(\boldsymbol{x}_{T} | \boldsymbol{x}_0)}+ \log \prod_{t=2}^T \frac{p_{\theta}(\boldsymbol{x}_{t-1} | \boldsymbol{x}_t)}{q(\boldsymbol{x}_{t-1} | \boldsymbol{x}_t, \boldsymbol{x}_0) }\right] \\
        &=\mathbb{E}_{q(\boldsymbol{x}_{1: T} | \boldsymbol{x}_0)}\left[\log \frac{p(\boldsymbol{x}_T) p_{\theta}(\boldsymbol{x}_0 | \boldsymbol{x}_1)}{q(\boldsymbol{x}_1 | \boldsymbol{x}_0)}\frac{q(\boldsymbol{x}_1 | \boldsymbol{x}_0)}{q(\boldsymbol{x}_T | \boldsymbol{x}_0)}+\log \prod_{t=2}^T \frac{p_{\theta}(\boldsymbol{x}_{t-1} | \boldsymbol{x}_t)}{q(\boldsymbol{x}_{t-1} | \boldsymbol{x}_t, \boldsymbol{x}_0)}\right] \\
        &=\mathbb{E}_{q(\boldsymbol{x}_{1: T} | \boldsymbol{x}_0)}\left[\log \frac{p(\boldsymbol{x}_T) p_{\theta}(\boldsymbol{x}_0 | \boldsymbol{x}_1)}{q(\boldsymbol{x}_T | \boldsymbol{x}_0)}+\sum_{t=2}^T \log \frac{p_{\theta}(\boldsymbol{x}_{t-1} | \boldsymbol{x}_t)}{q(\boldsymbol{x}_{t-1} | \boldsymbol{x}_t, \boldsymbol{x}_0)}\right] \\
        &=\mathbb{E}_{q(\boldsymbol{x}_{1: T} | \boldsymbol{x}_0)}\left[\log p_{\theta}(\boldsymbol{x}_0 | \boldsymbol{x}_1)\right]+\mathbb{E}_{q(\boldsymbol{x}_{1: T} | \boldsymbol{x}_0)}\left[\log \frac{p(\boldsymbol{x}_T)}{q(\boldsymbol{x}_T | \boldsymbol{x}_0)}\right]+\sum_{t=2}^T \mathbb{E}_{q(\boldsymbol{x}_{1: T} | \boldsymbol{x}_0)}\left[\log \frac{p_{\theta}(\boldsymbol{x}_{t-1} | \boldsymbol{x}_t)}{q(\boldsymbol{x}_{t-1} | \boldsymbol{x}_t, \boldsymbol{x}_0)}\right] \\
        &=\mathbb{E}_{q(\boldsymbol{x}_1 | \boldsymbol{x}_0)}\left[\log p_{\theta}(\boldsymbol{x}_0 | \boldsymbol{x}_1)\right]+\mathbb{E}_{q(\boldsymbol{x}_T | \boldsymbol{x}_0)}\left[\log \frac{p(\boldsymbol{x}_T)}{q(\boldsymbol{x}_T | \boldsymbol{x}_0)}\right]+\sum_{t=2}^T \mathbb{E}_{q(\boldsymbol{x}_{t-1}, \boldsymbol{x}_{t} | \boldsymbol{x}_0)}\left[\log \frac{p_{\theta}(\boldsymbol{x}_{t-1} | \boldsymbol{x}_t)}{q(\boldsymbol{x}_{t-1} | \boldsymbol{x}_t, \boldsymbol{x}_0)}\right] \\
        &=\mathbb{E}_{q(\boldsymbol{x}_1 | \boldsymbol{x}_0)}\left[\log p_{\theta}(\boldsymbol{x}_0 | \boldsymbol{x}_1)\right]-\mathbb{E}_{q(\boldsymbol{x}_T | \boldsymbol{x}_0)}\left[\log \frac{q(\boldsymbol{x}_T | \boldsymbol{x}_0)}{p(\boldsymbol{x}_T)}\right]-\sum_{t=2}^T \mathbb{E}_{q(\boldsymbol{x}_{t}|  \boldsymbol{x}_0)}\mathbb{E}_{q(\boldsymbol{x}_{t-1}| \boldsymbol{x}_{t}, \boldsymbol{x}_0)}\left[\log \frac{q(\boldsymbol{x}_{t-1} | \boldsymbol{x}_t, \boldsymbol{x}_0)}{p_{\theta}(\boldsymbol{x}_{t-1} | \boldsymbol{x}_t)}\right] \\
        &=\underbrace{\mathbb{E}_{q(\boldsymbol{x}_1 | \boldsymbol{x}_0)}\left[\log p_{\theta}(\boldsymbol{x}_0 | \boldsymbol{x}_1)\right]}_{\text {reconstruction term }}-\underbrace{D_{\mathrm{KL}}(q(\boldsymbol{x}_T | \boldsymbol{x}_0) \| p(\boldsymbol{x}_T))}_{\text {prior matching term }}-\sum_{t=2}^T \underbrace{\mathbb{E}_{q(\boldsymbol{x}_t | \boldsymbol{x}_0)}\left[D_{\mathrm{KL}}(q(\boldsymbol{x}_{t-1} | \boldsymbol{x}_t, \boldsymbol{x}_0) \| p_{\theta}(\boldsymbol{x}_{t-1} | \boldsymbol{x}_t))\right]}_{\text {denoising matching term }}
\end{aligned} \tag{12}
$$
> 现在第三项成了对比去噪，这里要注意，经过变换，我们的优化目标含义变成了 最小化 【真实的从 $\boldsymbol{x}_{t}$ 去噪声到 $\boldsymbol{x}_{t-1}$】and【估计的从 $\boldsymbol{x}_{t}$ 去噪声到 $\boldsymbol{x}_{t-1}$】。



我们将上面结论的第一项记作 $L_0$，





现在我们希望进一步对 $q\left(\boldsymbol{x}_{t-1} | \boldsymbol{x}_t, \boldsymbol{x}_0\right), p_\boldsymbol{\theta}(\boldsymbol{x}_{t-1}|\boldsymbol{x}_t)$ 进行建模，这样才能求解他们之间的KL散度。借助前面已经推导过的式(8-9)，我们可以首先建模$q$：
$$
\begin{aligned}
    q\left(\boldsymbol{x}_{t-1} | \boldsymbol{x}_t, \boldsymbol{x}_0\right)
    &=\frac{q\left(\boldsymbol{x}_t | \boldsymbol{x}_{t-1}, \boldsymbol{x}_0\right) q\left(\boldsymbol{x}_{t-1} | \boldsymbol{x}_0\right)}{q\left(\boldsymbol{x}_t | \boldsymbol{x}_0\right)}\\
    &=\frac{q\left(\boldsymbol{x}_t | \boldsymbol{x}_{t-1}\right) q\left(\boldsymbol{x}_{t-1} | \boldsymbol{x}_0\right)}{q\left(\boldsymbol{x}_t | \boldsymbol{x}_0\right)}\\
    &=\frac{\mathcal{N}\left(\boldsymbol{x}_t ; \sqrt{\alpha_t} \boldsymbol{x}_{t-1},\left(1-\alpha_t\right) \mathbf{I}\right) \mathcal{N}\left(\boldsymbol{x}_{t-1} ; \sqrt{\bar{\alpha}_{t-1}} \boldsymbol{x}_0,\left(1-\bar{\alpha}_{t-1}\right) \mathbf{I}\right)}{\mathcal{N}\left(\boldsymbol{x}_t ; \sqrt{\bar{\alpha}_t} \boldsymbol{x}_0,\left(1-\bar{\alpha}_t\right) \mathbf{I}\right)}\\
    &\propto \exp \left\{-\left[\frac{\left(\boldsymbol{x}_t-\sqrt{\alpha_t} \boldsymbol{x}_{t-1}\right)^2}{2\left(1-\alpha_t\right)}+\frac{\left(\boldsymbol{x}_{t-1}-\sqrt{\bar{\alpha}_{t-1}} \boldsymbol{x}_0\right)^2}{2\left(1-\bar{\alpha}_{t-1}\right)}-\frac{\left(\boldsymbol{x}_t-\sqrt{\bar{\alpha}_t} \boldsymbol{x}_0\right)^2}{2\left(1-\bar{\alpha}_t\right)}\right]\right\}\\
    &=\exp \left\{-\frac{1}{2}\left[\frac{\left(\boldsymbol{x}_t-\sqrt{\alpha_t} \boldsymbol{x}_{t-1}\right)^2}{1-\alpha_t}+\frac{\left(\boldsymbol{x}_{t-1}-\sqrt{\bar{\alpha}_{t-1}} \boldsymbol{x}_0\right)^2}{1-\bar{\alpha}_{t-1}}-\frac{\left(\boldsymbol{x}_t-\sqrt{\bar{\alpha}_t} \boldsymbol{x}_0\right)^2}{1-\bar{\alpha}_t}\right]\right\}\\
    &=\exp \left\{-\frac{1}{2}\left[\frac{-2 \sqrt{\alpha_t} \boldsymbol{x}_t \boldsymbol{x}_{t-1}+\alpha_t \boldsymbol{x}_{t-1}^2}{1-\alpha_t}+\frac{\boldsymbol{x}_{t-1}^2-2 \sqrt{\bar{\alpha}_{t-1}} \boldsymbol{x}_{t-1} \boldsymbol{x}_0}{1-\bar{\alpha}_{t-1}}+C\left(\boldsymbol{x}_t, \boldsymbol{x}_0\right)\right]\right\}\\
    &= \exp \left\{-\frac{1}{2}\left[-\frac{2 \sqrt{\alpha_t} \boldsymbol{x}_t \boldsymbol{x}_{t-1}}{1-\alpha_t}+\frac{\alpha_t \boldsymbol{x}_{t-1}^2}{1-\alpha_t}+\frac{\boldsymbol{x}_{t-1}^2}{1-\bar{\alpha}_{t-1}}-\frac{2 \sqrt{\alpha_{t-1}} \boldsymbol{x}_{t-1} \boldsymbol{x}_0}{1-\bar{\alpha}_{t-1}}+C\left(\boldsymbol{x}_t, \boldsymbol{x}_0\right)\right]\right\}\\
    &=\exp \left\{-\frac{1}{2}\left[\left(\frac{\alpha_t}{1-\alpha_t}+\frac{1}{1-\bar{\alpha}_{t-1}}\right) \boldsymbol{x}_{t-1}^2-2\left(\frac{\sqrt{\alpha_t} \boldsymbol{x}_t}{1-\alpha_t}+\frac{\sqrt{\bar{\alpha}_{t-1}} \boldsymbol{x}_0}{1-\bar{\alpha}_{t-1}}\right) \boldsymbol{x}_{t-1}+C\left(\boldsymbol{x}_t, \boldsymbol{x}_0\right)\right]\right\}\\
    &=\exp \left\{-\frac{1}{2}\left[\frac{\alpha_t\left(1-\bar{\alpha}_{t-1}\right)+1-\alpha_t}{\left(1-\alpha_t\right)\left(1-\bar{\alpha}_{t-1}\right)} \boldsymbol{x}_{t-1}^2-2\left(\frac{\sqrt{\alpha_t} \boldsymbol{x}_t}{1-\alpha_t}+\frac{\sqrt{\bar{\alpha}_{t-1}} \boldsymbol{x}_0}{1-\bar{\alpha}_{t-1}}\right) \boldsymbol{x}_{t-1}+C\left(\boldsymbol{x}_t, \boldsymbol{x}_0\right)\right]\right\}\\
    &=\exp \left\{-\frac{1}{2}\left[\frac{\alpha_t-\bar{\alpha}_t+1-\alpha_t}{\left(1-\alpha_t\right)\left(1-\bar{\alpha}_{t-1}\right)} \boldsymbol{x}_{t-1}^2-2\left(\frac{\sqrt{\alpha_t} \boldsymbol{x}_t}{1-\alpha_t}+\frac{\sqrt{\bar{\alpha}_{t-1}} \boldsymbol{x}_0}{1-\bar{\alpha}_{t-1}}\right) \boldsymbol{x}_{t-1}+C\left(\boldsymbol{x}_t, \boldsymbol{x}_0\right)\right]\right\}\\
    &=\exp \left\{-\frac{1}{2}\left[\frac{1-\bar{\alpha}_t}{\left(1-\alpha_t\right)\left(1-\bar{\alpha}_{t-1}\right)} \boldsymbol{x}_{t-1}^2-2\left(\frac{\sqrt{\alpha_t} \boldsymbol{x}_t}{1-\alpha_t}+\frac{\sqrt{\alpha_{t-1}} \boldsymbol{x}_0}{1-\bar{\alpha}_{t-1}}\right) \boldsymbol{x}_{t-1}+C\left(\boldsymbol{x}_t, \boldsymbol{x}_0\right)\right]\right\}\\
    &=\exp \left\{-\frac{1}{2}\left(\frac{1-\bar{\alpha}_t}{\left(1-\alpha_t\right)\left(1-\bar{\alpha}_{t-1}\right)}\right)\left[\boldsymbol{x}_{t-1}^2-2 \frac{\left(\frac{\sqrt{\alpha_t} \boldsymbol{x}_t}{1-\alpha_t}+\frac{\sqrt{\bar{\alpha}_{t-1}} \boldsymbol{x}_0}{1-\bar{\alpha}_{t-1}}\right)}{\frac{1-\bar{\alpha}_t}{\left(1-\alpha_t\right)\left(1-\bar{\alpha}_{t-1}\right)}} \boldsymbol{x}_{t-1}+C\left(\boldsymbol{x}_t, \boldsymbol{x}_0\right)\right]\right\}\\
    &=\exp \left\{-\frac{1}{2}\left(\frac{1-\bar{\alpha}_t}{\left(1-\alpha_t\right)\left(1-\bar{\alpha}_{t-1}\right)}\right)\left[\boldsymbol{x}_{t-1}^2-2 \frac{\left(\frac{\sqrt{\alpha_t} \boldsymbol{x}_t}{1-\alpha_t}+\frac{\sqrt{\bar{\alpha}_{t-1}} \boldsymbol{x}_0}{1-\bar{\alpha}_{t-1}}\right)\left(1-\alpha_t\right)\left(1-\bar{\alpha}_{t-1}\right)}{1-\bar{\alpha}_t} \boldsymbol{x}_{t-1}+C\left(\boldsymbol{x}_t, \boldsymbol{x}_0\right)\right]\right\}\\
    &=\exp \left\{-\frac{1}{2}\left(\frac{1}{\frac{\left(1-\alpha_t\right)\left(1-\bar{\alpha}_{t-1}\right)}{1-\bar{\alpha}_t}}\right)\left[\boldsymbol{x}_{t-1}^2-2 \frac{\sqrt{\alpha_t}\left(1-\bar{\alpha}_{t-1}\right) \boldsymbol{x}_t+\sqrt{\bar{\alpha}_{t-1}}\left(1-\alpha_t\right) \boldsymbol{x}_0}{1-\bar{\alpha}_t} \boldsymbol{x}_{t-1}+C\left(\boldsymbol{x}_t, \boldsymbol{x}_0\right)\right]\right\}\\
    &=\exp \left\{-\frac{\left(\boldsymbol{x}_{t-1} - \frac{\sqrt{\alpha_t}\left(1-\bar{\alpha}_{t-1}\right) \boldsymbol{x}_t+\sqrt{\bar{\alpha}_{t-1}}\left(1-\alpha_t\right) \boldsymbol{x}_0}{1-\bar{\alpha}_t}\right)^2}{2 \left( \frac{\left(1-\alpha_t\right)\left(1-\bar{\alpha}_{t-1}\right)}{1-\bar{\alpha}_t}\right)}\right\}\\
    &\propto \mathcal{N}\left(\boldsymbol{x}_{t-1} ; \underbrace{\frac{\sqrt{\alpha_t}\left(1-\bar{\alpha}_{t-1}\right) \boldsymbol{x}_t+\sqrt{\bar{\alpha}_{t-1}}\left(1-\alpha_t\right) \boldsymbol{x}_0}{1-\bar{\alpha}_t}}_{\mu_q\left(\boldsymbol{x}_t, \boldsymbol{x}_0\right)}, \underbrace{\frac{\left(1-\alpha_t\right)\left(1-\bar{\alpha}_{t-1}\right)}{1-\bar{\alpha}_t}}_{\boldsymbol{\Sigma}_q(t)}\mathbf{I}\right)
    \end{aligned} \tag{13}
$$

因此我们建模了 $q\left(\boldsymbol{x}_{t-1} | \boldsymbol{x}_t, \boldsymbol{x}_0\right)$，它也被称作是前向过程的后验分布，同时也写出原论文中的形式
$$
\begin{aligned}
\boldsymbol{x}_{t-1} \sim q\left(\boldsymbol{x}_{t-1}|\boldsymbol{x}_t, \boldsymbol{x}_0\right) = \mathcal{N}(\boldsymbol{\mu}_q, \boldsymbol{\Sigma}_q)
&= \mathcal{N}\left(\frac{\sqrt{\alpha_t}(1-\bar{\alpha}_{t-1}) \boldsymbol{x}_t+\sqrt{\bar{\alpha}_{t-1}}(1-\alpha_t) \boldsymbol{x}_0}{1-\bar{\alpha}_t}, \frac{(1-\alpha_t)(1-\bar{\alpha}_{t-1})}{1-\bar{\alpha}_t} \mathbf{I}\right)\\
&= \mathcal{N}\left(\frac{\sqrt{\bar{\alpha}_{t-1}} \beta_t}{1-\bar{\alpha}_t} \boldsymbol{x}_0+\frac{\sqrt{\alpha_t}\left(1-\bar{\alpha}_{t-1}\right)}{1-\bar{\alpha}_t} \boldsymbol{x}_t , \frac{1-\bar{\alpha}_{t-1}}{1-\bar{\alpha}_t} \beta_t \mathbf{I}\right)
\end{aligned} \tag{14}
$$
现在还缺 $p_\boldsymbol{\theta}(\boldsymbol{x}_{t-1}|\boldsymbol{x}_t) = \mathcal{N}(\boldsymbol{\mu}_\boldsymbol{\theta}, \boldsymbol{\Sigma}_\boldsymbol{\theta})$ 的建模，方差可以直接建模成一样的 $\boldsymbol{\Sigma}_\boldsymbol{\theta} = \boldsymbol{\Sigma}_q$，我们又根据
$$
D_{\mathrm{KL}}\left(\mathcal{N}\left(\boldsymbol{x} ; \boldsymbol{\mu}_x, \boldsymbol{\Sigma}_x\right) \| \mathcal{N}\left(\boldsymbol{y} ; \boldsymbol{\mu}_y, \boldsymbol{\Sigma}_y\right)\right)=\frac{1}{2}\left[\log \frac{\left|\boldsymbol{\Sigma}_y\right|}{\left|\boldsymbol{\Sigma}_x\right|}-d+\operatorname{tr}\left(\boldsymbol{\Sigma}_y^{-1} \boldsymbol{\Sigma}_x\right)+\left(\boldsymbol{\mu}_y-\boldsymbol{\mu}_x\right)^T \boldsymbol{\Sigma}_y^{-1}\left(\boldsymbol{\mu}_y-\boldsymbol{\mu}_x\right)\right] \tag{15}
$$
可以得到
$$
\begin{aligned}
    & \underset{\boldsymbol{\theta}}{\arg \min } D_{\mathrm{KL}}\left(q\left(\boldsymbol{x}_{t-1} | \boldsymbol{x}_t, \boldsymbol{x}_0\right) \| p_{\boldsymbol{\theta}}\left(\boldsymbol{x}_{t-1} | \boldsymbol{x}_t\right)\right) \\
    =& \underset{\boldsymbol{\theta}}{\arg \min } D_{\mathrm{KL}}\left(\mathcal{N}\left(\boldsymbol{x}_{t-1} ; \boldsymbol{\mu}_q, \boldsymbol{\Sigma}_q(t)\right) \| \mathcal{N}\left(\boldsymbol{x}_{t-1} ; \boldsymbol{\mu}_{\boldsymbol{\theta}}, \boldsymbol{\Sigma}_q(t)\right)\right) \\
    =& \underset{\boldsymbol{\theta}}{\arg \min } \frac{1}{2}\left[\log \frac{\left|\boldsymbol{\Sigma}_q(t)\right|}{\left|\boldsymbol{\Sigma}_q(t)\right|}-d+\operatorname{tr}\left(\boldsymbol{\Sigma}_q(t)^{-1} \boldsymbol{\Sigma}_q(t)\right)+\left(\boldsymbol{\mu}_{\boldsymbol{\theta}}-\boldsymbol{\mu}_q\right)^T \boldsymbol{\Sigma}_q(t)^{-1}\left(\boldsymbol{\mu}_{\boldsymbol{\theta}}-\boldsymbol{\mu}_q\right)\right] \\
    =& \underset{\boldsymbol{\theta}}{\arg \min } \frac{1}{2}\left[\log 1-d+d+\left(\boldsymbol{\mu}_{\boldsymbol{\theta}}-\boldsymbol{\mu}_q\right)^T \boldsymbol{\Sigma}_q(t)^{-1}\left(\boldsymbol{\mu}_{\boldsymbol{\theta}}-\boldsymbol{\mu}_q\right)\right] \\
    =& \underset{\boldsymbol{\theta}}{\arg \min } \frac{1}{2}\left[\left(\boldsymbol{\mu}_{\boldsymbol{\theta}}-\boldsymbol{\mu}_q\right)^T \boldsymbol{\Sigma}_q(t)^{-1}\left(\boldsymbol{\mu}_{\boldsymbol{\theta}}-\boldsymbol{\mu}_q\right)\right] \\
    =& \underset{\boldsymbol{\theta}}{\arg \min } \frac{1}{2}\left[\left(\boldsymbol{\mu}_{\boldsymbol{\theta}}-\boldsymbol{\mu}_q\right)^T\left(\sigma_q^2(t) \mathbf{I}\right)^{-1}\left(\boldsymbol{\mu}_{\boldsymbol{\theta}}-\boldsymbol{\mu}_q\right)\right] \\
    =& \underset{\boldsymbol{\theta}}{\arg \min } \frac{1}{2 \sigma_q^2(t)}\left[\left\|\boldsymbol{\mu}_{\boldsymbol{\theta}}-\boldsymbol{\mu}_q\right\|_2^2\right]
\end{aligned} \tag{16}
$$
通过这个结论我们可以发现，我们最后要比较的是两个模型的均值，其中 $\boldsymbol{\mu}_q$ 是已知的，$\boldsymbol{\mu}_\theta$ 是模型要学的。让我们来观察一下 $\boldsymbol{\mu}_q$ 的形式：
$$
\boldsymbol{\mu}_q = \frac{\sqrt{\bar{\alpha}_{t-1}} \beta_t}{1-\bar{\alpha}_t} \boldsymbol{x}_0+\frac{\sqrt{\alpha_t}\left(1-\bar{\alpha}_{t-1}\right)}{1-\bar{\alpha}_t} \boldsymbol{x}_t \tag{17}
$$
其中 $\boldsymbol{x}_0, \boldsymbol{x}_t$ 在正向过程中都是已知的，他们也能相互之间转化，而逆向过程的均值 $\boldsymbol{\mu}_\theta(\boldsymbol{x}_t, t)$ 是关于 $\boldsymbol{x}_t$ 的函数。最一般的建模方式是让神经网络直接根据 $(\boldsymbol{x}_t, t)$ 来学对应的真值 $\boldsymbol{\mu}_q$，这样显然有点复杂。因为如果 $\boldsymbol{\mu}_q$ 和  $\boldsymbol{\mu}_\theta$ 形式很相近的话，就会只需要对不同的地方做差，这样能大大简化优化过程。一个很自然而然的想法就是让神经网络去学真值 $\boldsymbol{x}_0$ ，也就是 $\hat{\boldsymbol{x}}_0 = f_\theta(\boldsymbol{x}_t, t)$。因此我们建模成：

$$
\boldsymbol{\mu}_\boldsymbol{\theta} = \frac{\sqrt{\bar{\alpha}_{t-1}} \beta_t}{1-\bar{\alpha}_t} f_\boldsymbol{\theta}(\boldsymbol{x}_t, t)+\frac{\sqrt{\alpha_t}\left(1-\bar{\alpha}_{t-1}\right)}{1-\bar{\alpha}_t} \boldsymbol{x}_t \tag{18}
$$
我们可以计算
$$
\begin{aligned}
    & \underset{\boldsymbol{\theta}}{\arg \min } D_{\mathrm{KL}}\left(q\left(\boldsymbol{x}_{t-1} | \boldsymbol{x}_t, \boldsymbol{x}_0\right) \| p_{\boldsymbol{\theta}}\left(\boldsymbol{x}_{t-1} | \boldsymbol{x}_t\right)\right) \\
    =& \underset{\boldsymbol{\theta}}{\arg \min } \frac{1}{2 \sigma_q^2(t)}\left[\left\|\boldsymbol{\mu}_{\boldsymbol{\theta}}-\boldsymbol{\mu}_q\right\|_2^2\right] \\
    =& \underset{\boldsymbol{\theta}}{\arg \min } \frac{1}{2 \sigma_q^2(t)}\left[\left\|\frac{\sqrt{\bar{\alpha}_{t-1}}\beta_t f_\boldsymbol{\theta}(\boldsymbol{x}_t, t)}{1-\bar{\alpha}_t}-\frac{\sqrt{\bar{\alpha}_{t-1}}\beta_t \boldsymbol{x}_0}{1-\bar{\alpha}_t}\right\|_2^2\right]\\
    =& \underset{\boldsymbol{\theta}}{\arg \min } \frac{1}{2 \sigma_q^2(t)}\left[\left\|\frac{\sqrt{\bar{\alpha}_{t-1}}\beta_t}{1-\bar{\alpha}_t}\left(f_\boldsymbol{\theta}(\boldsymbol{x}_t, t)-\boldsymbol{x}_0\right)\right\|_2^2\right]\\
    =& \underset{\boldsymbol{\theta}}{\arg \min } \frac{1}{2 \sigma_q^2(t)} \frac{\bar{\alpha}_{t-1}\beta_t^2}{\left(1-\bar{\alpha}_t\right)^2}\left[\|f_{\boldsymbol{\theta}}(\boldsymbol{x}_t, t)-\boldsymbol{x}_0\|_2^2\right]
\end{aligned} \tag{19}
$$

> 到这里，我们就可以得出结论，事实上可以理解成我们是在学习从任意 $t$ 步的噪声还原回原图。



**综上，我们最后就可以优化ELBO了**。



这个结论形式与原论文不一致，是为什么呢？让我们重新回到式(17)，借助式(5)我们可以消掉 $\boldsymbol{x}_0$ 得到
$$
\begin{aligned}
    \boldsymbol{\mu}_q 
    &= \frac{\sqrt{\bar{\alpha}_{t-1}} \beta_t}{1-\bar{\alpha}_t} \boldsymbol{x}_0+\frac{\sqrt{\alpha_t}\left(1-\bar{\alpha}_{t-1}\right)}{1-\bar{\alpha}_t} \boldsymbol{x}_t \\
    &= \frac{\sqrt{\bar{\alpha}_{t-1}} \beta_t}{1-\bar{\alpha}_t} \frac{\boldsymbol{x}_t-\sqrt{1-\bar{\alpha}_t} \boldsymbol{\varepsilon}_t}{\sqrt{\bar{\alpha}_t}}+\frac{\sqrt{\alpha_t}\left(1-\bar{\alpha}_{t-1}\right)}{1-\bar{\alpha}_t} \boldsymbol{x}_t \\
    &= \left[\frac{\sqrt {\color{Red}{{\bar{\alpha}_{t-1}}}} \beta_t}{(1-\bar{\alpha}_t) \sqrt{\color{Red}{\bar{\alpha}_t}}} + \frac{\sqrt{\alpha_t}\left(1-\bar{\alpha}_{t-1}\right)}{1-\bar{\alpha}_t}\right]\boldsymbol{x}_t - \frac{1-\alpha_t}{\sqrt{1-\bar{\alpha}_t} \sqrt{\alpha_t}} \boldsymbol{\varepsilon}_t \\
    &= \left[\frac{\beta_t}{(1-\bar{\alpha}_t) \sqrt{\color{Red}{{\alpha}_t}}} + \frac{\sqrt{\alpha_t}\left(1-\bar{\alpha}_{t-1}\right)}{1-\bar{\alpha}_t}\right]\boldsymbol{x}_t - \frac{1-\alpha_t}{\sqrt{1-\bar{\alpha}_t} \sqrt{\alpha_t}} \boldsymbol{\varepsilon}_t \\
    &= \frac{(1-\alpha_t)+\alpha_t(1-\bar{\alpha}_{t-1})}{\left(1-\bar{\alpha}_t\right) \sqrt{\alpha_t}} \boldsymbol{x}_t-\frac{1-\alpha_t}{\sqrt{1-\bar{\alpha}_t} \sqrt{\alpha_t}} \boldsymbol{\varepsilon}_t \\
    &= \frac{1-\alpha_t+\alpha_t-\bar{\alpha}_{t}}{\left(1-\bar{\alpha}_t\right) \sqrt{\alpha_t}} \boldsymbol{x}_t-\frac{1-\alpha_t}{\sqrt{1-\bar{\alpha}_t} \sqrt{\alpha_t}} \boldsymbol{\varepsilon}_t \\
    &= \frac{1}{\sqrt{\alpha_t}} \boldsymbol{x}_t-\frac{1-\alpha_t}{\sqrt{1-\bar{\alpha}_t} \sqrt{\alpha_t}} \boldsymbol{\varepsilon}_t
\end{aligned} \tag{20}
$$
现在来看的话，我们就让神经网络学 $\boldsymbol{x}_0$ 到 $\boldsymbol{x}_t$ 转换过程中加的噪声 $\boldsymbol{\varepsilon}_t$ ，即 $\hat{\boldsymbol{\varepsilon}}_t = f_\theta(\boldsymbol{x}_t, t)$ ，这样对于式(16)的优化目标我们就可以写成
$$
\begin{aligned}
    & \underset{\boldsymbol{\theta}}{\arg \min } D_{\mathrm{KL}}\left(q\left(\boldsymbol{x}_{t-1} | \boldsymbol{x}_t, \boldsymbol{x}_0\right) \| p_{\boldsymbol{\theta}}\left(\boldsymbol{x}_{t-1} | \boldsymbol{x}_t\right)\right) \\
    =& \underset{\boldsymbol{\theta}}{\arg \min } \frac{1}{2 \sigma_q^2(t)} \frac{(1-\alpha_t)^2}{\left(1-\bar{\alpha}_t\right)\alpha_t}\left[\left\|f_{\boldsymbol{\theta}}(\boldsymbol{x}_t, t)-\boldsymbol{\varepsilon}_t\right\|_2^2\right]
\end{aligned} \tag{21}
$$
不同点就在于一个是估计图像，一个是估计噪声，但经过实验发现，估计噪声的效果是更好的。同时省略掉前面的系数，也能带来更好的结果。









我们再缩小到一张图来看，是由一个个离散的像素点构成的，因此
$$
p_\theta(\boldsymbol{x}_0|\boldsymbol{x}_1) = \prod_{i=1}^D p_\theta(\boldsymbol{x}_0^i|\boldsymbol{x}_1^i)
$$
其中D是图像的大小，i指第几个像素。











参考资料：

[Understanding Diffusion Models: A Unified Perspective](https://arxiv.org/abs/2208.11970)

https://spaces.ac.cn/archives/9119
