# <p align=center>`Inverse Problem` </p>



[CR-GAN](#CR-GAN)

---

<span id="CR-GAN"></span>
[Analyzing Inverse Problems with Invertible Neural Networks](https://arxiv.org/pdf/1808.04730.pdf)  
**[`ICLR 2019`]  (`DKFZ, ZAH`)**  
*Lynton Ardizzone, Jakob Kruse, Sebastian Wirkert, Daniel Rahner, Eric W. Pellegrini, Ralf S. Klessen, Lena Maier-Hein, Carsten Rother, Ullrich Köthe*

<details><summary>Click to expand</summary>
<div align=center><img width="700" src="https://raw.githubusercontent.com/yzy1996/Image-Hosting/master/20210809114238.png"/></div>

> **Summary**

introduce additional latent output variables z to capture the information about x that is not contained in y.

> **Details**

$T(x)$ donates a stochastic data augmentation function. $D(x)$ donates the last layer before the activation function. The proposed regularization is given by:

Latex
$$
\operatorname{argmin}_{\theta} \mathcal{L}(\theta)=\mathbb{E}_{\mathbf{z}, \mathbf{y}, \alpha}\left[\left(A\left(G\left(T_{\theta}(\mathbf{z}, \alpha), \mathbf{y}\right)\right)-(A(G(\mathbf{z}, \mathbf{y}))+\alpha)\right)^{2}\right]
$$

$$
\mathbf{x}=f^{-1}(\mathbf{y}, \mathbf{z})=g(\mathbf{y}, \mathbf{z})
$$





</details>

---

