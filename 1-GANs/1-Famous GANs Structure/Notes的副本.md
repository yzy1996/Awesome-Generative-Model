<span id="EigenGAN"></span>
[EigenGAN: Layer-Wise Eigen-Learning for GANs](https://arxiv.org/pdf/2104.12476.pdf)  
*Zhenliang He, Meina Kan, Shiguang Shan*  
**[`ICCV 2021`]**

![image-20220301170824876](https://raw.githubusercontent.com/yzy1996/Image-Hosting/master/image-20220301170824876.png)

对每层网络有： $\begin{aligned} \phi_{i} &=\mathbf{U}_{i} \mathbf{L}_{i} \mathbf{Z}_{i}+\mu_{i} \\ &=\sum_{j=1}^{q} z_{i j} l_{i j} \mathbf{u}_{i j}+\mu_{i} \end{aligned}$， $\mathbf{h}_{i+1}=\operatorname{Conv} 2 \mathrm{x}\left(\mathbf{h}_{i}+f\left(\phi_{i}\right)\right)$

> 其中 $\mathbf{U}_{i}=\left[\mathbf{u}_{i 1}, \ldots, \mathbf{u}_{i q}\right], \mathbf{u}_{i j} \in \mathbb{R}^{H_{i} \times W_{i} \times C_i}$ 是正交基底； $\mathbf{L}_{i}=\operatorname{diag}\left(l_{i 1}, \ldots, l_{i q}\right)$是正交基的权重；$\mathbf{z}_i \in \mathbb{R}^q$ 是潜在变量，正态分布；$\mu_i$是子空间的原点；上图起点处的$\epsilon$是除开子空间但对结果依旧有作用的剩下潜在变量。

正交约束有：$\left\|\mathbf{U}_{i}^{\mathrm{T}} \mathbf{U}_{i}-\mathbf{I}\right\|_{F}^{2}$

EigenGAN有两种潜在变量，$\mathbf{z}$和$\epsilon$，实验发现两者都可以具备表示一些特征，前者捕捉到一些更重要的信息，后者可以捕捉到一些基本subtle的信息。

