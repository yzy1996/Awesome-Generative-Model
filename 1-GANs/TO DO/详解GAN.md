首先不谈公式，为了让你有个最直观的认识



 GANs involve training a generator and discriminator model in an adversarial game







首先从判别器的损失函数开始说起，对于判别器，他需要对 原真实数据 和 新生成数据 分别打分，记作 $D(x)$ $D(G(z))$ ，真实标签分别为 $1 \quad 0$

对他们求交叉熵，因为是二分类问题，所以使用的是 binary cross entropy
$$
BCE(D(x)) = -[1*\log(D(x)) + 0*\log(1-D(x))] = -\log(D(x))
$$

$$
BCE(D(G(z))) = -[0*\log(D(G(z))) + 1*\log(1-D(G(z)))] = -\log(1-D(G(z)))
$$

因此判别器的损失函数是上述两者的和，同时对数据进行了采样取均值处理
$$
\begin{align}
J^D 
& = \mathbb{E}_{\boldsymbol{x} \sim p_{\mathrm{data}}(\boldsymbol{x})}[BCE(D(x))] + \mathbb{E}_{\boldsymbol{z} \sim p_{\boldsymbol{z}}(\boldsymbol{z})}[BCE(D(G(z)))] \nonumber\\
& = - \left[\mathbb{E}_{\boldsymbol{x} \sim p_{\mathrm{data}}(\boldsymbol{x})}[\log D(\boldsymbol{x})]-\mathbb{E}_{\boldsymbol{z} \sim p_{\boldsymbol{z}}(\boldsymbol{z})}[\log (1-D(G(\boldsymbol{z})))]\right]
\end{align}
$$
此时是需要最小化 $J^D$，去掉负号后，变成了最大化 $-J^D$，到这里我们就得出了原表达式的一部分
$$
\max _{D} V(D, G)=\mathbb{E}_{\boldsymbol{x} \sim p_{\mathrm{data}}(\boldsymbol{x})}[\log D(\boldsymbol{x})]+\mathbb{E}_{\boldsymbol{z} \sim p_{\boldsymbol{z}}(\boldsymbol{z})}[\log (1-D(G(\boldsymbol{z})))]
$$


现在再来看生成器的损失函数，与上面类似，但现在只有判别器给 新生成数据 打分，记作 $D(G(z))$，真实标签为 1。注意这里是与上面反着的，判别器为了让自己给这个假数据打0分，而生成器为了骗判别器给这个假数据打1分。交叉熵表示为
$$
BCE(D(G(z)) = -[1*\log(D(G(z))) + 0*\log(1-D(G(z)))] = -\log(D(G(z)))
$$
于是

但现在
$$
-\log(D(G(z))) \rightarrow \log (1-D(G(\boldsymbol{z})))
$$
正确标签找最小到错误标签找最大，一个是看正确率（越小越好），一个是看错误率（越大越好），
$$
\min J^G = \mathbb{E}_{\boldsymbol{z} \sim p_{\boldsymbol{z}}(\boldsymbol{z})}[\log (1-D(G(\boldsymbol{z})))]
$$


所以我们得到了最终的表达式：
$$
\min _{G} \max _{D} V(D, G)=\mathbb{E}_{\boldsymbol{x} \sim p_{\mathrm{data}}(\boldsymbol{x})}[\log D(\boldsymbol{x})]+\mathbb{E}_{\boldsymbol{z} \sim p_{\boldsymbol{z}}(\boldsymbol{z})}[\log (1-D(G(\boldsymbol{z})))]
$$



**GAN**

无监督学习



in each training iteration

- Sample $m$ real examples $\{x^1, x^2, \dots, x^m\}$ from the dataset
- Sample $m$ noise $\{z^1, z^2, \dots, z^m\}$ from a random distribution
- Obtain $m$ generated/fake examples $\{{\tilde{x}}^1, {\tilde{x}}^2, \dots, {\tilde{x}}^m\}$, ${\tilde{x}}^i = G(z^i)$



update discriminator:
$$
\max J^D = \frac{1}{m} \sum_{i=1}^m \left[\log D(x^i) - \log (D({\tilde{x}}^i))\right]
$$
update generator:
$$
\max J^G = \frac{1}{m} \sum_{i=1}^m \log D({\tilde{x}}^i)
$$

---

**CGAN**

之前是随机给z，现在想要可控，能不能控制z，让给定一个范围内所有的z’都生成同一类结果

给z添加一个c，所以D会给相似满足c的pair打高分，给不相似满足c的打低分

这也是传统GAN的训练过程，但这个过程不足以训练D能判别是不是c，所以还要增加一个负样本，怎么来呢，从原数据集里找到不满足c的样本，与c pair后也打低分



讲究的是一个pair



in each training iteration

- Sample $m$ real examples $\{(c^1, x^1), (c^2, x^2), \dots, (c^m, x^m)\}$ from the dataset
- Sample $m$ noise $\{z^1, z^2, \dots, z^m\}$ from a random distribution
- Obtain $m$ generated/fake examples $\{\tilde{x}^1, \tilde{x}^2, \dots, \tilde{x}^m\}$, $\tilde{x}^i = G(c^i, z^i)$
- Sample $m$ non-label $c$ examples $\{{\hat{x}}^1, {\hat{x}}^2, \dots, {\hat{x}}^m\}$ from the dataset



update discriminator:
$$
\max J^D = \frac{1}{m} \sum_{i=1}^m \left[\log D(c^i, x^i) - \log (D(c^i, {\tilde{x}}^i)) - \log (D(c^i, {\hat{x}}^i))\right]
$$
update generator:
$$
\max J^G = \frac{1}{m} \sum_{i=1}^m \log D(\tilde{x}^i)
$$

---

**SGAN**

CGAN的D做的还是一个二分类的工作，我们在想能否让D在能二分类真假图片的同时，兼顾标签分类呢



本质都是特征提取，传统GAN提取了区分真假的特征，CGAN提取了区分pair图片真假的特征，而现在，一个任务是提取真假特征，一个任务是提取标签分类特征；这两个任务可以同时兼顾，相辅相成，两者效果都变好。进而让G的效果也变好，最后这三者达到一个平衡。



有N+1类：假，真1，真2…真N



in each training iteration

- Sample $m$ real examples $\{(c^1, x^1), (c^2, x^2), \dots, (c^m, x^m)\}$ from the dataset
- Sample $m$ noise $\{z^1, z^2, \dots, z^m\}$ from a random distribution
- Obtain $m$ generated/fake examples $\{\tilde{x}^1, \tilde{x}^2, \dots, \tilde{x}^m\}$, $\tilde{x}^i = G(z^i)$



update discriminator:
$$
\max J^D = \frac{1}{m} \sum_{i=1}^m \left[c^i \log D(x^i) - \log (D(\tilde{x}^i))\right]
$$
update generator:
$$
\max J^G = \frac{1}{m} \sum_{i=1}^m \log D(\tilde{x}^i)
$$

---

> 并没有为了实现CGAN的效果，只是让G表现得更好了

---

**ACGAN**

我们又想利用辅助分类器提升整体效果，又想控制条件输出怎么办呢？

SGAN是类别：假，真1，真2. . 真N

ACGAN是类别： 假1， 假2，..假N， 真1，真2，.. 真N



in each training iteration

- Sample $m$ real examples $\{(c^1, x^1), (c^2, x^2), \dots, (c^m, x^m)\}$ from the dataset
- Sample $m$ noise $\{z^1, z^2, \dots, z^m\}$ from a random distribution
- Obtain $m$ generated/fake examples $\{\tilde{x}^1, \tilde{x}^2, \dots, \tilde{x}^m\}$, $\tilde{x}^i = G(c^i, z^i)$
- Sample $m$ non-label $c$ examples $\{\hat{x}^1, \hat{x}^2, \dots, \hat{x}^m\}$ from the dataset

 

update discriminator:
$$
\max J^D = \frac{1}{m} \sum_{i=1}^m \left[\log D(x^i) - \log (D(\tilde{x}^i))\right]
$$
update auxiliary classifier:
$$
\max J^C = \frac{1}{m} \sum_{i=1}^m \left[c^i\log (C(x^i)) - c^i\log (C({\hat{x}}^i)) + c^i\log (C({\tilde{x}}^i))\right]
$$
update generator:
$$
\max J^G = \frac{1}{m} \sum_{i=1}^m \left[\log D({\tilde{x}}^i) + c^i\log (C({\tilde{x}}^i))\right]
$$



**MOGAN**

in each training iteration

- Sample $m$ real examples $\{x^1, x^2, \dots, x^m\}$ from the dataset
- Sample $m$ noise $\{z^1, z^2, \dots, z^m\}$ from a random distribution
- Obtain $m$ generated/fake examples $\{{\tilde{x}}^1, {\tilde{x}}^2, \dots, {\tilde{x}}^m\}$, ${\tilde{x}}^i = G(z^i)$



update discriminator:
$$
\max J^D = \frac{1}{m} \sum_{i=1}^m \left[\log D(x^i) - \log (D({\tilde{x}}^i))\right]
$$
update generator:
$$
\max J^G = \frac{1}{m} \sum_{i=1}^m \left[\log D\left({\tilde{x}}^i\right) + \log C\left({\tilde{x}}^i\right)\right]
$$







---








GAN的分类器是严重过拟合的

