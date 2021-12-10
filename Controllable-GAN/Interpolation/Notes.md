<span id="CR-GAN"></span>
[Autoencoder Image Interpolation by Shaping the Latent Space](https://arxiv.org/pdf/2008.01487.pdf)  
*Alon Oring, Zohar Yakhini, Yacov Hel-Or*  
**[`ICML 2021`] (`Israel`)**

<details><summary>Click to expand</summary>
<div align=center><img width="800" src="https://raw.githubusercontent.com/yzy1996/Image-Hosting/master/image-20211209160344423.png"/></div>

> **Summary**

This paper focuses on the interpolation problem in the autoencoder, hoping to improve the incongruities and artifacts produced during reconstruction.

The author propose a regularization mechanism consisting of an adversarial loss, a cycle-consistency loss, and a smoothness loss. 

In the end, they also find thire method could avoid overfiting.

> **Details**

The loss function
$$
\begin{aligned}
&\mathcal{L}^{i \rightarrow j}=\mathcal{L}_{R}^{i \rightarrow j}+\lambda_{A} \mathcal{L}_{A}^{i \rightarrow j}+\lambda_{C} \mathcal{L}_{C}^{i \rightarrow j}+\lambda_{S} \mathcal{L}_{S}^{i \rightarrow j}
\\
&\mathcal{L}_{R}^{i \rightarrow j}=\mathcal{L}\left(\boldsymbol{x}_{i}, \hat{\boldsymbol{x}}_{i}\right)+\mathcal{L}\left(\boldsymbol{x}_{j}, \hat{\boldsymbol{x}}_{j}\right)
\\
&\mathcal{L}_{A}^{i \rightarrow j}=\sum_{n=0}^{M}-\log D\left(\hat{\boldsymbol{x}}_{i \rightarrow j}(n / M)\right)
\\
&\mathcal{L}_{C}^{i \rightarrow j}=\sum_{n=0}^{M}\left\|z_{i \rightarrow j}(n / M)-\hat{z}_{i \rightarrow j}(n / M)\right\|^{2}
\\
&\mathcal{L}_{S}^{i \rightarrow j}=\sum_{n=0}^{M}\left\|\frac{\partial \hat{\boldsymbol{x}}_{i \rightarrow j}(\alpha)}{\partial \alpha}\right\|_{\alpha=n / M}^{2}
\end{aligned}
$$
