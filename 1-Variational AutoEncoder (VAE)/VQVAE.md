ref https://zhuanlan.zhihu.com/p/388620573



[toc]





找到最接近的VQ table 上的 z





几个问题？

如何保证生成的多样性呢？



是为了学到一个离散的隐空间

## VQ-VAE

[Neural Discrete Representation Learning](https://arxiv.org/abs/1711.00937)  
*Aaron van den Oord, Oriol Vinyals, Koray Kavukcuoglu*  
**[`NeurIPS 2017`] (``)** 

VQ (Vector Quantisation) 指的是 

为了解决过去VAE的“后验崩塌” (posterior collapse) 问题，



z空间是由一个codebook（例如m个 $e_1, \dots, e_m$）构成的，输入图片经过encoder得到z，然后找到最接近的e，然后将这个e输入decoder。那如何通过有限个e来重建x呢？特别的是encoder会输出多个向量z

![image-20220503213714623](https://raw.githubusercontent.com/yzy1996/Image-Hosting/master/image-20220503213714623.png)

> CNN输出 $m \times n$ 个 D 维向量 (用z表示)，codebook 是 $K$ 个 D 维向量 (用e表示)。然后通过算法找到这 $m \times n$ 个最接近的 e，图中用数字标注出来了对应关系。总共有 $K^{(m\times n)}$ 种组合方式，也就是可以重建出 $K^{(m\times n)}$ 个不同的图像局部结果。

$$
z_{q}(x)=e_{k}, \quad \text { where } \quad k=\operatorname{argmin}_{j}\left\|z_{e}(x)-e_{j}\right\|_{2}
$$

损失函数
$$
L=\log p\left(x \mid z_{q}(x)\right)+\left\|\operatorname{sg}\left[z_{e}(x)\right]-e\right\|_{2}^{2}+\beta\left\|z_{e}(x)-\operatorname{sg}[e]\right\|_{2}^{2}
$$

> 第一项是autoencoder的重建loss；第二项是codebook loss，sg 表示 stop gradient，也就是不计算这一项的梯度，这个loss只更新codebook，也就是希望e趋向于encoder出来的z；commitment loss，跟第二个loss恰恰相反，这就体现了一种交替更新的思想。



第二项loss是不连续的：
$$
\sum_j^{n_i} \|z_{i,j} - e_i\|
\\
e_i = \frac{1}{n_i} \sum_j^{n_i} z_{i,j}
\\
$$
当使用minibatches训练时，由于数据量不足，这么更新是不准确的，因此使用指数滑动平均来更新 e_i



但在训练第一个step时，由于数据不足，n_i可能为0，怎么会产生nan，因此要引入拉普拉斯平滑
$$
n_i = \frac{n_i + \epsilon}{N + K\epsilon} \cdot N
$$
在训练过程中，隐向量满足均匀分布。训练完成后，可以重新学习一个分布来生成有意义的结果。也就是说codebook是杂乱的，你怎么选择一个序列出来生成呢。训练一个自回归模型，一个接一个的来生成z，这样最后的 $m \times n$ 个 z 就是有关联的，然后能生成想要的图片。



他的好处是：





## VQ-VAE2

[Generating Diverse High-Fidelity Images with VQ-VAE-2](https://arxiv.org/abs/1906.00446)  
*Ali Razavi, Aaron van den Oord, Oriol Vinyals*  
**[`arXiv 2019`] (``)** 



Hierarchical-VQ-VAE，把隐空间分成两个，一个上层隐空间，一个下层隐空间。上层隐空间表示全局信息，下层隐空间表示局部信息。

![image-20220504001117815](https://raw.githubusercontent.com/yzy1996/Image-Hosting/master/image-20220504001117815.png)

