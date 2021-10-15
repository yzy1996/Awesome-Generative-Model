# Latent Space Image Manipulation



## Introduction

To tackle the instability of the training procedure...



These methods can be divided into two categories:

- ...



## Literature

unsorted

[Challenging common assumptions in the unsupervised learning of disentangled representations](https://arxiv.org/abs/1811.12359)



  



[GLO](#GLO)









---

<span id="GLO"></span>
[Optimizing the Latent Space of Generative Networks](https://arxiv.org/pdf/1707.05776.pdf)  
**[`ICML 2018`] (`Facebook`)**  
*Piotr Bojanowski, Armand Joulin, David Lopez-Paz, Arthur Szlam*

<details><summary>Click to expand</summary>

> **Summary**

> **Details**

compare the $\ell_2$ loss and the Laplacian pyramid Lap_1 loss, finally use a weighted combination of them.
$$
\operatorname{Lap}_{1}\left(x, x^{\prime}\right)=\sum_{j} 2^{2 j}\left|L^{j}(x)-L^{j}\left(x^{\prime}\right)\right|_{1}
$$
where $L^j(x)$ is the $j$-th level of the Laplacian pyramid representation of $x$. -[ref](Diffusion distance for histogram comparison)



</details>

---

<span id="LowRankGAN"></span>
[Low-Rank Subspaces in GANs](https://arxiv.org/pdf/2106.04488.pdf)  
**[`Arxiv 2021`] (`HKUST, Alibaba, USTC`)**  
*Jiapeng Zhu, Ruili Feng, Yujun Shen, Deli Zhao, Zhengjun Zha, Jingren Zhou, Qifeng Chen*


<div align=center><img width="700" src="https://raw.githubusercontent.com/yzy1996/Image-Hosting/master/20210911170730.png"/></div>

|      Name       |                 Symbol                  |
| :-------------: | :-------------------------------------: |
| the real image  | $\boldsymbol{x} \in \mathbb{R}^{d_{x}}$ |
| the latent code |  $\boldsymbol{z} \in \mathbb{R}^{d_z}$  |
|  the Generator  |               $G(\cdot)$                |



The Jacobian matrix $\boldsymbol{J}_z$ of the $G$ with respect to $\boldsymbol{z}$ is defined as $\left(\boldsymbol{J}_{z}\right)_{j, k}=\frac{\partial G(\boldsymbol{z})_{j}}{\partial z_{k}}$

$$
\boldsymbol{x} = G(\boldsymbol{z})
\\
\boldsymbol{x}^{edit} = G(\boldsymbol{z} + \alpha \boldsymbol{n})
\\
G(\boldsymbol{z} + \alpha \boldsymbol{n}) = G(\boldsymbol{z}) + \alpha \boldsymbol{J}_z \boldsymbol{n} + o(\alpha)
$$
the perturbation on the attribute direction only has effect on a specific region.



the low rank is $r_a$, the rest attribute vectors $d_z - r_a$





attribute matrix on region $\boldsymbol{A} = [\boldsymbol{a}_1, \boldsymbol{a}_2, \dots, \boldsymbol{a}_{d_z}]$, has $r_a$ attribute vectors can change the region, the rest $d_z - r_a$ attribute vectors has no effect on region A.

attribute matrix on region $\boldsymbol{B} = [\boldsymbol{b}_1, \boldsymbol{b}_2, \dots, \boldsymbol{b}_{d_z}]$, has $r_b$ attribute vectors can change the region, the rest $d_z - r_b$ attribute vectors has no effect on region B.



They project the specific attribute vector $v_i$ of region A into a space where the perturbation on the attribute direction has no effect on region B yet has an influence on region.



The null space 
